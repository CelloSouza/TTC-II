from math import pi
from math import sqrt
from scipy import integrate
from equilibrioQuimico import calcularKf
from momentoDeFermie import calcularTodosMomentosDeFermi
from pressao import calcularPressao
from densidadeEnergia import calcularDensidadeEnergia
from densidadeBaronica import calcularDensidadeBaronica
import matplotlib.pyplot as plt
from scipy.integrate import RK45
from scipy.interpolate import interp1d
from configuracao import massa
from configuracao import massaQuarks
from configuracao import massaLeptons
from configuracao import numeroQuarks
from configuracao import numeroLeptons
# from configuracao import sacola
from configuracao import valorInicial
from configuracao import valorFinal
from configuracao import pulo

def calcularPressaoVariandoMu(sacola):
    resultado = []
    for i in range(valorInicial,valorFinal, pulo):
        kf = calcularKf(i)
        kfQuarks = kf[:6]
        kfLeptons = kf[6:]
        resultado.append(calcularPressao(numeroQuarks, numeroLeptons, kfQuarks, kfLeptons, massaQuarks, massaLeptons, sacola))
    return resultado

def calcularDensidadeEnergiaVariandoMu(sacola):
    resultado = []
    for i in range(valorInicial,valorFinal, pulo):
        kf = calcularKf(i)
        kfQuarks = kf[:6]
        kfLeptons = kf[6:]
        resultado.append(calcularDensidadeEnergia(numeroQuarks, numeroLeptons, kfQuarks, kfLeptons, massaQuarks, massaLeptons, sacola))
    return resultado

def calcularDensidadeBaronicaVariandoMu(sacola):
    resultado = []
    for i in range(valorInicial,valorFinal, pulo):
        kf = calcularKf(i)
        kfQuarks = kf[:6]
        kfLeptons = kf[6:]
        resultado.append(calcularDensidadeBaronica(numeroQuarks, kfQuarks))
    return resultado

def EOS(sacola): 
    resultadoPressao = calcularPressaoVariandoMu(sacola)
    resultadoDensidadeEnergia = calcularDensidadeEnergiaVariandoMu(sacola)
    resultadoDensidadeBaronica = calcularDensidadeBaronicaVariandoMu(sacola)


    pressao = []
    energia = []

    for index in range(len(resultadoPressao)):
        if(resultadoPressao[index] > 0):
            pressao.append(resultadoPressao[index])
            energia.append(resultadoDensidadeEnergia[index])

    arquivo = open('resultado-pressao-com-negativos'+str(sacola)+'.txt','w')
    for index in resultadoPressao:
        arquivo.write(str(index) + "\n")

    arquivo = open('resultado-energia-com-negativos'+str(sacola)+'.txt','w')
    for index in resultadoDensidadeEnergia:
        arquivo.write(str(index) + "\n")

    arquivo = open('resultado-pressao-sem-negativos'+str(sacola)+'.txt','w')
    for index in pressao:
        arquivo.write(str(index) + "\n")

    arquivo = open('resultado-energia-sem-negativos'+str(sacola)+'.txt','w')
    for index in energia:
        arquivo.write(str(index) + "\n")

    # fig, ax = plt.subplots()
    # ax.set_xlim([0.95,1.5])
    # ax.set_ylim([0.050,0.2])
    # ax.plot(energia, pressao, 'yellow')
    # plt.xlabel('Energia')
    # plt.ylabel('Pressão')
    # plt.title('Equação de Estado')
    # fig.savefig("Equação de Estado"+str(sacola)+".png", transparent = True)
    # plt.show()

# EOS()