import math 
import tkinter as tk
import random

#idea: juego de parejas por dificultades, facil = 4(rejilla 2x4) parejas, normal = 8(regilla 4x4), dificil 12(regilla 6x4)

#Necesito extraer valores de las funciones que al seleccionar el boton de Tiempo y dificultad extraer esos valores y por lo menos el valor del tiempo pasarlo a la funcion actualizar temporizador, dificultad pasarle el por argumentos dificultad, que facil sea 2, medio sea 4 y dificil sea 6 para que asi al reemplazarlo por columna in range (0, dificultad) cree mas o menos columnas, tambien debo agregar las imagenes en matriz cartas para revolverlas con random shuffle 

root = tk.Tk()
root.geometry("900x900")
root.config(bg="#EB9401")

cardWidth = 115
cardHeight =int(cardWidth * 7 / 5)
tablero = tk.Frame(root)
tiempo = 0
tiempo_tardado=0
nombre_jugador = "jugador 1"
intentos = 0
texto_tiempo = tk.StringVar()

#Imagenes de comida y signo de interrogación 
interrogacion = tk.PhotoImage(file="./recursos/interrogacion.png")
burger = tk.PhotoImage(file="./recursos/hamburguesa.png")
papas = tk.PhotoImage(file="./recursos/papas.png")
helado = tk.PhotoImage(file="./recursos/helado.png")
pastas = tk.PhotoImage(file="./recursos/pastas.png")
perro = tk.PhotoImage(file="./recursos/perro.png")
pizza = tk.PhotoImage(file="./recursos/pizza.png")
pollo = tk.PhotoImage(file="./recursos/pollo.png")
cafe = tk.PhotoImage(file="./recursos/cafe.png")
colita = tk.PhotoImage(file="./recursos/colita.png")
gaseosa = tk.PhotoImage(file="./recursos/gaseosa.png")
crispetas = tk.PhotoImage(file="./recursos/crispetas.png")
sushi = tk.PhotoImage(file="./recursos/sushi.png")

matriz_botones = []
imagenes = [burger,papas,helado,pastas,perro,pizza,pollo,cafe,colita,gaseosa,crispetas,sushi]
matriz_cartas = []
eleccion = []

def condicionVictoria(tiempo):
    tablero.forget()
    mostrar_victoria(nombre_jugador, tiempo, intentos+8, intentos)

def actualizar_temporizador(tiempo, tiempo_cronometro):
    if tiempo == -1:  # ilimitado, cuenta hacia arriba
        mins, secs = divmod(tiempo_cronometro, 60)  # necesitas otra variable para esto
        texto_tiempo.set(f"{mins:02d}:{secs:02d}")
        tiempo_cronometro +=1

        root.after(1000, actualizar_temporizador, tiempo, tiempo_cronometro)
    elif tiempo > 0:  # cuenta regresiva
        mins, secs = divmod(tiempo, 60)
        texto_tiempo.set(f"{mins:02d}:{secs:02d}")
        tiempo -= 1
        tiempo_cronometro
        root.after(1000, actualizar_temporizador, tiempo, tiempo_cronometro)
    else:
        texto_tiempo.set("¡Tiempo terminado!")
        root.after(1000, lambda:(condicionVictoria(tiempo_cronometro)))
        

