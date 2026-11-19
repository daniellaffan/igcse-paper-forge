"""Line art for the labelled biology diagrams (black on white, textbook style).

Each diagram is a body of SVG drawn in a 440 x 300 box plus a list of labelled structures. The label
point (x, y) of every structure sits on the part it names; biology_diag.build_svg adds the letters and
leader lines. Tubes (airways, vessels, gut, tubules) are drawn as a dark stroke with a narrower white
stroke on top, so they read as hollow tubes and branches join cleanly.
"""
from collections import namedtuple

St = namedtuple("St", "name x y side func accept")
K = "currentColor"
GREY = "#d9d9d9"
LIGHT = "#efefef"


def st(name, x, y, side, func, accept=None):
    return St(name, x, y, side, func, accept)


def P(d, w=1.4, fill="none", extra=""):
    return f'<path d="{d}" stroke="{K}" stroke-width="{w}" fill="{fill}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'


def E(cx, cy, rx, ry, w=1.3, fill="none", extra=""):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" stroke="{K}" stroke-width="{w}" fill="{fill}" {extra}/>'


def C(cx, cy, r, w=1.2, fill="none", extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{K}" stroke-width="{w}" fill="{fill}" {extra}/>'


def tubes(items, fill="#fff"):
    """items: (path d, inner width). All outlines first, then all bores, so branches merge."""
    outer = "".join(f'<path d="{d}" stroke="{K}" stroke-width="{w + 2.8}" fill="none" stroke-linejoin="round" stroke-linecap="butt"/>' for d, w in items)
    inner = "".join(f'<path d="{d}" stroke="{fill}" stroke-width="{w}" fill="none" stroke-linejoin="round" stroke-linecap="square"/>' for d, w in items)
    return outer + inner


# ------------------------------------------------------------------ bacterial cell
BACT = "".join([
    P("M 95 150 C 95 98 150 82 220 82 C 290 82 345 98 345 150 C 345 202 290 218 220 218 C 150 218 95 202 95 150 Z", 1.2, extra='stroke-dasharray="5 3"'),
    P("M 107 150 C 107 106 156 94 220 94 C 284 94 333 106 333 150 C 333 194 284 206 220 206 C 156 206 107 194 107 150 Z", 2.6),
    P("M 115 150 C 115 112 160 101 220 101 C 280 101 325 112 325 150 C 325 188 280 199 220 199 C 160 199 115 188 115 150 Z", 1.1),
    P("M 190 135 C 205 115 245 120 238 140 C 232 158 200 150 210 135 C 222 120 262 140 250 160 C 240 176 196 170 196 152 C 196 140 218 138 226 150", 1.6),
    C(288, 128, 8, 1.4), C(282, 128, 0.1), C(158, 175, 6, 1.4),
    P("M 333 175 C 348 172 352 192 364 188 C 376 184 380 204 392 200", 1.6),
    "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="{K}"/>' for x, y in [(160, 130), (175, 150), (262, 180), (300, 165), (140, 150), (275, 110), (245, 185), (185, 185)]),
])
BACT_S = [st("capsule / slime coat", 220, 82, "L", "protects the cell / helps it stick to surfaces"),
          st("cell wall", 140, 99, "L", "gives support and stops the cell bursting"),
          st("cell membrane", 116, 158, "L", "controls what enters and leaves the cell"),
          st("circular DNA / chromosome", 238, 140, "R", "carries the genes that control the cell"),
          st("plasmid", 296, 128, "R", "carries extra genes, e.g. for antibiotic resistance"),
          st("flagellum", 372, 192, "R", "used for movement"),
          st("cytoplasm", 172, 196, "L", "where most chemical reactions take place")]


# ------------------------------------------------------------------ plant cell
def chloroplast(x, y, rot=0):
    g = "".join(f'<line x1="{x - 7 + 4 * i}" y1="{y - 2.5}" x2="{x - 7 + 4 * i}" y2="{y + 2.5}" stroke="{K}" stroke-width="1"/>' for i in range(4))
    return f'<g transform="rotate({rot} {x} {y})">{E(x, y, 13, 6.5, 1.3, LIGHT)}{g}</g>'


def mito(x, y, rot=0, s=1.0):
    rx, ry = 12 * s, 6 * s
    cr = P(f"M {x - rx + 3} {y} l 3 -4 l 3 7 l 3 -7 l 3 7 l 3 -7 l 3 7 l 3 -4", 0.9)
    return f'<g transform="rotate({rot} {x} {y})">{E(x, y, rx, ry, 1.3)}{cr}</g>'


PLANT = "".join([
    '<rect x="105" y="35" width="230" height="235" rx="8" stroke="currentColor" fill="#efefef" stroke-width="1.3"/>',
    '<rect x="113" y="43" width="214" height="219" rx="5" stroke="currentColor" fill="#fff" stroke-width="1.3"/>',
    P("M 160 95 C 200 80 270 85 290 105 C 305 130 300 200 285 220 C 255 240 185 235 165 215 C 150 190 145 115 160 95 Z", 1.3, "#f6f6f6"),
    C(145, 72, 19, 1.5, LIGHT), C(148, 70, 6, 1, GREY),
    chloroplast(300, 68, 20), chloroplast(132, 140, 80), chloroplast(310, 160, -70), chloroplast(140, 235, 10), chloroplast(230, 248, 0),
    mito(296, 240, -20, 0.9), mito(215, 63, 0, 0.9),
    "".join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="{K}"/>' for x, y in [(190, 60), (250, 58), (128, 190), (315, 205), (180, 250)]),
])
PLANT_S = [st("nucleus", 145, 72, "L", "contains genetic material that controls the activities of the cell"),
           st("cell wall", 107, 120, "L", "made of cellulose; strengthens the cell and gives it support"),
           st("cell membrane", 114, 200, "L", "controls the movement of substances into and out of the cell"),
           st("chloroplast", 300, 68, "R", "absorbs light energy for photosynthesis"),
           st("vacuole", 240, 160, "R", "contains cell sap; keeps the cell firm / turgid"),
           st("mitochondrion", 296, 240, "R", "site of aerobic respiration"),
           st("cytoplasm", 312, 112, "R", "where most chemical reactions take place")]

ANIMAL = "".join([
    P("M 115 150 C 108 80 200 45 280 62 C 350 78 360 170 330 215 C 300 258 200 262 150 232 C 125 216 117 185 115 150 Z", 1.6, "#fbfbfb"),
    C(232, 148, 32, 1.5, LIGHT), C(236, 144, 9, 1, GREY),
    mito(165, 115, 30), mito(292, 205, -15), mito(180, 210, 10),
    "".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="{K}"/>' for x, y in [(280, 100), (287, 110), (296, 101), (150, 165), (158, 172), (305, 150), (268, 238)]),
])
ANIMAL_S = [st("cell membrane", 117, 150, "L", "controls the movement of substances into and out of the cell"),
            st("mitochondrion", 165, 115, "L", "site of aerobic respiration"),
            st("cytoplasm", 140, 195, "L", "where most chemical reactions take place"),
            st("nucleus", 258, 138, "R", "contains genetic material that controls the activities of the cell"),
            st("ribosome", 287, 110, "R", "site of protein synthesis")]


# ------------------------------------------------------------------ leaf section
def _leaf():
    out = [P("M 70 38 L 370 38", 3.5)]                                                     # upper cuticle
    out += [f'<rect x="{70 + i * 30}" y="40" width="30" height="16" stroke="{K}" fill="#fff" stroke-width="1"/>' for i in range(10)]
    for i in range(15):                                                                      # palisade
        x = 72 + i * 19.7
        out.append(f'<rect x="{x:.1f}" y="58" width="16" height="54" rx="6" stroke="{K}" fill="#fff" stroke-width="1"/>')
        out += [E(x + 8, y, 3.2, 2, 0.8, GREY) for y in (70, 84, 98)]
    sp = [(95, 135), (130, 128), (165, 140), (275, 130), (310, 138), (348, 128), (85, 172), (120, 168), (150, 182),
          (290, 172), (325, 178), (355, 165), (105, 200), (160, 205), (300, 205), (345, 200)]
    out += [P(f"M {x - 13} {y} C {x - 13} {y - 12} {x + 13} {y - 13} {x + 13} {y} C {x + 14} {y + 12} {x - 12} {y + 12} {x - 13} {y} Z", 1, "#fff") for x, y in sp]
    out.append(C(220, 168, 30, 1.3, "#fff"))                                                # vascular bundle
    out += [C(x, y, 5, 1.1, "#fff") for x, y in [(208, 155), (222, 152), (234, 158), (213, 168), (228, 168)]]
    out += [C(x, y, 2.6, 0.8) for x, y in [(210, 183), (220, 186), (230, 182)]]
    out += [f'<rect x="{70 + i * 30}" y="222" width="30" height="16" stroke="{K}" fill="#fff" stroke-width="1"/>' for i in range(10) if i not in (6, 7)]
    out += [f'<rect x="250" y="222" width="12" height="16" stroke="{K}" fill="#fff" stroke-width="1"/>', f'<rect x="298" y="222" width="32" height="16" stroke="{K}" fill="#fff" stroke-width="1"/>']
    out += [P("M 262 222 C 276 220 278 238 262 238 Z", 1.3, GREY), P("M 298 222 C 284 220 282 238 298 238 Z", 1.3, GREY)]   # guard cells
    out.append(P("M 70 240 L 370 240", 2.5))
    return "".join(out)


LEAF = _leaf()
LEAF_S = [st("waxy cuticle", 120, 38, "L", "reduces water loss by evaporation"),
          st("upper epidermis", 100, 50, "L", "transparent, so light passes through to the mesophyll"),
          st("palisade mesophyll cell", 100, 88, "L", "contains many chloroplasts; main site of photosynthesis"),
          st("spongy mesophyll", 120, 168, "L", "has air spaces that allow gases to diffuse"),
          st("xylem / vein", 222, 152, "R", "transports water and mineral ions to the leaf"),
          st("air space", 255, 185, "R", "allows carbon dioxide to diffuse to cells"),
          st("guard cell", 293, 230, "R", "opens and closes the stoma")]


# ------------------------------------------------------------------ digestive system
GUT = "".join([
    tubes([("M 222 168 C 205 175 190 185 175 192", 7),
           ("M 160 196 L 290 196 C 304 196 304 212 290 212 L 160 212 C 146 212 146 228 160 228 L 290 228 C 304 228 304 244 290 244 L 160 244 C 146 244 140 252 128 250", 7)]),
    tubes([("M 128 268 L 128 186 Q 128 176 138 176 L 322 176 Q 332 176 332 186 L 332 245 C 332 270 270 258 250 272 L 250 298", 16)]),
    tubes([("M 214 8 L 214 82", 9)]),
    P("M 210 80 C 240 52 312 64 306 104 C 300 136 258 148 234 134 C 222 127 216 112 210 80 Z", 1.5, LIGHT),
    P("M 232 133 L 222 160", 6, extra='stroke-opacity="0"'),
    tubes([("M 238 138 C 230 150 226 158 222 168", 7)]),
    P("M 218 150 C 245 142 300 140 322 149 C 324 158 300 162 272 160 C 246 159 228 162 218 150 Z", 1.3, GREY),
    P("M 88 74 C 130 48 205 58 222 82 C 214 104 172 124 128 120 C 98 117 82 98 88 74 Z", 1.5, "#e4e4e4"),
    E(176, 120, 10, 7, 1.2, "#fff"),
])
GUT_S = [st("oesophagus", 214, 30, "L", "carries food from the mouth to the stomach by peristalsis"),
         st("liver", 120, 92, "L", "makes bile"),
         st("large intestine / colon", 128, 220, "L", "absorbs water from undigested food"),
         st("rectum", 250, 288, "L", "stores faeces"),
         st("stomach", 280, 100, "R", "produces protease and hydrochloric acid / churns food"),
         st("pancreas", 305, 152, "R", "produces amylase, protease and lipase"),
         st("small intestine", 270, 212, "R", "completes digestion and absorbs soluble food molecules")]


# ------------------------------------------------------------------ thorax (lungs)
def _thorax():
    out = []
    # chest wall: ribs in section with intercostal muscles between them
    ry = [70, 100, 130, 160, 190, 220]
    for side, x in (("L", 78), ("R", 362)):
        for i, y in enumerate(ry):
            out.append(E(x, y, 8, 10, 1.3, GREY))
            if i < len(ry) - 1:
                for k in range(4):
                    yy = y + 12 + k * 4
                    out.append(f'<line x1="{x - 6}" y1="{yy}" x2="{x + 6}" y2="{yy + 3}" stroke="{K}" stroke-width="1.1"/>')
    # lungs
    out.append(P("M 200 72 C 170 58 130 70 108 110 C 92 150 94 205 102 238 C 140 228 180 228 204 240 C 206 200 205 120 200 72 Z", 1.6, LIGHT))
    out.append(P("M 240 72 C 270 58 310 70 332 110 C 348 150 346 205 338 238 C 300 228 268 226 244 236 C 250 214 262 196 252 178 C 240 160 240 120 240 72 Z", 1.6, LIGHT))
    # airways
    tr = [("M 220 6 L 220 92", 16), ("M 220 92 L 180 122", 11), ("M 220 92 L 260 122", 11),
          ("M 180 122 L 150 150", 6), ("M 180 122 L 175 170", 6), ("M 260 122 L 292 150", 6), ("M 260 122 L 268 172", 6),
          ("M 150 150 L 128 168", 3), ("M 150 150 L 145 182", 3), ("M 175 170 L 160 200", 3), ("M 175 170 L 188 205", 3),
          ("M 292 150 L 312 170", 3), ("M 292 150 L 296 182", 3), ("M 268 172 L 280 205", 3), ("M 268 172 L 254 198", 3)]
    out.append(tubes(tr, LIGHT))
    out += [f'<line x1="{213}" y1="{y}" x2="{227}" y2="{y}" stroke="{K}" stroke-width="1.2"/>' for y in range(14, 88, 9)]   # cartilage rings
    # alveoli clusters at the ends of bronchioles
    for cx, cy in [(126, 171), (144, 186), (159, 204), (190, 209), (314, 173), (296, 186), (281, 209), (253, 202)]:
        for dx, dy in [(0, 0), (-5, 3), (5, 3), (0, 6), (-3, -3), (4, -3)]:
            out.append(C(cx + dx, cy + dy, 3, 0.8, "#fff"))
    # diaphragm (two domes under the lungs)
    out.append(P("M 70 262 C 95 238 150 222 205 244 C 215 250 225 250 235 244 C 290 222 345 238 370 262", 4))
    return "".join(out)


THORAX = _thorax()
THORAX_S = [st("trachea", 220, 40, "L", "carries air to and from the lungs; held open by rings of cartilage"),
            st("bronchus", 197, 108, "L", "carries air into each lung"),
            st("rib", 78, 130, "L", "protects the lungs; moves up and out when breathing in"),
            st("alveolus / air sac", 144, 189, "L", "site of gas exchange"),
            st("bronchiole", 284, 143, "R", "carries air to the alveoli"),
            st("intercostal muscle", 362, 178, "R", "contracts to move the ribs up and out during inhalation"),
            st("diaphragm", 320, 240, "R", "contracts and flattens to increase the volume of the thorax")]


# ------------------------------------------------------------------ heart
def _heart():
    out = []
    # great vessels (behind the heart outline)
    out.append(tubes([("M 132 8 L 132 112", 22),                                             # vena cava
                      ("M 250 112 L 250 52 C 250 18 300 12 330 22 C 352 30 356 48 356 70", 20),   # aorta arch
                      ("M 205 112 L 205 72 C 205 52 190 40 168 36", 18),                     # pulmonary artery
                      ("M 330 128 L 395 120", 12), ("M 334 150 L 395 156", 12)], "#fff"))    # pulmonary veins
    # outer wall
    out.append(P("M 205 100 C 150 92 108 112 110 162 C 112 220 172 266 236 292 C 300 266 346 220 340 160 C 337 120 305 98 262 102 Z", 1.8, GREY))
    # chambers (white cavities); left ventricle wall is thicker than the right
    out.append(P("M 122 118 C 140 106 190 106 212 114 L 212 168 L 122 168 Z", 1.3, "#fff"))          # right atrium
    out.append(P("M 244 114 C 270 106 318 108 330 124 L 330 162 L 244 162 Z", 1.3, "#fff"))          # left atrium
    out.append(P("M 122 176 L 212 176 L 214 262 C 175 245 132 214 122 176 Z", 1.3, "#fff"))          # right ventricle
    out.append(P("M 252 176 L 314 176 C 312 216 290 244 256 258 Z", 1.3, "#fff"))                   # left ventricle
    # valves and tendons
    for x0, x1 in ((122, 212), (252, 314)):
        m = (x0 + x1) / 2
        out.append(P(f"M {x0 + 6} 170 L {m - 6} 186 M {x1 - 6} 170 L {m + 6} 186", 1.6))
        out.append(P(f"M {m - 6} 186 L {m - 2} 215 M {m + 6} 186 L {m + 2} 215", 0.7))
    return "".join(out)


HEART = _heart()
HEART_S = [st("vena cava", 132, 40, "L", "brings deoxygenated blood from the body to the heart"),
           st("right atrium", 160, 140, "L", "receives deoxygenated blood from the body"),
           st("right ventricle", 168, 222, "L", "pumps deoxygenated blood to the lungs"),
           st("pulmonary artery", 186, 40, "L", "carries deoxygenated blood to the lungs"),
           st("aorta", 300, 18, "R", "carries oxygenated blood to the body"),
           st("pulmonary vein", 372, 123, "R", "brings oxygenated blood from the lungs"),
           st("left ventricle", 282, 210, "R", "has a thick muscular wall; pumps oxygenated blood to the body"),
           st("septum", 232, 230, "R", "separates oxygenated and deoxygenated blood")]


# ------------------------------------------------------------------ nephron
def _neph():
    out = []
    out.append(P("M 104 46 C 60 46 52 112 104 114 C 118 114 126 106 130 98", 2.4))          # Bowman's capsule (outer wall)
    out.append(P("M 104 58 C 72 58 68 102 104 102 C 112 102 118 98 122 92", 1.2))
    out.append(P("M 96 64 c 14 -6 22 10 10 16 c -12 6 -20 -8 -6 -12 c 12 -4 18 12 6 18 c -10 4 -16 -8 -6 -10", 2))   # glomerulus
    out.append(tubes([("M 70 50 L 92 66", 4), ("M 70 104 L 94 86", 3)]))                  # afferent / efferent arterioles
    out.append(tubes([
        ("M 128 96 C 150 104 140 130 165 132 C 190 134 178 104 200 106 C 222 108 214 134 234 140 L 234 262 C 234 282 262 282 262 262 L 262 160 "
         "C 262 140 284 152 296 132 C 306 116 322 122 336 108 L 350 100", 9),
        ("M 362 20 L 362 296", 14), ("M 350 100 L 362 100", 9)]))
    return "".join(out)


NEPH = _neph()
NEPH_S = [st("glomerulus", 104, 72, "L", "knot of capillaries where ultrafiltration happens"),
          st("Bowman's capsule", 60, 82, "L", "collects the glomerular filtrate"),
          st("proximal convoluted tubule", 165, 132, "L", "selective reabsorption of glucose"),
          st("loop of Henle", 248, 280, "L", "helps to concentrate the urine / reabsorbs water"),
          st("distal convoluted tubule", 300, 128, "R", "adjusts the ion content of the blood"),
          st("collecting duct", 362, 210, "R", "water is reabsorbed here under the control of ADH")]


# ------------------------------------------------------------------ eye (horizontal section)
EYE = "".join([
    P("M 150 72 C 210 22 330 30 362 120 C 378 168 352 246 290 268 C 230 288 168 262 150 228", 2.6),      # sclera
    P("M 158 82 C 214 40 320 46 350 124 C 364 166 342 236 288 254 C 236 272 176 250 160 220", 1.2),     # choroid / retina
    P("M 150 72 C 108 100 108 200 150 228", 1.6),                                                        # cornea
    P("M 146 104 L 146 136 M 146 164 L 146 196", 4),                                                     # iris
    E(168, 150, 13, 34, 1.4, LIGHT),                                                                     # lens
    E(170, 98, 7, 9, 1.2, GREY), E(170, 202, 7, 9, 1.2, GREY),                                          # ciliary muscle
    P("M 168 116 L 170 107 M 163 117 L 166 107 M 173 117 L 174 107 M 168 184 L 170 193 M 163 183 L 166 193 M 173 183 L 174 193", 0.8),  # suspensory ligaments
    P("M 358 150 c -4 -4 -8 -4 -8 0 c 0 4 4 4 8 0", 1.2),                                               # fovea pit
    tubes([("M 348 178 L 392 184", 18)]),                                                                # optic nerve
])
EYE_S = [st("cornea", 118, 150, "L", "refracts / bends light entering the eye"),
         st("iris", 146, 120, "L", "controls the size of the pupil"),
         st("lens", 168, 150, "L", "focuses light onto the retina"),
         st("suspensory ligament", 167, 188, "L", "attaches the lens to the ciliary muscle"),
         st("ciliary muscle", 170, 204, "L", "contracts or relaxes to change the shape of the lens"),
         st("retina", 330, 80, "R", "contains receptor cells (rods and cones) that detect light"),
         st("fovea", 352, 150, "R", "part of the retina with most cones; gives sharp vision"),
         st("optic nerve", 380, 182, "R", "carries impulses from the retina to the brain")]


# ------------------------------------------------------------------ insect-pollinated flower (half flower)
FLOWER = "".join([
    P("M 220 298 L 220 222", 3),                                                                          # stalk
    P("M 190 218 C 200 232 240 232 250 218 C 248 206 192 206 190 218 Z", 1.3, GREY),                    # receptacle
    P("M 196 220 C 170 228 140 236 118 252 C 140 248 172 238 200 226 Z", 1.3, LIGHT),                   # sepals
    P("M 244 220 C 270 228 300 236 322 252 C 300 248 268 238 240 226 Z", 1.3, LIGHT),
    P("M 196 212 C 150 190 112 130 120 64 C 158 92 186 150 202 206 Z", 1.5, "#fff"),                     # petals
    P("M 244 212 C 290 190 328 130 320 64 C 282 92 254 150 238 206 Z", 1.5, "#fff"),
    P("M 204 214 C 196 196 200 176 212 170 L 228 170 C 240 176 244 196 236 214 Z", 1.5, LIGHT),         # ovary
    E(214, 192, 4, 5, 1, "#fff"), E(226, 192, 4, 5, 1, "#fff"), E(220, 204, 4, 5, 1, "#fff"),          # ovules
    P("M 216 170 L 217 92 M 224 170 L 223 92", 1.3),                                                     # style
    P("M 208 90 C 208 78 218 76 220 86 C 222 76 232 78 232 90 C 232 96 208 96 208 90 Z", 1.4, GREY),    # stigma
    P("M 205 210 C 196 170 186 130 178 102 M 235 210 C 244 170 254 130 262 102", 1.3),                  # filaments
    E(176, 96, 7, 11, 1.4, GREY, 'transform="rotate(-15 176 96)"'), E(264, 96, 7, 11, 1.4, GREY, 'transform="rotate(15 264 96)"'),
])
FLOWER_S = [st("petal", 140, 110, "L", "brightly coloured to attract insects"),
            st("anther", 176, 96, "L", "produces pollen grains (male gametes)"),
            st("filament", 190, 150, "L", "supports the anther"),
            st("sepal", 150, 240, "L", "protects the flower when it is a bud"),
            st("stigma", 225, 86, "R", "sticky surface that catches pollen"),
            st("style", 220, 130, "R", "connects the stigma to the ovary; pollen tube grows through it"),
            st("ovary", 236, 180, "R", "contains ovules; becomes the fruit"),
            st("ovule", 220, 204, "R", "contains the female gamete; becomes the seed")]


# ------------------------------------------------------------------ female reproductive system (front view)
FEM = "".join([
    tubes([("M 184 104 C 160 84 128 82 108 104 C 100 112 96 120 98 128", 6), ("M 256 104 C 280 84 312 82 332 104 C 340 112 344 120 342 128", 6)]),
    P("M 92 128 l -6 8 M 98 130 l 0 10 M 104 128 l 6 8 M 348 128 l 6 8 M 342 130 l 0 10 M 336 128 l -6 8", 1.2),   # fimbriae
    E(100, 158, 22, 14, 1.4, LIGHT), E(340, 158, 22, 14, 1.4, LIGHT),                                    # ovaries
    C(94, 156, 4, 0.9, "#fff"), C(108, 162, 3, 0.9, "#fff"), C(336, 154, 4, 0.9, "#fff"),
    P("M 176 100 C 176 170 194 214 206 226 L 206 246 L 234 246 L 234 226 C 246 214 264 170 264 100 C 240 92 200 92 176 100 Z", 1.8, GREY),  # uterus wall
    P("M 196 112 C 196 166 208 196 218 208 L 222 208 C 232 196 244 166 244 112 C 228 108 212 108 196 112 Z", 1.2, "#fff"),               # cavity
    P("M 196 112 C 196 166 208 196 218 208", 3.5, extra='stroke-opacity="0.45"'), P("M 244 112 C 244 166 232 196 222 208", 3.5, extra='stroke-opacity="0.45"'),  # lining
    P("M 218 208 L 218 246 M 222 208 L 222 246", 1),
    P("M 204 246 L 200 298 M 236 246 L 240 298", 1.8), P("M 212 248 L 210 298 M 228 248 L 230 298", 0.8),   # vagina
])
FEM_S = [st("ovary", 100, 158, "L", "produces eggs and the hormones oestrogen and progesterone"),
         st("oviduct / fallopian tube", 140, 86, "L", "carries the egg to the uterus; fertilisation happens here"),
         st("cervix", 207, 238, "L", "ring of muscle at the entrance to the uterus"),
         st("vagina", 210, 275, "L", "receives sperm during intercourse"),
         st("uterus", 256, 150, "R", "where the embryo implants and develops"),
         st("uterus lining", 240, 140, "R", "thickens to receive an embryo / forms part of the placenta")]


# ------------------------------------------------------------------ industrial fermenter
FERM = "".join([
    '<rect x="186" y="6" width="68" height="26" rx="3" stroke="currentColor" fill="#d9d9d9" stroke-width="1.5"/>',   # motor
    P("M 120 70 C 120 52 140 42 160 42 L 280 42 C 300 42 320 52 320 70 L 320 250 C 320 268 300 280 280 280 L 160 280 C 140 280 120 268 120 250 Z", 2.2, LIGHT),  # jacket (outer)
    P("M 134 74 C 134 60 148 54 164 54 L 276 54 C 292 54 306 60 306 74 L 306 246 C 306 260 292 268 276 268 L 164 268 C 148 268 134 260 134 246 Z", 1.8, "#fff"),   # vessel
    P("M 150 118 C 180 112 260 112 290 118", 0.8, extra='stroke-dasharray="4 3"'),                  # liquid surface
    P("M 220 32 L 220 236", 2.2),                                                                     # shaft
    '<rect x="190" y="150" width="60" height="7" fill="currentColor"/>', '<rect x="190" y="210" width="60" height="7" fill="currentColor"/>',  # paddles
    tubes([("M 60 252 L 168 252 L 168 244 L 272 244", 5)]),                                           # air in -> sparger ring
    "".join(f'<circle cx="{x}" cy="244" r="1.3" fill="currentColor"/>' for x in range(180, 270, 12)),
    tubes([("M 160 4 L 160 54", 7), ("M 286 4 L 286 54", 6)]),                                       # nutrient inlet, waste gas
    tubes([("M 320 230 L 380 230", 6), ("M 320 84 L 380 84", 6)]),                                  # water out/in (jacket)
    P("M 306 110 L 268 110 L 268 128", 2.2), C(268, 132, 4, 1.4, GREY), P("M 306 110 L 340 110 L 360 104", 1.2),   # probe
    tubes([("M 220 268 L 220 298", 7)]), '<rect x="212" y="284" width="16" height="6" fill="currentColor"/>',          # outlet + valve
])
FERM_S = [st("nutrient inlet", 160, 30, "L", "adds nutrients / glucose for respiration and growth"),
          st("stirring paddles", 205, 153, "L", "mix the contents so nutrients and temperature are even"),
          st("air inlet / sparger", 90, 252, "L", "supplies oxygen for aerobic respiration"),
          st("motor shaft", 220, 80, "R", "turns the stirrer"),
          st("water jacket", 313, 170, "R", "carries cold water to remove heat and keep the temperature constant"),
          st("temperature / pH probe", 268, 132, "R", "monitors conditions so they stay at the optimum"),
          st("outlet for product", 220, 292, "R", "allows the product to be removed")]
