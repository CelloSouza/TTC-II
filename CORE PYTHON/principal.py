from math import pi
from math import sqrt
from scipy import integrate
from equilibrioQuimico import calcularMu
from momentoDeFermie import calcularTodosMomentosDeFermi
from pressao import calcularPressao
from densidadeEnergia import calcularDensidadeEnergia
from densidadeBaronica import calcularDensidadeBaronica

massa = [2.2,4.7,95,1275,4180,173000, 0.511, 105.7, 1777]
massaQuarks = [2.2,4.7,95,1275,4180,173000]
massaLeptons = [0.511, 105.7, 1777]
numeroQuarks = 5
numeroLeptons = 3
sacola = 200

def calcularPressaoVariandoMu():
    resultado = []
    for i in range(10,100, 10):
        Mu = calcularMu(i)
        kfQuarks, kfLeptons = calcularTodosMomentosDeFermi(Mu, massa)
        resultado.append(calcularPressao(numeroQuarks, numeroLeptons, kfQuarks, kfLeptons, massaQuarks, massaLeptons, sacola))
    return resultado

def calcularDensidadeEnergiaVariandoMu():
    resultado = []
    for i in range(10,100, 10):
        Mu = calcularMu(i)
        kfQuarks, kfLeptons = calcularTodosMomentosDeFermi(Mu, massa)
        resultado.append(calcularDensidadeEnergia(numeroQuarks, numeroLeptons, kfQuarks, kfLeptons, massaQuarks, massaLeptons, sacola))
    return resultado

def calcularDensidadeBaronicaVariandoMu():
    resultado = []
    for i in range(10,100, 10):
        Mu = calcularMu(i)
        kfQuarks, kfLeptons = calcularTodosMomentosDeFermi(Mu, massa)
        resultado.append(calcularDensidadeBaronica(numeroQuarks, kfQuarks))
    return resultado

resultadoPressao = calcularPressaoVariandoMu()
resultadoDensidadeEnergia = calcularDensidadeEnergiaVariandoMu()
resultadoDensidadeBaronica = calcularDensidadeBaronicaVariandoMu()
print(resultadoDensidadeBaronica)