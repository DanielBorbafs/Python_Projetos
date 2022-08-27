import tkinter
from tkinter import *
from tkinter import ttk

# * significa importar toda biblioteca

cor1 = "#1e1f1e" # preta
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("300x418") # largura x altura
janela.config(bg=cor1)

# Frames Criados
frame_tela = Frame(janela, width=400, height=55, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=400, height=368)
frame_corpo.grid(row=1, column=0)

# Criando botões

b_1 = Button(frame_corpo, text="APAGAR", width=18, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=195, y=0)
b_3 = Button(frame_corpo, text="/", width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=265, y=0)


b_4 = Button(frame_corpo, text="7", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_4 = Button(frame_corpo, text="8", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=70, y=52)
b_4 = Button(frame_corpo, text="9", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=195, y=52)
b_3 = Button(frame_corpo, text="*", width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=265, y=52)


janela.mainloop()
