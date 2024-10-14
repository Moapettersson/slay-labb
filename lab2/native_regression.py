from matrix2 import *
import sys
import matplotlib.pyplot as plt


def main():
    data = loadtxt(sys.argv[1])
    data_set = transpose(data)
    X = [float(i) for i in data_set[0]]
    Y = [float(i) for i in data_set[1]]

    Xp = powers(X, 0, 1)
    Yp = powers(Y, 1, 1)
    Xpt = transpose(Xp)

    [[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    Y2 = [b + m * i for i in X]

    plt.plot(X, Y, "ro")
    plt.plot(X, Y2)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
