import enum
import pygame

class KeyName(enum.Enum):
    K_UNKNOWN = "unknown"
    K_A = "a"
    K_B = "b"
    K_C = "c"
    K_D = "d"
    K_E = "e"
    K_F = "f"
    K_G = "g"
    K_H = "h"
    K_I = "i"
    K_J = "j"
    K_K = "k"
    K_L = "l"
    K_M = "m"
    K_N = "n"
    K_O = "o"
    K_P = "p"
    K_Q = "q"
    K_R = "r"
    K_S = "s"
    K_T = "t"
    K_U = "u"
    K_V = "v"
    K_W = "w"
    K_X = "x"
    K_Y = "y"
    K_Z = "z"
    K_0 = "0"
    K_1 = "1"
    K_2 = "2"
    K_3 = "3"
    K_4 = "4"
    K_5 = "5"
    K_6 = "6"
    K_7 = "7"
    K_8 = "8"
    K_9 = "9"
    K_SPACE = "space"
    K_EXCLAIM = "!"
    K_QUOTEDBL = "\""
    K_HASH = "#"
    K_PERCENT = "%"
    K_DOLLAR = "$"
    K_AMPERSAND = "&"
    K_QUOTE = "'"
    K_LEFTPAREN = "("
    K_RIGHTPAREN = ")"
    K_ASTERISK = "*"
    K_PLUS = "+"
    K_COMMA = ","
    K_MINUS = "-"
    K_PERIOD = "."
    K_SLASH = "/"
    K_COLON = ":"
    K_SEMICOLON = ";"
    K_LESS = "<"
    K_EQUALS = "="
    K_GREATER = ">"
    K_QUESTION = "?"
    K_AT = "@"
    K_LEFTBRACKET = "["
    K_BACKSLASH = "\\"
    K_RIGHTBRACKET = "]"
    K_CARET = "^"
    K_UNDERSCORE = "_"
    K_BACKQUOTE = "`"
    K_KP_0 = "kp0"
    K_KP_1 = "kp1"
    K_KP_2 = "kp2"
    K_KP_3 = "kp3"
    K_KP_4 = "kp4"
    K_KP_5 = "kp5"
    K_KP_6 = "kp6"
    K_KP_7 = "kp7"
    K_KP_8 = "kp8"
    K_KP_9 = "kp9"
    K_KP_PERIOD = "kp."
    K_KP_DIVIDE = "kp/"
    K_KP_MULTIPLY = "kp*"
    K_KP_MINUS = "kp-"
    K_KP_PLUS = "kp+"
    K_KP_ENTER = "kpenter"
    K_KP_EQUALS = "kp="
    K_UP = "up"
    K_DOWN = "down"
    K_RIGHT = "right"
    K_LEFT = "left"
    K_HOME = "home"
    K_END = "end"
    K_PAGEUP = "pageup"
    K_PAGEDOWN = "pagedown"
    K_INSERT = "insert"
    K_BACKSPACE = "backspace"
    K_TAB = "tab"
    K_CLEAR = "clear"
    K_RETURN = "return"
    K_DELETE = "delete"
    K_F1 = "f1"
    K_F2 = "f2"
    K_F3 = "f3"
    K_F4 = "f4"
    K_F5 = "f5"
    K_F6 = "f6"
    K_F7 = "f7"
    K_F8 = "f8"
    K_F9 = "f9"
    K_F10 = "f10"
    K_F11 = "f11"
    K_F12 = "f12"
    K_F13 = "f13"
    K_F14 = "f14"
    K_F15 = "f15"
    K_NUMLOCK = "numlock"
    K_CAPSLOCK = "capslock"
    K_SCROLLLOCK = "scrolllock"
    K_RSHIFT = "rshift"
    K_LSHIFT = "lshift"
    K_RCTRL = "rctrl"
    K_LCTRL = "lctrl"
    K_RALT = "ralt"
    K_LALT = "lalt"
    K_RGUI = "rgui"
    K_LGUI = "lgui"
    K_RMETA = "rmeta"
    K_LMETA = "lmeta"
    K_RSUPER = "rsuper"
    K_LSUPER = "lsuper"
    K_MODE = "mode"
    K_PAUSE = "pause"
    K_ESCAPE = "escape"
    K_HELP = "help"
    K_PRINT = "print"
    K_PRINTSCREEN = "printscreen"
    K_SYSREQ = "sysreq"
    K_BREAK = "break"
    K_MENU = "menu"
    K_POWER = "power"
    K_EURO = "euro"
    K_ANDROIDBACK = "androidback"

