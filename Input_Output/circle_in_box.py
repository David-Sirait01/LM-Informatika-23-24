from math import pi

def main():
    s = int(input("Sisi\n>>> "))
    var = []

    '''
        var[0] = luas persegi
        var[1] = r
        var[2] = luas lingkaran
        var[3] = L.lingkaran - L.persegi
    '''

    var.append((s**2))
    var.append(s/2)
    ls = pi * var[1] ** 2
    var.append(ls)
    var.append(var[0] - var[2])

    print(f"")