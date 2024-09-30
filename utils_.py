from random import randrange

def InputValidator(txt, a, A):
    while True:
        i = (input(f"{txt} ({a}-{A}) :"))
        i = (''.join([e if e.isdigit() else '' for e in i]))
        if i != '':
            i = int(i)
            if i >= a and i <= A:
                break
            else:
                print("Datos no validos, Inténtalo de nuevo ")
        else:
            print("Datos no validos, Inténtalo de nuevo ")
    return i

def InputTextValidator(txt, A):
    while True:
        i = (input(f"{txt} (0 a {A} caracteres) :"))
        if len(i) <= A:
            break
        else:
            print("Datos no validos, Inténtalo de nuevo ")
    return i.upper()

def generarAleatorio():
    while True:
        m = [randrange(2),randrange(2),randrange(2),randrange(2),randrange(2)]
        if 1 in m:
            break
    return m