#Esta funcion es diseñada para las cartas y su ubicacion
def generarTablero(dificultad):
    #Temporizador
    tablero.pack()
    
    total_pares = (dificultad * 4) // 2  # 4, 8 o 12

    pares = []
    for i in range(total_pares):
        pares.append(imagenes[i])
        pares.append(imagenes[i])
    
    random.shuffle(pares)
    
    matriz_cartas.clear()
    for carta in pares:
        matriz_cartas.append(carta)

    lbl_tiempo = tk.Label(tablero, textvariable=texto_tiempo, font=("Lucida Console", 18, "bold"),bg="#EB9401", fg="white")
    lbl_tiempo.pack(pady=5)
    
    frame_grid = tk.Frame(tablero)
    frame_grid.pack(pady=(20, 0))

    for columna in range(0,dificultad):
        fila_carta=[]
        for fila in range(0,4):
            card = tk.Button(frame_grid,image=interrogacion,bg="#BD2600",activebackground="#9C0015",fg="white",font=("Lucida Console",20,"bold"), width=cardWidth, height=cardHeight)
            #card = tk.Label(frame_grid,image=burger,bg="white",highlightbackground="#3541b0",highlightthickness=3,fg="white",font=("Lucida Console",24,"bold"), width=cardWidth, height=cardHeight)
            card.grid(row=fila, column=columna, padx=30, pady=10, )
            #indice = fila * dificultad + columna
            card.bind("<Button-1>", mostrarCarta)
            fila_carta.append(card)
        matriz_botones.append(fila_carta)

# REVISAR ERRORES

bloqueado = False

def desbloquear():
    global bloqueado
    bloqueado = False

def voltearCarta(carta1, carta2):
    carta1.config(image=interrogacion, bg="#BD2600", state="normal")
    carta2.config(image=interrogacion, bg="#BD2600", state="normal")
    intento += 1
    desbloquear()  # desbloquear justo después de voltear

def mostrarCarta(event):
    global bloqueado

    if bloqueado:
        return

    presionado = event.widget

    if presionado["state"] == "disabled":  # evitar re-clickear carta ya encontrada
        return

    info = presionado.grid_info()
    fila = info["row"]
    columna = info["column"]
    num_columnas = len(matriz_botones)
    indice = fila * num_columnas + columna

    presionado.config(image=matriz_cartas[indice], bg="white",
                      highlightbackground="#3541b0", highlightthickness=3, state="disabled")

    eleccion.append((matriz_cartas[indice], presionado))

    if len(eleccion) == 2:
        bloqueado = True  # bloquear clicks mientras se evalúa

        if eleccion[0][0] == eleccion[1][0]:
            # pareja encontrada, quedan volteadas
            eleccion.clear()
            bloqueado = False
        else:
            carta1 = eleccion[0][1]
            carta2 = eleccion[1][1]
            eleccion.clear()
            root.after(500, lambda: voltearCarta(carta1, carta2))  # delay de 500ms para voltear



#funcion para quitar el menú y que aparezcan solo las cartas


