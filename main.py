import math 
import tkinter as tk

#preguntas: se puede usar imports? o todo en un solo archivo

#roles; que necesito? cual es el siguiente paso? necesito hacer algo para avanzar?
#diseño
#funciones


#idea: juego de parejas por dificultades, facil = 4(rejilla 2x4) parejas, normal = 8(regilla 4x4), dificil 12(regilla 6x4)
root = tk.Tk()
root.geometry("900x900")

cardWidth = 120
cardHeight = cardWidth * 7 / 5

dificultad = ""

def menu():
    boton_iniciar = tk.Button(width=10,text="Iniciar Juego",justify="center", pady=10,command=generarTablero)
    boton_iniciar.pack()

#necesita recibir el tipo de dificultad seleccionada desde el menú 
#usar for dentro de for para hacer la rejilla, for padre seria para filas y el de dentro para columnas
def generarTablero():
    frame_grid = tk.Frame(root)
    frame_grid.pack(pady=(100, 0))
    for columna in range(0,4):
        # fila_carta=[]
        for fila in range(0,4):
            #card = tk.Button(frame_grid,image=img1,bg="#3541b0",activebackground="#262e82",fg="white",font=("Arial",24,"bold"), width=cardWidth, height=cardHeight)
            card = tk.Label(frame_grid,image=img1,bg="white",highlightbackground="#3541b0",highlightthickness=3,fg="white",font=("Arial",24,"bold"), width=cardWidth, height=cardHeight)
            card.grid(row=fila, column=columna, padx=30, pady=10, )
            # fila_carta.append(card)
img1 = tk.PhotoImage(file="./recursos/hamburguesa.png")
menu()
root.mainloop()