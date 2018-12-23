import ast
import matplotlib.pyplot as plt

tov = []

plt.errorbar(13.8, 2.1, xerr=1.8, yerr=0.28, fmt='+')
plt.annotate('EXO 0748-67' , xycoords='data', xy=(13.8, 2.1), textcoords='offset points',)
plt.xlabel('Raio (KM)')
plt.ylabel('Massa')
plt.title('Raio x Massa - Sacola')

arquivo = open('resultado-TOV120.txt','r')
tovString = arquivo.readlines()

for index in tovString:
    aux = index.split("\n")[0]
    aux = ast.literal_eval(aux)
    tov.append(aux)
    
massas1 = []
raios1 = []
for index in tov:
    massas1.append(index.get("Massa"))
    raios1.append(index.get("Raio"))


arquivo = open('resultado-TOV128.txt','r')
tovString1 = arquivo.readlines()

for index in tovString1:
    aux = index.split("\n")[0]
    aux = ast.literal_eval(aux)
    tov.append(aux)
    
massas2 = []
raios2 = []
for index in tov:
    massas2.append(index.get("Massa"))
    raios2.append(index.get("Raio"))

plt.plot(raios1, massas1, 'r')
plt.savefig("resultados1", transparent = True)
plt.show()
plt.plot(raios2, massas2, 'b')
plt.savefig("resultados2", transparent = True)
plt.show()