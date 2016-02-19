from Tkinter import *

v0 = Tk()
v1 = Toplevel(v0)

def mostrar(ventana): ventana.deiconify()
def ocultar(ventana): ventana.withdraw()
def ejecutar(f): v0.after(200, f)

v0.config(bg='black')
v0.geometry('500x200')

b1=Button(v0, text='ABRIR VENTANA V1', command=lambda: ejecutar(mostrar(v1)))
b1.grid(row=1, column=1)
b2=Button(v0, text='OCULTAR VENTANA V1', command=lambda: ejecutar(ocultar(v1)))
b2.grid(row=1, column=2)

v1.withdraw()
v0.mainloop()
