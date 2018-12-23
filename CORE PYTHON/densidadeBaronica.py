from math import pi
from math import sqrt
from scipy import integrate

def calcularDensidadeBaronica(numeroQuarks, kfQuarks):
    resultado = 0
    densidadeAuxiliarQ = 0
    for i in range(0 , numeroQuarks):
        resultado = integrate.quadrature(lambda k : (k**2), 0,kfQuarks[i])
        densidadeAuxiliarQ += resultado[0]
    return ((1/(pi**2))*densidadeAuxiliarQ)


def calcularDensidade(kf):
    resultado = integrate.quadrature(lambda k : (k**2), 0, abs(kf))
    return ((1/(pi**2))*resultado[0])

def calcularDensidadeLeptons(kf):
    resultado = integrate.quadrature(lambda k : (k**2), 0, abs(kf))
    return ((1/(3*pi**2))*resultado[0])