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
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   
                      Enjoy the NK Creams!"""
                                                
keylist = {
    # Letters
    "A": pygame.mixer.Sound("sounds/A.wav"),
    "B": pygame.mixer.Sound("sounds/B.wav"),
    "C": pygame.mixer.Sound("sounds/C.wav"),
    "D": pygame.mixer.Sound("sounds/D.wav"),
    "E": pygame.mixer.Sound("sounds/E.wav"),
    "F": pygame.mixer.Sound("sounds/F.wav"),
    "G": pygame.mixer.Sound("sounds/G.wav"),
    "H": pygame.mixer.Sound("sounds/H.wav"),
    "I": pygame.mixer.Sound("sounds/I.wav"),
    "J": pygame.mixer.Sound("sounds/J.wav"),
    "K": pygame.mixer.Sound("sounds/K.wav"),
    "L": pygame.mixer.Sound("sounds/L.wav"),
    "M": pygame.mixer.Sound("sounds/M.wav"),
    "N": pygame.mixer.Sound("sounds/N.wav"),
    "O": pygame.mixer.Sound("sounds/O.wav"),
    "P": pygame.mixer.Sound("sounds/P.wav"),
    "Q": pygame.mixer.Sound("sounds/Q.wav"),
    "R": pygame.mixer.Sound("sounds/R.wav"),
    "S": pygame.mixer.Sound("sounds/S.wav"),
    "T": pygame.mixer.Sound("sounds/T.wav"),
    "U": pygame.mixer.Sound("sounds/U.wav"),
    "V": pygame.mixer.Sound("sounds/V.wav"),
    "W": pygame.mixer.Sound("sounds/W.wav"),
    "X": pygame.mixer.Sound("sounds/X.wav"),
    "Y": pygame.mixer.Sound("sounds/Y.wav"),
    "Z": pygame.mixer.Sound("sounds/Z.wav"),
    # Numbers, symbols
    "`": pygame.mixer.Sound("sounds/A.wav"),
    '"': pygame.mixer.Sound("sounds/A.wav"),
    ";": pygame.mixer.Sound("sounds/A.wav"),
    ":": pygame.mixer.Sound("sounds/A.wav"),
    "'": pygame.mixer.Sound("sounds/K.wav"),
    ",": pygame.mixer.Sound("sounds/J.wav"),
    "<": pygame.mixer.Sound("sounds/J.wav"),
    ".": pygame.mixer.Sound("sounds/F.wav"),
    ">": pygame.mixer.Sound("sounds/F.wav"),
    "?": pygame.mixer.Sound("sounds/U.wav"),
    "\\": pygame.mixer.Sound("sounds/E.wav"),
    "|": pygame.mixer.Sound("sounds/E.wav"),
    "/": pygame.mixer.Sound("sounds/E.wav"),
    "[": pygame.mixer.Sound("sounds/S.wav"),
    "]": pygame.mixer.Sound("sounds/C.wav"),
    "{": pygame.mixer.Sound("sounds/S.wav"),
    "}": pygame.mixer.Sound("sounds/C.wav"),
    "~": pygame.mixer.Sound("sounds/R.wav"),
    "+": pygame.mixer.Sound("sounds/C.wav"),
    "=": pygame.mixer.Sound("sounds/C.wav"),
    "-": pygame.mixer.Sound("sounds/R.wav"),
    "_": pygame.mixer.Sound("sounds/R.wav"),

    "1": pygame.mixer.Sound("sounds/P.wav"),
    "2": pygame.mixer.Sound("sounds/Q.wav"),
    "3": pygame.mixer.Sound("sounds/R.wav"),
    "4": pygame.mixer.Sound("sounds/S.wav"),
    "5": pygame.mixer.Sound("sounds/T.wav"),
    "6": pygame.mixer.Sound("sounds/U.wav"),
    "7": pygame.mixer.Sound("sounds/V.wav"),
    "8": pygame.mixer.Sound("sounds/W.wav"),
    "9": pygame.mixer.Sound("sounds/X.wav"),
    "0": pygame.mixer.Sound("sounds/Y.wav"),

    "!": pygame.mixer.Sound("sounds/P.wav"),
    "@": pygame.mixer.Sound("sounds/Q.wav"),
    "#": pygame.mixer.Sound("sounds/R.wav"),
    "$": pygame.mixer.Sound("sounds/S.wav"),
    "%": pygame.mixer.Sound("sounds/T.wav"),
    "^": pygame.mixer.Sound("sounds/U.wav"),
    "&": pygame.mixer.Sound("sounds/V.wav"),
    "*": pygame.mixer.Sound("sounds/W.wav"),
    "(": pygame.mixer.Sound("sounds/X.wav"),
    ")": pygame.mixer.Sound("sounds/Y.wav"),

    # Big keys, random keys
    "BACKSPACE": pygame.mixer.Sound("sounds/BACKSPACE.wav"),
    "CAPS_LOCK": pygame.mixer.Sound("sounds/CAPS LOCK.wav"),
    "SPACE": pygame.mixer.Sound("sounds/SPACE.wav"),
    "ENTER": pygame.mixer.Sound("sounds/ENTER.wav"),
    "CTRL": pygame.mixer.Sound("sounds/CTRL.wav"),
    "CTRL_R": pygame.mixer.Sound("sounds/CTRL.wav"),
    "MENU": pygame.mixer.Sound("sounds/K.wav"),
    "TAB": pygame.mixer.Sound("sounds/TAB.wav"),
    "ALT": pygame.mixer.Sound("sounds/ALT.wav"),
    "ALT_R": pygame.mixer.Sound("sounds/ALT.wav"),
    "SHIFT": pygame.mixer.Sound("sounds/SHIFT.wav"),
    "SHIFT_R": pygame.mixer.Sound("sounds/SHIFT_R.wav"),
    "ESC": pygame.mixer.Sound("sounds/B.wav"),
    "NONE": pygame.mixer.Sound("sounds/B.wav"),

    # Arrows
    "UP": pygame.mixer.Sound("sounds/J.wav"),
    "LEFT": pygame.mixer.Sound("sounds/A.wav"),
    "RIGHT": pygame.mixer.Sound("sounds/D.wav"),
    "DOWN": pygame.mixer.Sound("sounds/S.wav"),

    # Function Keys
    "F1": pygame.mixer.Sound("sounds/P.wav"),
    "F2": pygame.mixer.Sound("sounds/Q.wav"),
    "F3": pygame.mixer.Sound("sounds/R.wav"),
    "F4": pygame.mixer.Sound("sounds/S.wav"),
    "F5": pygame.mixer.Sound("sounds/T.wav"),
    "F6": pygame.mixer.Sound("sounds/U.wav"),
    "F7": pygame.mixer.Sound("sounds/V.wav"),
    "F8": pygame.mixer.Sound("sounds/W.wav"),
    "F9": pygame.mixer.Sound("sounds/X.wav"),
    "F10": pygame.mixer.Sound("sounds/Y.wav"),
    "F11": pygame.mixer.Sound("sounds/Z.wav"),
    "F12": pygame.mixer.Sound("sounds/Z.wav"),
    
    # 
    "PRINT_SCREEN": pygame.mixer.Sound("sounds/T.wav"),
    "SCROLL_LOCK": pygame.mixer.Sound("sounds/U.wav"),
    "PAUSE": pygame.mixer.Sound("sounds/V.wav"),
    "INSERT": pygame.mixer.Sound("sounds/W.wav"),
    "HOME": pygame.mixer.Sound("sounds/X.wav"),
    "PAGE_UP": pygame.mixer.Sound("sounds/Y.wav"),
    "DELETE": pygame.mixer.Sound("sounds/Z.wav"),
    "END": pygame.mixer.Sound("sounds/Z.wav"),
    "PAGE_DOWN": pygame.mixer.Sound("sounds/A.wav"),
}