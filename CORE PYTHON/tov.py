import matplotlib.pyplot as plt
from math import pi
from scipy.integrate import RK45
from scipy.interpolate import interp1d
# from configuracao import sacola
from configuracao import nomeEstrela
from EOS import EOS

def chamarTOV(sacola):
    EOS(sacola)
    arquivo = open('resultado-energia-sem-negativos'+str(sacola)+'.txt','r')
    energiaString = arquivo.readlines()

    energia = []
    for index in energiaString:
        aux = index.split("\n")[0]
        energia.append(float(aux))

    arquivo = open('resultado-energia-com-negativos'+str(sacola)+'.txt','r')
    energiaComNegativoString = arquivo.readlines()
    energiaComNegativo = []

    for index in energiaComNegativoString:
        aux = index.split("\n")[0]
        energiaComNegativo.append(float(aux))

    arquivo = open('resultado-pressao-sem-negativos'+str(sacola)+'.txt','r')
    pressaoString = arquivo.readlines()

    pressao = []
    for index in pressaoString:
        aux = index.split("\n")[0]
        pressao.append(float(aux))

    arquivo = open('resultado-pressao-com-negativos'+str(sacola)+'.txt','r')
    pressaoComNegativoString = arquivo.readlines()
    pressaoComNegativo = []

    for index in pressaoComNegativoString:
        aux = index.split("\n")[0]
        pressaoComNegativo.append(float(aux))


    interp = interp1d(pressaoComNegativo, energiaComNegativo, kind='cubic')

    def func(t, y):
        r = t
        p = y[0]
        m = y[1]   
        e = interp(p)
        ms = 5660.57
        gms = 1.47556
        dpdr = -(e+p)*(m+4*pi*r**3*p/ms)/(r**2/gms-2*r*m)
        dmdr = 4*pi*r**2*e/ms
        return dpdr , dmdr

    R = []
    M = []
    T = []
    maiorMassa = 0
    for p in pressao:  
        rungeKutta = RK45(func, 0.0000001, [p,0], 10000000000, max_step = 0.15)
        for i in range(0,200):
            rungeKutta.step()       
            if rungeKutta.y[0] < 0.01: 
                R.append(rungeKutta.t_old)
                M.append(rungeKutta.y_old[1])
                T.append({"Pressão": p, "Raio": rungeKutta.t_old, "Massa": rungeKutta.y_old[1]})
                if rungeKutta.y_old[1] > maiorMassa:
                    raioCorrespondente = rungeKutta.t_old
                    maiorMassa = rungeKutta.y_old[1]
                break
        
    
    arquivo = open('resultado-TOV'+str(sacola)+'.txt','w')
    for index in T:
        # print(index)
        arquivo.write(str(index) + "\n")

    # print(T)
    print("Maior Massa: ", maiorMassa)
    fig, ax = plt.subplots()
    ax.plot(R, M, 'yellow')
    ax.errorbar(13.8, 2.1, xerr=1.8, yerr=0.28, fmt='+', color='black')
    ax.annotate(nomeEstrela, xycoords='data', xy=(13.8, 2.1), textcoords='offset points')
    plt.xlabel('Raio (KM)')
    plt.ylabel('Massa')
    plt.title('Raio x Massa')
    ax.set_xlim([6,16])
    ax.set_ylim([0.5,2.8])
    fig.savefig("rungeKutta"+str(sacola), transparent = True)
    plt.show()