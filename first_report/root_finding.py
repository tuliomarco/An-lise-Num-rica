import sys

class Roots:
    def __init__(self):
        try:
            file_name = input("Digite o nome do arquivo de entrada: ")
            with open(file_name, "r") as file:
                inputs = file.read().split(";")
            
            self.a = float(inputs[0])
            self.b = float(inputs[1])
            self.t = eval(inputs[2])
            
            inputs = inputs[-1].split("\n")
            self.func = inputs[0]

            if self.funcao(self.a) * self.funcao(self.b) > 0:
                print("O intervalo não contém raiz")
                return
            
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            sys.exit()

    def funcao(self, x):
        return eval(self.func)

    def bisection(self):
        k = 0
        a = self.a
        b = self.b
        t = self.t

        with open("roots_output.txt", "w") as arq:
            arq.write(" k |    a    |    b    |   f(a)   |   f(b)  |   b-a   | (b-a)/x\n")
            
            while True:
                x = (a + b) / 2
                aproximacao = (b - a) / 2
                erro_relativo = (b - a) / max(abs(x), 1e-10)

                k += 1
                arq.write(f"{k:2} | {a:.5f} | {b:.5f} | {self.funcao(a):.5f} | {self.funcao(b):.5f} | {b-a:.5f} | {erro_relativo:.5f}\n")

                if abs(self.funcao(x)) < t or aproximacao < t:
                    print(f"Raiz encontrada: {x:.5f} após {k} iterações.")
                    return

                if self.funcao(a) * self.funcao(x) < 0:
                    b = x
                else:
                    a = x
    
    def false_position(self):
            k = 0
            a = self.a
            b = self.b
            tol = self.t

            with open("roots_output_fp.txt", "w") as arq:
                arq.write(" k |    a    |    b    |   f(a)   |   f(b)  |   b-a   |    c    |   f(c)\n")

                while True:
                    c = (a * self.funcao(b) - b * self.funcao(a)) / (self.funcao(b) - self.funcao(a))
                    e = abs(b - a) / max(abs(c), 1e-10)

                    k += 1
                    arq.write(f"{k:2} | {a:.5f} | {b:.5f} | {self.funcao(a):.5f} | {self.funcao(b):.5f} | {b-a:.5f} | {c:.5f} | {self.funcao(c):.5f}\n")

                    if abs(self.funcao(c)) < tol or e < tol:
                        print(f"Raiz encontrada: {c:.5f} após {k} iterações.")
                        return

                    if self.funcao(a) * self.funcao(c) < 0:
                        b = c
                    else:
                        a = c
