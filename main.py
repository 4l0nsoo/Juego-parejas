import math 
import tkinter as tk

#preguntas: se puede usar imports? o todo en un solo archivo

#roles; que necesito? cual es el siguiente paso? necesito hacer algo para avanzar?
#diseño
#funciones

#idea: juego de parejas por dificultades, facil = 4(rejilla 2x4) parejas, normal = 8(regilla 4x4), dificil 12(regilla 6x4)
root = tk.Tk()
root.geometry("900x900")
root.config(bg="#EB9401")


cardWidth = 90
cardHeight = int(cardWidth * 7 / 5)

matriz_botones = []
matriz_cartas = []
eleccion = []

dificultad = ""

def menu():
    titulo=tk.Label(root, text='MEMORAMA :)', font=("Lucida Console",25,"bold"),bg="#EB9401")
    titulo.pack(pady=(20,10)) #muestra la etiqueta del titulo 'memorama'

    nombre=tk.Label(root, text='NOMBRE DEL JUGADOR:',font=("Lucida Console",16,"bold"),bg="#EB9401", fg="white")
    nombre.pack(pady=(10,5)) #muestra la etiqueta 'nombre del jugador'

    entradaNombre=tk.Entry(root, font=("Lucida Console", 16), justify="center", width=20)
    entradaNombre.pack(pady=(5,20)) #muestra la caja de texto
    entradaNombre.insert(0,'Jugador 1')

    boton_iniciar = tk.Button(width=20,text="INICIAR JUEGO",justify="center", pady=10,command=generarTablero,font=("Lucida Console",16,'bold'),bg="#9C0015",activebackground="#700210",fg="white", activeforeground='white')
    boton_iniciar.pack(pady=20) #muestra boton

dificultad=tk.Label(root, text='Selecciona la dificultad', font=('Lucida Console',16))


def mostrarCarta(event):
    presionado = event.widget
    info = presionado.grid_info()
    fila = info["row"]
    columna = info["column"]
    
    indice = fila * 4 + columna
    #card = tk.Label(frame_grid,image=img2,bg="white",highlightbackground="#3541b0",highlightthickness=3,fg="white",font=("Lucida Console",24,"bold"), width=cardWidth, height=cardHeight)
    
#necesita recibir el tipo de dificultad seleccionada desde el menú 
#usar for dentro de for para hacer la rejilla, for padre seria para filas y el de dentro para columnas
def generarTablero():
    frame_grid = tk.Frame(root)
    frame_grid.pack(pady=(20, 0))
    for columna in range(0,4):
        fila_carta=[]
        for fila in range(0,4):
            card = tk.Button(frame_grid,image=img1,bg="#BD2600",activebackground="#9C0015",fg="white",font=("Lucida Console",20,"bold"), width=cardWidth, height=cardHeight)
            #card = tk.Label(frame_grid,image=img2,bg="white",highlightbackground="#3541b0",highlightthickness=3,fg="white",font=("Lucida Console",24,"bold"), width=cardWidth, height=cardHeight)
            card.grid(row=fila, column=columna, padx=30, pady=10, )
            
            card.bind("<Button-1>", mostrarCarta)
            fila_carta.append(card)
        matriz_botones.append(fila_carta)

                



img1 = tk.PhotoImage(file="./recursos/interrogacion.png")
img2 = tk.PhotoImage(file="./recursos/hamburguesa.png")
menu()

root.mainloop()
