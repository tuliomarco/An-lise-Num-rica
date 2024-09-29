import sys
import numpy as np

class Matrix:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                inputs = file.readlines()
                self.A = np.array([list(map(float, line.strip().strip('[]').split(','))) for line in inputs if line.strip()])

        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            sys.exit()

    def lu_factorization(self):
        A = self.A.copy()
        n = len(A)

        L = np.eye(n)
        U = A.copy()

        for i in range(n):
            for j in range(i + 1, n):
                if U[i, i] == 0:
                    raise ValueError("Pivô não pode ser zero.")
                L[j, i] = U[j, i] / U[i, i]
                U[j] -= L[j, i] * U[i]

        return L, U

    def inverse(self):
        L, U = self.lu_factorization()
        n = len(U)

        inv_matrix = np.zeros((n, n))

        for i in range(n):
            b = np.zeros(n)
            b[i] = 1
            y = np.zeros(n)

            for j in range(n):
                y[j] = b[j] - np.dot(L[j, :j], y[:j])

            x = np.zeros(n)

            for j in range(n - 1, -1, -1):
                x[j] = (y[j] - np.dot(U[j, j + 1:], x[j + 1:])) / U[j, j]

            inv_matrix[:, i] = x

        return inv_matrix

    def condition_number(self):
        norm_A = np.linalg.norm(self.A, ord=2) 
        inv_A = self.inverse()
        norm_A_inv = np.linalg.norm(inv_A, ord=2)
        cond_number = norm_A * norm_A_inv

        with open("matrix_output.txt", "w") as file:
            file.write(f"Número de condição da matriz: {cond_number:.5f}\n")
            file.write("\nMatriz inversa:\n")
            for row in inv_A:
                file.write(f"[{', '.join(f'{value:.5f}' for value in row)}]\n")