def menu():
    #para mostrar en pantalla el nivel de dificultad que seleccione el jugador:
    difiSelect = tk.StringVar()
    difiSelect.set('Medio')
    diff = tk.IntVar()
    diff.set(4)

    timeSelect = tk.StringVar()
    timeSelect.set("Ilimitado")
    time = tk.IntVar()
    time.set(-1)

    def comenzarPartida():
        nombre_jugador = entradaNombre.get()
        for elemento in root.winfo_children():
            elemento.pack_forget() #hacemos que cada cosa dentro del menú se quite
        actualizar_temporizador(time.get(), 0)
        generarTablero(diff.get())

    ###### Esto es para el titulo, el boton de inicio del juego, para la etiqueta de nombre, para ingresar el nombre
    titulo = tk.Label(root, text='MEMORAMA :)', font=("Lucida Console", 25, "bold"), bg="#EB9401", fg="white")
    titulo.pack(pady=(20, 10)) #muestra la etiqueta del titulo 'memorama'

    nombre = tk.Label(root, text='NOMBRE DEL JUGADOR:', font=("Lucida Console", 16, "bold"), bg="#EB9401", fg="Black")
    nombre.pack(pady=(10, 5)) #muestra la etiqueta 'nombre del jugador'

    entradaNombre = tk.Entry(root, font=("Lucida Console", 16), justify="center", width=20, bg="#D6D6D6")
    entradaNombre.pack(pady=(5, 20)) #muestra la caja de texto para ingresar el nombre
    entradaNombre.insert(0, 'JUGADOR 1')

    boton_iniciar = tk.Button(root, width=20, text="INICIAR JUEGO", justify="center", pady=10,
                              command=comenzarPartida, font=("Lucida Console", 16, 'bold'),
                              bg="#9C0015", activebackground="#700210", fg="white", activeforeground='white') #muestra boton de iniciar juego

    ######### Esto es para lo del menú principal, para la selección de dificultad
    #etiqueta para 'selecciona la dificultad'
    tk.Label(root, text='SELECCIONA LA DIFICULTAD:', font=('Lucida Console', 16, 'bold'), bg='#EB9401', fg='Black').pack(pady=5)

    #etiqueta que dice 'dificultad seleccionada'
    tk.Label(root, text='Dificultad seleccionada:', font=('Lucida Console', 14, 'bold'), fg='Black', bg='#EB9401').pack(pady=10)

    #etiqueta que muestra la selección de la dificultad en tiempo real según el usuario escoja:
    tk.Label(root, textvariable=difiSelect, font=('Lucida Console', 14), fg='Black', bg='#EB9401', padx=10, pady=5).pack(pady=5)

    #Caja donde se guardarán los niveles de dificultad
    frame_difi = tk.Frame(root, bg='#EB9401')
    frame_difi.pack(pady=10)

    #botón de seleccion nivel facil
    #ubicación del botón facil
    tk.Button(frame_difi, text='Nivel fácil', font=('Lucida Console', 16), width=20,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (difiSelect.set('Fácil'), diff.set(2))).grid(row=0, column=0, padx=10)

    #boton de seleccion nivel medio
    #ubicación del botón medio
    tk.Button(frame_difi, text='Nivel medio', font=('Lucida Console', 16), width=20,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (difiSelect.set('Medio'), diff.set(4))).grid(row=0, column=1, padx=10)

    #boton de seleccion nivel dificil
    #ubicación del botón dificil
    tk.Button(frame_difi, text='Nivel difícil', font=('Lucida Console', 16), width=20,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (difiSelect.set('Difícil'), diff.set(6))).grid(row=0, column=2, padx=10)

    #Opciones de tiempo (Etiqueta de seleccion de tiempo)
    tk.Label(root, text='SELECCIONA EL TIEMPO:', font=('Lucida Console', 16, 'bold'), bg='#EB9401', fg='Black').pack(pady=5)

    #etiqueta que muestra el tiempo seleccionado en tiempo real
    tk.Label(root, textvariable=timeSelect, font=('Lucida Console', 16, 'bold'), bg='#EB9401', fg='Black').pack()

    frame_time = tk.Frame(root, bg='#EB9401')
    frame_time.pack(pady=10)

    #botón de tiempo ilimitado
    #ubicación tiempo ilimitado
    tk.Button(frame_time, text='Ilimitado', font=('Lucida Console', 16), width=10,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (timeSelect.set('Ilimitado'), time.set(-1))).grid(row=0, column=0, padx=8)

    #boton de tiempo 1 minuto
    #ubicación tiempo 1 minuto
    tk.Button(frame_time, text='1 minuto', font=('Lucida Console', 16), width=10,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (timeSelect.set('1 minuto'), time.set(60))).grid(row=0, column=1, padx=8)

    #boton de tiempo 2 minutos
    #ubicación de tiempo 2 minutos
    tk.Button(frame_time, text='2 minutos', font=('Lucida Console', 16), width=10,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (timeSelect.set('2 minutos'), time.set(120))).grid(row=0, column=2, padx=8)

    #boton de tiempo 5 minutos
    #ubicación de tiempo 5 minutos
    tk.Button(frame_time, text='5 minutos', font=('Lucida Console', 16), width=10,
              bg="#BD2600", activebackground="#911F03", fg="white",
              command=lambda: (timeSelect.set('5 minutos'), time.set(300))).grid(row=0, column=3, padx=8)

    boton_iniciar.pack(pady=20) #lo puse aquí porque quería que el botón saliera de último (solo por estética), esto corresponde a la linea 51

