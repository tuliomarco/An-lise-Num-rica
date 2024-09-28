import sys
from math import *
from sympy import *

def function(x, f):
    return eval(f)

class Roots:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                inputs = file.read().split(";")
            
            self.len_inputs = len(inputs)
            self.a = float(inputs[0])
            self.b = float(inputs[1]) if self.len_inputs == 4 else None
            self.t = eval(inputs[2 if self.len_inputs == 4 else 1])
            
            inputs = inputs[-1].split("\n")
            self.func = inputs[0].strip()
            
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            sys.exit()
    
    def derivative(self, a):
        x = Symbol("x")
        symbolic_func = eval(self.func)
        symbolic_derivative = symbolic_func.diff(x)
        return symbolic_derivative.subs(x, a)


    def bisection(self):
        k = 0
        a = self.a
        b = self.b
        tol = self.t

        if self.len_inputs < 4: 
            print("\nFormato esperado: <a>;<b>;<tol>;<function>\n")
            return
        elif function(a, self.func) * function(b, self.func) > 0:
            print("O intervalo não contém raiz")
            return

        with open("roots_output.txt", "w") as file:
            file.write(" k |     a     |     b     |   f(a)    |    f(b)   |    b-a    |  (b-a)/a  |     c     |   f(c)    \n")
            
            while True:
                c = (a + b) / 2
                erro_relativo = abs(b - a) / (abs(a) if a != 0 else 1)

                k += 1
                file.write(f"{k:2} | {a:9.5f} | {b:9.5f} | {function(a, self.func):9.5f} | {function(b, self.func):9.5f} | {b-a:9.5f} | {erro_relativo:9.5f} | {c:9.5f} | {function(c, self.func):9.5f}\n")

                if abs(function(c, self.func)) < tol or abs(b-a) < tol:
                    file.write(f"\nResultado {c:.5f} obtido pelo método da bissecção.")
                    return

                if function(a, self.func) * function(c, self.func) < 0:
                    b = c
                else:
                    a = c

    
    def false_position(self):
            k = 0
            a = self.a
            b = self.b
            tol = self.t

            if(self.len_inputs < 4): 
                print("\nFormato esperado: <a>;<b>;<tol>;<function>\n")
                return
            if function(a, self.func) * function(b, self.func) > 0:
                print("O intervalo não contém raiz")
                return

            with open("roots_output.txt", "w") as file:
                file.write(" k |     a     |     b     |    f(a)   |    f(b)   |    b-a    |     c     |   f(c)\n")

                while True:
                    c = (a * function(b, self.func) - b * function(a, self.func)) / (function(b, self.func) - function(a, self.func))
                    relative_error = abs(b - a) / max(abs(c), 1e-10)

                    k += 1
                    file.write(f"{k:2} | {a:9.5f} | {b:9.5f} | {function(a, self.func):9.5f} | {function(b, self.func):9.5f} | {b-a:9.5f} | {c:9.5f} | {function(c, self.func):9.5f}\n")

                    if abs(function(c, self.func)) < tol or relative_error < tol:
                        file.write(f"\nResultado {c:.5f} obtido pelo método da posição falsa.")
                        return

                    if function(a, self.func) * function(c, self.func) < 0:
                        b = c
                    else:
                        a = c

    def newton_raphson(self):
        i = 0
        a = self.a
        tol = self.t

        if(self.len_inputs < 3): 
            print("\nFormato esperado: <a>;<tol>;<function>\n")
            return
                
        with open("roots_output.txt", "w") as file:
            file.write(" k |    a    |   f(a)   |  f'(a)  |  Erro relativo \n")
            
            while True:
                i += 1
                fa = function(a, self.func)
                f_deriv = self.derivative(a)
                
                if f_deriv == 0 or f_deriv < 10**-10:
                    print("A derivada é zero! O método de Newton-Raphson falhou.")
                    file.write(f"{i:2} | {a:7.5f} | {fa:8.5f} | {f_deriv:7.5f} |  Derivada zero, método falhou\n")
                    return
                
                delta = fa / f_deriv
                a -= delta
                relative_error = abs(delta) / max(abs(a), 1e-10)

                file.write(f"{i:2} | {a:7.5f} | {fa:8.5f} | {f_deriv:7.5f} | {relative_error:8.5f}\n")

                if abs(fa) < tol or relative_error < tol:
                    file.write(f"\nResultado {a:.5f} obtido pelo método de Newton-Raphson.")
                    return
    
    def secant(self):
        k = 0
        a = self.a
        b = self.b
        tol = self.t

        if(self.len_inputs < 4): 
            print("\nFormato esperado: <a>;<b>;<tol>;<function>\n")
            return
        
        with open("roots_output.txt", "w") as file:
            file.write(" k |    a    |    b    |    x    |   f(a)   |   f(b)   |   f(x)   |  Erro Relativo \n")

            while True:
                f_a = function(a, self.func)
                f_b = function(b, self.func)
                c = b - f_b * (a - b) / (f_a - f_b)
                f_c = function(c, self.func)

                relative_error = abs((c - b) / max(abs(c), 1e-10))

                k += 1
                file.write(f"{k:2} | {a:7.5f} | {b:7.5f} | {c:7.5f} | {f_a:8.5f} | {f_b:8.5f} | {f_c:8.5f} | {relative_error:8.5f}\n")

                if abs(f_c) < tol or relative_error < tol:
                    file.write(f"\nResultado {c:.5f} obtido pelo método da secante.")
                    return

                a, b = b, c