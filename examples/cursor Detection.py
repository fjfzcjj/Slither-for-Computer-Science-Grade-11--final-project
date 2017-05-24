from ctypes import windll, Structure, c_ulong, byref


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}



while True:
    pos = queryMousePosition()
    print(pos)
