import root_finding

print("Qual método você deseja testar?"
      "\n1. Bissecção\n2. Posição falsa\n3. Newton-Raphson\n4. Secante")
method = int(input())

r = root_finding.Roots()
if(method == 1):
    r.bisection()
elif(method == 2):
    r.false_position()
elif(method == 3):
    r.newton_raphson()
elif(method == 4):
    r.secant()
else:
    print("Método ainda não implementado ou inexistente")