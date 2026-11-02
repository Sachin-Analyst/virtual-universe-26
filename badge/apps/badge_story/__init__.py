# BADGE STORY - PHASE 1 + PHASE 2: press any button -> loading -> three apps
# LinkedIn app: intro animation -> small logo + name -> C back to menu
# GitHub app: logo intro -> SACHIN / DATA ANALYST card -> C back to menu
# Universe 26 opens the animated congratulations screen

import math
import os
import random
import sys

# Keep the app's artwork rooted in its own folder in the badge runtime.
APP_DIR = "/system/apps/badge_story"
os.chdir(APP_DIR)
sys.path.insert(0, APP_DIR)

badge.mode(LORES | VSYNC)

# If everything runs too fast, raise this. If too slow, lower it.
TICKS_PER_SECOND = 1000

# True = five tiny squares at the top-left light up when the badge sees a button
# press. Order: A, B, C, UP, DOWN. Use this if the buttons seem to do nothing.
DEBUG = False

# ---------- colours (red, green, blue: each 0 to 255) ----------
SPACE_BG = (9, 12, 30)        # dark space background
CREAM = (238, 233, 196)
ICE = (150, 215, 255)
GOLD = (255, 200, 40)
WHITE = (255, 255, 255)
DARK = (28, 45, 78)           # dark navy  -> "Vishnu Ram"
LI_BLUE = (41, 103, 176)      # LinkedIn blue -> "Sachin"
ACCENT = (214, 92, 28)        # warm orange -> "Data Analyst"
GH_LIGHT = (243, 246, 242)    # GitHub card / LinkedIn off-white background
GH_BLACK = (8, 8, 8)
UNI_PURPLE = (112, 106, 255)  # GitHub Universe purple
GREENS = [(30, 38, 56), (14, 68, 41), (0, 109, 50), (38, 166, 65), (57, 211, 83)]

