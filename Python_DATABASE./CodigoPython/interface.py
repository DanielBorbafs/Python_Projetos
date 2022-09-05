import tkinter
from tkinter import *
from tkinter import ttk, StringVar, ttk


# Importanto calendario



cor1 = "#1e1f1e" # preta
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"


interface = Tk()
interface.title("RH - System")
interface.geometry("800x500")
interface.config(bg=cor1)
#interface.resizable(width=FALSE, height=FALSE)

style = ttk.Style()
style.theme_use("clam")


# Cabeçalho
frame_tela = Frame(interface, width=810, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)
texto1= Label(frame_tela, text="Cadastro de Colaboradores", width =900, height=50, font='Ivy 25 bold', bg=cor3, fg=cor4, anchor=NW)
texto1.place(x=175, y=5)

# Corpo
Colaborador_matricula = Label(interface, text='Nome', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_matricula.place(x=10, y=100)
Btn_Colaborador_matricula = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_matricula.place(x=130, y=100)

Colaborador_nascimento = Label(interface, text='Nascimento', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_nascimento.place(x=10, y=150)
Btn_Colaborador_nascimento = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_nascimento.place(x=130, y=150)

Colaborador_cpf = Label(interface, text='CPF', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_cpf.place(x=10, y=200)
Btn_Colaborador_cpf = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_cpf.place(x=130, y=200)

Colaborador_rg = Label(interface, text='RG', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_rg.place(x=10, y=250)
Btn_Colaborador_rg = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_rg.place(x=130, y=250)

Colaborador_nacionalidade= Label(interface, text='Nacionalidade', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_nacionalidade.place(x=10, y=300)
Btn_Colaborador_nacionalidade = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_nacionalidade.place(x=130, y=300)


# Coluna da direita
Colaborador_estado = Label(interface, text='Estado', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_estado.place(x=380, y=100)
Btn_Colaborador_estado = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_estado.place(x=500, y=100)

Colaborador_bairro = Label(interface, text='Bairro', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_bairro.place(x=380, y=150)
Btn_Colaborador_bairro = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_bairro.place(x=500, y=150)

Colaborador_rua = Label(interface, text='Rua/Av', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_rua.place(x=380, y=200)
Btn_Colaborador_rua = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_rua.place(x=500, y=200)

Colaborador_numero = Label(interface, text='Numero', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_numero.place(x=380, y=250)
Btn_Colaborador_numero = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_numero.place(x=500, y=250)

Colaborador_cep = Label(interface, text='CEP', height=1, anchor=NW, font=('ivy 10 bold'), bg=cor1, fg=cor4)
Colaborador_cep.place(x=380, y=300)
Btn_Colaborador_cep = Entry(interface, width=30, justify='left', relief=SOLID)
Btn_Colaborador_cep.place(x=500, y=300)


b_cadastro = Button(interface, width=30, justify='left', relief=SOLID, bg=cor1, fg=cor2, text='CADASTRAR', font=('ivy 10 bold'))
b_cadastro.place(x=250, y=400)


















interface.mainloop()
