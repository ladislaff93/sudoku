def fun():
    for i in range(3):
        if fun(i):
            return True
    return False

fun()