# RAUL ARAM VAZQUEZ FIGUEROA   MATRICULA: 370132   FECHA: 24/11/2023 #
# Actividad#14 "Calculadora Funcional" #

from tkinter import*
from tkinter import ttk
import math

def Ingresar_Valores(tecla):
  if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
    entrada2.set(entrada2.get()+tecla)
  if tecla == '/' or tecla == '*' or tecla == '+' or tecla == '-':
      if tecla == '/':
          entrada1.set(entrada2.get() + '/')
      elif tecla == '*':
          entrada1.set(entrada2.get() + '*')
      elif tecla == '+':
          entrada1.set(entrada2.get() + '+')
      elif tecla == '-':
          entrada1.set(entrada2.get() + '-')
      entrada2.set('')
  if tecla == '=':
      entrada1.set(entrada1.get() + entrada2.get())
      resultado = eval(entrada1.get())
      entrada2.set(resultado)
      
def Raiz_Cuadrada(tecla):
    entrada1.set('')
    resultado=math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
    
def Borrar():
    inicio=0
    final=len(entrada2.get())
    entrada2.set(entrada2.get()[inicio:final-1])
    
def BorrarTodo():
    entrada1.set('')
    entrada2.set('')

def Ingresar_Valores_Teclado(event):
    tecla = event.char  
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
      entrada2.set(entrada2.get()+tecla)
    if tecla == '/' or tecla == '*' or tecla == '+' or tecla == '-':
      if tecla == '/':
          entrada1.set(entrada2.get() + '/')
      elif tecla == '*':
          entrada1.set(entrada2.get() + '*')
      elif tecla == '+':
          entrada1.set(entrada2.get() + '+')
      elif tecla == '-':
          entrada1.set(entrada2.get() + '-')
      entrada2.set('')
    if tecla == '=':
      entrada1.set(entrada1.get() + entrada2.get())
      resultado = eval(entrada1.get())
      entrada2.set(resultado)

root =Tk()
root.title("CALCULADORA")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos=ttk.Style()
estilos.configure('mainframe.TFrame', background="#DBDBDB")
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0)

estilos_label1=ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 14", anchor="E")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1)
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(N, E, S, W))

entrada2=StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(N, E, S, W))

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 21", width=5, background="#FFFFFF", relief="flat")

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 21", width=5, background="#CECECE", relief="flat")

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 21", width=5, background="#CECECE", relief="flat")

button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: Ingresar_Valores('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style='Botones_borrar.TButton', command=lambda: Borrar())
button_borrar_todo = ttk.Button(mainframe, text = "C", style='Botones_borrar.TButton', command=lambda: BorrarTodo())
button_parentesis1 = ttk.Button(mainframe, text="(", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('('))
button_parentesis2 = ttk.Button(mainframe, text=")", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores(')'))
button_punto = ttk.Button(mainframe, text =".", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('.'))
button_igual= ttk.Button(mainframe, text="=", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('='))

button_division = ttk.Button(mainframe, text=chr(247), style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('/'))
button_multiplicacion = ttk.Button(mainframe, text="x", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('*'))
button_resta = ttk.Button(mainframe, text="-", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('-'))
button_suma = ttk.Button(mainframe, text = "+", style='Botones_restantes.TButton', command=lambda: Ingresar_Valores('+'))
button_raiz_cuadrada = ttk.Button(mainframe, text= "√", style='Botones_restantes.TButton', command=lambda: Raiz_Cuadrada('√'))

button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)

button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid(column=0, row=6, columnspan=2, sticky=(W, E))
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, E))
button_raiz_cuadrada.grid(column=3, row=7)

for child in mainframe.winfo_children():
    child.grid_configure(ipady=15, padx=1, pady=1)

root.bind('<Key>', Ingresar_Valores_Teclado)

root,mainloop()



