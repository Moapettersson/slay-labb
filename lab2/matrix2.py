import sys
from wordfreq import *

matrix = [[1, 2], [3, 4]]


def transpose(matrix):
    if len(matrix) < 1:
        return []

    new_matrix = []
    for x in range(len(matrix[0])):
        new_matrix.append([])

    for i in matrix:
        count = 0
        for j in i:
            new_matrix[count].append(j)
            count += 1

    return new_matrix


# print(transpose(matrix))

lista = [2, 3, 4]
n = 0
m = 2


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

    return new_lista


# print(powers(lista, n, m))

A = [[0, 1], [1, 0]]

B = [[1, 0], [0, -1]]
# rader är antal listor i matrisen
# kolumner antal element i varje lista
# vi ska ta antal rader från matris A
# och antal kolumner från matris B


def matmul(A, B):
    if len(A) <= 0:
        return []
    if len(B) <= 0:
        return []

    A_rader = len(A)
    A_kolumner = len(A[0])
    B_rader = len(B)
    B_kolumner = len(B[0])

    if A_kolumner != B_rader:
        raise ValueError(
            "Antalet kolumner i matris A och antalet rader i martis B är inte samma."
        )

    result = [[0 for _ in range(B_kolumner)] for _ in range(A_rader)]
    # fyller nya matrisen med rätt antal nollor i listorna

    for i in range(A_rader):
        for j in range(B_kolumner):
            for k in range(A_kolumner):
                result[i][j] += A[i][k] * B[k][j]
    # 'result[i][j]' representerar aktuella index i nya matrisen
    # 'A[i][k]' tar index från A-matrisen
    # 'B[k][j]' tar idex fron B-matrisen
    return result


# print(matmul(A, B))

m1 = [[1, 2], [3, 4]]


def invert(m1):
    new_m1 = []
    for x in range(len(m1)):
        new_m1.append([])
    det = (m1[0][0] * m1[1][1]) - (m1[0][1] * m1[1][0])

    new_m1[0].append(m1[1][1] / det)
    new_m1[0].append(-1 * m1[0][1] / det)
    new_m1[1].append(-1 * m1[1][0] / det)
    new_m1[1].append(m1[0][0] / det)

    return new_m1


# print(invert(m1))


def loadtxt(file_name):
    new_mtx = []
    with open(file_name, "r") as file:
        text = file.read()
    for i in text:
        if i == "\n":
            new_mtx.append([])

    text = text.split()

    kolumner = len(text) / len(new_mtx)

    count = 0
    count1 = 1
    for i in text:
        if count == len(new_mtx):
            break
        elif count1 % kolumner == 0:
            new_mtx[count].append(i)
            count1 += 1
            count += 1
        else:
            new_mtx[count].append(i)
            count1 += 1
    return new_mtx


# eller

# def loadtxt(file):
#     f = open(file, "r")
#     lines = f.readlines()
#     matrix = []
#     for line in lines:
#         line = line.replace('\n', '').split('\t')
#         matrix.append(line)
#     return matrix

# print(loadtxt("chirps.txt"))
