// Dibuja los «circuitos» del cartel de la Semana de la IA 2026 (trazas cian y ámbar con brillo) como PNG transparentes.
// Uso: node circuitos.js  → ../assets/circuito_*.png
const sharp = require("sharp");
const path = require("path");

function rnd(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }

// Trazas que salen de un punto y avanzan en ángulos de 0/45/90 grados, como las pistas de una placa.
function trazas(w, h, ox, oy, n, largo, seed, dirs) {
  const r = rnd(seed); let out = "";
  for (let i = 0; i < n; i++) {
    const color = r() < 0.62 ? "#5BC8EE" : "#F2A93B";
    let x = ox + (r() - 0.5) * 40, y = oy + (r() - 0.5) * 40, d = "M" + x.toFixed(1) + " " + y.toFixed(1);
    let ang = dirs[Math.floor(r() * dirs.length)];
    const tramos = 2 + Math.floor(r() * 3);
    for (let t = 0; t < tramos; t++) {
      const L = largo * (0.3 + r() * 0.7);
      x += Math.cos(ang) * L; y += Math.sin(ang) * L;
      d += " L" + x.toFixed(1) + " " + y.toFixed(1);
      ang += (r() < 0.5 ? -1 : 1) * Math.PI / 4 * (r() < 0.5 ? 1 : 0);
    }
    const sw = (1.2 + r() * 1.6).toFixed(1);
    out += `<path d="${d}" stroke="${color}" stroke-width="${sw}" fill="none" stroke-linecap="round" filter="url(#g)" opacity="${(0.55 + r() * 0.45).toFixed(2)}"/>`;
    out += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(3 + r() * 3).toFixed(1)}" fill="none" stroke="${color}" stroke-width="2" filter="url(#g)"/>`;
  }
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>${out}</svg>`;
}

(async () => {
  const A = path.join(__dirname, "..", "assets");
  const P = Math.PI;
  // esquina superior derecha
  await sharp(Buffer.from(trazas(900, 600, 900, 0, 46, 160, 7, [P, P * 0.75, P * 0.5]))).png().toFile(path.join(A, "circuito_esquina.png"));
  // abanico inferior (como el suelo del cartel)
  const fundido = (w, h, desde) => Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><defs><linearGradient id="f" x1="0" y1="${desde}" x2="0" y2="${1 - desde}"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.45" stop-color="#fff" stop-opacity="1"/></linearGradient></defs><rect width="${w}" height="${h}" fill="url(#f)"/></svg>`);
  await sharp(Buffer.from(trazas(1600, 420, 800, 420, 70, 230, 11, [P * 1.5, P * 1.25, P * 1.75, P, 0])))
    .composite([{ input: fundido(1600, 420, 0), blend: "dest-in" }]).png().toFile(path.join(A, "circuito_suelo.png"));
  // banda fina para separadores
  await sharp(Buffer.from(trazas(1600, 160, 0, 80, 40, 260, 23, [0, P * 0.25, -P * 0.25]))).png().toFile(path.join(A, "circuito_banda.png"));
  console.log("circuitos ok");
})();
