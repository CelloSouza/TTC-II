from tkinter import *
from TOV import chamarTOV

  
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        # self.quartoContainer = Frame(master)
        # self.quartoContainer["pady"] = 2.5
        # self.quartoContainer.pack()

        # self.quintoContainer = Frame(master)
        # self.quintoContainer["pady"] = 2.5
        # self.quintoContainer.pack()

        # self.sextoContainer = Frame(master)
        # self.sextoContainer["pady"] = 2.5
        # self.sextoContainer.pack()

        # self.setimoContainer = Frame(master)
        # self.setimoContainer["pady"] = 2.5
        # self.setimoContainer.pack()

        # self.oitavoContainer = Frame(master)
        # self.oitavoContainer["pady"] = 2.5
        # self.oitavoContainer.pack()

        # self.nonoContainer = Frame(master)
        # self.nonoContainer["pady"] = 2.5
        # self.nonoContainer.pack()

        self.decimoContainer = Frame(master)
        self.decimoContainer["pady"] = 10
        self.decimoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Simulador de estrelas de quark")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Informe o valor para a sacola", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.sacola = Entry(self.terceiroContainer)
        self.sacola["width"] = 20
        self.sacola["font"] = self.fontePadrao
        self.sacola.pack(side=RIGHT)

        # self.nomeLabel = Label(self.quartoContainer,text="Massa do quark u = 2.2", font=self.fontePadrao)
        # self.nomeLabel.pack(side=LEFT)

        # self.nomeLabel = Label(self.quintoContainer,text="Massa do quark d = 4.7", font=self.fontePadrao)
        # self.nomeLabel.pack(side=LEFT)

        # self.nomeLabel = Label(self.sextoContainer,text="Massa do quark s = 95", font=self.fontePadrao)
        # self.nomeLabel.pack(side=LEFT)

        # self.nomeLabel = Label(self.setimoContainer,text="Massa do elétron = 0.511", font=self.fontePadrao)
        # self.nomeLabel.pack(side=LEFT)

        # self.nomeLabel = Label(self.oitavoContainer,text="Massa do múon = 105.7", font=self.fontePadrao)
        # self.nomeLabel.pack(side=LEFT)

        # self.nomeLabel = Label(self.nonoContainer,text="Massa do taun = 1777", font=self.fontePadrao)
        # self.nomeLabel.pack(side=LEFT)
  
        self.autenticar = Button(self.decimoContainer)
        self.autenticar["text"] = "Simular"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.simular
        self.autenticar.pack()
  
        self.mensagem = Label(self.decimoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
        

  
    #Método verificar senha
    def simular(self):
        self.mensagem["text"] = "Carregando"
        sac = self.sacola.get()
        
        chamarTOV(int(sac))
  
  
root = Tk()
Application(root)
root.mainloop()