# ---------- letter shapes (5 wide x 7 tall; g, y have an 8th row for the descender) ----------
FONT = {
  " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
  "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
  "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
  "C": [".####", "#....", "#....", "#....", "#....", "#....", ".####"],
  "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
  "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
  "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
  "G": [".####", "#....", "#....", "#.###", "#...#", "#...#", ".###."],
  "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
  "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
  "J": ["..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."],
  "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
  "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
  "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
  "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
  "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
  "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
  "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
  "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
  "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
  "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
  "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
  "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
  "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"],
  "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
  "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
  "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
  "0": [".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."],
  "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
  "2": [".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"],
  "3": ["#####", "...#.", "..#..", "...#.", "....#", "#...#", ".###."],
  "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
  "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
  "6": ["..##.", ".#...", "#....", "####.", "#...#", "#...#", ".###."],
  "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
  "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
  "9": [".###.", "#...#", "#...#", ".####", "....#", "...#.", ".##.."],
  "%": ["##..#", "##..#", "...#.", "..#..", ".#...", "#..##", "#..##"],
  ".": [".....", ".....", ".....", ".....", ".....", ".....", "..#.."],
  # lowercase, for "Vishnu Ram" / "Sachin" / "Data Analyst" and the LinkedIn words
  "a": [".....", ".....", ".###.", "....#", ".####", "#...#", ".####"],
  "c": [".....", ".....", ".###.", "#...#", "#....", "#...#", ".###."],
  "d": ["....#", "....#", ".####", "#...#", "#...#", "#...#", ".####"],
  "e": [".....", ".....", ".###.", "#...#", "#####", "#....", ".###."],
  "f": ["..##.", ".#...", "####.", ".#...", ".#...", ".#...", ".#..."],
  "g": [".....", ".....", ".###.", "#...#", "#...#", ".####", "....#", ".###."],
  "h": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "#...#"],
  "i": ["..#..", ".....", "..#..", "..#..", "..#..", "..#..", "..#.."],
  "k": ["#....", "#....", "#..#.", "#.#..", "##...", "#.#..", "#..#."],
  "l": [".##..", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
  "m": [".....", ".....", "##.#.", "#.#.#", "#.#.#", "#...#", "#...#"],
  "n": [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#"],
  "o": [".....", ".....", ".###.", "#...#", "#...#", "#...#", ".###."],
  "r": [".....", ".....", "#.##.", "##..#", "#....", "#....", "#...."],
  "s": [".....", ".....", ".####", "#....", ".###.", "....#", "####."],
  "t": [".#...", ".#...", "####.", ".#...", ".#...", ".#..#", "..##."],
  "u": [".....", ".....", "#...#", "#...#", "#...#", "#..##", ".##.#"],
  "w": [".....", ".....", "#...#", "#...#", "#.#.#", "#.#.#", ".#.#."],
  "y": [".....", ".....", "#...#", "#...#", "#...#", ".####", "....#", ".###."],
}

GLYPH = {}
for ch in FONT:
  rows = FONT[ch]
  if len(rows) == 7:
    rows = rows + ["....."]
  blocks_list = []
  for r in range(8):
    row = rows[r]
    c = 0
    while c < 5:
      if row[c] == "#":
        c2 = c
        while c2 < 5 and row[c2] == "#":
          c2 += 1
        blocks_list.append(shape.rectangle(c, r, c2 - c, 1))
        c = c2
      else:
        c += 1
  GLYPH[ch] = blocks_list

# ---------- the white "in" of the LinkedIn logo, for the menu card (44 x 44 pixel map) ----------
def pad(row, n):
  return row + "." * (n - len(row))

IN_PREFIX = (
  [""] * 6 +
  ["........####", ".......######", "......#######", "......########",
   "......########", "......#######", ".......#####", ".........##"] +
  ["", ""] +
  [".......######....######...#######",
   "......#######....######..##########",
   "......#######....###################",
   "......#######....###################",
   "......#######....####################",
   "......#######....####################",
   "......#######....########.....#######",
   "......#######....#######......#######"] +
  ["......#######....#######.......######"] * 13 +
  [""] * 7
)
IN_BLOCKS = []
for y in range(44):
  row = pad(IN_PREFIX[y], 44)
  x = 0
  while x < 44:
    if row[x] == "#":
      x2 = x
      while x2 < 44 and row[x2] == "#":
        x2 += 1
      IN_BLOCKS.append(shape.rectangle(x, y, x2 - x, 1.04))
      x = x2
    else:
      x += 1

# ---------- the small white "in" for the 32 pixel LinkedIn logo (x, y, width, height) ----------
IN32_RECTS = [
  (6, 5, 3, 1), (5, 6, 5, 3), (6, 9, 3, 1),                   # the dot of the "i"
  (5, 12, 5, 15),                                              # stem of the "i"
  (12, 12, 5, 15),                                             # left stem of the "n"
  (18, 12, 5, 1), (17, 13, 8, 1), (17, 14, 9, 2), (17, 16, 2, 1),   # arch of the "n"
  (21, 16, 5, 11),                                             # right stem of the "n"
]
IN32_BLOCKS = [shape.rectangle(r[0], r[1], r[2], r[3]) for r in IN32_RECTS]

# ---------- the white cat of the GitHub logo (56 x 56 pixel map) ----------
CAT = [
  "", "", "", "", "", "", "", "", "", "", "",
  "..............#..........................##",
  ".............#####....................#####",
  ".............#######......####......#######",
  ".............###############################",
  ".............###############################",
  ".............###############################",
  ".............###############################",
  ".............##############################",
  ".............##############################",
  "............################################",
  "............#################################",
  "...........##################################",
  "...........##################################",
  "...........###################################",
  "..........####################################",
  "..........####################################",
  "..........####################################",
  "..........####################################",
  "..........####################################",
  "..........####################################",
  "...........###################################",
  "...........##################################",
  "...........##################################",
  "...........##################################",
  "............################################",
  "............################################",
  ".............##############################",
  "..............############################",
  "...............##########################",
  "........##.......######################",
  "........###.........################",
  ".........###..........############",
  "..........###.........############",
  "...........###.......##############",
  "...........####......##############",
  "............####....###############",
  "............#######################",
  ".............######################",
  "..............#####################",
  ".....................##############",
  ".....................##############",
  ".....................##############",
  ".......................##########",
  "", "",
]
CAT_BLOCKS = []
for y in range(56):
  row = pad(CAT[y], 56)
  x = 0
  while x < 56:
    if row[x] == "#":
      x2 = x
      while x2 < 56 and row[x2] == "#":
        x2 += 1
      CAT_BLOCKS.append(shape.rectangle(x, y, x2 - x, 1.05))
      x = x2
    else:
      x += 1

# ---------- basic shapes ----------
CIRCLE = shape.circle(0, 0, 1)
STAR = shape.star(0, 0, 5, 0.5, 1)
BOX_PARTS = [                 # a rounded square, size 1
  shape.rectangle(-0.5, -0.3, 1, 0.6),
  shape.rectangle(-0.3, -0.5, 0.6, 1),
  shape.circle(-0.3, -0.3, 0.2),
  shape.circle(0.3, -0.3, 0.2),
  shape.circle(-0.3, 0.3, 0.2),
  shape.circle(0.3, 0.3, 0.2),
]

# ---------- helpers ----------
def clamp01(u):
  return max(0.0, min(1.0, u))

def ease(u):
  u = clamp01(u)
  return u * u * (3 - 2 * u)

def lerp(a, b, u):
  return a + (b - a) * u

def mix(c, d, a):
  return (d[0] + (c[0] - d[0]) * a, d[1] + (c[1] - d[1]) * a, d[2] + (c[2] - d[2]) * a)

def rgb(c):
  return color.rgb(int(c[0]), int(c[1]), int(c[2]))

def pen(c, a=1.0, base=SPACE_BG):
  screen.pen = rgb(mix(c, base, clamp01(a)))

def text(s, cx, top, cell, col, a=1.0, base=SPACE_BG):
  # sharp pixel text, centred on cx. cell = size of each dot in pixels
  n = len(s)
  left = int(cx - (n * 6 - 1) * cell / 2)
  pen(col, a, base)
  for j in range(n):
    ch = s[j]
    if ch == " ":
      continue
    tf = (mat3().translate(left + (j * 6 + 2.5) * cell, top + 3.5 * cell)
          .scale(cell).translate(-2.5, -3.5))
    for b in GLYPH[ch]:
      b.transform = tf
      screen.shape(b)

def rbox(cx, cy, size, col, a, base=SPACE_BG):
  if size < 1:
    return
  pen(col, a, base)
  tf = mat3().translate(cx, cy).scale(size)
  for p in BOX_PARTS:
    p.transform = tf
    screen.shape(p)

# ---------- extra drawing helpers for the LinkedIn intro ----------
def draw_box(cx, cy, size, rot, col, a, base):
  if size < 0.5:
    return
  pen(col, a, base)
  tf = mat3().translate(cx, cy).rotate(rot).scale(size)
  for p in BOX_PARTS:
    p.transform = tf
    screen.shape(p)

def draw_letter(ch, xc, yc, cell, col, a, pop, base):
  if ch == " " or cell < 0.2:
    return
  pen(col, a, base)
  tf = mat3().translate(xc, yc).scale(cell * pop).translate(-2.5, -3.5)
  for b in GLYPH[ch]:
    b.transform = tf
    screen.shape(b)

def draw_crisp(ch, xc, yc, col, a, pop):
  # sharp letter for the name: xc and yc are whole numbers, every dot is T_CELL pixels
  if ch == " ":
    return
  pen(col, a, GH_LIGHT)
  tf = mat3().translate(xc, yc).scale(T_CELL * pop).translate(-2.5, -3.5)
  for b in GLYPH[ch]:
    b.transform = tf
    screen.shape(b)

def draw_tick(cx, cy, size, p, a):
  # a white tick that draws itself: first the short stroke, then the long one
  pen(WHITE, a, LI_BLUE)
  base_tf = mat3().translate(cx, cy).scale(size)
  p1 = ease(p * 2)
  p2 = ease(p * 2 - 1)
  ax = -0.26
  ay = 0.02
  bx = -0.08
  by = 0.24
  if p1 > 0.01:
    seg = shape.rectangle(0, -0.055, 0.284 * p1, 0.11)
    seg.transform = base_tf.translate(ax, ay).rotate(50.7)
    screen.shape(seg)
    dot = shape.circle(ax, ay, 0.055)
    dot.transform = mat3().translate(cx, cy).scale(size)
    screen.shape(dot)
  if p2 > 0.01:
    seg2 = shape.rectangle(0, -0.055, 0.584 * p2, 0.11)
    seg2.transform = mat3().translate(cx, cy).scale(size).translate(bx, by).rotate(-52)
    screen.shape(seg2)
    ang = -52 * 3.1416 / 180
    ex = bx + math.cos(ang) * 0.584 * p2
    ey = by + math.sin(ang) * 0.584 * p2
    for pt in ((bx, by), (ex, ey)):
      d2 = shape.circle(pt[0], pt[1], 0.055)
      d2.transform = mat3().translate(cx, cy).scale(size)
      screen.shape(d2)

def draw_in(alpha):
  # the white "in" on the small logo (32 grid, so it is drawn at 1 pixel per dot)
  pen(WHITE, alpha, LI_BLUE)
  tf = mat3().translate(80, LOGO_CY).scale(LOGO_S / 32).translate(-16, -16)
  for b in IN32_BLOCKS:
    b.transform = tf
    screen.shape(b)

# ---------- twinkling background stars ----------
random.seed(11)
TW = [(random.randint(2, 157), random.randint(2, 117),
       random.uniform(0, 6.28), random.choice((1, 1, 2))) for _ in range(30)]

def draw_twinkles(gt, strength):
  for tw in TW:
    b = (0.2 + 0.8 * (0.5 + 0.5 * math.sin(gt * 1.6 + tw[2]))) * strength
    pen(CREAM, b)
    screen.shape(shape.rectangle(tw[0], tw[1], tw[3], tw[3]))

# ---------- loading screen: a contribution-graph style grid ----------
COLS = 12
ROWS = 5
PITCH = 12
CELL = 9
GX0 = 10
GY0 = 38
random.seed(7)
LEVELS = []
STARTS = []
for r in range(ROWS):
  for c in range(COLS):
    LEVELS.append(random.choice([0, 1, 1, 2, 2, 3, 3, 4]))
    ft2 = (c + r * 0.7) / (COLS + ROWS * 0.7)
    STARTS.append(0.25 + ft2 * 2.4 + random.uniform(0, 0.15))
LOAD_END = 3.1                # loading finished, squares shrink away
LOAD_DONE = 3.55              # menu appears

def draw_loading(t, gt):
  draw_twinkles(gt, 0.5)
  text("LOADING", 80, 12, 2, CREAM)
  for r in range(ROWS):
    for c in range(COLS):
      i = r * COLS + c
      lv = LEVELS[i]
      size = CELL
      col = GREENS[0]
      s = t - STARTS[i]
      if s >= 0 and lv > 0:
        u = clamp01(s / 0.3)
        size = CELL * (0.6 + 0.4 * ease(u))
        col = mix(GREENS[lv], (230, 255, 230), ease(u))
      if t > LOAD_END:
        k = clamp01((t - LOAD_END - c * 0.02) / 0.25)
        size = size * (1 - ease(k))
      if size < 0.5:
        continue
      pen(col)
      screen.shape(shape.rectangle(GX0 + c * PITCH + (CELL - size) / 2,
                                   GY0 + r * PITCH + (CELL - size) / 2, size, size))
  pct = int(clamp01((t - 0.25) / 2.6) * 100)
  if t < LOAD_END:
    text(str(pct) + "%", 80, 104, 2, ICE)

# ---------- start screen ----------
def draw_start(t, gt):
  draw_twinkles(gt, 1.0)
  intro = ease(t / 0.8)
  pen(GOLD, intro)
  STAR.transform = mat3().translate(80, 22 + math.sin(gt * 1.8) * 2).scale(11).rotate(gt * 40)
  screen.shape(STAR)
  b = (0.6 + 0.4 * (0.5 + 0.5 * math.sin(gt * 3.0))) * intro
  text("PRESS ANY", 80, 42, 2, CREAM, b)
  text("BUTTON", 80, 60, 2, CREAM, b)
  text("TO BEGIN", 80, 84, 2, ICE, intro)

# ---------- menu ----------
CARD_X = [28, 80, 132]
CARD_Y = 50
NAMES = ["LINKEDIN", "GITHUB", "UNIVERSE 26"]
OPEN_BG = [LI_BLUE, GH_LIGHT, UNI_PURPLE]
OPEN_FG = [WHITE, GH_BLACK, CREAM]
PHASE_TXT = ["", "PHASE 4 GOES HERE", "PHASE 6 GOES HERE"]

def draw_card(i, cx, cy, size, dim, selected, gt):
  if size < 1:
    return
  if selected:
    rbox(cx, cy, size + 7, GOLD, 1.0)          # gold outline
  if i == 0:
    rbox(cx, cy, size, LI_BLUE, dim)
    pen(WHITE, dim)
    tf = mat3().translate(cx, cy).scale(size / 44).translate(-22, -22)
    for b in IN_BLOCKS:
      b.transform = tf
      screen.shape(b)
  elif i == 1:
    rbox(cx, cy, size, GH_LIGHT, dim)
    pen(GH_BLACK, dim)
    CIRCLE.transform = mat3().translate(cx, cy).scale(size * 0.4)
    screen.shape(CIRCLE)
    pen(GH_LIGHT, dim)
    tf = mat3().translate(cx, cy).scale(size * 0.8 / 56).translate(-28, -28)
    for b in CAT_BLOCKS:
      b.transform = tf
      screen.shape(b)
  else:
    rbox(cx, cy, size, UNI_PURPLE, dim)
    pen(CREAM, dim)
    spin = gt * 40 if selected else 0
    STAR.transform = mat3().translate(cx, cy).scale(size * 0.3).rotate(spin)
    screen.shape(STAR)

# ---------- Universe 26 congratulations screen ----------
CONGRATS_SKY = color.rgb(13, 17, 38)
CONGRATS_WHITE = color.rgb(255, 255, 255)
CONGRATS_DIM = color.rgb(120, 130, 175)
CONGRATS_FLAME = [
  color.rgb(255, 230, 120),
  color.rgb(255, 170, 60),
  color.rgb(240, 98, 70),
  color.rgb(163, 113, 247),
]
CONGRATS_GLYPH_CHARS = "@-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CONGRATS_FONTS = [
  ("assets/glyphs.png", [21, 9, 16, 9, 14, 14, 15, 14, 15, 13, 14, 15, 15, 15, 14, 15, 14, 9, 14, 15, 6, 6, 14, 6, 23, 15, 14, 15, 15, 9, 13, 9, 15, 14, 19, 14, 14, 12, 18, 16, 18, 17, 15, 14, 19, 18, 7, 10, 17, 13, 21, 18, 19, 16, 19, 17, 16, 15, 17, 18, 24, 18, 17, 15]),
  ("assets/glyphs_small.png", [14, 6, 11, 6, 9, 10, 10, 10, 10, 9, 10, 10, 10, 10, 9, 10, 9, 6, 10, 10, 4, 4, 10, 4, 16, 10, 10, 10, 10, 6, 9, 6, 10, 9, 13, 10, 9, 8, 12, 11, 12, 12, 10, 10, 13, 12, 4, 7, 12, 9, 14, 12, 13, 11, 13, 11, 11, 10, 12, 12, 16, 12, 12, 10]),
]
CONGRATS_TITLE = image.load("assets/title.png").spritesheet(1, 5).sprite(0, 0)
CONGRATS_SUBTITLE = image.load("assets/subtitle.png").spritesheet(1, 5).sprite(0, 0)
CONGRATS_MONA = [image.load("assets/mona_%d.png" % i) for i in range(5)]
CONGRATS_LOGIN = None
try:
  with open("github_login.txt") as f:
    login = f.read().strip()
  login = "".join(ch for ch in login if ch in CONGRATS_GLYPH_CHARS)
  CONGRATS_LOGIN = "@" + login.lstrip("@") if login else None
