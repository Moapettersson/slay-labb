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


def poly(a, x):
    return sum(a[i] * (x**i) for i in range(len(a)))


def main():
    # Load the data from the file
    data = loadtxt(sys.argv[1])
    n = int(sys.argv[2])  # Degree of the polynomial

    # Transpose the data to get X and Y
    data_set = transpose(data)
    X = [float(i) for i in data_set[0]]
    Y = [float(i) for i in data_set[1]]

    # Create the design matrix for polynomial regression
    # Xp = powers(X, 0, n)  # Adjust powers for the given degree
    # Yp = array(Y).reshape(-1, 1)  # Reshape Y into a column vector

    # # Transpose Xp for matrix multiplication
    # Xpt = transpose(Xp)

    Xp = powers(X, 0, n)
    Yp = powers(Y, 1, 1)
    Xpt = Xp.transpose()

    # Calculate the polynomial regression coefficients
    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    # Create a smooth curve for the polynomial by generating more X values
    X2 = linspace(min(X), max(X), int((max(X) - min(X)) / 0.2))
    Y2 = [sum([a[i] * (x**i) for i in range(len(a))]) for x in X2]

    # Plot the original data and the polynomial curve
    plt.plot(X, Y, "ro")  # Original data points
    plt.plot(X2, Y2)  # Polynomial regression curve
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
