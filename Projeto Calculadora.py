from tkinter import *
from tkinter import ttk

cor1 = "#000000"  # preto
cor2 = "#8194b3"  # azul
cor3 = "#dce1e8"  # branco
cor4 = "#de3761"  # vermelho
cor5 = "#f0f0f0"  # cinza claro
cor6 = "#333333"  # cinza escuro

janela = Tk()
janela.title("Calculadora")
janela.geometry("210x331")  # Ajuste da largura e altura da janela

frame_tela = Frame(janela, width=210, height=50, bg=cor5)
frame_tela.grid(row=0, column=0) #criando a tela da calculadora onda irão aparecer os números digitados

frame_corpo = Frame(janela, width=240, height=270, bg=cor6)
frame_corpo.grid(row=1, column=0)#criando o corpo da calculadora aonde irão ficar os botões que criari mais para frente

todos_valores = ''
valor_texto = StringVar()

# Programando o funcionamento da calculadora através de funções

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18 "), bg=cor2, fg="white")
app_label.place(x=0, y=0)

# Criando os botões
b_clean = Button(frame_corpo, command=limpar_tela, text="C", width=12, height=3, bg=cor4, fg="white")
b_clean.grid(row=0, column=0, columnspan=2, sticky=NSEW)

b_dividir = Button(frame_corpo, command=lambda:entrar_valores('/'), text="/", width=6, height=3, bg=cor4, fg="white")
b_dividir.grid(row=0, column=2, sticky=NSEW)

b_multiplicacao = Button(frame_corpo, command=lambda:entrar_valores('*'), text="x", width=6, height=3, bg=cor4, fg="white")
b_multiplicacao.grid(row=0, column=3, sticky=NSEW)

b_7 = Button(frame_corpo, command=lambda:entrar_valores('7'), text="7", width=6, height=3, bg=cor3)
b_7.grid(row=1, column=0, sticky=NSEW)

b_8 = Button(frame_corpo, command=lambda:entrar_valores('8'), text="8", width=6, height=3, bg=cor3)
b_8.grid(row=1, column=1, sticky=NSEW)

b_9 = Button(frame_corpo, command=lambda:entrar_valores('9'), text="9", width=6, height=3, bg=cor3)
b_9.grid(row=1, column=2, sticky=NSEW)

b_menos = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=6, height=3, bg=cor4, fg="white")
b_menos.grid(row=1, column=3, sticky=NSEW)

b_4 = Button(frame_corpo, command=lambda:entrar_valores('4'), text="4", width=6, height=3, bg=cor3)
b_4.grid(row=2, column=0, sticky=NSEW)

b_5 = Button(frame_corpo, command=lambda:entrar_valores('5'), text="5", width=6, height=3, bg=cor3)
b_5.grid(row=2, column=1, sticky=NSEW)

b_6 = Button(frame_corpo, command=lambda:entrar_valores('6'), text="6", width=6, height=3, bg=cor3)
b_6.grid(row=2, column=2, sticky=NSEW)

b_mais = Button(frame_corpo, command=lambda:entrar_valores('+'), text="+", width=6, height=3, bg=cor4, fg="white")
b_mais.grid(row=2, column=3, sticky=NSEW)

b_1 = Button(frame_corpo, command=lambda:entrar_valores('1'), text="1", width=6, height=3, bg=cor3)
b_1.grid(row=3, column=0, sticky=NSEW)

b_2 = Button(frame_corpo, command=lambda:entrar_valores('2'), text="2", width=6, height=3, bg=cor3)
b_2.grid(row=3, column=1, sticky=NSEW)

b_3 = Button(frame_corpo, command=lambda:entrar_valores('3'), text="3", width=6, height=3, bg=cor3)
b_3.grid(row=3, column=2, sticky=NSEW)

b_igual = Button(frame_corpo, command=calcular, text="=", width=6, height=6, bg=cor4, fg="white")
b_igual.grid(row=3, column=3, rowspan=2, sticky=NSEW)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('0'), text="0", width=12, height=3, bg=cor3)
b_0.grid(row=4, column=0, columnspan=2, sticky=NSEW)

b_ponto = Button(frame_corpo, command=lambda:entrar_valores('.'), text=".", width=6, height=3, bg=cor3)
b_ponto.grid(row=4, column=2, sticky=NSEW)

# Ajustando as colunas e linhas para preencher o espaço
for i in range(5):
    frame_corpo.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame_corpo.grid_columnconfigure(i, weight=1)

janela.mainloop() 
