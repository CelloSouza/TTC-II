from math import pi
from math import sqrt
from scipy import integrate

def calcularPressao(numeroQuarks, numeroLeptons, kfQuarks, kfLeptons, massaQuarks, massaLeptons, sacola):
    resultado = 0
    pressaoAuxiliarQ = 0
    pressaoAuxiliarL = 0
    for i in range(0 , numeroQuarks):
        resultado = integrate.quadrature(lambda k : (k**4)/(((k**2)+(massaQuarks[i]**2))**(1/2)) , 0,kfQuarks[i])
        pressaoAuxiliarQ += resultado[0]
    for j in range(0 , numeroLeptons):
        resultado = integrate.quadrature(lambda k : (k**4)/(((k**2)+(massaLeptons[j]**2))**(1/2)) , 0,kfLeptons[j])
        pressaoAuxiliarL += resultado[0]
    return (1/(pi**2))*pressaoAuxiliarQ + (1/(3*pi**2))*pressaoAuxiliarL-sacola