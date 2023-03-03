import tkinter 

class App():
    #Cria o um método construtor da minha Classe App.
    def __init__(self, title, x , y):       
          window = tkinter.Tk()
          window.title("First App")
          window.minsize(width = x , height = y)
    # Fica executando a janela para que ela não feche.
          window.mainloop()
# Inicializando um novo objeto
janela = App("Janela",1280,920)