from numpy import *
import sys
import matplotlib.pyplot as plt


def powers(lista, n, m):
    new_lista = []

    for i in range(len(lista)):
        new_lista.append([])

    for i in range(len(new_lista)):
        count = 0
        l = n
        for j in lista:
            n = l
            while n <= m:
                new_lista[count].append(j**n)
                n += 1
            count += 1

    return array(new_lista)


def main():
    data = loadtxt(sys.argv[1])
    n = int(sys.argv[2])
    data_set = transpose(data)
    X = [float(i) for i in data_set[0]]
    Y = [float(i) for i in data_set[1]]

    Xp = powers(X, 0, n)
    Yp = powers(Y, 1, 1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[:, 0]

    [[b], [m]] = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    # X2 =
    # Y2 =

    plt.plot(X, Y, "ro")
    # plt.plot(X, Y2)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
