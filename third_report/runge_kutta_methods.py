import sys
from sympy import symbols


class RungeKuttaMethods:
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

    def runge_kutta_3(self):
        x, y = symbols('x y')
        try:
            with open("output_rk.txt", "w") as file:
                for idx in range(len(self.functions)):
                    valor_x = self.intervals[idx][0]
                    valor_y = self.initial_values[idx]
                    results = []

                    while valor_x <= self.intervals[idx][1]:
                        k1 = self.functions[idx].subs({x: valor_x, y: valor_y})
                        k2 = self.functions[idx].subs({x: valor_x + (1/2) * self.steps[idx], y: valor_y + (1/2) * self.steps[idx] * k1})
                        k3 = self.functions[idx].subs({x: valor_x + self.steps[idx], y: valor_y - self.steps[idx] * k1 + 2 * self.steps[idx] * k2})
                        
                        valor_y += (self.steps[idx] / 6) * (k1 + 4 * k2 + k3)
                        valor_y = round(valor_y, 5)
                        results.append([round(valor_x, 5), round(valor_y, 5)])

                        valor_x = round(valor_x + self.steps[idx], 5)

                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in results:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método de Runge-Kutta de 3ª Ordem.\n")

        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()

    @staticmethod
    def runge_kutta_4_aux(func, interval, h, initial_value):
        x, y = symbols('x y')
        try:
            valor_x = interval[0]
            valor_y = initial_value
            results = []

            while valor_x <= interval[1]:
                k1 = func.subs({x: valor_x, y: valor_y}).evalf()
                k2 = func.subs({x: valor_x + (1/2) * h, y: valor_y + (1/2) * h * k1}).evalf()
                k3 = func.subs({x: valor_x + (1/2) * h, y: valor_y + (1/2) * h * k2}).evalf()
                k4 = func.subs({x: valor_x + h, y: valor_y + h * k3}).evalf()

                valor_y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

                results.append([round(valor_x, 5), round(valor_y, 5)])

                valor_x = round(valor_x + h, 5)

            return results

        except Exception as e:
            print(f"Erro no cálculo do Método de Runge-Kutta 4ª ordem auxiliar: {e}")
            sys.exit()


    def runge_kutta_4(self):
        try:
            with open("output_rk.txt", "w") as file:
                for idx in range(len(self.functions)):
                    func = self.functions[idx]
                    interval = self.intervals[idx]
                    h = self.steps[idx]
                    initial = self.initial_values[idx]

                    results = self.runge_kutta_4_aux(func, interval, h, initial)


                    file.write(f"Problema {idx + 1}:\n")
                    for x_val, y_val in results:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("Resultados obtidos pelo Método de Runge-Kutta de 4ª Ordem.\n")
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
