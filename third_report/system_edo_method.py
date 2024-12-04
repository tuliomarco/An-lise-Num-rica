from runge_kutta_methods import RungeKuttaMethods
import sys
from sympy import symbols

class SystemEdoMethods:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                self.functions = []
                self.initial_values = []
                self.intervals = []
                self.steps = []

                x, y, z = symbols("x y z")

                for line in file:
                    if line.strip():
                        aux = line.strip().split(";")
                        

                        func_str = aux[0].strip()
                        func = eval(func_str)  
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


    def solve_system(self):
        try:
            results = []
            for func, interval, initial_value, step in zip(self.functions, self.intervals, self.initial_values, self.steps):
                results.append(RungeKuttaMethods.runge_kutta_4_aux(func, interval, step, initial_value))

            with open("output_system.txt", "w") as file:
                for idx, result in enumerate(results):
                    file.write(f"Solução do sistema {idx + 1}:\n")
                    for x_val, y_val in result:
                        file.write(f"x = {x_val:.5f}, y = {y_val:.5f}\n")
                    file.write("\n")
                file.write("\nResultado do sistema de EDO.\n")
        except Exception as e:
            print(f"Erro ao resolver o sistema: {e}")
            sys.exit()

