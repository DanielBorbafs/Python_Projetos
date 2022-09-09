from tkinter import *
 # Importar as cores

cor1 = '#2F4F4F' # Bg
cor2 = '#B0C4DE' # Frames
cor3 = '#20B2AA' # Botoes
cor4 = '#F8F8FF' # Branco
cor5 = '#00000' # Preto

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg= cor1)
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width= 400, height=300)

Application()
