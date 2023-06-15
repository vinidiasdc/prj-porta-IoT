from tkinter import *
from engine import CadastrarRostoAutorizado
from webCam import IniciarVigilancia

app = Tk()
app.title("Reconhecimeqnto Facial ESP8266")
app.geometry("450x300")
app.configure(background="#fff")

Button(app, text="Nova Pessoa Autorizada", command=CadastrarRostoAutorizado).place(x=10, y=100, width=200, height=50)
Button(app, text="Iniciar Vigilância", command=IniciarVigilancia).place(x=230, y=100, width=200, height=50)

app.mainloop()