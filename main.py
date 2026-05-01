import math 
import tkinter as tk

#preguntas: se puede usar imports? o todo en un solo archivo

#roles; que necesito? cual es el siguiente paso? necesito hacer algo para avanzar?
#diseño
#funciones


#idea: juego de parejas por dificultades, facil = 4(rejilla 2x4) parejas, normal = 8(regilla 4x4), dificil 12(regilla 6x4)
root = tk.Tk()
root.geometry("900x900")

cardWidth = 200
cardHeight = cardWidth * 7 / 5

dificultad = ""

#necesita recibir el tipo de dificultad seleccionada desde el menú 
#usar for dentro de for para hacer la rejilla, for padre seria para filas y el de dentro para columnas
def generarTablero(difiultad):
    if dificultad == "facil":
        print("se selecciono dificultad facil")
    
    

img1 = tk.PhotoImage(file="./recursos/estrella.png")

card1 = tk.Label(root, image=img1, borderwidth=3, relief="solid", width=cardWidth, height=cardHeight)
card2 = tk.Label(root, image=img1, borderwidth=3, relief="solid", width=cardWidth, height=cardHeight)
card3 = tk.Label(root, image=img1, borderwidth=3, relief="solid", width=cardWidth, height=cardHeight)
card4 = tk.Label(root, image=img1, borderwidth=3, relief="solid", width=cardWidth, height=cardHeight)
card1.grid(row=0, column=0, padx=10, pady=10)
card2.grid(row=0, column=1, padx=10, pady=10)
card3.grid(row=0, column=2, padx=10, pady=10)
card4.grid(row=1, column=0, padx=10, pady=10)


root.mainloop()