import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Mateo
apellido: Diaz Beleña
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        

        contador_pares = 0

        multiplos_cinco = 0

        numeros_divisibles_cien = 0

        suma_total = 0

        contador = 0 

        numero = prompt("Error", "Ingrese número entre el 100 y 1000")

        numero = int(numero)

        while numero < 99 or numero > 1001:

            numero = prompt("Error", "Ingrese número entre el 100 y 1000")

            numero = int(numero)


        while contador < numero:

            if contador % 2 == 0:

                contador_pares = contador_pares + 1

            if contador % 5 == 0:

                multiplos_cinco = multiplos_cinco + 1

            

            if contador % 100 == 0:

                numeros_divisibles_cien = numeros_divisibles_cien + 1   

            contador = contador + 1        

            suma_total = suma_total + contador

            

        
        alert("Resultado", f"El numero igresado es {contador}, hay {contador_pares} pares, {numeros_divisibles_cien} números divisibles por cien, {multiplos_cinco} multiplos de cinco y la suma acumluda de todos números {suma_total}")





    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()