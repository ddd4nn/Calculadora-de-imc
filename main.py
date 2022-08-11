from tkinter import *
from tkinter import font
from tkinter import ttk



#--------cores-------#

""" 
    
    paleta de cores teste
    #343434 cinza 1
    #464646 cinza 2
    #FFFFFF branco
    #0077b6 azul claro
    
"""

co0 = '#00303b' #branco / white
co1 = '#ff7777' #preto / black
co2 = '#ffce96' #azul / blue

#---------janela--------#

janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co0)

#--------------- divisão das janelas ---------------#

frame_cima= Frame(janela, width=295, height=50, bg=co0, pady= 0, padx=0, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg=co0, pady= 0, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#--------------- configurando frame cima ---------------#

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ubuntu 16 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=1300, height=1, padx=0, relief='flat', anchor='center', font=('Ubuntu 1 '), bg=co2, fg=co2)
app_linha.place(x=0, y=35)


def calcular():
    # ----------------- logica -----------------#

    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = float(peso / altura**2)

    resultado = imc

    if imc < 17:
        l_resultado_texto['text'] = "está muito abaixo do peso"

    elif imc >= 17.1 and imc < 18.49:
        l_resultado_texto['text'] = "está abaixo do peso"

    elif imc >= 18.5 and imc < 24.99:
        l_resultado_texto['text'] = "está com peso normal"

    elif imc >= 25 and imc < 28.99:
        l_resultado_texto['text'] = "está acima do peso"

    elif imc >= 30 and imc < 34.99:
        l_resultado_texto['text'] = "está com obesidade nivel 1"

    elif imc >= 35 and imc < 39.99:
        l_resultado_texto['text'] = "está com obesidade nivel 2"

    l_resultado['text'] = "{:.{}f}".format(imc, 2)


 #--------------- configurando frame baixo ---------------#

#label e entry do peso
l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ubuntu 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width= 5, relief='solid', font=('Ubuntu 10 bold'), justify='center',)
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


#label e entry da altura
l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ubuntu 10 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width= 5, relief='solid', font=('Ubuntu 10 bold'), justify='center',)
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


#--------------exibindo o resultado-------------------#

#frame do resultado
l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ubuntu 24 bold'), bg=co2, fg=co1)
l_resultado.place(x=170, y=10)
l_resultado_texto = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ubuntu 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=85)

#botão de calcular
b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=34, height=1,overrelief='solid', relief='raised', anchor='center', font=('Ubuntu 10 bold'), bg=co2, fg=co1)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=40)





janela.mainloop()

