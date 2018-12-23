from math import pi
from math import sqrt
from scipy import integrate
from equilibrioQuimico import calcularKf
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
from configuracao import sacola
from configuracao import valorInicial
from configuracao import valorFinal
from configuracao import pulo


interp = interp1d(resultadoPressao, resultadoDensidadeEnergia, kind='cubic')


# def funex(x):
#     print(interp(x))

# funex(17.440813814786996)

def func(t, y):
    r = t
    p = y[0]
    m = y[1]   
    e = interp(p)
    ms = 5660.57
    gms = 1.47556
    # G = (1.326849021*10**(11))
    # dy0 = -G*(p+p)*(m+4*pi*(r**3)*p)/(r*(r-2*m))
    # dy1 = (4*pi)*p*(r**2)
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
            # print("P: ",p, " T:", rungeKutta.t, " M: ", rungeKutta.y, " Step Size: ", rungeKutta.step_size)
            R.append(rungeKutta.t_old)
            M.append(rungeKutta.y_old[1])
            T.append({"Pressão": p, "Raio": rungeKutta.t_old, "Massa": rungeKutta.y_old[1]})
            if rungeKutta.y_old[1] > maiorMassa:
                maiorMassa = rungeKutta.y_old[1]
            break
    # print("p: " , p, " T: ", rungeKutta.t, rungeKutta.y)    
    # R.append(rungeKutta.t)
    # M.append(rungeKutta.y[1])
    
# # rungeKutta = BDF(func, 1, [pressao[0],0], 999999999)
# # # print(dir(rungeKutta))
# # for i in range(0,1):
# #     if rungeKutta.y[0] <= 0.001:  
# #         print("T: ", rungeKutta.t)
# #         print("Y: ", rungeKutta.y)
# #         break 
# #     rungeKutta.step()
    
    
    


# print("RAIO: ",R)
# print("MASSA: ", M)
print(T)
print("Maior Massa: ", maiorMassa)
fig, ax = plt.subplots()

ax.plot(R, M)
# ax.set_xlim([5,15])
# ax.set_ylim([0.5,2.5])

fig.savefig("rungeKutta"+str(sacola)+"semLimite.png")
plt.show()