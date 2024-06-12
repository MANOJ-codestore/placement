def x_shape(size):
    if size % 2 == 0:
        return

    for row in range(size):
        for col in range(size):
            if col == row or row+col == size-1 :
                print("*", end="")
            else:
                print(" ", end="")
        print()


n = 5
x_shape(n)