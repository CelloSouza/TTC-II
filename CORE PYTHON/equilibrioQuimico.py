from numpy import array
from scipy import optimize
Mu = []
def calculaEquilibrioQuimico(x):
    mu, md = 5, 5
    ms, mc, mb, mt,me, mmu, mz = x[:7]
    M = mu, md, ms, mc, mb, mt,me, mmu, mz
    f0 = md - mu - me
    f1 = ms - md
    f2 = mc - mu
    f3 = mb - md
    f4 = mt - md - me
    f5 = mmu - me
    f6 = mz - me
    return f0,f1,f2,f3,f4,f5,f6


root = optimize.root(calculaEquilibrioQuimico, [0,0,0,0,0,0,0], method='broyden1')
Mu = [5,5]
for item in root.x:
    Mu.append(item)

