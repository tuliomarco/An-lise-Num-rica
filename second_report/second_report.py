import regression_approximation, interpolation, numerical_derivation, numerical_integration

print("Qual método você deseja testar?"
      "\n1. Regressão Linear"
      "\n2. Aproximação Polinomial - Caso Discreto"
      "\n3. Aproximação Polinomial - Caso Contínuo"
      "\n4. Interpolação Polinomial - Polinômios de Lagrange"
      "\n5. Interpolação Polinomial - Diferenças Divididas de Newton"
      "\n6. Derivação Numérica - 1ª Ordem (Diferenças Finitas)"
      "\n7. Derivação Numérica - 2ª Ordem (Diferenças Finitas)"
      "\n8. Integração Numérica - Trapézios Simples"
      "\n9. Integração Numérica - Trapézios Múltiplos"
      "\n10. Integração Numérica - Regra de Simpson 1/3 Simples"
      "\n11. Integração Numérica - Regra de Simpson 1/3 Múltiplos"
      "\n12. Integração Numérica - Regra de Simpson 3/8 Simples"
      "\n13. Integração Numérica - Regra de Simpson 3/8 Múltiplos"
      "\n14. Integração Numérica - Extrapolação de Richards"
      "\n15. Integração Numérica - Quadratura de Gauss")
method = int(input())

if method in {1, 2, 3}:
    reg = regression_approximation.RegressionApproximation(method)
elif method in {4, 5}:
    interp = interpolation.Interpolation()
elif method in {6, 7}:
    deriv = numerical_derivation.NumericalDerivation()
else:
    integ = numerical_integration.NumericalIntegration()

if method == 1:
    reg.linear_regression()
elif method == 2:
    reg.discrete_polynomial_approximation()
elif method == 3:
    reg.continuous_polynomial_approximation()
elif method == 4:
    interp.lagrange_polynomial()
elif method == 5:
    interp.newton_divided_differences()
elif method == 6:
    deriv.first_order_finite_difference()
elif method == 7:
    deriv.second_order_finite_difference()
elif method == 8:
    integ.simple_trapezoidal()
elif method == 9:
    integ.multiple_trapezoidal()
elif method == 10:
    integ.simple_simpson_1_3()
elif method == 11:
    integ.multiple_simpson_1_3()
elif method == 12:
    integ.simple_simpson_3_8()
elif method == 13:
    integ.multiple_simpson_3_8()
elif method == 14:
    integ.richards_extrapolation()
elif method == 15:
    integ.gaussian_quadrature()
else:
    print("Método ainda não implementado ou inexistente")
