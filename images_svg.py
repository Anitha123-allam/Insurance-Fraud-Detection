# ---------- IMAGES: simple illustrations drawn with code (SVG) ----------
# Each function returns SVG text. app.py turns it into an <img> tag.

LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs>'
        '<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4f46e5"/>'
        '<stop offset="1" stop-color="#06b6d4"/></linearGradient></defs>'
        '<path d="M32 4 L56 14 V32 C56 46 46 56 32 60 C18 56 8 46 8 32 V14 Z" fill="url(#g)"/>'
        '<path d="M21 32 L29 40 L44 24" fill="none" stroke="#fff" stroke-width="6" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')

HERO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 440"><defs>'
        '<linearGradient id="a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6366f1"/>'
        '<stop offset="1" stop-color="#06b6d4"/></linearGradient>'
        '<linearGradient id="b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8b5cf6"/>'
        '<stop offset="1" stop-color="#4f46e5"/></linearGradient>'
        '<filter id="s" x="-20%" y="-20%" width="140%" height="160%">'
        '<feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0b132b" flood-opacity=".35"/></filter></defs>'
        '<circle cx="300" cy="220" r="190" fill="#fff" opacity=".07"/>'
        '<circle cx="470" cy="70" r="56" fill="#06b6d4" opacity=".28"/>'
        '<circle cx="80" cy="110" r="32" fill="#f59e0b" opacity=".4"/>'
        '<g filter="url(#s)"><rect x="130" y="50" width="270" height="340" rx="22" fill="#fff"/></g>'
        '<rect x="130" y="50" width="270" height="62" rx="22" fill="url(#b)"/>'
        '<rect x="130" y="90" width="270" height="22" fill="url(#b)"/>'
        '<text x="156" y="90" font-family="Arial,sans-serif" font-size="20" font-weight="700" fill="#fff">Insurance Claim</text>'
        '<rect x="156" y="136" width="140" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="320" y="136" width="56" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="156" y="170" width="110" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="320" y="170" width="56" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="146" y="200" width="240" height="48" rx="12" fill="#fee2e2"/>'
        '<circle cx="174" cy="224" r="13" fill="#ef4444"/>'
        '<text x="174" y="230" text-anchor="middle" fill="#fff" font-size="18" font-weight="700" font-family="Arial">!</text>'
        '<rect x="198" y="212" width="110" height="12" rx="6" fill="#fca5a5"/>'
        '<rect x="198" y="230" width="70" height="10" rx="5" fill="#fecaca"/>'
        '<rect x="156" y="270" width="150" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="320" y="270" width="56" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="156" y="304" width="120" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="320" y="304" width="56" height="12" rx="6" fill="#e5e7ef"/>'
        '<rect x="156" y="346" width="220" height="14" rx="7" fill="#e5e7ef"/>'
        '<rect x="156" y="346" width="172" height="14" rx="7" fill="url(#a)"/>'
        '<g transform="translate(420 118)" filter="url(#s)"><path d="M0 -58 L50 -38 V8 C50 42 26 62 0 74 '
        'C-26 62 -50 42 -50 8 V-38 Z" fill="url(#a)"/><path d="M-20 6 L-6 20 L22 -12" fill="none" '
        'stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>'
        '<g filter="url(#s)"><circle cx="296" cy="292" r="50" fill="#fff" fill-opacity=".55" stroke="#06b6d4" stroke-width="12"/>'
        '<line x1="333" y1="329" x2="380" y2="376" stroke="#0e7490" stroke-width="18" stroke-linecap="round"/></g>'
        '<g filter="url(#s)"><rect x="8" y="285" width="118" height="58" rx="16" fill="#fff"/>'
        '<text x="24" y="308" font-size="12" fill="#6b7280" font-family="Arial">Fraud score</text>'
        '<text x="24" y="333" font-size="24" font-weight="700" fill="#ef4444" font-family="Arial">87%</text></g>'
        '<g transform="translate(30 362)" filter="url(#s)"><path d="M0 40 L12 14 C16 6 24 2 34 2 H78 '
        'C88 2 94 8 100 16 L112 24 C122 26 126 32 126 42 V48 H0 Z" fill="#f59e0b"/>'
        '<path d="M30 8 H52 V24 H20 Z M58 8 H78 C84 8 88 12 92 24 H58 Z" fill="#fff" opacity=".85"/>'
        '<circle cx="30" cy="50" r="14" fill="#1f2937"/><circle cx="30" cy="50" r="6" fill="#d1d5db"/>'
        '<circle cx="98" cy="50" r="14" fill="#1f2937"/><circle cx="98" cy="50" r="6" fill="#d1d5db"/></g></svg>')

