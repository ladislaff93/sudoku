'''
    To-Do:
        -spravit logicku sekvenciu aby sa nedalo klinut čislo predtym nez kliknem na poličko kam chcem cislo pridat
        -
'''
def fun():
    for i in range(3):
        if fun(i):
            return True
    return False

fun()