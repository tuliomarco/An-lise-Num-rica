import sys, math
from sympy import *
import numpy as np

def function(x_value, f):
    return eval(f, {"x": x_value, "math": math})

class NumericalIntegration:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                lines = file.readlines()

            self.functions, self.intervals, self.subdivisions = [], [], []
            
            for line in lines:
                if line.strip():
                    func_str, interval_str, sub_str = line.strip().split(";")
                    
                    interval = list(map(float, interval_str.split(",")))
                    subdivisions = int(sub_str)
                    
                    self.functions.append(func_str)
                    self.intervals.append(interval)
                    self.subdivisions.append(subdivisions)
                    
        except Exception as e:
            print(f"Erro ao ler o arquivo de entrada: {e}")
            sys.exit()
    
    def simple_trapezoidal(self):
        try:
            results = []
            for func_str, interval, n in zip(self.functions, self.intervals, self.subdivisions):
                a, b = interval
                h = (b - a) / n
                x_vals = np.linspace(a, b, n + 1)
                y_vals = [function(x, func_str) for x in x_vals]
                
                integral = h * (0.5 * y_vals[0] + sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
                results.append(round(integral, 4))
            
            with open("output_integration.txt", "w") as file:
                for i, result in enumerate(results):
                    file.write(f"Integral da função {i+1}: {result}\n")
                file.write("\nResultado obtido através da regra do trapézio simples.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
        
    def multiple_trapezoidal(self):
        try:
            results = []
            for func_str, interval, n in zip(self.functions, self.intervals, self.subdivisions):
                a, b = interval
                h = (b - a) / n
                x_vals = np.linspace(a, b, n + 1)
                
                y_vals = [function(x, func_str) for x in x_vals]
                
                integral = h * (0.5 * y_vals[0] + sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
                results.append(round(integral, 4))
            
            with open("output_integration.txt", "w") as file:
                for i, result in enumerate(results):
                    file.write(f"Integral da função {i+1}: {result}\n")
                file.write("\nResultado obtido através da regra dos trapézios múltiplos.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

    def simple_simpson_1_3_aux(self, func_str, interval, n):
        try:
            a, b = interval
            h = (b - a) / 2
            func_at_a = function(a, func_str)
            func_at_mid = function((a + b) / 2, func_str)
            func_at_b = function(b, func_str)

            integral_value = (h / 3) * (func_at_a + 4 * func_at_mid + func_at_b)
            return integral_value

        except Exception as e:
            print(f"Erro no cálculo do método de Simpson 1/3 auxiliar: {e}")
            sys.exit()

    def simple_simpson_1_3(self):
        try:
            with open("output_integration.txt", "w") as file:
                for i, func_str in enumerate(self.functions):
                    a, b = self.intervals[i]
                    n = self.subdivisions[i]

                    integral_value = self.simple_simpson_1_3_aux(func_str, (a, b), n)
                    file.write(f"Integral da função {i + 1}: {integral_value:.4f}\n")
                file.write("\nResultado obtido através da integração pelo método simples de Simpson 1/3\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def multiple_simpson_1_3(self):
        try:
            with open("output_integration.txt", "w") as file:
                for i, func_str in enumerate(self.functions):
                    a, b = self.intervals[i]
                    n = self.subdivisions[i]

                    if n % 2 != 0:
                        n += 1

                    h = (b - a) / n

                    integral_value = function(a, func_str) + function(b, func_str)
                    for j in range(1, n):
                        x_j = a + j * h
                        coeficiente = 4 if j % 2 != 0 else 2
                        integral_value += coeficiente * function(x_j, func_str)

                    integral_value *= h / 3

                    file.write(f"Integral da função {i + 1}: {integral_value:.4f}\n")
                file.write("\nResultado obtido através da integração pelo método múltiplo de Simpson 1/3\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def simple_simpson_3_8(self):
        try:
            with open("output_integration.txt", "w") as file:
                for i, func_str in enumerate(self.functions):
                    a, b = self.intervals[i]
                    n = self.subdivisions[i]

                    if n % 3 != 0:
                        n = n + (3 - (n % 3))

                    h = (b - a) / n

                    integral_value = function(a, func_str) + function(b, func_str)
                    for j in range(1, n):
                        x_j = a + j * h
                        coeficiente = 3 if j % 3 != 0 else 2
                        integral_value += coeficiente * function(x_j, func_str)

                    integral_value *= (3 * h) / 8

                    file.write(f"Integral da função {i + 1}: {integral_value:.4f}\n")
                file.write("\nResultado obtido através da integração pelo método simples de Simpson 3/8\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

    def multiple_simpson_3_8(self):
        try:
            with open("output_integration.txt", "w") as file:
                for i, func_str in enumerate(self.functions):
                    a, b = self.intervals[i]
                    n = self.subdivisions[i]

                    if n % 3 != 0:
                        n = n + (3 - (n % 3))

                    h = (b - a) / n

                    integral_value = 0
                    for j in range(0, n, 3):
                        x0 = a + j * h
                        x1 = a + (j + 1) * h
                        x2 = a + (j + 2) * h
                        x3 = a + (j + 3) * h

                        integral_value += (3 * h / 8) * (function(x0, func_str) + 3 * function(x1, func_str) + 3 * function(x2, func_str) + function(x3, func_str))

                    file.write(f"Integral da função {i + 1}: {integral_value:.4f}\n")
                file.write("\nResultado obtido através da integração pelo método múltiplo de Simpson 3/8\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def richards_extrapolation(self):
        try:
            results = []
            for func_str, interval in zip(self.functions, self.intervals):
                integral_n1 = self.simple_simpson_1_3_aux(func_str, interval, 250)
                integral_n2 = self.simple_simpson_1_3_aux(func_str, interval, 500)

                richardson_result = ((4 / 3) * integral_n2) - ((1 / 3) * integral_n1)
                results.append(richardson_result)

            with open("output_integration.txt", "w") as file:
                for i, result in enumerate(results):
                    file.write(f"Integral da função {i+1}: {round(result, 4)}\n")
                file.write("\nResultado obtido através da extrapolação de Richardson.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
        
    def gaussian_quadrature(self):
        try:
            results = []
            for func_str, interval in zip(self.functions, self.intervals):
                a, b = interval

                pontos_gauss = [-math.sqrt(3)/3, math.sqrt(3)/3]
                pesos_gauss = [1, 1]

                t = lambda u: 0.5 * (b - a) * u + 0.5 * (a + b)

                integral_value = 0
                for i in range(len(pontos_gauss)):
                    integral_value += pesos_gauss[i] * function(t(pontos_gauss[i]), func_str)
                
                integral_value *= (b - a) / 2

                results.append(round(integral_value, 4))

            with open("output_integration.txt", "w") as file:
                for i, result in enumerate(results):
                    file.write(f"Integral da função {i + 1}: {result}\n")
                file.write("\nResultado obtido através da quadratura de Gauss.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

