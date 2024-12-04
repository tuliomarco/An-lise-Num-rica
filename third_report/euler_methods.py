import sys
from sympy import symbols


class EulerMethods:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                self.functions = []
                self.initial_values = []
                self.intervals = []
                self.steps = []

                for line in file:
                    if line.strip():
                        aux = line.strip().split(";")
                        
                        # Lendo função
                        x, y = symbols("x y")
                        func = eval(aux[0].strip())
                        self.functions.append(func)
                        
                        # Lendo valor inicial de y
                        y0 = float(aux[1].strip())
                        self.initial_values.append(y0)
                        
                        # Lendo intervalo
                        interval = [float(val) for val in aux[2].strip().split(",")]
                        self.intervals.append(interval)
                        
                        # Lendo passo h
                        h = float(aux[3].strip())
                        self.steps.append(h)
        
        except Exception as e:
            print(f"Erro ao ler o arquivo de entrada: {e}")
            sys.exit()

    def euler(self):
        try:
            with open("output_euler.txt", "w") as file:
                for idx, (func, y0, interval, h) in enumerate(
                    zip(self.functions, self.initial_values, self.intervals, self.steps)
                ):
                    x, y = symbols("x y")
                    x_current, y_current = interval[0], y0
                    results = []

                    # Iterando com o método de Euler
                    while x_current < interval[1]:
                        y_next = y_current + h * func.subs({x: x_current, y: y_current}).evalf()
                        y_current = round(y_next, 5)
                        results.append((round(x_current, 5), y_current))
                        x_current = round(x_current + h, 5)

                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in results:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método de Euler.\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def heun(self):
        try:
            with open("output_euler.txt", "w") as file:
                for idx, (func, y0, interval, h) in enumerate(
                    zip(self.functions, self.initial_values, self.intervals, self.steps)
                ):
                    x, y = symbols("x y")
                    x_current, y_current = interval[0], y0
                    results_heun = []

                    # Iterando com o método de Heun
                    while x_current < interval[1]:
                        # Previsão de Euler
                        y_euler = y_current + h * func.subs({x: x_current, y: y_current}).evalf()

                        # Correção de Heun
                        y_current = y_current + (h / 2) * (
                            func.subs({x: x_current, y: y_current}).evalf() +
                            func.subs({x: x_current + h, y: y_euler}).evalf()
                        )
                        y_current = round(y_current, 5)
                        results_heun.append((round(x_current, 5), y_current))
                        x_current = round(x_current + h, 5)

                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in results_heun:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método de Heun.\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def modified_euler(self):
        try:
            with open("output_euler.txt", "w") as file:
                for idx, (func, y0, interval, h) in enumerate(
                    zip(self.functions, self.initial_values, self.intervals, self.steps)
                ):
                    x, y = symbols("x y")
                    x_current, y_current = interval[0], y0
                    results = []

                    # Iteração com o método de Euler modificado
                    while x_current < interval[1]:
                        k1 = func.subs({x: x_current, y: y_current}).evalf()
                        k2 = func.subs({x: x_current + h, y: y_current + h * k1}).evalf()
                        y_next = y_current + (h / 2) * (k1 + k2)
                        y_current = round(y_next, 5)
                        results.append((round(x_current, 5), y_current))
                        x_current = round(x_current + h, 5)

                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in results:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método de Euler Modificado.\n")
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

    def ralston(self):
        x, y = symbols('x y')
        try:
            with open("output_euler.txt", "w") as file:
                for idx in range(len(self.functions)):
                    valor_x = self.intervals[idx][0]
                    valor_y = self.initial_values[idx]
                    results = []

                    while valor_x <= self.intervals[idx][1]:
                        k1 = self.functions[idx].subs({x: valor_x, y: valor_y})
                        k2 = self.functions[idx].subs({
                            x: valor_x + (3 / 4) * self.steps[idx],
                            y: valor_y + (3 / 4) * self.steps[idx] * k1
                        })

                        valor_y += self.steps[idx] * ((1 / 3) * k1 + (2 / 3) * k2)
                        valor_y = round(valor_y, 5)
                        results.append([round(valor_x, 5), round(valor_y, 5)])

                        valor_x = round(valor_x + self.steps[idx], 5)

                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in results:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método de Ralston.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
