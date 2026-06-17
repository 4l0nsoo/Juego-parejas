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

cardWidth = 115
cardHeight =int(cardWidth * 7 / 5)

matriz_botones = []
matriz_cartas = []
eleccion = []

#Esta funcion es diseñada para las cartas y su ubicacion
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


def mostrarCarta(event):
    presionado = event.widget
    info = presionado.grid_info()
    fila = info["row"]
    columna = info["column"]
    
    indice = fila * 4 + columna
    #card = tk.Label(frame_grid,image=img2,bg="white",highlightbackground="#3541b0",highlightthickness=3,fg="white",font=("Lucida Console",24,"bold"), width=cardWidth, height=cardHeight)
    
#necesita recibir el tipo de dificultad seleccionada desde el menú 
#usar for dentro de for para hacer la rejilla, for padre seria para filas y el de dentro para columnas

#Imagenes de comida y signo de interrogación 
img1 = tk.PhotoImage(file="./recursos/interrogacion.png")
img2 = tk.PhotoImage(file="./recursos/hamburguesa.png")

#funcion para quitar el menú y que aparezcan solo las cartas
def comenzarPartida():
    for elemento in root.winfo_children():
        elemento.pack_forget() #hacemos que cada cosa dentro del menú se quite
    generarTablero()

def menu():
    #para mostrar en pantalla el nivel de dificultad que seleccione el jugador:
    difiSelect=tk.StringVar()
    difiSelect.set('Normal')
    #funciones para cada botton de dificultad para que al presionarlos cambie el texto de forma dinámica de (difiSelect)
    def selecFacil():
        difiSelect.set('Fácil')
    def selecMedio():
        difiSelect.set('Medio')
    def selecDificil():
        difiSelect.set('Difícil')

######Esto es para el titulo, el boton de inicio del juego, para la etiqueta de nombre, para ingresar el nombre 
    titulo=tk.Label(root, text='MEMORAMA :)', font=("Lucida Console",25,"bold"),bg="#EB9401",fg="white")
    titulo.pack(pady=(20,10)) #muestra la etiqueta del titulo 'memorama'

    nombre=tk.Label(root, text='NOMBRE DEL JUGADOR:',font=("Lucida Console",16,"bold"),bg="#EB9401", fg="Black")
    nombre.pack(pady=(10,5)) #muestra la etiqueta 'nombre del jugador'

    entradaNombre=tk.Entry(root, font=("Lucida Console", 16), justify="center", width=20,bg="#D6D6D6")
    entradaNombre.pack(pady=(5,20)) #muestra la caja de texto para ingresar el nombre
    entradaNombre.insert(0,'JUGADOR 1')

    boton_iniciar = tk.Button(width=20,text="INICIAR JUEGO",justify="center", pady=10,command=comenzarPartida,font=("Lucida Console",16,'bold'),bg="#9C0015",activebackground="#700210",fg="white", activeforeground='white')  #muestra boton de iniciar juego

        #########Esto es para lo del menú principal, para la selección de dificultad
    #etiqueta para 'selecciona la dificultad'
    dificultad=tk.Label(root, text='SELECCIONA LA DIFICULTAD:', font=('Lucida Console',16,'bold'), bg='#EB9401', fg='Black')
    dificultad.pack(pady=5)
    #etiqueta que dice 'dificultad seleccionada'
    seleccionDifi=tk.Label(root, text='Dificultad seleccionada:', font=('Lucida Console', 14, 'bold'), fg='Black', bg='#EB9401')
    seleccionDifi.pack(pady=10)
    #etiqueta que muestra la selección de la dificultad en tiempo real según el usuario escoja:
    lblDinamica=tk.Label(root, textvariable=difiSelect, font=('Lucida Console', 14),fg='Black', bg='#EB9401', padx=10, pady=5)
    lblDinamica.pack(pady=5)
    #Caja donde se guardarán los niveles de dificultad
    dificultad=tk.Frame(root, bg='#EB9401')
    dificultad.pack(pady=10)
    #botón de seleccion nivel facil
    btnFacil=tk.Button(dificultad, text='Nivel fácil', font=('Lucida Console',16), width=20, bg="#BD2600",activebackground="#911F03",fg="white", command=selecFacil)
    #ubicación del botón facil
    btnFacil.grid(row=0, column=0, padx=10)
    #boton de seleccion nivel medio
    btnMedio=tk.Button(dificultad, text='Nivel medio', font=('Lucida Console',16), width=20, bg="#BD2600",activebackground="#911F03",fg="white", command=selecMedio)
    #ubicación del botón medio
    btnMedio.grid(row=0, column=1, padx=10)
    #boton de seleccion nivel dificil
    btnDificil=tk.Button(dificultad, text='Nivel difícil', font=('Lucida Console',16), width=20, bg="#BD2600", activebackground="#911F03",fg="white", command=selecDificil)
    #ubicación del botón dificil
    btnDificil.grid(row=0, column=2, padx=10)
    #Opciones de tiempo (Etiqueta de seleccion de tiempo)
    time=tk.Label(root, text='SELECCIONA EL TIEMPO:', font=('Lucida Console',16,'bold'), bg='#EB9401', fg='Black')
    time.pack(pady=5)
    time=tk.Frame(root, bg='#EB9401')
    time.pack(pady=10)

    #botón de tiempo ilimitado
    btnIlimitado=tk.Button(time, text='Ilimitado', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white")
    #ubicación tiempo ilimitado
    btnIlimitado.grid(row=0, column=0, padx=8)
    #boton de tiempo 1 minuto
    btn1=tk.Button(time, text='1 minuto', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white")
    #ubicación tiempo 1 minuto
    btn1.grid(row=0, column=1, padx=8)
    #boton de tiempo 2 minutos
    btn2=tk.Button(time, text='2 minutos', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white")
    #ubicación de tiempo 2 minutos
    btn2.grid(row=0, column=2, padx=8)
    #boton de tiempo 5 minutos
    btn5=tk.Button(time, text='5 minutos', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white")
    #ubicación de tiempo 5 minutos
    btn5.grid(row=0, column=3, padx=8)
    
    boton_iniciar.pack(pady=20) #lo puse aquí porque quería que el botón saliera de último (solo por estética), esto corresponde a la linea 51

menu()
root.mainloop()


