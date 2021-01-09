a = 1
b = 100


def birden_yuze():
    global a
    global b
    a += 1
    if a < b and a % 2 == 0:
        birden_yuze()
    elif a < b and a % 2 != 0:
        print(a)
        birden_yuze()


birden_yuze()
