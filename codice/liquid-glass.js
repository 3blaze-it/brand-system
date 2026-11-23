/*!
 * 3blaze Liquid Glass — v1.0 (2027)
 * Rifrazione reale (feDisplacementMap) + dispersione cromatica sui bordi ("rainbow edge").
 * Non è un blur: la lente sposta i pixel dello sfondo come un vetro spesso con bordo convesso.
 *
 * Uso:
 *   <div class="lg" data-lg data-lg-radius="36" data-lg-bezel="28" data-lg-scale="70"></div>
 *   includere liquid-glass.js con un tag script: si inizializza da solo su [data-lg]
 *   LiquidGlass.attach(el, { radius, bezel, scale, dispersion, blur, specular })
 *
 * Supporto: rifrazione completa su Chromium (Chrome, Edge, Arc, Opera, Brave) via backdrop-filter:url().
 * Safari/Firefox: fallback automatico a vetro sfocato + bordo iridescente (classe .lg--fallback).
 */
(function (root) {
  'use strict';
  var NS = 'http://www.w3.org/2000/svg';
  var uid = 0;
  var isChromium = !!(root.chrome || /Chrom(e|ium)\//.test(navigator.userAgent)) && !/Firefox\//.test(navigator.userAgent);
  var supportsUrlBackdrop = isChromium && CSS.supports('backdrop-filter', 'url(#x)');

  function defs() {
    var svg = document.getElementById('lg-defs');
    if (!svg) {
      svg = document.createElementNS(NS, 'svg');
      svg.id = 'lg-defs';
      svg.setAttribute('aria-hidden', 'true');
      svg.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden;pointer-events:none';
      svg.appendChild(document.createElementNS(NS, 'defs'));
      document.body.appendChild(svg);
    }
    return svg.firstChild;
  }

  /* Signed distance da un rettangolo arrotondato (negativa dentro). */
  function sdRoundRect(px, py, hw, hh, r) {
    var qx = Math.abs(px) - hw + r, qy = Math.abs(py) - hh + r;
    var ox = Math.max(qx, 0), oy = Math.max(qy, 0);
    return Math.min(Math.max(qx, qy), 0) + Math.sqrt(ox * ox + oy * oy) - r;
  }


  /* Distanza euclidea esatta (Felzenszwalb & Huttenlocher) da una maschera: per forme libere (es. fiamma). */
  function edt1d(f, n) {
    var d = new Float64Array(n), v = new Int32Array(n), z = new Float64Array(n + 1), k = 0;
    v[0] = 0; z[0] = -Infinity; z[1] = Infinity;
    for (var q = 1; q < n; q++) {
      var s = ((f[q] + q * q) - (f[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k]);
      while (s <= z[k]) { k--; s = ((f[q] + q * q) - (f[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k]); }
      k++; v[k] = q; z[k] = s; z[k + 1] = Infinity;
    }
    k = 0;
    for (q = 0; q < n; q++) { while (z[k + 1] < q) k++; d[q] = (q - v[k]) * (q - v[k]) + f[v[k]]; }
    return d;
  }
  function insideDistance(mask, w, h) {          // mask: Uint8 1 = dentro
    var INF = 1e20, g = new Float64Array(w * h), col = new Float64Array(h), row = new Float64Array(w), x, y;
    for (x = 0; x < w; x++) {
      for (y = 0; y < h; y++) col[y] = mask[y * w + x] ? INF : 0;
      var dc = edt1d(col, h);
      for (y = 0; y < h; y++) g[y * w + x] = dc[y];
    }
    for (y = 0; y < h; y++) {
      for (x = 0; x < w; x++) row[x] = g[y * w + x];
      var dr = edt1d(row, w);
      for (x = 0; x < w; x++) g[y * w + x] = Math.sqrt(dr[x]);
    }
    return g;                                      // distanza dal bordo, 0 fuori
  }
  function fieldFromPath(d, vb, w, h) {
    var W = w + 2, H = h + 2;                       // 1px di cornice vuota: anche i lati a filo hanno un bordo
    var c = document.createElement('canvas'); c.width = W; c.height = H;
    var ctx = c.getContext('2d');
    ctx.setTransform(w / vb[2], 0, 0, h / vb[3], 1 - vb[0] * w / vb[2], 1 - vb[1] * h / vb[3]);
    ctx.fill(new Path2D(d));
    var px = ctx.getImageData(0, 0, W, H).data, m = new Uint8Array(W * H);
    for (var i = 0; i < W * H; i++) m[i] = px[i * 4 + 3] > 127 ? 1 : 0;
    for (var x = 0; x < W; x++) { m[x] = 0; m[(H - 1) * W + x] = 0; }
    for (var y = 0; y < H; y++) { m[y * W] = 0; m[y * W + W - 1] = 0; }
    var dist = insideDistance(m, W, H);
    return function (x, y) { x = Math.max(0, Math.min(W - 1, Math.round(x) + 1)); y = Math.max(0, Math.min(H - 1, Math.round(y) + 1)); return dist[y * W + x]; };
  }
  function fieldRoundRect(w, h, r) {
    return function (x, y) { return -sdRoundRect(x + 0.5 - w / 2, y + 0.5 - h / 2, w / 2, h / 2, r); };
  }

  /* Mappa di spostamento: R = dx, G = dy (128 = neutro). Profilo di lente convessa con coda lunga.
     La normale è il gradiente del campo di distanza: il campione si sposta verso l'interno,
     quindi il bordo comprime e piega lo sfondo (il backdrop è ritagliato sull'elemento). */
  function displacementMap(w, h, field, bezel) {
    var c = document.createElement('canvas'); c.width = w; c.height = h;
    var ctx = c.getContext('2d'), img = ctx.createImageData(w, h), d = img.data, e = 1;
    for (var y = 0; y < h; y++) for (var x = 0; x < w; x++) {
      var i = (y * w + x) * 4, dist = field(x, y), dx = 0, dy = 0;
      if (dist > 0 && dist < bezel) {
        var t = dist / bezel, m = Math.pow(1 - t, 1.5) * (0.6 + 0.4 * Math.cos(t * Math.PI / 2));
        var gx = field(x + e, y) - field(x - e, y), gy = field(x, y + e) - field(x, y - e);
        var gl = Math.sqrt(gx * gx + gy * gy) || 1;
        dx = (gx / gl) * m; dy = (gy / gl) * m;
      }
      d[i] = 128 + dx * 127; d[i + 1] = 128 + dy * 127; d[i + 2] = 128; d[i + 3] = 255;
    }
    ctx.putImageData(img, 0, 0); return c.toDataURL('image/png');
  }

  /* Mappa speculare: luce radente dall'alto a sinistra, solo sul filo del bordo. */
  function specularMap(w, h, field, bezel) {
    var c = document.createElement('canvas'); c.width = w; c.height = h;
    var ctx = c.getContext('2d'), img = ctx.createImageData(w, h), d = img.data, e = 1;
    var lx = -0.6, ly = -0.8, rim = Math.max(2, bezel * 0.18);
    for (var y = 0; y < h; y++) for (var x = 0; x < w; x++) {
      var i = (y * w + x) * 4, dist = field(x, y), a = 0;
      if (dist > 0 && dist < rim) {
        var gx = field(x + e, y) - field(x - e, y), gy = field(x, y + e) - field(x, y - e);
        var gl = Math.sqrt(gx * gx + gy * gy) || 1;
        a = Math.pow(Math.abs((gx / gl) * lx + (gy / gl) * ly), 3) * Math.pow(1 - dist / rim, 1.5);
      }
      d[i] = d[i + 1] = d[i + 2] = 255; d[i + 3] = Math.round(a * 255);
    }
    ctx.putImageData(img, 0, 0); return c.toDataURL('image/png');
  }

  function el(tag, attrs, parent) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }

  function buildFilter(id, w, h, o) {
    var f = el('filter', { id: id, x: '0', y: '0', width: w, height: h, filterUnits: 'userSpaceOnUse',
      primitiveUnits: 'userSpaceOnUse', 'color-interpolation-filters': 'sRGB' });
    var field = o.path ? fieldFromPath(o.path, o.viewBox, w, h) : fieldRoundRect(w, h, o.radius);
    var dmap = displacementMap(w, h, field, o.bezel);
    el('feGaussianBlur', { in: 'SourceGraphic', stdDeviation: o.blur, result: 'src' }, f);
    el('feImage', { href: dmap, x: 0, y: 0, width: w, height: h, result: 'map', preserveAspectRatio: 'none' }, f);
    // Dispersione: tre canali spostati con intensità diverse (R < G < B) → frange arcobaleno sul bordo
    var s = o.scale, k = o.dispersion;
    [['R', s * (1 - k), '1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0'],
     ['G', s,           '0 0 0 0 0  0 1 0 0 0  0 0 0 0 0  0 0 0 1 0'],
     ['B', s * (1 + k), '0 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0']].forEach(function (c) {
      el('feDisplacementMap', { in: 'src', in2: 'map', scale: c[1], xChannelSelector: 'R', yChannelSelector: 'G', result: 'd' + c[0] }, f);
      el('feColorMatrix', { in: 'd' + c[0], type: 'matrix', values: c[2], result: 'c' + c[0] }, f);
    });
    el('feComposite', { in: 'cR', in2: 'cG', operator: 'arithmetic', k1: 0, k2: 1, k3: 1, k4: 0, result: 'rg' }, f);
    el('feComposite', { in: 'rg', in2: 'cB', operator: 'arithmetic', k1: 0, k2: 1, k3: 1, k4: 0, result: 'rgb' }, f);
    el('feColorMatrix', { in: 'rgb', type: 'saturate', values: o.saturate, result: 'sat' }, f);
    if (o.specular > 0) {
      el('feImage', { href: specularMap(w, h, field, o.bezel), x: 0, y: 0, width: w, height: h, result: 'spec', preserveAspectRatio: 'none' }, f);
      el('feComponentTransfer', { in: 'spec', result: 'specA' }, f).appendChild(el('feFuncA', { type: 'linear', slope: o.specular }));
      el('feBlend', { in: 'specA', in2: 'sat', mode: 'screen', result: 'fin' }, f);
    }
    if (o.path) {   // forma libera: il risultato esiste solo dentro la forma (fuori resta lo sfondo originale)
      var mc = document.createElement('canvas'); mc.width = w; mc.height = h;
      var mx = mc.getContext('2d'); mx.setTransform(w / o.viewBox[2], 0, 0, h / o.viewBox[3], -o.viewBox[0] * w / o.viewBox[2], -o.viewBox[1] * h / o.viewBox[3]);
      mx.fill(new Path2D(o.path));
      el('feImage', { href: mc.toDataURL('image/png'), x: 0, y: 0, width: w, height: h, result: 'shape', preserveAspectRatio: 'none' }, f);
      el('feFlood', { 'flood-color': '#FDF6E2', 'flood-opacity': o.fill, result: 'veil' }, f);
      el('feBlend', { in: 'veil', in2: o.specular > 0 ? 'fin' : 'sat', mode: 'screen', result: 'veiled' }, f);
      el('feComposite', { in: 'veiled', in2: 'shape', operator: 'in' }, f);
    }
    return f;
  }

  function attach(node, opts) {
    var ds = node.dataset || {};
    var o = {
      radius: +(opts && opts.radius || ds.lgRadius || 32),
      bezel: +(opts && opts.bezel || ds.lgBezel || 40),
      scale: +(opts && opts.scale || ds.lgScale || 70),
      dispersion: +(opts && opts.dispersion || ds.lgDispersion || 0.22),
      blur: +(opts && opts.blur != null ? opts.blur : (ds.lgBlur || 1.2)),
      saturate: +(opts && opts.saturate || ds.lgSaturate || 1.35),
      specular: +(opts && opts.specular != null ? opts.specular : (ds.lgSpecular || 0.9)),
      fill: +(opts && opts.fill != null ? opts.fill : (ds.lgFill || 0.06)),
      path: (opts && opts.path) || ds.lgPath || null,                       // forma libera: path SVG
      viewBox: ((opts && opts.viewBox) || ds.lgViewbox || '0 0 100 100').toString().split(/[ ,]+/).map(Number)
    };
    if (o.path) {   // la forma ritaglia l'elemento: clipPath in coordinate relative (ritaglia anche il backdrop)
      var cid = 'lgc-' + (++uid), cp = el('clipPath', { id: cid, clipPathUnits: 'objectBoundingBox' }, defs());
      el('path', { d: o.path, transform: 'scale(' + (1 / o.viewBox[2]) + ' ' + (1 / o.viewBox[3]) + ') translate(' + (-o.viewBox[0]) + ' ' + (-o.viewBox[1]) + ')' }, cp);
      node.style.clipPath = 'url(#' + cid + ')';
      node.classList.add('lg--shape');
    }
    if (!o.path) node.style.borderRadius = o.radius + 'px';
    if (!supportsUrlBackdrop) { node.classList.add('lg--fallback'); return null; }
    var id = 'lg-' + (++uid), d = defs(), current = null;
    function render() {
      var r = node.getBoundingClientRect();
      var w = Math.max(2, Math.round(r.width)), h = Math.max(2, Math.round(r.height));
      if (current && current.w === w && current.h === h) return;
      var old = document.getElementById(id); if (old) old.remove();
      d.appendChild(buildFilter(id, w, h, Object.assign({}, o, { radius: Math.min(o.radius, w / 2, h / 2) })));
      node.style.backdropFilter = 'url(#' + id + ')';
      node.style.webkitBackdropFilter = 'url(#' + id + ')';
      current = { w: w, h: h };
    }
    render();
    if (root.ResizeObserver) new ResizeObserver(render).observe(node);
    return { id: id, refresh: function () { current = null; render(); } };
  }

  function init(scope) {
    (scope || document).querySelectorAll('[data-lg]').forEach(function (n) { if (!n.__lg) n.__lg = attach(n) || true; });
  }

  root.LiquidGlass = { attach: attach, init: init, supported: supportsUrlBackdrop };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); });
  else init();
})(window);