string_to_key = {
    "unknown": pygame.K_UNKNOWN,
    "a": pygame.K_a,
    "b": pygame.K_b,
    "c": pygame.K_c,
    "d": pygame.K_d,
    "e": pygame.K_e,
    "f": pygame.K_f,
    "g": pygame.K_g,
    "h": pygame.K_h,
    "i": pygame.K_i,
    "j": pygame.K_j,
    "k": pygame.K_k,
    "l": pygame.K_l,
    "m": pygame.K_m,
    "n": pygame.K_n,
    "o": pygame.K_o,
    "p": pygame.K_p,
    "q": pygame.K_q,
    "r": pygame.K_r,
    "s": pygame.K_s,
    "t": pygame.K_t,
    "u": pygame.K_u,
    "v": pygame.K_v,
    "w": pygame.K_w,
    "x": pygame.K_x,
    "y": pygame.K_y,
    "z": pygame.K_z,
    "0": pygame.K_0,
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9,
    "space": pygame.K_SPACE,
    "!": pygame.K_EXCLAIM,
    "\"": pygame.K_QUOTEDBL,
    "#": pygame.K_HASH,
    "$": pygame.K_DOLLAR,
    "&": pygame.K_AMPERSAND,
    "%": pygame.K_PERCENT,
    "'": pygame.K_QUOTE,
    "(": pygame.K_LEFTPAREN,
    ")": pygame.K_RIGHTPAREN,
    "*": pygame.K_ASTERISK,
    "+": pygame.K_PLUS,
    ",": pygame.K_COMMA,
    "-": pygame.K_MINUS,
    ".": pygame.K_PERIOD,
    "/": pygame.K_SLASH,
    ":": pygame.K_COLON,
    ";": pygame.K_SEMICOLON,
    "<": pygame.K_LESS,
    "=": pygame.K_EQUALS,
    ">": pygame.K_GREATER,
    "?": pygame.K_QUESTION,
    "@": pygame.K_AT,
    "[": pygame.K_LEFTBRACKET,
    "\\": pygame.K_BACKSLASH,
    "]": pygame.K_RIGHTBRACKET,
    "^": pygame.K_CARET,
    "_": pygame.K_UNDERSCORE,
    "`": pygame.K_BACKQUOTE,
    "kp0": pygame.K_KP0,
    "kp1": pygame.K_KP1,
    "kp2": pygame.K_KP2,
    "kp3": pygame.K_KP3,
    "kp4": pygame.K_KP4,
    "kp5": pygame.K_KP5,
    "kp6": pygame.K_KP6,
    "kp7": pygame.K_KP7,
    "kp8": pygame.K_KP8,
    "kp9": pygame.K_KP9,
    "kp.": pygame.K_KP_PERIOD,
    "kp/": pygame.K_KP_DIVIDE,
    "kp*": pygame.K_KP_MULTIPLY,
    "kp-": pygame.K_KP_MINUS,
    "kp+": pygame.K_KP_PLUS,
    "kpenter": pygame.K_KP_ENTER,
    "kp=": pygame.K_KP_EQUALS,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "right": pygame.K_RIGHT,
    "left": pygame.K_LEFT,
    "home": pygame.K_HOME,
    "end": pygame.K_END,
    "pageup": pygame.K_PAGEUP,
    "pagedown": pygame.K_PAGEDOWN,
    "insert": pygame.K_INSERT,
    "backspace": pygame.K_BACKSPACE,
    "tab": pygame.K_TAB,
    "clear": pygame.K_CLEAR,
    "return": pygame.K_RETURN,
    "delete": pygame.K_DELETE,
    "f1": pygame.K_F1,
    "f2": pygame.K_F2,
    "f3": pygame.K_F3,
    "f4": pygame.K_F4,
    "f5": pygame.K_F5,
    "f6": pygame.K_F6,
    "f7": pygame.K_F7,
    "f8": pygame.K_F8,
    "f9": pygame.K_F9,
    "f10": pygame.K_F10,
    "f11": pygame.K_F11,
    "f12": pygame.K_F12,
    "f13": pygame.K_F13,
    "f14": pygame.K_F14,
    "f15": pygame.K_F15,
    "numlock": pygame.K_NUMLOCK,
    "capslock": pygame.K_CAPSLOCK,
    "scrolllock": pygame.K_SCROLLLOCK,
    "rshift": pygame.K_RSHIFT,
    "lshift": pygame.K_LSHIFT,
    "rctrl": pygame.K_RCTRL,
    "lctrl": pygame.K_LCTRL,
    "ralt": pygame.K_RALT,
    "lalt": pygame.K_LALT,
    "rgui": pygame.K_RGUI,
    "lgui": pygame.K_LGUI,
    "rmeta": pygame.K_RMETA,
    "lmeta": pygame.K_LMETA,
    "rsuper": pygame.K_RSUPER,
    "lsuper": pygame.K_LSUPER,
    "mode": pygame.K_MODE,
    "pause": pygame.K_PAUSE,
    "escape": pygame.K_ESCAPE,
    "help": pygame.K_HELP,
    "print": pygame.K_PRINT,
    "printscreen": pygame.K_PRINTSCREEN,
    "sysreq": pygame.K_SYSREQ,
    "break": pygame.K_BREAK,
    "menu": pygame.K_MENU,
    "power": pygame.K_POWER,
    "euro": pygame.K_EURO,
    "androidback": pygame.K_AC_BACK
}

class Input:
    def __init__(self) -> None:
        pass

    def pressed(self, keyname: KeyName) -> bool:
        wrapper = pygame.key.get_pressed()
        keycode = string_to_key.get(keyname, pygame.K_UNKNOWN)
        return wrapper[keycode]
    
    def just_pressed(self, keyname: KeyName) -> bool:
        wrapper = pygame.key.get_just_pressed()
        keycode = string_to_key.get(keyname, pygame.K_UNKNOWN)
        return wrapper[keycode]
    
    def released(self, keyname: KeyName) -> bool:
        return not self.pressed(keyname)

    def just_released(self, keyname: KeyName) -> bool:
        wrapper = pygame.key.get_just_released()
        keycode = string_to_key.get(keyname, pygame.K_UNKNOWN)
        return wrapper[keycode]
