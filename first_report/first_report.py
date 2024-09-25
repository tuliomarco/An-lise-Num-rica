import root_finding

print("Qual método você deseja testar?\n1. Bissecção\n2.Posição falsa")
method = int(input())

r = root_finding.Roots()
if(method == 1):
    r.bisection()
elif(method == 2):
    r.false_position()
else:
    print("Método ainda não implementado ou inexistente")