import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mateo 
apellido: Diaz Beleña
---
Ejercicio: if_06
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente 
(edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_ingresada = self.txt_edad.get()

        edad_ingresada = int(edad_ingresada)

        if edad_ingresada < 10:

            mensaje_edad = "Usted es niño/a"
        
        elif edad_ingresada < 14:

            mensaje_edad = "Usted es pre-adolescente"
        
        elif edad_ingresada < 18:

            mensaje_edad = "Usted es adolescente"
        
        else:

            mensaje_edad = "Usted es mayor"

        alert("INFO", mensaje_edad)

#otra forma sin usar el elif
        #captura de pantalla en la carpeta de utn programación

        

        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()