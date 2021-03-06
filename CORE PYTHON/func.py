from math import pi
from math import sqrt
from scipy import integrate


nQuarks = 2 
sacola = 200 
massa = [2.2,4.7,95,1275,4180,173000,0.511, 105.7, 1777]
def calcularPressao(nQuarks, sacola, massa):
    resultado = 0
    pAuxiliar = 0
    p = []
    for kf in range(1,1001):
        for i in range(0,nQuarks):
            resultado = integrate.quadrature(lambda k : (k**4)/(((k**2)+(massa[i]**2))**(1/2)) , 0,kf)
            pAuxiliar += resultado[0]
        p.append((1/(pi**2))*pAuxiliar-sacola)
        resultado = 0
        pAuxiliar = 0
    return p 

def calcularUnicaPressao(kf, massa, sacola):
    resultado = integrate.quadrature(lambda k : (k**4)/(((k**2)+(massa**2))**(1/2)) , 0,kf)
    return (1/(pi**2))*resultado[0]-sacola

print(calcularUnicaPressao(4.48998886413, 2.2, sacola))




def calcularDensidadeEnergia(nQuarks, sacola, massa):
    resultado = 0
    eAuxiliar = 0
    e = []
    for kf in range(1,1001):
        for i in range(0,nQuarks):
            resultado = integrate.quadrature(lambda k : (k**2)*(((k**2) + (massa[i]**2))**(1/2)), 0,kf)
            eAuxiliar += resultado[0]
        e.append((6/((2*pi)**2))*eAuxiliar+sacola)
        resultado = 0
        eAuxiliar = 0
    return e


def calcularDensidadeBaronica(nQuarks, sacola, massa):
    resultado = 0
    nAuxiliar = 0
    n = []
    for kf in range(1,1001):
        for i in range(0,nQuarks):
            resultado = integrate.quadrature(lambda k : (k**2), 0,kf)
            nAuxiliar += resultado[0]
        n.append(((1/(pi**2))*nAuxiliar+sacola))
        resultado = 0
        nAuxiliar = 0
    return n

# print(calcularDensidadeBaronica(nQuarks, sacola, massa))