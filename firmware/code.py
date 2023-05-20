print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import unicode_codepoint_sequence
from kmk.handlers.sequences import send_string
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP2, board.GP3, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.row_pins = (board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# custom keys
______ = KC.NO
KC_SQRT = unicode_codepoint_sequence(["221a"]) # square root symbol
KC_PI = unicode_codepoint_sequence(["03c0"]) # pi symbol
KC_SUM = unicode_codepoint_sequence(["2140"]) # summation symbol
KC_INF = unicode_codepoint_sequence(["221e"]) # infinity
KC_INT = unicode_codepoint_sequence(["222b"]) # integral
KC_EX = unicode_codepoint_sequence(["0065","1d61"]) # e^x
KC_LN = send_string("LN") # LN
KC_SIN = send_string("SIN") # SIN
KC_COS = send_string("COS") # COS
KC_TAN = send_string("TAN") # TAN
KC_THTA = unicode_codepoint_sequence(["03b8"]) # theta
KC_PWR = unicode_codepoint_sequence(["23fb"]) # power
KC_NXT = simple_key_sequence(
    (
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.TAB,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
    )
)

# layer keys
MOUSE_EN = KC.MO(1)
MOUSE_TG = KC.TG(1)
SEC_EN = KC.MO(2)
DIA_EN = KC.MO(3)


keyboard.keymap = [
    [ # Layer 0
        ______,  MOUSE_EN, SEC_EN,   KC.ESC,  KC.UP,   KC.RIGHT, KC.LPRN, KC.RPRN, KC.COMMA, KC.SLASH,
        KC.F1,   KC.F5,    KC.LCTRL, ______,  KC.LEFT, KC.DOWN,  KC.N7,   KC.N8,   KC.N9,    KC.ASTERISK,
        KC.F2,   KC.F6,    KC.DEL,   KC.LGUI, KC.ENT,  ______,   KC.N4,   KC.N5,   KC.N6,    KC.MINUS,
        KC.F3,   KC.F7,    KC_LN,    ______,  ______,  ______,   KC.N1,   KC.N2,   KC.N3,    KC.PLUS,
        KC.F4,   KC.F8,    KC_SIN,   KC_COS,  KC_TAN,  KC.CIRC,  KC.N0,   KC.DOT,  KC.MINUS, KC.ENT,
        KC.Q,    KC.W,     KC.E,     KC.R,    KC.T,    KC.Y,     KC.U,    KC.I,    KC.O,     KC.P,
        KC.A,    KC.S,     KC.D,     KC.F,    KC.G,    KC.H,     KC.J,    KC.K,    KC.L,     ______,
        KC.LSFT, KC.Z,     KC.X,     KC.C,    KC.V,    KC.B,     KC.N,    KC.M,    KC_THTA,  KC.ENT,
        KC.LALT,  DIA_EN,   SEC_EN,   KC.TAB,  KC.SPC,  ______,   KC.EQL,  KC.BSPC, ______,   ______,
    ],
    [ # Layer 1 (mouse)
        ______,  ______,   SEC_EN,   KC.ESC,    KC.MS_UP,  KC.MS_RT, KC.LPRN, KC.RPRN, KC.COMMA, KC.SLASH,
        KC.F1,   KC.F5,    KC.LCTRL, ______,    KC.MS_LT,  KC.MS_DN, KC.N7,   KC.N8,   KC.N9,    KC.ASTERISK,
        KC.F2,   KC.F6,    KC.DEL,   KC.MB_LMB, KC.MB_RMB, ______,   KC.N4,   KC.N5,   KC.N6,    KC.MINUS,
        KC.F3,   KC.F7,    KC_LN,    ______,    ______,    ______,   KC.N1,   KC.N2,   KC.N3,    KC.PLUS,
        KC.F4,   KC.F8,    KC_SIN,   KC_COS,    KC_TAN,    KC.CIRC,  KC.N0,   KC.DOT,  KC.MINUS, KC.ENT,
        KC.Q,    KC.W,     KC.E,     KC.R,      KC.T,      KC.Y,     KC.U,    KC.I,    KC.O,     KC.P,
        KC.A,    KC.S,     KC.D,     KC.F,      KC.G,      KC.H,     KC.J,    KC.K,    KC.L,     ______,
        KC.LSFT, KC.Z,     KC.X,     KC.C,      KC.V,      KC.B,     KC.N,    KC.M,    KC_THTA,  KC.ENT,
        KC.LALT,  DIA_EN,   SEC_EN,   KC.TAB,    KC.SPC,    ______,   KC.EQL,  KC.BSPC, ______,   ______,
    ],
    [ # Layer 2 (2nd)
        ______,  MOUSE_TG, SEC_EN,   KC.ESC,  KC.UP,   KC.RIGHT, KC.LCBR, KC.RCBR, KC.LBRC,  KC.RBRC,
        KC.F1,   KC.F5,    KC.LCTRL, ______,  KC.LEFT, KC.DOWN,  KC_INT,  KC.N8,   KC.N9,    KC_SQRT,
        KC.F2,   KC.F6,    KC.DEL,   KC.LGUI, KC.ENT,  ______,   KC_SUM,  KC.N5,   KC.N6,    KC.MINUS,
        KC.F3,   KC.F7,    KC_EX,    ______,  ______,  ______,   KC.N1,   KC.N2,   KC.N3,    KC.PLUS,
        KC.F4,   KC.F8,    KC_SIN,   KC_COS,  KC_TAN,  KC_PI,    KC.LABK, KC.RABK, KC.MINUS, KC.ENT,
        KC.Q,    KC.W,     KC.E,     KC.R,    KC.T,    KC.Y,     KC.U,    KC.I,    KC.O,     KC.P,
        KC.A,    KC.S,     KC.D,     KC.F,    KC.G,    KC.H,     KC_INF,  KC.PIPE, KC.QUOTE, ______,
        KC.CAPS, KC.CAPS,  KC.X,     KC.C,    KC.V,    KC.B,     KC.N,    KC.SCLN, KC.COLN,  KC.ENT,
        KC_PWR,  DIA_EN,   SEC_EN,   KC.TAB,  KC.SPC,  ______,   KC.BSLS, KC.INS,  ______,   ______,
    ],
    [ # Layer 3 (<>)
        ______,  MOUSE_EN, SEC_EN,   KC.ESC,  KC.VOLU, KC.RIGHT, KC.LPRN, KC.RPRN, KC.COMMA, KC.SLASH,
        KC.F1,   KC.F5,    KC.LCTRL, ______,  KC.LEFT, KC.VOLD,  KC.N7,   KC.N8,   KC.N9,    KC.ASTERISK,
        KC.F2,   KC.F6,    KC.DEL,   KC.LGUI, KC.ENT,  ______,   KC.N4,   KC.N5,   KC.N6,    KC.BRID,
        KC.F3,   KC.F7,    KC_LN,    ______,  ______,  ______,   KC.N1,   KC.N2,   KC.N3,    KC.BRIU,
        KC.F4,   KC.F8,    KC_SIN,   KC_COS,  KC_TAN,  KC.CIRC,  KC.N0,   KC.DOT,  KC.MINUS, KC.ENT,
        KC.HOME, KC.W,     KC_NXT,   KC.R,    KC.T,    KC.Y,     KC.U,    KC.I,    KC.O,     KC.P,
        KC.A,    KC.S,     KC.D,     KC.F,    KC.G,    KC.H,     KC.J,    KC.K,    KC.L,     ______,
        KC.LSFT, KC.Z,     KC.X,     KC.C,    KC.V,    KC.B,     KC.N,    KC.M,    KC_THTA,  KC.ENT,
        KC.LALT,  DIA_EN,   SEC_EN,   KC.TAB,  KC.SPC,  ______,   KC.EQL,  KC.DEL,  ______,   ______,
    ]
]

if __name__ == '__main__':
    keyboard.go()
