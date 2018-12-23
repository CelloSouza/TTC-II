from math import pi
from math import sqrt
from scipy import integrate

def calcularDensidadeEnergia(numeroQuarks, numeroLeptons, kfQuarks, kfLeptons, massaQuarks, massaLeptons, sacola):
    resultado = 0
    densidadeAuxiliarQ = 0
    densidadeAuxiliarL = 0
    for i in range(0 , numeroQuarks):
        resultado = integrate.quadrature(lambda k : (k**2)*(((k**2) + (massaQuarks[i]**2))**(1/2)), 0,kfQuarks[i])
        densidadeAuxiliarQ += resultado[0]
    for j in range(0 , numeroLeptons):
        resultado = integrate.quadrature(lambda k : (k**2)*(((k**2) + (massaLeptons[j]**2))**(1/2)), 0,kfLeptons[j])
        densidadeAuxiliarL += resultado[0]
    return ((3/(pi**2))*densidadeAuxiliarQ+(1/(pi**2))*densidadeAuxiliarL+(sacola**4))/197**4
