a = 1
b = 500
def birden_besyuze():
    global a
    global b
    a += 1
    if a < b and a % 5 == 0:
        print(a)
        birden_besyuze()
    elif a < b and a % 5 != 0:

        birden_besyuze()


birden_besyuze()