def verResultados():
    pass

def mostrar_victoria(nombre, tiempo, intentos, fail):

    #Fondo negro, en lugar de este deben estar las cartas
    frame_victory= tk.Frame(root, bg="#1a1a1a")
    frame_victory.place(relx=0, rely=0, relwidth=1, relheight=1)

    #Tarjeta central gris
    carta= tk.Frame(frame_victory, bg="#2a2a2a", padx=40, pady=30)
    carta.place(relx=0.5, rely=0.5, anchor="center")

    #figura de copa
    Label_titulo=tk.Label(carta, text="🏆", font=("Lucida Console", 40), fg="#FFD700", bg="#2a2a2a" )
    Label_titulo.pack()
    # Mensaje "Ganaste"
    Label_text1=tk.Label(carta, text=f"Ganaste {nombre}", font=("Snap ITC", 25, "bold"),
                        bg="#2a2a2a",
                        fg="#FFD700")
    Label_text1.pack()
    #Mensaje "Encontraste todas las cartas"
    Label_text2= tk.Label(carta, text="Encontraste todas las parejas", font=("Lucida Console", 11),
                        bg="#2a2a2a",
                        fg="#FFA500")
    Label_text2.pack()

    #En Esta aparecera los resultados del juego
    frame_estad= tk.Frame(carta, bg="#2a2a2a",
                        padx=20, pady=10)
    frame_estad.pack(fill="x", pady=(0,15))

    #Cuadros con los datos del juego
    estadisticas= [("Tiempo", tiempo), ("Total de Intentos", intentos), ("Intentos Fallidos", fail)]

    for i, (label, valor) in enumerate(estadisticas):
        #caracteristicas del cuadro donde se encuentras los datos del juego
        col= tk.Frame(frame_estad, bg="black", padx=15)
        col.grid(row=0, column=i, padx=10)

        #Subtitulos de los cuadros
        tk.Label(col, text=label, font=("Lucida Console", 10, "bold"),
                bg="black", fg="#FFA500").pack()
        
        #Valores principales
        Label_fund=tk.Label(col, text=str(valor), font=("Lucida Console", 18, "bold"),
                bg="black", fg="#FFA500")
        Label_fund.pack()
    tk.Frame(carta, bg="#ddd", height=1).pack(fill="x", pady=10)

    #Botones
    
    #Este Boton tiene que permitir volver a la pantalla principal
    def volver_menu():                                           #Esta funcion conecta esta interfaz con la principal
        frame_victory.destroy()
        menu()
        
    boton_volver = tk.Button(carta, text="Volver al menú",
                        font=("Lucida Console", 12, "bold"),
                        fg="White",
                        bg="#9C0015",
                        borderwidth=2,
                        activebackground="White",
                        width=22, pady=8, 
                        relief="solid",
                        command=volver_menu)
    boton_volver.pack(pady=4)

#Este boton debe de permitir ver los resultados de juegos o partidas anteriores
    boton_resultados= tk. Button(carta, text="Ver resultados",
                                font=("Lucida Console", 12, "bold"),
                                fg="white",
                                bg="#9C0015",
                                borderwidth=2,
                                activebackground="white",
                                width=22, pady=8,
                                relief="solid",
                                command=verResultados)
    boton_resultados.pack(pady=4)

#Este boton permite salir del juego, cerrando directamente la pestaña
    boton_salir=tk.Button(carta, text="Salir", 
                        font=("Lucida Console", 12, "bold"),
                        fg="White",
                        bg="#9C0015",
                        borderwidth=2,
                        activebackground="White",
                        width=22, pady=8,
                        relief="solid",
                        command= root.destroy)
    boton_salir.pack(pady=(4,0))

menu()
root.mainloop()


