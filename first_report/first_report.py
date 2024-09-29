import root_finding, linear_systems_solutions

print("Qual método você deseja testar?"
      "\n1. Bissecção\n2. Posição falsa\n3. Newton-Raphson\n4. Secante"
      "\n5. Eliminação de Gauss\n6. Fatoração LU\n7. Jacobi\n8. Gauss-Seidel")
method = int(input())

if(method in {0, 1, 2, 3}):
    r = root_finding.Roots()
elif(method in {5, 6, 7, 8}):
    ls = linear_systems_solutions.LinearSystems()

if(method == 1):
    r.bisection()
elif(method == 2):
    r.false_position()
elif(method == 3):
    r.newton_raphson()
elif(method == 4):
    r.secant()
elif(method == 5):
    ls.gaussian_elimination()
elif(method == 6):
    ls.lu_factorization()
elif(method == 7):
    ls.jacobi()
elif(method == 8):
    ls.gauss_seidel()
else:
    print("Método ainda não implementado ou inexistente")