DASH_MOCK = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 370"><defs>'
             '<linearGradient id="k1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4f46e5"/><stop offset="1" stop-color="#7c3aed"/></linearGradient>'
             '<linearGradient id="k2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f59e0b"/><stop offset="1" stop-color="#fb7185"/></linearGradient>'
             '<linearGradient id="k3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#06b6d4"/><stop offset="1" stop-color="#10b981"/></linearGradient>'
             '<filter id="s" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#1b2559" flood-opacity=".25"/></filter></defs>'
             '<g filter="url(#s)"><rect x="10" y="10" width="500" height="340" rx="18" fill="#fff"/></g>'
             '<path d="M10 28 A18 18 0 0 1 28 10 H492 A18 18 0 0 1 510 28 V44 H10 Z" fill="#eef0f7"/>'
             '<circle cx="30" cy="27" r="5" fill="#ef4444"/><circle cx="48" cy="27" r="5" fill="#f59e0b"/><circle cx="66" cy="27" r="5" fill="#10b981"/>'
             '<rect x="30" y="62" width="145" height="62" rx="14" fill="url(#k1)"/>'
             '<rect x="187" y="62" width="145" height="62" rx="14" fill="url(#k2)"/>'
             '<rect x="344" y="62" width="145" height="62" rx="14" fill="url(#k3)"/>'
             '<rect x="46" y="80" width="60" height="9" rx="4" fill="#fff" opacity=".7"/><rect x="46" y="98" width="86" height="14" rx="6" fill="#fff"/>'
             '<rect x="203" y="80" width="60" height="9" rx="4" fill="#fff" opacity=".7"/><rect x="203" y="98" width="86" height="14" rx="6" fill="#fff"/>'
             '<rect x="360" y="80" width="60" height="9" rx="4" fill="#fff" opacity=".7"/><rect x="360" y="98" width="86" height="14" rx="6" fill="#fff"/>'
             '<rect x="30" y="140" width="290" height="190" rx="14" fill="#f6f8fc"/>'
             '<rect x="56" y="262" width="34" height="48" rx="6" fill="#c7d2fe"/><rect x="106" y="230" width="34" height="80" rx="6" fill="#818cf8"/>'
             '<rect x="156" y="190" width="34" height="120" rx="6" fill="#ef4444"/><rect x="206" y="244" width="34" height="66" rx="6" fill="#818cf8"/>'
             '<rect x="256" y="274" width="34" height="36" rx="6" fill="#c7d2fe"/>'
             '<rect x="336" y="140" width="153" height="190" rx="14" fill="#f6f8fc"/>'
             '<circle cx="412" cy="226" r="42" fill="none" stroke="#10b981" stroke-width="20"/>'
             '<circle cx="412" cy="226" r="42" fill="none" stroke="#ef4444" stroke-width="20" stroke-dasharray="66 264" transform="rotate(-90 412 226)"/>'
             '<rect x="368" y="290" width="90" height="10" rx="5" fill="#dfe3ef"/></svg>')


def icon(glyph, c1, c2):
    """Rounded square icon with a white glyph (96 x 96 grid)."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><defs>'
            f'<linearGradient id="i" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/>'
            f'<stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
            f'<rect width="96" height="96" rx="26" fill="url(#i)"/>'
            f'<g fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">{glyph}</g></svg>')


GLYPHS = {
    "dashboard": '<path d="M28 70 V50 M48 70 V32 M68 70 V42"/><path d="M22 72 H74"/>',
    "search": '<circle cx="42" cy="42" r="16"/><path d="M54 54 L70 70"/><path d="M42 35 V43 M42 49 V49"/>',
    "upload": '<path d="M48 62 V30 M35 43 L48 30 L61 43"/><path d="M26 60 V70 H70 V60"/>',
    "models": '<circle cx="28" cy="48" r="7"/><circle cx="68" cy="28" r="7"/><circle cx="68" cy="68" r="7"/><circle cx="48" cy="48" r="7"/>'
              '<path d="M35 48 H41 M54 45 L62 32 M54 51 L62 64"/>',
    "data": '<ellipse cx="48" cy="30" rx="20" ry="8"/><path d="M28 30 V66 C28 71 37 74 48 74 C59 74 68 71 68 66 V30"/>'
            '<path d="M28 48 C28 53 37 56 48 56 C59 56 68 53 68 48"/>',
    "features": '<path d="M26 32 H70 M26 48 H70 M26 64 H70"/><circle cx="40" cy="32" r="5" fill="#fff"/>'
                '<circle cx="58" cy="48" r="5" fill="#fff"/><circle cx="36" cy="64" r="5" fill="#fff"/>',
    "alert": '<path d="M30 62 C34 58 34 52 34 44 C34 36 40 30 48 30 C56 30 62 36 62 44 C62 52 62 58 66 62 Z"/>'
             '<path d="M42 70 C44 74 52 74 54 70"/>',
}
ICONS = {
    "dashboard": icon(GLYPHS["dashboard"], "#4f46e5", "#7c3aed"),
    "search": icon(GLYPHS["search"], "#f59e0b", "#fb7185"),
    "upload": icon(GLYPHS["upload"], "#06b6d4", "#10b981"),
    "models": icon(GLYPHS["models"], "#7c3aed", "#ec4899"),
    "data": icon(GLYPHS["data"], "#4f46e5", "#06b6d4"),
    "features": icon(GLYPHS["features"], "#f59e0b", "#ef4444"),
    "alert": icon(GLYPHS["alert"], "#10b981", "#06b6d4"),
}