except OSError:
  pass

def congrats_name_line(login):
  if not login:
    return None
  for path, advances in CONGRATS_FONTS:
    width = sum(advances[CONGRATS_GLYPH_CHARS.index(ch)] for ch in login)
    if width <= 2 * 160 - 12 or path == CONGRATS_FONTS[-1][0]:
      break
  sheet = image.load(path).spritesheet(8, 8)
  while width > 2 * 160 - 12 and len(login) > 2:
    width -= advances[CONGRATS_GLYPH_CHARS.index(login[-1])]
    login = login[:-1]
  x = (2 * 160 - width) // 2 - 4
  result = []
  for ch in login:
    i = CONGRATS_GLYPH_CHARS.index(ch)
    result.append((sheet.sprite(i % 8, i // 8), x / 2))
    x += advances[i]
  return result

CONGRATS_NAME = congrats_name_line(CONGRATS_LOGIN)
CONGRATS_STARS = [
  [random.randint(0, 159), random.randint(0, 119), random.choice((4, 8, 15))]
  for _ in range(70)
]
CONGRATS_SPARKS = []

def draw_congrats_stars(dt):
  for star in CONGRATS_STARS:
    star[0] -= star[2] * dt
    if star[0] < 0:
      star[0] = 159 + random.randint(0, 12)
      star[1] = random.randint(0, 119)
    screen.pen = CONGRATS_WHITE if star[2] == 15 else CONGRATS_DIM
    screen.rectangle(int(star[0]), star[1], 1, 1)

def congrats_mona_path(t):
  x = 160 + 108 * math.sin(t / 1500)
  y = 160 + 16 * math.sin(t / 750)
  return x / 2, y / 2

def draw_congrats_sparks(dt):
  keep = []
  for particle in CONGRATS_SPARKS:
    particle[0] += particle[2] * dt
    particle[1] += particle[3] * dt
    particle[4] -= dt
    if particle[4] > 0:
      screen.pen = CONGRATS_FLAME[min(3, int((0.6 - particle[4]) * 6))]
      screen.rectangle(int(particle[0]), int(particle[1]), 1, 1)
      keep.append(particle)
  CONGRATS_SPARKS[:] = keep

def draw_congrats_mona(t, dt):
  x, y = congrats_mona_path(t)
  nx, _ = congrats_mona_path(t + 40)
  dx = nx - x
  speed = abs(dx)
  frame = 2 if speed < 0.4 else (1 if speed < 1.1 else 0)
  img = CONGRATS_MONA[frame]
  w = img.width / 2
  h = img.height / 2
  left = int(x - w / 2)
  top = int(y - h / 2)
  back = -1 if dx >= 0 else 1
  fx = x + back * w * 0.25
  fy = y + h * 0.42
  for _ in range(3):
    CONGRATS_SPARKS.append([
      fx + random.randint(-2, 2),
      fy + random.randint(-1, 1),
      back * random.randint(10, 25),
      random.randint(12, 30),
      0.6,
    ])
  draw_congrats_sparks(dt)
  if dx >= 0:
    screen.blit(img, rect(left, top, w, h))
  else:
    screen.blit(img, rect(left + w, top, -w, h))

def draw_universe_congrats(now, dt):
  screen.pen = CONGRATS_SKY
  screen.rectangle(0, 0, 160, 120)
  draw_congrats_stars(dt)
  draw_congrats_mona(now, dt)
  screen.blit(CONGRATS_TITLE, rect(0, 0, 160, 20))
  if CONGRATS_NAME:
    for glyph, x in CONGRATS_NAME:
      screen.blit(glyph, rect(int(x), 15, 16, 20))
  else:
    screen.font = font.ziplock
    screen.pen = CONGRATS_WHITE
    label = "Well done!"
    width, _ = screen.measure_text(label)
    screen.text(label, int((160 - width) / 2), 21)
  screen.blit(CONGRATS_SUBTITLE, rect(0, 27, 160, 20))

# ==============================================================
# LINKEDIN INTRO (rolling box -> L-I-N-K-E-D-I-N -> small logo + name)
# ==============================================================
WORDS = ["Learn", "Initiate", "Network", "Knowledge",
         "Engage", "Differentiate", "Influence", "Nurture"]
NAME_LINES = ["Vishnu Ram", "Sachin"]
NAME_COLS = [DARK, LI_BLUE]
ROLE_LINE = "Data Analyst"

S = 22                        # size of the small box
GAP = 8                       # space between a word and its box
MAXW = 160 - 12 - GAP - S     # widest a word may be
CELL_MAX = 2.2                # biggest letter size (short words use this)
GROUND = 60 + S / 2           # the box rolls along this line
N_FLIPS = 4                   # how many times the box flips before it lands
RC = 2.6                      # letter size in the LINKEDIN row
RB = 2.0                      # size of "IN" when it becomes the logo
LOGO_S = 32                   # logo size (small)
LOGO_CY = 25                  # logo height on screen

# name text: every dot is 2 x 2 pixels, so the letters stay sharp
T_CELL = 2
LINE_TOPS = [48, 66]          # top of "Vishnu Ram" and "Sachin"
DIV_Y = 86                    # divider line
ROLE_TOP = 94                 # top of "Data Analyst"

ROLL0 = 0.9                   # box starts rolling
PERIOD = 0.46                 # time per flip
FLIP_D = 0.42                 # time a flip takes
LG = 0.05                     # delay between letters of a word
HOLD = 0.6                    # how long a ticked word stays
LET_GAP = 0.14                # delay between LINKEDIN letters
LET_DUR = 0.55
NAME_LG = 0.05                # delay between letters of the name

def word_layout(w):
  cells = len(w) * 6 - 1
  cell = min(CELL_MAX, MAXW / cells)
  ww = cells * cell
  total = ww + GAP + S
  left = 80 - total / 2
  bx = left + ww + GAP + S / 2
  return (cell, left, bx)

WL = [word_layout(w) for w in WORDS]
BX = [item[2] for item in WL]
COUNT_W = len(WORDS)
START_X = BX[0] - N_FLIPS * S

ROLL_END = ROLL0 + (N_FLIPS - 1) * PERIOD + FLIP_D

WS = []
TICK0 = []
TICK1 = []
OUT0 = []
tc = ROLL_END + 0.2
for w in WORDS:
  WS.append(tc)
  tk0 = tc + len(w) * LG + 0.1
  tk1 = tk0 + 0.35
  o0 = tk1 + HOLD
  TICK0.append(tk0)
  TICK1.append(tk1)
  OUT0.append(o0)
  tc = o0 + 0.4

LETTERS = [w[0] for w in WORDS]
REV0 = OUT0[COUNT_W - 1] + 0.3
LAND = REV0 + 7 * LET_GAP + LET_DUR
REV1 = LAND + 0.7
LOGO0 = REV1 + 0.3
XFADE0 = REV1 + 1.3
XFADE1 = XFADE0 + 0.45

# name timing: line 1, line 2, divider, then the role
NAME0 = XFADE1 + 0.2
LINE_T0 = [NAME0, NAME0 + len(NAME_LINES[0]) * NAME_LG + 0.1]
DIV_T0 = LINE_T0[1] + len(NAME_LINES[1]) * NAME_LG + 0.1
ROLE_T0 = DIV_T0 + 0.35
FINAL_T = ROLE_T0 + len(ROLE_LINE) * NAME_LG + 0.3     # everything is on screen from here

X0 = 80 - (8 * 6 - 1) * RC / 2
SLOT_X = [X0 + (6 * j + 2.5) * RC for j in range(8)]
IN_X = [80 - 3 * RB, 80 + 3 * RB]

def line_left(s):
  return 80 - (len(s) * 6 - 1) * T_CELL // 2

def draw_line(s, top, t_start, col, it):
  left = line_left(s)
  for j in range(len(s)):
    a = ease((it - t_start - j * NAME_LG) / 0.15)
    if a > 0:
      xc = left + j * 6 * T_CELL + 5
      yc = top + 7 + int((1 - a) * 3)
      draw_crisp(s[j], xc, yc, col, a, 1.0)

def box_x(it):
  x = BX[0]
  for k in range(COUNT_W - 1):
    s0 = OUT0[k] + 0.15
    if it >= s0:
      x = lerp(BX[k], BX[k + 1], ease((it - s0) / 0.3))
  return x

def roll_state(it):
  s = it - ROLL0
  if s < 0:
    return (START_X, 60, 0)
  f = int(s / PERIOD)
  if f >= N_FLIPS:
    f = N_FLIPS - 1
  u = (s - f * PERIOD) / FLIP_D
  if u > 1:
    u = 1
  th = 90 * ease(u)
  th_r = th * 3.1416 / 180
  x0 = START_X + f * S
  px = x0 + S / 2
  vx = -S / 2
  vy = -S / 2
  cx = px + vx * math.cos(th_r) - vy * math.sin(th_r)
  cy = GROUND + vx * math.sin(th_r) + vy * math.cos(th_r)
  return (cx, cy, th)

def draw_intro(it):
  if it < REV0 + 0.4:
    if it < ROLL_END:
      cx, cy, ang = roll_state(it)
      size = S * ease(it / 0.5)
    else:
      cx = box_x(it)
      cy = 60
      ang = 0
      size = S
      for k in range(COUNT_W):
        d = it - TICK1[k]
        if d >= 0 and d < 0.25:
          size = S * (1 + 0.1 * math.sin(3.1416 * d / 0.25))
      if it >= REV0:
        size = S * (1 - ease((it - REV0) / 0.4))
    draw_box(cx, cy, size, ang, LI_BLUE, 1.0, GH_LIGHT)

    for k in range(COUNT_W):
      if it < WS[k] or it > OUT0[k] + 0.3:
        continue
      w = WORDS[k]
      cell = WL[k][0]
      left = WL[k][1]
      ex = ease((it - OUT0[k]) / 0.25)
      for j in range(len(w)):
        a = ease((it - WS[k] - j * LG) / 0.12)
        if a <= 0:
          continue
        draw_letter(w[j], left + (j * 6 + 2.5) * cell, 60, cell, LI_BLUE,
                    a * (1 - ex), (0.6 + 0.4 * a) * (1 - 0.2 * ex), GH_LIGHT)
      p = (it - TICK0[k]) / 0.35
      if p > 0 and ex < 1:
        draw_tick(cx, cy, size, clamp01(p), 1 - ex)

  if it >= REV0:
    if it >= LOGO0:
      draw_box(80, LOGO_CY, LOGO_S * ease((it - LOGO0) / 0.8), 0, LI_BLUE, 1.0, GH_LIGHT)

    for j in range(8):
      u1 = ease((it - REV0 - j * LET_GAP) / LET_DUR)
      if u1 <= 0:
        continue
      x = lerp(BX[COUNT_W - 1], SLOT_X[j], u1)
      y = 60 - 10 * math.sin(3.1416 * u1)
      cell = RC * u1
      col = LI_BLUE
      alpha = u1
      base = GH_LIGHT
      if j < 6:
        alpha = u1 * (1 - ease((it - REV1) / 0.4))
      elif it >= REV1:
        m = ease((it - REV1) / 0.7)
        x = lerp(SLOT_X[j], IN_X[j - 6], m)
        y = lerp(60, LOGO_CY, m)
        cell = lerp(RC, RB, m)
        col = mix(WHITE, LI_BLUE, ease((it - REV1 - 0.45) / 0.4))
        if it >= REV1 + 0.45:
          base = LI_BLUE
        if it >= XFADE0:
          alpha = 1 - ease((it - XFADE0) / 0.45)
      if alpha > 0.02:
        draw_letter(LETTERS[j], x, y, cell, col, alpha, 1.0, base)

    if it >= XFADE0:
      draw_in(ease((it - XFADE0) / 0.45))

    # ----- your name: three lines, three colours -----
    if it >= NAME0:
      for n in range(2):
        draw_line(NAME_LINES[n], LINE_TOPS[n], LINE_T0[n], NAME_COLS[n], it)
    if it >= DIV_T0:
      dw = int(36 * ease((it - DIV_T0) / 0.35)) // 2 * 2
      if dw > 0:
        pen(ACCENT, 1.0, GH_LIGHT)
        screen.shape(shape.rectangle(80 - dw // 2, DIV_Y, dw, 2))
    if it >= ROLE_T0:
      draw_line(ROLE_LINE, ROLE_TOP, ROLE_T0, ACCENT, it)



# ==============================================================
# GITHUB APP ANIMATION (isolated from LinkedIn/menu drawing names)
# ==============================================================
def build_github_animation():
  # If everything runs too fast, raise this. If too slow, lower it.
  TICKS_PER_SECOND = 1000

  # ---------- colours (red, green, blue: each 0 to 255) ----------
  BACKGROUND = (12, 24, 84)     # navy
  LOGO = (255, 255, 255)        # white logo and "GitHub" text
  GOLD = (255, 200, 40)         # icons, stars, rings and the name SACHIN
  AN_COLOR = (150, 215, 255)    # ice blue for "DATA ANALYST"

  # ---------- the GitHub logo as a 56 x 56 pixel map (# = white block) ----------
  ROWS = [
    ".....................##############.....................",
    "..................####################..................",
    "................########################................",
    "..............############################..............",
    "............################################............",
    "...........##################################...........",
    "..........####################################..........",
    ".........######################################.........",
    "........########################################........",
    ".......##########################################.......",
    "......############################################......",
    ".....########...########################...########.....",
    ".....########......##################......########.....",
    "....#########.......###..........###.......#########....",
    "....#########..............................#########....",
    "...##########..............................##########...",
    "...##########..............................##########...",
    "..###########..............................###########..",
    "..###########..............................###########..",
    "..##########................................##########..",
    ".###########................................###########.",
    ".##########..................................##########.",
    ".##########..................................##########.",
    ".##########..................................##########.",
    ".##########...................................#########.",
    "##########....................................##########",
    "##########....................................##########",
    "##########....................................##########",
    "###########..................................###########",
    "###########..................................###########",
    ".##########..................................##########.",
    ".##########..................................##########.",
    ".###########................................###########.",
    ".###########................................###########.",
    ".############..............................############.",
    "..###########..............................###########..",
    "..############............................############..",
    "..##############........................##############..",
    "...#####..########....................###############...",
    "...#####....##########............###################...",
    "....######...#########............##################....",
    "....######...#########............##################....",
    ".....######...#######..............################.....",
    ".....#######....#####..............###############......",
    "......######.......................###############......",
    ".......######......................##############.......",
    "........######.....................#############........",
    ".........#######....#..............############.........",
    "..........###########..............###########..........",
    "...........##########..............##########...........",
    ".............########..............########.............",
    "..............#######..............#######..............",
    "................#####..............#####................",
    "..................###..............###..................",
    "........................................................",
    "........................................................",
  ]
  N = 56

  blocks = []
  for y in range(N):
    row = ROWS[y]
    x = 0
    while x < N:
      if row[x] == "#":
        x2 = x
        while x2 < N and row[x2] == "#":
          x2 += 1
        blocks.append(shape.rectangle(x, y, x2 - x, 1.05))
        x = x2
      else:
        x += 1

  # ---------- basic shapes used to build the icons ----------
  CIRCLE = shape.circle(0, 0, 1)
  STAR = shape.star(0, 0, 5, 0.5, 1)
  BAR_H = shape.rectangle(-0.9, -0.15, 1.8, 0.3)
  BAR_V = shape.rectangle(-0.15, -0.9, 0.3, 1.8)

  # each part: (shape, x, y, rotation, size, colour) where colour 0 = gold, 1 = background
  ICONS = [
    # 0: star
    [(STAR, 0, 0, 0, 1.1, 0)],
    # 1: git branch
    [(BAR_V, -0.45, 0, 0, 1.0, 0),
     (CIRCLE, -0.45, -0.85, 0, 0.32, 0),
     (CIRCLE, -0.45, 0.85, 0, 0.32, 0),
     (CIRCLE, 0.55, -0.45, 0, 0.32, 0),
     (BAR_H, 0.05, -0.12, -33, 0.66, 0)],
    # 2: commit (a ring on a line)
    [(BAR_H, 0, 0, 0, 1.0, 0),
     (CIRCLE, 0, 0, 0, 0.6, 0),
     (CIRCLE, 0, 0, 0, 0.3, 1)],
    # 3: code brackets  < / >
    [(BAR_H, -0.625, -0.35, -47, 0.55, 0),
     (BAR_H, -0.625, 0.35, 47, 0.55, 0),
     (BAR_H, 0.625, -0.35, 47, 0.55, 0),
     (BAR_H, 0.625, 0.35, -47, 0.55, 0),
     (BAR_V, 0, 0, 14, 0.9, 0)],
  ]
  ORBIT = [0, 1, 2, 3, 0]       # icon in each orbit slot. Slot 0 is the star that becomes the title star
  COUNT = len(ORBIT)

  # ---------- letter shapes (5 wide x 7 tall, # = a block or star goes here) ----------
  FONT = {
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "C": [".####", "#....", "#....", "#....", "#....", "#....", ".####"],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "G": [".####", "#....", "#....", "#.###", "#...#", "#...#", ".###."],
    "i": ["..#..", ".....", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "t": ["..#..", "..#..", "#####", "..#..", "..#..", "..#..", "...##"],
    "u": [".....", ".....", "#...#", "#...#", "#...#", "#..##", ".##.#"],
    "b": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "####."],
    "n": [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "a": [".....", ".....", ".###.", "....#", ".####", "#...#", ".####"],
    "l": [".##..", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "y": [".....", ".....", "#...#", "#...#", ".####", "....#", ".###."],
    "s": [".....", ".....", ".####", "#....", ".###.", "....#", "####."],
  }
  NAME = "SACHIN"
  TITLE2 = "DATA ANALYST"        # one line. For mixed case use "Data Analyst"
  WORDMARK = "GitHub"

  def pixels(letter):
    return [(c, r) for r, row in enumerate(FONT[letter])
            for c, ch in enumerate(row) if ch == "#"]

  # ---------- the word "GitHub" under the logo (white blocks) ----------
  text_blocks = []
  for li, ch in enumerate(WORDMARK):
    for r, row in enumerate(FONT[ch]):
      c = 0
      while c < 5:
        if row[c] == "#":
          c2 = c
          while c2 < 5 and row[c2] == "#":
            c2 += 1
          text_blocks.append(shape.rectangle(li * 6 + c, r, c2 - c, 1.05))
          c = c2
        else:
          c += 1
  TEXT_W = len(WORDMARK) * 6 - 1
  TEXT_H = 7
  TEXT_CELL = 1.5               # size of each block of "GitHub"
  TEXT_Y = 99                   # vertical position of "GitHub"

  # ---------- title target positions ----------
  BIG_C = 11
  BIG_R = 6.5
  bx0 = 80 - (5 * BIG_C) / 2
  by0 = 60 - (7 * BIG_C) / 2
  big_targets = [(bx0 + (c + 0.5) * BIG_C, by0 + (r + 0.5) * BIG_C)
                 for c, r in pixels("S")]
  S_COUNT = len(big_targets)

  # SACHIN (bigger stars)
  NC = 4
  NAME_R = 2.4
  NAME_Y0 = 34
  nx0 = 80 - (len(NAME) * 6 - 1) * NC / 2
  name_targets = []
  for li, letter in enumerate(NAME):
    for c, r in pixels(letter):
      name_targets.append((nx0 + (li * 6 + c + 0.5) * NC, NAME_Y0 + (r + 0.5) * NC))
  NAME_COUNT = len(name_targets)

  # DATA ANALYST (smaller stars, one line below the name, 142 px wide)
  AC = 2.0                      # spacing between stars
  AN_R = 1.15                   # star size
  AN_Y0 = 70                    # vertical position
  AN_STARS = True               # False = tiny squares instead of stars (lighter, if it lags)
  ax0 = 80 - (len(TITLE2) * 6 - 1) * AC / 2
  analyst_targets = []
  for li, letter in enumerate(TITLE2):
    for c, r in pixels(letter):
      analyst_targets.append((ax0 + (li * 6 + c + 0.5) * AC, AN_Y0 + (r + 0.5) * AC))

  TOTAL = NAME_COUNT + len(analyst_targets)

  # ---------- layout of the GitHub scene ----------
  CX = 80
  CY = 54
  SCALE = 1.05                  # logo size (56 * 1.05 = about 59 px)
  RX = 56                       # orbit width
  RY = 38                       # orbit height
  ICON_R = 8                    # icon size in pixels
  ORBIT_SPEED = 0.8             # radians per second

  # ---------- timeline (seconds) ----------
  T_IN = 1.0                    # first icon starts flying in
  IN_GAP = 0.45                 # gap between icons arriving
  FLY = 1.4                     # time for one icon to arrive
  T_OUT = 8.4                   # the other icons dive into the logo
  OUT_GAP = 0.15
  OUT_FLY = 1.0
  T_H0 = 9.6                    # the star leaves the orbit and heads to the centre
  HF = 1.6                      # how long that trip takes
  T_H1 = T_H0 + HF              # title card scene starts here (tt = 0)
  T_L0 = 9.7                    # logo starts spinning away
  T_L1 = 10.9                   # logo is gone

  RING_STARTS = [2.0, 4.5, 7.0, T_H0]
  RING_LIFE = 2.2

  # title card times (seconds after T_H1)
  T_TO_S = 2.0
  T_S_DONE = 4.5
  T_SPLIT = 5.5
  T_NAME_DONE = 7.5
  T_AN_START = 7.2              # "DATA ANALYST" stars start flying out of the name
  T_AN_FLY = 1.3
  T_FADE = 11.2                 # everything fades out, then restarts
  T_TITLE_END = 12.0
  T_TOTAL = T_H1 + T_TITLE_END

  # ---------- setup ----------
  random.seed(5)
  BASE = [k * 6.2832 / COUNT for k in range(COUNT)]
  SPAWN = []
  for k in range(COUNT):
    a = (k * 72 + 30) * 3.1416 / 180
    SPAWN.append((CX + math.cos(a) * 120, CY + math.sin(a) * 100))

  TWINKLES = [(random.uniform(4, 156), random.uniform(4, 116),
               random.uniform(1.0, 2.2), random.uniform(0, 6.28)) for _ in range(14)]

  random.seed(3)
  base = [(random.uniform(25, 135), random.uniform(20, 100)) for _ in range(TOTAL)]
  big_size = [random.uniform(14, 24) for _ in range(TOTAL)]
  spin_dir = [random.choice((-1, 1)) for _ in range(TOTAL)]
  split_from = [big_targets[random.randrange(S_COUNT)] for _ in range(TOTAL)]
  an_from = [name_targets[random.randrange(NAME_COUNT)] for _ in range(TOTAL)]
  stars = [shape.star(0, 0, 5, 0.5, 1) for _ in range(TOTAL)]
  if not AN_STARS:
    for i in range(NAME_COUNT, TOTAL):
      stars[i] = shape.rectangle(-0.8, -0.8, 1.6, 1.6)

  base[0] = (80, 54)            # the handoff star settles near the centre
  big_size[0] = 22              # and is the biggest star

  # ---------- helpers ----------
  def ease(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3 - 2 * u)

  def lerp(a, b, u):
    return a + (b - a) * u

  def gold(b):
    return color.rgb(int(GOLD[0] * b), int(GOLD[1] * b), int(GOLD[2] * b))

  def bg_pen():
    screen.pen = color.rgb(BACKGROUND[0], BACKGROUND[1], BACKGROUND[2])

  def drift(i, tt):
    return (base[i][0] + math.sin(tt * 1.3 + i) * 8,
            base[i][1] + math.cos(tt * 1.1 + i * 2) * 6)

  def draw_icon(kind, x, y, s, a):
    for part in ICONS[kind]:
      shp = part[0]
      if part[5] == 1:
        bg_pen()
      else:
        screen.pen = gold(1.0)
      shp.transform = (mat3().translate(x, y).rotate(a).scale(s)
                       .translate(part[1], part[2]).rotate(part[3]).scale(part[4]))
      screen.shape(shp)

  def icon_state(k, t):
    th = BASE[k] + (t - T_IN) * ORBIT_SPEED
    ox = CX + math.cos(th) * RX
    oy = CY + math.sin(th) * RY
    depth = 0.8 + 0.3 * math.sin(th)
    front = math.sin(th) >= 0
    s_in = T_IN + k * IN_GAP
    s_out = T_OUT + k * OUT_GAP
    if t < s_in:
      return None
    if t < s_in + FLY:
      u = ease((t - s_in) / FLY)
      return (lerp(SPAWN[k][0], ox, u), lerp(SPAWN[k][1], oy, u), ICON_R * depth * u, front)
    if t < s_out:
      return (ox, oy, ICON_R * depth, front)
    if t < s_out + OUT_FLY:
      u = ease((t - s_out) / OUT_FLY)
      return (lerp(ox, CX, u), lerp(oy, CY, u), ICON_R * depth * (1 - u), front)
    return None

  def star0_state(t):
    # the special star: orbits like the others, then flies to the title card position
    if t < T_IN:
      return None
    th = BASE[0] + (t - T_IN) * ORBIT_SPEED
    ox = CX + math.cos(th) * RX
    oy = CY + math.sin(th) * RY
    depth = 0.8 + 0.3 * math.sin(th)
    front = math.sin(th) >= 0
    rad = 1.1 * ICON_R * depth
    if t < T_IN + FLY:
      u = ease((t - T_IN) / FLY)
      return (lerp(SPAWN[0][0], ox, u), lerp(SPAWN[0][1], oy, u), rad * u, front)
    if t < T_H0:
      return (ox, oy, rad, front)
    if t < T_H1:
      u = ease((t - T_H0) / HF)
      tx, ty = drift(0, 0)
      return (lerp(ox, tx, u), lerp(oy, ty, u), lerp(rad, big_size[0], u), True)
    return None

  def draw_star0(st, t):
    screen.pen = gold(1.0)
    stars[0].transform = mat3().translate(st[0], st[1]).scale(st[2]).rotate(t * 50)
    screen.shape(stars[0])

  def draw_item(k, st, t):
    if k == 0:
      draw_star0(st, t)
    else:
      kind = ORBIT[k]
      a = t * 50 + k * 40 if kind == 0 else math.sin(t * 2 + k) * 12
      draw_icon(kind, st[0], st[1], st[2], a)

  def draw_logo(t):
    pop = 1.0
    if t < 0.6:
      pop = 0.8 + 0.2 * ease(t / 0.6)                  # pop in at the start
    exit_f = 1.0
    spin = 0
    if t > T_L0:
      u = ease((t - T_L0) / (T_L1 - T_L0))
      exit_f = 1 - u                                   # shrinks away
      spin = 270 * u                                   # while spinning

    # --- the logo ---
    grow = pop * (1.0 + 0.03 * math.sin(t * 2.5)) * exit_f   # breathing
    bob = math.sin(t * 2.0) * 2.5                      # floating up and down
    sway = math.sin(t * 1.5) * 3 + spin                # small tilt
    if grow >= 0.02:
      screen.pen = color.rgb(LOGO[0], LOGO[1], LOGO[2])
      tf = (mat3().translate(CX, CY + bob).rotate(sway).scale(SCALE * grow)
            .translate(-N / 2, -N / 2))
      for b in blocks:
        b.transform = tf
        screen.shape(b)

    # --- the word "GitHub" under the logo ---
    tg = pop * exit_f
    if tg >= 0.02:
      br = ease(t / 0.6)                               # fades in with the logo
      screen.pen = color.rgb(int(LOGO[0] * br), int(LOGO[1] * br), int(LOGO[2] * br))
      ty = TEXT_Y + math.sin(t * 2.0 + 1.0) * 1.2
      tf2 = (mat3().translate(CX, ty).scale(TEXT_CELL * tg)
             .translate(-TEXT_W / 2, -TEXT_H / 2))
      for b in text_blocks:
        b.transform = tf2
        screen.shape(b)

  def draw_title(t):
    tt = t - T_H1
    settle = ease((tt - 4.0) / 1.5)       # stars stop spinning as they form letters
    white = ease((tt - 3.0) / 2.0)        # stars reach full brightness as they form
    fade = ease((tt - T_FADE) / 0.7)      # everything fades out at the very end
    s0x, s0y = drift(0, tt)

    for i in range(TOTAL):
      if i < S_COUNT:
        # ----- stars that make the S -----
        if tt < T_TO_S:
          x, y = drift(i, tt)
          if i == 0:
            r = big_size[0]                # the handoff star is already full size
          else:
            # new stars split off from the handoff star and spread out
            e = ease((tt - 0.1 - i * 0.03) / 1.0)
            x = lerp(s0x, x, e)
            y = lerp(s0y, y, e)
            r = big_size[i] * e
        elif tt < T_S_DONE:
          u = ease((tt - T_TO_S) / (T_S_DONE - T_TO_S))
          sx, sy = drift(i, T_TO_S)
          x = lerp(sx, big_targets[i][0], u)
          y = lerp(sy, big_targets[i][1], u)
          r = lerp(big_size[i], BIG_R, u)
        elif tt < T_SPLIT:
          x, y = big_targets[i]
          r = BIG_R
        else:
          u = ease((tt - T_SPLIT) / (T_NAME_DONE - T_SPLIT))
          x = lerp(big_targets[i][0], name_targets[i][0], u)
          y = lerp(big_targets[i][1], name_targets[i][1], u)
          r = lerp(BIG_R, NAME_R, u)
        col = GOLD
      elif i < NAME_COUNT:
        # ----- extra stars that appear when the S splits (rest of SACHIN) -----
        if tt < T_SPLIT:
          continue
        u = ease((tt - T_SPLIT) / (T_NAME_DONE - T_SPLIT))
        x = lerp(split_from[i][0], name_targets[i][0], u)
        y = lerp(split_from[i][1], name_targets[i][1], u)
        r = NAME_R * u
        col = GOLD
      else:
        # ----- small ice-blue stars that fly out of the name to spell DATA ANALYST -----
        if tt < T_AN_START:
          continue
        u = ease((tt - T_AN_START) / T_AN_FLY)
        target = analyst_targets[i - NAME_COUNT]
        x = lerp(an_from[i][0], target[0], u)
        y = lerp(an_from[i][1], target[1], u)
        r = AN_R * u
        col = AN_COLOR

      if r < 0.3:
        continue

      # ----- colour, fading into the navy background at the very end -----
      shade = 255 if i == 0 else 235 + (i * 17) % 21
      b = lerp(shade, 255, white) / 255
      screen.pen = color.rgb(int(lerp(col[0] * b, BACKGROUND[0], fade)),
                             int(lerp(col[1] * b, BACKGROUND[1], fade)),
                             int(lerp(col[2] * b, BACKGROUND[2], fade)))

      if i == 0:
        angle = t * 50 * (1 - settle)      # same spin as the star had in the GitHub scene
      else:
        angle = spin_dir[i] * badge.ticks / 10 * (1 - settle)
      stars[i].transform = mat3().translate(x, y).scale(r).rotate(angle)
      screen.shape(stars[i])

  def render_github_frame(t):
    if t > T_TOTAL:
      t = t % T_TOTAL
    bg_pen()
    screen.clear()

    # --- pulse rings behind everything (the last one carries into the title card) ---
    for start in RING_STARTS:
      u = (t - start) / RING_LIFE
      if u >= 0 and u < 1:
        r = lerp(30, 80, ease(u))
        screen.pen = gold((1 - u) * 0.7)
        CIRCLE.transform = mat3().translate(CX, CY).scale(r)
        screen.shape(CIRCLE)
        bg_pen()
        CIRCLE.transform = mat3().translate(CX, CY).scale(r - 1.6)
        screen.shape(CIRCLE)

    # --- twinkling background stars (fade away before the S forms) ---
    tw_fade = ease(t / 1.0) * (1 - ease((t - T_H0) / 2.5))
    if tw_fade > 0.02:
      for tw in TWINKLES:
        b = (0.25 + 0.5 * (0.5 + 0.5 * math.sin(t * 2.0 + tw[3]))) * tw_fade
        screen.pen = gold(b)
        STAR.transform = mat3().translate(tw[0], tw[1]).scale(tw[2]).rotate(t * 30)
        screen.shape(STAR)

    if t < T_H1:
      # ----- GITHUB SCENE -----
      back = []
      front = []
      for k in range(COUNT):
        if k == 0:
          st = star0_state(t)
        else:
          st = icon_state(k, t)
        if st is not None and st[2] > 0.3:
          if st[3]:
            front.append((k, st))
          else:
            back.append((k, st))

      for item in back:
        draw_item(item[0], item[1], t)
      draw_logo(t)
      for item in front:
        draw_item(item[0], item[1], t)
    else:
      # ----- TITLE CARD SCENE -----
      draw_title(t)

  return render_github_frame

# ==============================================================
# MAIN LOOP
# ==============================================================
scene = 0            # 0 = start, 1 = loading, 2 = menu, 3 = an app is open
sc_t0 = badge.ticks
sel = 0
sel_t0 = badge.ticks
open_i = 0
dbg = [-10.0, -10.0, -10.0, -10.0, -10.0]

li_stage = 'ZOOM'    # ZOOM -> FADE -> INTRO -> EXIT, only used when open_i == 0
li_t0 = badge.ticks
github_render = build_github_animation()
gh_t0 = badge.ticks
gh_stage = 'ZOOM'
GH_PROFILE_FRAME = 20.8  # hold on the completed SACHIN / DATA ANALYST title card

while True:
  now = badge.ticks
  t = (now - sc_t0) / TICKS_PER_SECOND          # time inside the current scene
  gt = now / TICKS_PER_SECOND                   # overall time (for twinkling)

  pa = badge.pressed(BUTTON_A)
  pb = badge.pressed(BUTTON_B)
  pc = badge.pressed(BUTTON_C)
  pup = badge.pressed(BUTTON_UP)
  pdn = badge.pressed(BUTTON_DOWN)
  anyp = pa or pb or pc or pup or pdn

  bg = SPACE_BG
  if scene == 1 and t < 0.3:
    bg = mix(SPACE_BG, WHITE, ease(t / 0.3))
  screen.pen = rgb(bg)
  screen.clear()

  if scene == 0:
    draw_start(t, gt)
    if anyp:
      scene = 1
      sc_t0 = now

  elif scene == 1:
    draw_loading(t, gt)
    if t > LOAD_DONE:
      scene = 2
      sc_t0 = now
      sel_t0 = now

  elif scene == 2:
    draw_twinkles(gt, 0.7)
    text("CHOOSE AN APP", 80, 6, 1, ICE, 0.9)
    for i in range(3):
      k = (t - 0.12 * i) / 0.35
      pop = ease(k) * (1 + 0.15 * math.sin(3.1416 * clamp01(k)))
      if i == sel:
        draw_card(i, CARD_X[i], CARD_Y - 2 + math.sin(gt * 3) * 1.5, 46 * pop, 1.0, True, gt)
      else:
        draw_card(i, CARD_X[i], CARD_Y, 38 * pop, 0.5, False, gt)
    a = ease((now - sel_t0) / TICKS_PER_SECOND / 0.2)
    text(NAMES[sel], 80, 88 + int((1 - a) * 4), 2, CREAM, a)
    text("A B MOVE   C OPEN", 80, 109, 1, ICE, 0.8)
    if pa or pup:
      sel = (sel - 1) % 3
      sel_t0 = now
    elif pb or pdn:
      sel = (sel + 1) % 3
      sel_t0 = now
    elif pc:
      scene = 3
      sc_t0 = now
      open_i = sel
      li_stage = 'ZOOM'
      li_t0 = now
      gh_stage = 'ZOOM'
      gh_t0 = now

  elif scene == 3 and open_i == 0:
    # ================= LINKEDIN APP =================
    if li_stage == 'ZOOM':
      u = ease(t / 0.45)
      cx = lerp(CARD_X[0], 80, u)
      cy = lerp(CARD_Y, 60, u)
      w = lerp(40, 170, u)
      h = lerp(40, 130, u)
      pen(LI_BLUE)
      screen.shape(shape.rectangle(cx - w / 2, cy - h / 2, w, h))
      if t > 0.45:
        li_stage = 'FADE'
        li_t0 = now

    elif li_stage == 'FADE':
      ft = (now - li_t0) / TICKS_PER_SECOND
      u = ease(ft / 0.3)
      pen(mix(GH_LIGHT, LI_BLUE, u))
      screen.shape(shape.rectangle(-5, -5, 170, 130))
      if ft > 0.3:
        li_stage = 'INTRO'
        li_t0 = now

    elif li_stage == 'INTRO':
      pen(GH_LIGHT)
      screen.shape(shape.rectangle(-5, -5, 170, 130))
      it = (now - li_t0) / TICKS_PER_SECOND

      draw_intro(it)

      if anyp:
        if it < FINAL_T:
          li_t0 = now - int(FINAL_T * TICKS_PER_SECOND)     # skip straight to the name screen
        elif pc:
          li_stage = 'EXIT'
          li_t0 = now

    elif li_stage == 'EXIT':
      # the screen shrinks back into the LinkedIn card
      ft = (now - li_t0) / TICKS_PER_SECOND
      u = ease(ft / 0.35)
      cx = lerp(80, CARD_X[0], u)
      cy = lerp(60, CARD_Y, u)
      w = lerp(170, 40, u)
      h = lerp(130, 40, u)
      pen(mix(GH_LIGHT, LI_BLUE, u))
      screen.shape(shape.rectangle(cx - w / 2, cy - h / 2, w, h))
      if ft > 0.35:
        scene = 2
        sc_t0 = now
        sel_t0 = now
        li_stage = 'ZOOM'

  elif scene == 3 and open_i == 1:
    # ================= GITHUB APP =================
    if gh_stage == 'ZOOM':
      u = ease(t / 0.45)
      cx = lerp(CARD_X[1], 80, u)
      cy = lerp(CARD_Y, 60, u)
      w = lerp(40, 170, u)
      h = lerp(40, 130, u)
      pen(GH_LIGHT)
      screen.shape(shape.rectangle(cx - w / 2, cy - h / 2, w, h))
      if t >= 0.45:
        gh_stage = 'PLAY'
        gh_t0 = now
    elif gh_stage == 'PLAY':
      github_elapsed = (now - gh_t0) / TICKS_PER_SECOND
      if github_elapsed < GH_PROFILE_FRAME:
        github_render(github_elapsed)
      else:
        # Hold the finished GitHub identity card, just like LinkedIn's name screen.
        github_render(GH_PROFILE_FRAME)
        if anyp and github_elapsed > 0.8:
          if pc:
            gh_stage = 'EXIT'
            gh_t0 = now
    elif gh_stage == 'EXIT':
      ft = (now - gh_t0) / TICKS_PER_SECOND
      u = ease(ft / 0.35)
      cx = lerp(80, CARD_X[1], u)
      cy = lerp(60, CARD_Y, u)
      w = lerp(170, 40, u)
      h = lerp(130, 40, u)
      pen(mix(GH_LIGHT, SPACE_BG, u))
      screen.shape(shape.rectangle(cx - w / 2, cy - h / 2, w, h))
      if ft > 0.35:
        scene = 2
        sc_t0 = now
        sel_t0 = now
        gh_stage = 'ZOOM'

  elif scene == 3 and open_i == 2:
    # ================= UNIVERSE 26 CONGRATULATIONS =================
    u = ease(t / 0.4)
    cx = lerp(CARD_X[2], 80, u)
    cy = lerp(CARD_Y, 60, u)
    w = lerp(40, 170, u)
    h = lerp(40, 130, u)
    if t < 0.4:
      pen(OPEN_BG[2])
      screen.shape(shape.rectangle(cx - w / 2, cy - h / 2, w, h))
    else:
      dt = min(badge.ticks_delta, 100) / 1000
      draw_universe_congrats(now, dt)
    if t > 0.8 and anyp:
      scene = 2
      sc_t0 = now
      sel_t0 = now

  if DEBUG:
    flags = [pa, pb, pc, pup, pdn]
    for i in range(5):
      if flags[i]:
        dbg[i] = gt
      pen(GOLD if gt - dbg[i] < 0.4 else (60, 60, 80))
      screen.shape(shape.rectangle(2 + i * 6, 2, 4, 4))

  badge.update()