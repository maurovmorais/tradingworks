###Gera a Tela para entrada de dados na tela

from tkinter import *


# Função onde recebe a carga apos confirmada.
def carga_horaria():
    print("Carga horária informada: %s"%carga.get())
    app.destroy()
    return carga

app = Tk()
app.title("CARGA HORÁRIA")
app.geometry("270x120")
app.configure(background="#dde")

Label(app,text="Carga horária",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=80,height=20)

# Variavel recebe o valor informado
carga = Entry(app)
carga.place(x=100, y=10,width=50,height=20)

# Define o botão Confirmar
Button(app,text="Confirmar",command=carga_horaria).place(x=85,y=70,width=100,height=20)

# Garante que a tela fique aparecendo, fica executando....
app.mainloop()
