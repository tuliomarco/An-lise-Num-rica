import sys
from sympy import *
import numpy as np

import math

def function(x, f):
    return eval(f, {"x": x, "math": math})

class RegressionApproximation:
    def __init__(self, method):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                self.data_sets = []
                self.functions, self.intervals = [], []
                
                x = Symbol("x")
                
                for line in file:
                    if line.strip():
                        aux = line.split(";")
                        
                        if method == 1 or method == 2:
                            x_vals = [eval(x_val) for x_val in aux[0].split(",")]
                            y_vals = [eval(y_val) for y_val in aux[1].strip().split(",")]
                            self.data_sets.append((x_vals, y_vals))
                        elif method == 3:
                            func = function(x, aux[0].strip())
                            interval = [eval(x_val) for x_val in aux[1].split(",")]
                            self.functions.append(func)
                            self.intervals.append(interval)
            
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            sys.exit()

    def linear_regression(self):
        try:
            with open("output_regression_approximation.txt", "w") as file:
                
                for idx, (values_x, values_y) in enumerate(self.data_sets):
                    x_sum = sum(values_x)
                    y_sum = sum(values_y)
                    xy_sum = sum(x * y for x, y in zip(values_x, values_y))
                    x_squared_sum = sum(x**2 for x in values_x)
                    n = len(values_x)

                    b = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum**2)
                    a = (y_sum - b * x_sum) / n
                    
                    b, a = round(b, 2), round(a, 2)
                    result = f"y = {b}*x + {a}" if a >= 0 else f"y = {b}*x - {abs(a)}"
                    file.write(f"Conjunto {idx+1}: {result}\n")
                file.write("\nResultado obtido pela regressão linear\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def discrete_polynomial_approximation(self):
        try:
            x = Symbol("x")
            basis_functions = [1, x, x**2]
            num_functions = len(basis_functions)
            
            with open("output_regression_approximation.txt", "w") as file:

                for idx, (values_x, values_y) in enumerate(self.data_sets):
                    num_values = len(values_x)
                    matrix_Ui = [[1] * num_values]

                    for func in basis_functions[1:]:
                        row = [func.subs(x, value) for value in values_x]
                        matrix_Ui.append(row)

                    vector_F = np.zeros((num_functions, 1))
                    matrix_M = np.zeros((num_functions, num_functions))
                    
                    for i in range(num_functions):
                        for j in range(num_functions):
                            matrix_M[i, j] = sum(np.multiply(matrix_Ui[i], matrix_Ui[j]))
                        vector_F[i, 0] = sum(np.multiply(values_y, matrix_Ui[i]))

                    solution = np.linalg.solve(matrix_M, vector_F)
                    result_expression = sum(round(solution[i, 0], 2) * x**i for i in range(num_functions))
                    
                    file.write(f"Conjunto {idx+1}: y = {result_expression}\n")
                file.write("\nResultado obtido pela aproximação polinomial discreta\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def continuous_polynomial_approximation(self):
        try:
            x = Symbol("x")
            basis_functions = [1, x, x**2]
            num_basis = len(basis_functions)
            
            with open("output_regression_approximation.txt", "w") as file:
                
                for idx, (func, interval) in enumerate(zip(self.functions, self.intervals)):
                    matrix_M = zeros(num_basis)
                    vector_F = zeros(num_basis, 1)
                    
                    for i in range(num_basis):
                        for j in range(num_basis):
                            integrand_M = basis_functions[i] * basis_functions[j]
                            matrix_M[i, j] = integrate(integrand_M, (x, interval[0], interval[1]))
                        
                        integrand_F = basis_functions[i] * func
                        vector_F[i, 0] = integrate(integrand_F, (x, interval[0], interval[1]))

                    coefficients = matrix_M.LUsolve(vector_F)
                    
                    approx_expression = sum(round(coefficients[i, 0], 5) * basis_functions[i] for i in range(num_basis))
                    file.write(f"Função {idx+1}: y = {approx_expression}\n")
                file.write("\nResultado obtido pela aproximação polinomial contínua\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
