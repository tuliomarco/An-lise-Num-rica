import sys
import numpy as np

class LinearSystems:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                inputs = file.readlines()
                A = [list(map(float, row.strip("[]").split(","))) for row in inputs[0].strip().split("][")]
                b = list(map(float, inputs[1].strip("[]").split(",")))
                
                self.A = np.array(A)
                self.b = np.array(b)

        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            sys.exit()

    def gaussian_elimination(self):
        A = self.A.copy()
        b = self.b.copy()
        n = len(b)

        for i in range(n):
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                A[j] -= factor * A[i]
                b[j] -= factor * b[i]

        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

        x[np.abs(x) < 1e-10] = 0.0

        with open("linear_systems_output.txt", "w") as file:
            file.write("Solução: " + "[" + ", ".join(f"{val:.5f}" for val in x) + "]")
            file.write("\nResultado obtido com o método da Eliminação de Gauss.")
    
    def lu_factorization(self):
        A = self.A.copy()
        b = self.b.copy()
        n = len(b)

        L = np.eye(n)
        for i in range(n):
            for j in range(i + 1, n):
                L[j, i] = A[j, i] / A[i, i]
                A[j] -= L[j, i] * A[i]

        U = A
        y = np.zeros(n)
        for i in range(n):
            y[i] = b[i] - np.dot(L[i, :i], y[:i])

        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
        
        x[np.abs(x) < 1e-10] = 0.0

        with open("linear_systems_output.txt", "w") as file:
            file.write("Solução: [" + ", ".join(f"{val:.5f}" for val in x) + "]")
            file.write("\nResultado obtido com o método da Fatoração LU")

    def jacobi(self, max_iterations=100, tolerance=1e-5):
        self.make_diagonally_dominant()

        A = self.A.copy()
        b = self.b.copy()
        n = len(b)
        x = np.zeros(n)
        x_new = np.zeros(n)
        iterations = 0

        with open("linear_systems_output.txt", "w") as file:
            file.write("Contador:\n")

            for iteration in range(max_iterations):
                for i in range(n):
                    sum_ax = sum(A[i][j] * x[j] for j in range(n) if i != j)
                    x_new[i] = (b[i] - sum_ax) / A[i][i]

                if np.linalg.norm(x_new - x) < tolerance:
                    break

                x[:] = x_new
                iterations += 1
                
                file.write(f"{iterations}  {x.tolist()}\n")

            file.write("\nResultado final: " + "[" + ", ".join(f"{val:.5f}" for val in x) + "]\n")
            file.write("\nResultado obtido com o método de Jacobi")

    def gauss_seidel(self, max_iterations=100, tolerance=1e-5):
            self.make_diagonally_dominant()
            
            A = self.A.copy()
            b = self.b.copy()
            n = len(b)
            x = np.zeros(n)
            iterations = 0

            with open("linear_systems_output.txt", "w") as file:
                file.write("Contador:\n")

                for iteration in range(max_iterations):
                    x_old = np.copy(x)
                    for i in range(n):
                        sum_ax = sum(A[i][j] * x[j] for j in range(i))
                        sum_ax += sum(A[i][j] * x_old[j] for j in range(i + 1, n))
                        x[i] = (b[i] - sum_ax) / A[i][i]

                    if np.linalg.norm(x - x_old) < tolerance:
                        break

                    iterations += 1
                    
                    file.write(f"{iterations}  {x.tolist()}\n")

                file.write("\nResultado final: " + "[" + ", ".join(f"{val:.5f}" for val in x) + "]\n")
                file.write("\nResultado obtido com o método de Gauss-Seidel")

    def make_diagonally_dominant(self):
        A = self.A.copy()
        b = self.b.copy()
        n = len(b)

        for i in range(n):
            max_index = i + np.argmax(np.abs(A[i:, i]))
            if max_index != i:
                A[[i, max_index]] = A[[max_index, i]]
                b[[i, max_index]] = b[[max_index, i]]

        self.A = A
        self.b = b