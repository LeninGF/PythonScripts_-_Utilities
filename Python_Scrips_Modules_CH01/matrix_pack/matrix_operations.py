import numpy as np


def matrix_sum(matrix1, matrix2):
    fila1, col1 = np.shape(matrix1)
    fila2, col2 = np.shape(matrix2)

    if not fila1==fila2 and col1==col2:
        raise ValueError('dimensiones incompatibles')
    else:
        c = np.zeros((fila1, col1))
        # c = matrix2
        for fila in range(fila1):
            for columna in range(col1):
                c[fila][columna] = matrix1[fila][columna]+matrix2[fila][columna]
    return c


def main():
    a = np.array([[1, 2, 3], [1, 2, 3]])
    b = np.array([[4, 5, 6], [7, 8, 9]])
    ans = matrix_sum(a, b)
    print('Suma de \n', a)
    print('con \n', b)
    print('es')
    print(ans)


if __name__ == '__main__':
    main()