import sys
import numpy as np
from sympy import symbols, sympify

class BoundaryMethods:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                self.functions = []
                self.initial_values = []
                self.intervals = []
                self.target_values = []
                self.steps = []
                self.points = []
                self.parameters_list = []  # Lista de dicionários para armazenar parâmetros

                for line in file:
                    if line.strip():
                        aux = line.strip().split(";")
                        
                        # Lendo função
                        x, y = symbols("x y")
                        func = sympify(aux[0].strip())  # Avaliação segura da função
                        self.functions.append(func)

                        # Lendo valor inicial de y
                        y0 = float(aux[1].strip())
                        self.initial_values.append(y0)

                        # Lendo intervalo
                        interval = [float(val) for val in aux[2].strip().split(",")]
                        self.intervals.append(interval)

                        # Lendo valor alvo
                        target = float(aux[3].strip())
                        self.target_values.append(target)

                        # Lendo passo h
                        h = float(aux[4].strip())
                        self.steps.append(h)

                        # Lendo número de pontos
                        n = int(aux[5].strip())
                        self.points.append(n)

                        # Lendo parâmetros adicionais
                        parameters = {}
                        if len(aux) > 6:
                            for param in aux[6:]:
                                key, value = param.strip().split("=")
                                parameters[key.strip()] = float(value.strip())
                        self.parameters_list.append(parameters)
        
        except Exception as e:
            print(f"Erro ao ler o arquivo de entrada: {e}")
            sys.exit()

    def shooting_method(self):
        try:
            with open("output_boundary.txt", "w") as file:
                for idx, (func, y0, interval, target, h, n, parameters) in enumerate(
                    zip(self.functions, self.initial_values, self.intervals, self.target_values, self.steps, self.points, self.parameters_list)
                ):
                    x, y = symbols("x y")
                    x_values = [interval[0] + i * h for i in range(n + 1)]

                    y_values = [y0]
                    z_values = [0]  # Chute inicial para derivada

                    # Substituir parâmetros pelo dicionário
                    func = func.subs(parameters)

                    # Primeiro chute para o valor de z
                    for i in range(1, len(x_values)):
                        y_values.append(y_values[i - 1] + h * z_values[i - 1])
                        z_values.append(z_values[i - 1] + h * func.subs({x: x_values[i - 1], y: y_values[i - 1]}).evalf())

                    y_end_first = y_values[-1]

                    # Segundo chute para o valor de z
                    z_values = [1]  # Segundo chute
                    y_values = [y0]

                    for i in range(1, len(x_values)):
                        y_values.append(y_values[i - 1] + h * z_values[i - 1])
                        z_values.append(z_values[i - 1] + h * func.subs({x: x_values[i - 1], y: y_values[i - 1]}).evalf())

                    y_end_second = y_values[-1]

                    # Ajustando o valor de z
                    z_correct = 0 + (target - y_end_first) * (1 - 0) / (y_end_second - y_end_first)

                    # Usando o z correto para encontrar a solução final
                    z_values = [z_correct]
                    y_values = [y0]

                    for i in range(1, len(x_values)):
                        y_values.append(y_values[i - 1] + h * z_values[i - 1])
                        z_values.append(z_values[i - 1] + h * func.subs({x: x_values[i - 1], y: y_values[i - 1]}).evalf())

                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in zip(x_values, y_values):
                        file.write(f"x = {x_val:.6f}, y = {y_val:.6f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método do Shooting.\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

    def finite_differences(self):
        try:
            with open("output_boundary.txt", "w") as file:
                for idx, (func, y0, interval, target, h, n, parameters) in enumerate(
                    zip(self.functions, self.initial_values, self.intervals, self.target_values, self.steps, self.points, self.parameters_list)
                ):
                    x, y = symbols("x y")
                    
                    # Substituir parâmetros adicionais antes de iniciar
                    func = func.subs(parameters)
                    
                    # Divisão do intervalo
                    x_values = np.linspace(interval[0], interval[1], n + 1)
                    y_values = np.zeros(n + 1)  # Inicializa o vetor de soluções
                    y_values[0] = y0  # Condição de contorno no início
                    y_values[-1] = target  # Condição de contorno no final

                    # Função f(x) avaliada nos pontos
                    func_vals = [func.subs(x, float(xi)).subs(y, float(y_values[i])).evalf() for i, xi in enumerate(x_values)]

                    # Montando o sistema linear
                    A = np.zeros((n - 1, n - 1))
                    b = np.zeros(n - 1)

                    for i in range(1, n):  # Preenchendo o sistema linear
                        A[i - 1, i - 1] = -2 / h**2
                        if i > 1:
                            A[i - 1, i - 2] = 1 / h**2
                        if i < n - 1:
                            A[i - 1, i] = 1 / h**2
                        b[i - 1] = -func_vals[i]

                    # Usando a Eliminação de Gauss para resolver o sistema
                    x_solution = self.gaussian_elimination(A, b)

                    # Preenchendo os valores de y usando a solução de x
                    y_values[1:-1] = x_solution

                    # Salvando os resultados no arquivo
                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in zip(x_values, y_values):
                        file.write(f"x = {x_val:.6f}, y = {y_val:.6f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método das Diferenças Finitas.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

    def gaussian_elimination(self, A, b):
        n = len(b)
        A = A.astype(float)  # Garante que a matriz A seja do tipo float
        b = b.astype(float)  # Garante que o vetor b seja do tipo float

        # Eliminação para triangularizar a matriz A
        for i in range(n):
            # Garantir que o elemento diagonal seja diferente de zero
            if A[i][i] == 0:
                raise ValueError(f"A matriz A possui um elemento diagonal nulo na posição ({i},{i})")
            
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                A[j] -= factor * A[i]
                b[j] -= factor * b[i]

        # Substituição para obter a solução
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

        x[np.abs(x) < 1e-10] = 0.0  # Considera valores muito pequenos como zero
        return x