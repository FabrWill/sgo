from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c+"/nomes.txt"
print(nomeArquivo)


def gravarDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write("\nNome....: %s" % vnome.get())
    arquivo.write("\nIdade...: %s" % vidade.get())
    arquivo.write("\nDetalhes: %s" % vdetalhes.get("1.0", END))
    arquivo.write("\n\n")
    arquivo.close()

app = Tk()
app.title('SGO - Sistema Gestão Odontológica')
app.geometry('800x600')
# app.configure(background='red')

txt1 = Label(app, text='TEXTO 1', bg='yellow', fg='black')
txt2 = Label(app, text='TEXTO 1', bg='yellow', fg='black')

txt1.place(x=10, y=10, width=150, height=30)
txt2.place(x=170, y=10, width=150, height=30)

vtxt = "Modulo 1"
vbg = 'green'
vfg = 'orange'
txt3 = Label(app, text=vtxt, bg=vbg, fg=vfg)
txt3.pack(ipadx=100, ipady=200, padx=40, pady=20, side="top", fill=X, expand=True)


# anchor usa pontos cardeais, N, S, E, W
# 
Label(app, text="Nome", bg='red', fg='black', anchor=W).place(x=50, y=100, width=100, height=20)
vnome = Entry(app)
vnome.place(x=160, y=100, height=20)

Label(app, text="Idade", bg='red', fg='black', anchor=W).place(x=50, y=140, width=100, height=20)
vidade = Entry(app)
vidade.place(x=160, y=140, height=20)

Label(app, text="Detalhes", bg='red', fg='black', anchor=E).place(x=50, y=180, width=100, height=20)
vdetalhes = Text(app)
vdetalhes.place(x=30, y=220, height=60)

Button(app, text="Gravar", command=gravarDados).place(x=30, y=300, height=20)

app.mainloop()