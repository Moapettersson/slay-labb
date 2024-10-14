from numpy import *
import sys
import matplotlib.pyplot as plt


def powers(base_list, n, m):
    new_list = []

    # Lägger till nya tomma listor (rows) för new_list
    for i in range(len(base_list)):
        new_list.append([])

    for i in range(len(new_list)):
        count = 0
        l = n  # Sparar n-värdet så att vi kan iterera över det men sedan återanvända ursprungsvärdet i nästa loop
        for j in base_list:
            n = l
            while n <= int(
                m
            ):  # Lägger till värdet med rätt potens på varje plats n-m gånger
                new_list[count].append((j) ** n)
                n += 1
            count += 1

    matrises = array(new_list)

    return matrises


# Adderar ihop summan av polynomet enligt formeln
def poly(a, x):
    koefficient = 0
    for i in range(len(a)):
        koefficient += a[i] * (x**i)

    return koefficient


def main():

    n = sys.argv[2]

    # Laddar in datan och delar upp kolumnernas olika värde i egna listor m.h.a transpose
    data = loadtxt(sys.argv[1])
    data_set = transpose(data)
    X = [float(i) for i in data_set[0]]
    Y = [float(i) for i in data_set[1]]

    Xp = powers(X, 0, n)
    Yp = powers(Y, 1, 1)
    Xpt = transpose(Xp)

    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[:, 0]

    X2 = linspace(min(X), max(X), int((max(X) - min(X)) / 0.2)).tolist()
    Y2 = [poly(a, x) for x in X2]

    plt.plot(X, Y, "ro")  # Ritar punkter
    plt.plot(X2, Y2)  # Ritar linje
    plt.show()


if __name__ == "__main__":
    main()
