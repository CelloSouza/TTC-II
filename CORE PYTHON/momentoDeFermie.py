from equilibrioQuimico import Mu
from math import sqrt

def calcularMomentoDeFermi(M, massa):
    resultado = (M**2) - (massa**2)
    if resultado < 0:
        return 0
    else:
        return sqrt(resultado)

def calcularTodosMomentosDeFermi(M, massa):
    
print(calcularMomentoDeFermi(Mu[0], 2))