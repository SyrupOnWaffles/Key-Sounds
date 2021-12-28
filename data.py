import pygame
pygame.init()
asciiArt = """
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                 
            <                NOk0OxxON                 >
            <                XodkxxddK                 >
            <             WXXOd0XKX0k0NNNWW            >
            <          WXKOdkkdxkk0OkOkxxOOOX          >
            <        WNKKX0OOOxddxkkxxdxOKXK0N         >
            <        NKNNNNNNNNXXXXXKK0OX  WKxx0N      >
            <      WXOK  WWWWNNNNNNNKXNKXN  W0kkk0N    >
            <     WKxxX            WXXXOk0WWNK0OxON    >
            <    NOk0KKKKKXXXNWWWW WKkkxOK00KkOOOW     >
            <    WK0K00Ooloxkx0K0KKKKOO0kxxOXkxkK      >
            <      XX0OOocoOKOk0OkkKOk0kxkdkOxx0N      >
            <      NX0OX0oo0NXkxxOOKkONkxOk00XW        >
            <       N00NN0OXWWNO0NWWOO0dkKNWW          >
            <         WNN0lxXNXK0KXXOkx0W              >
            <            XdOW  WNNNNNKOK               >
            <            WNW         WNW               >
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
switch = "Tecsee Carrots"
                                                
keylist = {
    # Letters
    "A": pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
    "B": pygame.mixer.Sound("sounds/" + switch + "/B.wav"),
    "C": pygame.mixer.Sound("sounds/" + switch + "/C.wav"),
    "D": pygame.mixer.Sound("sounds/" + switch + "/D.wav"),
    "E": pygame.mixer.Sound("sounds/" + switch + "/E.wav"),
    "F": pygame.mixer.Sound("sounds/" + switch + "/F.wav"),
    "G": pygame.mixer.Sound("sounds/" + switch + "/G.wav"),
    "H": pygame.mixer.Sound("sounds/" + switch + "/H.wav"),
    "I": pygame.mixer.Sound("sounds/" + switch + "/I.wav"),
    "J": pygame.mixer.Sound("sounds/" + switch + "/J.wav"),
    "K": pygame.mixer.Sound("sounds/" + switch + "/K.wav"),
    "L": pygame.mixer.Sound("sounds/" + switch + "/L.wav"),
    "M": pygame.mixer.Sound("sounds/" + switch + "/M.wav"),
    "N": pygame.mixer.Sound("sounds/" + switch + "/N.wav"),
    "O": pygame.mixer.Sound("sounds/" + switch + "/O.wav"),
    "P": pygame.mixer.Sound("sounds/" + switch + "/P.wav"),
    "Q": pygame.mixer.Sound("sounds/" + switch + "/Q.wav"),
    "R": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),
    "S": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),
    "T": pygame.mixer.Sound("sounds/" + switch + "/T.wav"),
    "U": pygame.mixer.Sound("sounds/" + switch + "/U.wav"),
    "V": pygame.mixer.Sound("sounds/" + switch + "/V.wav"),
    "W": pygame.mixer.Sound("sounds/" + switch + "/W.wav"),
    "X": pygame.mixer.Sound("sounds/" + switch + "/X.wav"),
    "Y": pygame.mixer.Sound("sounds/" + switch + "/Y.wav"),
    "Z": pygame.mixer.Sound("sounds/" + switch + "/Z.wav"),
    # Numbers, symbols
    "`": pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
    '"': pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
    ";": pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
    ":": pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
    "'": pygame.mixer.Sound("sounds/" + switch + "/K.wav"),
    ",": pygame.mixer.Sound("sounds/" + switch + "/J.wav"),
    "<": pygame.mixer.Sound("sounds/" + switch + "/J.wav"),
    ".": pygame.mixer.Sound("sounds/" + switch + "/F.wav"),
    ">": pygame.mixer.Sound("sounds/" + switch + "/F.wav"),
    "?": pygame.mixer.Sound("sounds/" + switch + "/U.wav"),
    "\\": pygame.mixer.Sound("sounds/" + switch + "/E.wav"),
    "|": pygame.mixer.Sound("sounds/" + switch + "/E.wav"),
    "/": pygame.mixer.Sound("sounds/" + switch + "/E.wav"),
    "[": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),
    "]": pygame.mixer.Sound("sounds/" + switch + "/C.wav"),
    "{": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),
    "}": pygame.mixer.Sound("sounds/" + switch + "/C.wav"),
    "~": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),
    "+": pygame.mixer.Sound("sounds/" + switch + "/C.wav"),
    "=": pygame.mixer.Sound("sounds/" + switch + "/C.wav"),
    "-": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),
    "_": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),

    "1": pygame.mixer.Sound("sounds/" + switch + "/P.wav"),
    "2": pygame.mixer.Sound("sounds/" + switch + "/Q.wav"),
    "3": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),
    "4": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),
    "5": pygame.mixer.Sound("sounds/" + switch + "/T.wav"),
    "6": pygame.mixer.Sound("sounds/" + switch + "/U.wav"),
    "7": pygame.mixer.Sound("sounds/" + switch + "/V.wav"),
    "8": pygame.mixer.Sound("sounds/" + switch + "/W.wav"),
    "9": pygame.mixer.Sound("sounds/" + switch + "/X.wav"),
    "0": pygame.mixer.Sound("sounds/" + switch + "/Y.wav"),

    "!": pygame.mixer.Sound("sounds/" + switch + "/P.wav"),
    "@": pygame.mixer.Sound("sounds/" + switch + "/Q.wav"),
    "#": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),
    "$": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),
    "%": pygame.mixer.Sound("sounds/" + switch + "/T.wav"),
    "^": pygame.mixer.Sound("sounds/" + switch + "/U.wav"),
    "&": pygame.mixer.Sound("sounds/" + switch + "/V.wav"),
    "*": pygame.mixer.Sound("sounds/" + switch + "/W.wav"),
    "(": pygame.mixer.Sound("sounds/" + switch + "/X.wav"),
    ")": pygame.mixer.Sound("sounds/" + switch + "/Y.wav"),

    # Big keys, random keys
    "BACKSPACE": pygame.mixer.Sound("sounds/" + switch + "/BACKSPACE.wav"),
    "CAPS_LOCK": pygame.mixer.Sound("sounds/" + switch + "/CAPS LOCK.wav"),
    "SPACE": pygame.mixer.Sound("sounds/" + switch + "/SPACE.wav"),
    "ENTER": pygame.mixer.Sound("sounds/" + switch + "/ENTER.wav"),
    "CTRL": pygame.mixer.Sound("sounds/" + switch + "/CTRL.wav"),
    "CTRL_R": pygame.mixer.Sound("sounds/" + switch + "/CTRL.wav"),
    "MENU": pygame.mixer.Sound("sounds/" + switch + "/K.wav"),
    "TAB": pygame.mixer.Sound("sounds/" + switch + "/TAB.wav"),
    "ALT": pygame.mixer.Sound("sounds/" + switch + "/ALT.wav"),
    "ALT_R": pygame.mixer.Sound("sounds/" + switch + "/ALT.wav"),
    "SHIFT": pygame.mixer.Sound(  "sounds/" + switch + "/SHIFT.wav"),
    "SHIFT_R": pygame.mixer.Sound("sounds/" + switch + "/SHIFT.wav"),
    "ESC": pygame.mixer.Sound("sounds/" + switch + "/B.wav"),
    "NONE": pygame.mixer.Sound("sounds/" + switch + "/B.wav"),

    # Arrows
    "UP": pygame.mixer.Sound("sounds/" + switch + "/J.wav"),
    "LEFT": pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
    "RIGHT": pygame.mixer.Sound("sounds/" + switch + "/D.wav"),
    "DOWN": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),

    # Function Keys
    "F1": pygame.mixer.Sound("sounds/" + switch + "/P.wav"),
    "F2": pygame.mixer.Sound("sounds/" + switch + "/Q.wav"),
    "F3": pygame.mixer.Sound("sounds/" + switch + "/R.wav"),
    "F4": pygame.mixer.Sound("sounds/" + switch + "/S.wav"),
    "F5": pygame.mixer.Sound("sounds/" + switch + "/T.wav"),
    "F6": pygame.mixer.Sound("sounds/" + switch + "/U.wav"),
    "F7": pygame.mixer.Sound("sounds/" + switch + "/V.wav"),
    "F8": pygame.mixer.Sound("sounds/" + switch + "/W.wav"),
    "F9": pygame.mixer.Sound("sounds/" + switch + "/X.wav"),
    "F10": pygame.mixer.Sound("sounds/" + switch + "/Y.wav"),
    "F11": pygame.mixer.Sound("sounds/" + switch + "/Z.wav"),
    "F12": pygame.mixer.Sound("sounds/" + switch + "/Z.wav"),
    
    # 
    "PRINT_SCREEN": pygame.mixer.Sound("sounds/" + switch + "/T.wav"),
    "SCROLL_LOCK": pygame.mixer.Sound("sounds/" + switch + "/U.wav"),
    "PAUSE": pygame.mixer.Sound("sounds/" + switch + "/V.wav"),
    "INSERT": pygame.mixer.Sound("sounds/" + switch + "/W.wav"),
    "HOME": pygame.mixer.Sound("sounds/" + switch + "/X.wav"),
    "PAGE_UP": pygame.mixer.Sound("sounds/" + switch + "/Y.wav"),
    "DELETE": pygame.mixer.Sound("sounds/" + switch + "/Z.wav"),
    "END": pygame.mixer.Sound("sounds/" + switch + "/Z.wav"),
    "PAGE_DOWN": pygame.mixer.Sound("sounds/" + switch + "/A.wav"),
}