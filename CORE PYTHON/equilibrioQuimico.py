from numpy import array
from scipy import optimize
from momentoDeFermie import calcularMomentosDeFermiEmUmArray
from densidadeBaronica import calcularDensidade
from densidadeBaronica import calcularDensidadeLeptons

def calculaEquilibrioQuimico(x):
    massa = [2.2,4.7,95,1275,4180,173000, 0.511, 105.7, 1777]
    carga = [0.666666667, 0.333333333, 0.333333333, 0.666666667, 0.333333333, 0.666666667, -1.0, -1.0, -1.0]
    mu, md, ms, mc, mb, mt, me, mmu, mz = x[:9]
    f0 = mu - mu
    f1 = md - mu - me
    f2 = ms - md
    f3 = mc - mu
    f4 = mb - md
    f5 = mt - md - me
    f6 = mmu - me
    f7 = mz - me
    kf = calcularMomentosDeFermiEmUmArray(x, massa)
    f8 = (calcularDensidade(kf[0])*carga[0])+(calcularDensidade(kf[1])*carga[1])+(calcularDensidade(kf[2])*carga[2])+(calcularDensidade(kf[3])*carga[3])+(calcularDensidade(kf[4])*carga[4])+(calcularDensidade(kf[5])*carga[5])+(calcularDensidadeLeptons(kf[6])*carga[6])*(calcularDensidadeLeptons(kf[7])*carga[7])+(calcularDensidadeLeptons(kf[8])*carga[8])    
    return f0,f1,f2,f3,f4,f5,f6,f7,f8


def calcularMu(valorU):
    Mu = []
    result = optimize.root(calculaEquilibrioQuimico, [valorU,0,0,0,0,0,0,0,0], method='broyden1')
    for item in result.x:
        Mu.append(item)
    return Mu

print(calcularMu(10))