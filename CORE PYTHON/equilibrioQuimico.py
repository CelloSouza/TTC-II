from numpy import array
from scipy import optimize

def calculaEquilibrioQuimico(x):
    mu, md, ms, mc, mb, mt,me, mmu, mz = x[:9]
    f0 = mu - mu
    f1 = md - md
    f2 = md - mu - me
    f3 = ms - md
    f4 = mc - mu
    f5 = mb - md
    f6 = mt - md - me
    f7 = mmu - me
    f8 = mz - me
    return f0,f1,f2,f3,f4,f5,f6,f7,f8


def calcularMu(valorU):
    Mu = []
    result = optimize.root(calculaEquilibrioQuimico, [valorU,2000,0,0,0,0,0,0,0], method='broyden1')
    for item in result.x:
        Mu.append(item)
    return Mu

