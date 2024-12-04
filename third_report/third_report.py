import euler_methods, runge_kutta_methods, system_edo_method, boundary_methods

print("Qual método você deseja testar?"
      "\n1. Método de Euler"
      "\n2. Método de Heun"
      "\n3. Método de Euler Modificado"
      "\n4. Método de Ralston"
      "\n5. Método de Runge-Kutta de 3ª Ordem"
      "\n6. Método de Runge-Kutta de 4ª Ordem"
      "\n7. Sistemas de EDO"
      "\n8. Método do Shooting"
      "\n9. Método das Diferenças Finitas")
method = int(input())

if method in {1, 2, 3, 4}:
    euler = euler_methods.EulerMethods()
elif method in {5, 6}:
    rk = runge_kutta_methods.RungeKuttaMethods()
elif method in {8, 9}:
    boundary = boundary_methods.BoundaryMethods()

if method == 1:
    euler.euler()
elif method == 2:
    euler.heun()
elif method == 3:
    euler.modified_euler()
elif method == 4:
    euler.ralston()
elif method == 5:
    rk.runge_kutta_3()
elif method == 6:
    rk.runge_kutta_4()
elif method == 7:
    system_edo_method.SystemEdoMethods().solve_system()
elif method == 8:
    boundary.shooting_method()
elif method == 9:
    boundary.finite_differences()
else:
    print("Método ainda não implementado ou inexistente")
