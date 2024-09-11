from Matriz import MatrizTablero
from tkinter import *

raiz = Tk()
frame: Frame = Frame()
texto1: Label
cuadro = Canvas()
bot1:Button

def main()-> None:
   crearGraf()


def crearGraf()->None:
    raiz.title("Gato de 4*4*4")
    raiz.resizable(False,False)
    frame.pack()
    frame.config(width="1280",height="720")

    cuadro.pack()
    cuadro.config(width="1280",height="720")
    
    cuadro.place(x=0,y=0)

    dibujarTabla("black")

    setTexto("Primer plano","black")

    bot1 = Button(raiz)
    raiz.mainloop()
   
def dibujarTabla(argu: str) -> None:
    cuadro.create_line(380,100,900,100,width=4,fill=argu)
    cuadro.create_line(380,620,900,620,width=4,fill=argu)
    cuadro.create_line(380,100,380,620,width=4,fill=argu)
    cuadro.create_line(900,100,900,620,width=4,fill=argu)
    for x in range(4):
        cuadro.create_line(380,100+x*130,900,100+x*130,width=2,fill=argu)
        cuadro.create_line(380+x*130,100,380+x*130,620,width=2,fill=argu)

def setTexto(mens: str, color: str) -> None:
    texto1 = Label(raiz,text = mens,fg = color, font=("Arial",20))
    texto1.place(x=560,y=20)


main()