from math import pi
from numpy import array
from scipy import optimize
from math import sqrt
from momentoDeFermie import calcularMomentosDeFermiEmUmArray
from densidadeBaronica import calcularDensidade
from densidadeBaronica import calcularDensidadeLeptons

def calculaEquilibrioQuimico(kf):
    massa = [2.2,4.7,95,1275,4180,173000, 0.511, 105.7, 1777]
    carga = [0.666666667, -0.333333333, -0.333333333, 0.666666667, -0.333333333, 0.666666667, -1.0, -1.0, -1.0]
    f0 = sqrt((kf[0]**2)+(massa[0]**2)) - sqrt((kf[0]**2)+(massa[0]**2))
    f1 = sqrt((kf[1]**2)+(massa[1]**2)) - sqrt((kf[0]**2)+(massa[0]**2)) - sqrt((kf[6]**2)+(massa[6]**2))
    f2 = kf[2]#sqrt((kf[2]**2)+(massa[2]**2)) - sqrt((kf[1]**2)+(massa[1]**2))
    f3 = kf[3] #sqrt((kf[3]**2)+(massa[3]**2)) - sqrt((kf[0]**2)+(massa[0]**2))
    f4 = kf[4] #sqrt((kf[4]**2)+(massa[4]**2)) - sqrt((kf[1]**2)+(massa[1]**2))
    f5 = kf[5] #sqrt((kf[5]**2)+(massa[5]**2)) - sqrt((kf[1]**2)+(massa[1]**2)) - sqrt((kf[6]**2)+(massa[6]**2))
    f6 = sqrt((kf[6]**2)+(massa[6]**2)) - sqrt((kf[7]**2)+(massa[7]**2))
    f7 = (1/(pi**2))*(kf[0]**3*carga[0]+kf[1]**3*carga[1]+kf[2]**3*carga[2]+kf[3]**3*carga[3]+kf[4]**3*carga[4]+kf[5]**3*carga[5])+((1/3*pi**2))*(kf[6]**3*carga[6]+kf[7]**3*carga[7]+kf[8]**3*carga[8]) #
    f8 = kf[8] #sqrt((kf[8]**2)+(massa[8]**2)) - sqrt((kf[6]**2)+(massa[6]**2))
    return f0,f1,f2,f3,f4,f5,f6,f7,f8


def calcularKf(valorU):
    kf = []
    result = optimize.root(calculaEquilibrioQuimico, [valorU,valorU,0,0,0,0,valorU/5,valorU/10,0], method='anderson')
    for item in result.x:
        kf.append(abs(item))
    return kf
# kf = []
# for i in range(20, 500, 22):
#     result = calcularKf(i)
#     kf.append({"Resultado "+str(i): result})
#     result = 0

# print(kf)