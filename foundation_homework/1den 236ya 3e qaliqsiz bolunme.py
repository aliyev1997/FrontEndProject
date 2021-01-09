a = 1
b = 236
def birden_ikiyuz():
    global a
    global b
    a += 1
    if a < b and a % 3 == 0:
        print(a)
        birden_ikiyuz()
    elif a < b and a % 3 != 0:

        birden_ikiyuz()

birden_ikiyuz()
