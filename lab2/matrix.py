def transpose(matrix):
    if len(matrix) < 1:  # Om matrix har mindre än ett element ge tillbaka en tom lista
        return []

    new_matrix = []

    for x in range(
        len(matrix[0])
    ):  # Lägger till nya tomma listor (rows) för new_matrix
        new_matrix.append([])

    for i in matrix:  # Lägger till varje element i 'count' row
        count = 0
        for j in i:
            new_matrix[count].append(j)
            count += 1

    return new_matrix


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
            while (
                n <= m
            ):  # Lägger till värdet med rätt potens på varje plats n-m gånger
                new_list[count].append((j) ** n)
                n += 1
            count += 1

    return new_list


def matmul(mx_1, mx_2):

    # If-loop som hanterar specialfall med tomma matriser samt kollar så att mx_1 och mx_2 är på rätt m x n
    if len(mx_1) <= 0:
        return []
    elif len(mx_2) <= 0:
        return []
    elif len(mx_1[0]) != len(mx_2):
        return

    # Skapar resultatmatrisen och fyller varje plats med nollor så att vi har index-värden till dem
    new_matrix = []
    count = 0
    for i in range(len(mx_1)):
        new_matrix.append([])
        for j in range(len(mx_2[0])):
            new_matrix[count].append(0)
        count += 1

    # Adderar in varje multiplikation av tal från matriserna till respektive plats
    for i in range(len(mx_1)):
        for j in range(len(mx_2[0])):
            for k in range(len(mx_1[0])):
                new_matrix[i][j] += mx_1[i][k] * mx_2[k][j]

    return new_matrix


def invert(mtrx_list):
    list_inv = []

    # Skapar rätt mängd rows i vår inverterade matris
    for i in range(len(mtrx_list)):
        list_inv.append([])

    det = (mtrx_list[0][0] * mtrx_list[1][1]) - (mtrx_list[0][1] * mtrx_list[1][0])

    # Placerar och räknar ut rätt värden för en 2x2 matris
    list_inv[0].append(mtrx_list[1][1] / det)
    list_inv[0].append(-1 * mtrx_list[0][1] / det)
    list_inv[1].append(-1 * mtrx_list[1][0] / det)
    list_inv[1].append(mtrx_list[0][0] / det)

    return list_inv


def loadtxt(file_name):
    new_mtrx = []

    with open(file_name, "r") as file:
        lines = file.read()

    # Lägger till rätt mängd rows i matrisen
    for i in lines:
        if i == "\n":
            new_mtrx.append([])

    lines = lines.split()

    columns = len(lines) // len(new_mtrx)

    count = 0  # Värde som används för att hitta rätt lista (row)
    count_1 = 1  # Värde som används för att hålla koll på hur många element som ska finnas i varje row
    for i in lines:
        if count == len(new_mtrx):  # Ser till att count inte blir för stort
            break
        elif count_1 % columns == 0:  # Flyttar oss till ny lista (row) när det behövs
            new_mtrx[count].append(i)
            count += 1
            count_1 += 1
        else:  # Annars lägger vi bara till värdet i nuvarande lista (row)
            new_mtrx[count].append(i)
            count_1 += 1

    return new_mtrx
