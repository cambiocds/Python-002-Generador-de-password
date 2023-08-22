"""
Pasosparaimplementarlo:

1.Solicitaralusuarioqueingreselalongituddeseadaparalacontraseña.
2.Crearunalistadecaracteresválidos","incluyendoletrasmayúsculas","
minúsculas","dígitosysímbolos.
3.Utilizarlafunciónrandom.choice()paraseleccionarcaracteresalazar
delalistayconstruirlacontraseña.
4.Repetirelprocesohastaalcanzarlalongituddeseada.
5.Mostrarlacontraseñageneradaalusuario.

"""
import random
import tkinter as tk
import clipboard
from tkinter import messagebox

listaDeCaracteres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","'","!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]","|",":",";","<",">",".","?","/"]

def generar_pass():
    passFinalGenerada = ""
    if longitud_entry.get().isnumeric() and (int(longitud_entry.get())<=20 and int(longitud_entry.get())>0): # Compruebo que sea numerico y entre 1 y 20
        for n in range(int(longitud_entry.get())): 
            passFinalGenerada+=random.choice(listaDeCaracteres) # Voy almacenandoun elemento random de listaDeCaracteres
        clipboard.copy(passFinalGenerada) #Copiamos la pass generada en el portapeles
        mostrarPassGenerada_label.config(text=passFinalGenerada, font=("Verdana",15),fg="purple")# Cambio el valor del label para que muestre la pass genrada
        mensajePortapapeles_label.config(text="La pass ha sido copiada en el portapapeles \nPulse las teclas Ctrl + V donde desee pegarla",font="bold") #Muestro mensaje para que sepa que tiene la pass copiada en el portapapeles

    
    else:
        messagebox.showerror("Error","La cantidad debe ser númerica entre 1 y 20")




#Crear la ventana
ventana=tk.Tk()
ventana.geometry('350x180')
ventana.title("Generador de passwords")
ventana.eval('tk::PlaceWindow . center')#Centra la ventana
ventana.resizable(width=False,height=False)#No permite que la ventana sea redimensionable

#Crear etiquetas y campos de entrada
longitud_label=tk.Label(ventana,text="Introduzca el numero de caracteres de la contraseña entre 1 y 20")
longitud_label.pack()

longitud_entry=tk.Entry(ventana, width=2, justify= "center")
longitud_entry.pack()


#Botón para generar relresultado
generar_button=tk.Button(ventana,text="Generar",command=lambda:generar_pass())
generar_button.pack()

#Creo etiqueta para mostrar el resultado
tituloMostrarPassGenerada_label  = tk.Label(ventana, text="La pass generada es:")
tituloMostrarPassGenerada_label.pack()

mostrarPassGenerada_label  = tk.Label(ventana, text=" ")
mostrarPassGenerada_label.pack()

mensajePortapapeles_label  = tk.Label(ventana, text=" ")
mensajePortapapeles_label.pack()
#Iniciar el bucle principal de la aplicación
ventana.mainloop()