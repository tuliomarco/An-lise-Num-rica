import root_finding

print("Qual método você deseja testar?\n1. Bissecção")
method = int(input())

r = root_finding.Roots()
if(method == 1):
    r.bisection()
else:
    print("Método ainda não implementado ou inexistente")