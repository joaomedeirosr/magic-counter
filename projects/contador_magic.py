import tkinter

class App:
    # O self é um parâmetro que diz que uma variavel ou algo se refere aquela classe.
    def __init__(self):

        self.window = tkinter.Tk()

        self.valor = 20
        # Criando o "Esqueleto da Janela"
        self.window.title("Marcador de vida")
        self.window.minsize(width= 360 , height=640)
        self.window.maxsize(width=360,height=640)
        
        #Label é responsavél por criar o texto ou título/"rótulo" a ser exibido
        self.text = tkinter.Label(self.window, text="20", font="Calibri 80 bold",pady=50)
        #Pack serve para guardar esta variavél literalmente de dentro de um "pacote" na janela
        self.text.pack()

        #O Frame é uma caixa vazia para você adicionar seus elementos.
        self.frame = tkinter.Frame(self.window, bg="white")
        self.frame.pack()

        #Criação do botão adicionar
        self.button_botaoAdd = tkinter.Button(self.frame,text = "Adicionar", bg="orange",width = 20, command= self.botaoAdd)
        self.button_botaoAdd.pack(side="left")

        #Criação do botão Subtrair
        self.button_botaoSubtrai = tkinter.Button(self.frame,text = "Subtrair", bg="orange", width = 20 , command= self.botaoSubtrai)
        self.button_botaoSubtrai.pack(side = "left")

        self.window.mainloop()

#Criando as funções para disparar os botões (Triggers)
    def botaoAdd(self):
        if self.valor < 20:
            self.valor  +=1
            self.text.config(text = "{}".format(self.valor))

    def botaoSubtrai(self):
        if self.valor > 0:
            self.valor -=1
            self.text.config(text = "{}".format(self.valor))
App()