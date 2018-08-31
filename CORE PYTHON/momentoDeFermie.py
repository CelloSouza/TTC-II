from math import sqrt

def calcularMomentoDeFermi(M, massa):
    resultado = (M**2) - (massa**2)
    if resultado < 0:
        return 0
    else:
        return sqrt(resultado)

def calcularTodosMomentosDeFermi(Mu, massa):
    kfQuarks = []
    kfLeptons = []
    for i in range(0,9):
        if i < 6:
             kfQuarks.append(calcularMomentoDeFermi(Mu[i], massa[i]))
        else:
           kfLeptons.append(calcularMomentoDeFermi(Mu[i], massa[i])) 
    return kfQuarks, kfLeptons
         
