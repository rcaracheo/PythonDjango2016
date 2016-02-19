import Tkinter, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

numero = tkSimpleDialog.askinteger("Entero", "Intoduce un entero")
print numero
texto = tkSimpleDialog.askstring("String", "Intoduce un String")
print texto