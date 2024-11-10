import sys
from sympy import *
import math

def function(x_value, f):
    return eval(f, {"x": x_value, "math": math})

class NumericalDerivation:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            
            self.functions = []
            self.x_values = []

            for line in lines:
                func_str, x_str = line.strip().split(";")
                x_value = float(x_str.strip())
                self.functions.append(func_str)
                self.x_values.append(x_value)

        except Exception as e:
            print(f"Erro ao ler o arquivo de entrada: {e}")
            sys.exit()

    def first_order_finite_difference(self):
        try:
            h = 1
            with open("output_derivation.txt", "w") as file:
                for i, func_str in enumerate(self.functions):
                    x_value = self.x_values[i]
                    func_plus_h = function(x_value + h, func_str)
                    func_minus_h = function(x_value - h, func_str)
                    
                    d = (func_plus_h - func_minus_h) / (2 * h)
                    
                    file.write(f"Derivada da função {i+1}: {d}\n")
                file.write("\nResultado obtido através da derivação numérica de primeira ordem\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
    
    def second_order_finite_difference(self):
        try:
            h = 0.1
            with open("output_derivation.txt", "w") as file:
                for i, func_str in enumerate(self.functions):
                    x_value = self.x_values[i]
                    func_plus_h = function(x_value + h, func_str)
                    func_minus_h = function(x_value - h, func_str)
                    func_at_x = function(x_value, func_str)
                    
                    d = (func_plus_h - 2 * func_at_x + func_minus_h) / (h ** 2)
                    
                    file.write(f"Derivada da função {i+1}: {d}\n")
                file.write("\nResultado obtido através da derivação numérica de segunda ordem\n")
        
        except Exception as e:
            print(f"Erro ao escrever no arquivo de saída: {e}")
            sys.exit()
