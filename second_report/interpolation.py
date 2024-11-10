import sys
from sympy import *
import numpy as np

class Interpolation:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                lines = file.readlines()

            self.data_sets = []
            for line in lines:
                x_values_str, y_values_str = line.strip().split(";")
                x_values = list(map(float, x_values_str.split(",")))
                y_values = list(map(float, y_values_str.split(",")))
                self.data_sets.append((x_values, y_values))

        except Exception as e:
            print(f"Erro ao ler o arquivo de entrada: {e}")
            sys.exit()

    def lagrange_polynomial(self):
        x = Symbol('x')
        output_file = "output_interpolation.txt"
        
        try:
            with open(output_file, "w") as file:
                for idx, (x_values, y_values) in enumerate(self.data_sets, start=1):
                    n = len(x_values)
                    lagrange_poly = 0

                    for i in range(n):
                        L_i = 1
                        for j in range(n):
                            if i != j:
                                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
                        lagrange_poly += L_i * y_values[i]

                    lagrange_poly = expand(lagrange_poly)
                    file.write(f"Conjunto {idx}: {lagrange_poly}\n")
                file.write("\nResultado obtido pelo polinômio de Lagrange\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def newton_divided_differences(self):
        output_file = "output_interpolation.txt"
        try:
            with open(output_file, "w") as file:
                for idx, (x_values, y_values) in enumerate(self.data_sets, start=1):
                    n = len(x_values)
                    diferencas_div = np.zeros((n, n))
                    diferencas_div[:, 0] = y_values

                    for j in range(1, n):
                        for i in range(n - j):
                            diferencas_div[i][j] = (diferencas_div[i + 1][j - 1] - diferencas_div[i][j - 1]) / (x_values[i + j] - x_values[i])

                    newton_poly = diferencas_div[0][0]
                    x = Symbol('x')
                    for j in range(1, n):
                        termo = diferencas_div[0][j]
                        for i in range(j):
                            termo *= (x - x_values[i])
                        newton_poly += termo

                    newton_poly = expand(newton_poly)
                    file.write(f"Conjunto {idx}: {newton_poly}\n")
                file.write("\nResultado obtido pelo polinômio de Newton\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
