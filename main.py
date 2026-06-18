import math 
import tkinter as tk
import time
import random

#idea: juego de parejas por dificultades, facil = 4(rejilla 2x4) parejas, normal = 8(regilla 4x4), dificil 12(regilla 6x4)

#Necesito extraer valores de las funciones que al seleccionar el boton de Tiempo y dificultad extraer esos valores y por lo menos el valor del tiempo pasarlo a la funcion actualizar temporizador, dificultad pasarle el por argumentos dificultad, que facil sea 2, medio sea 4 y dificil sea 6 para que asi al reemplazarlo por columna in range (0, dificultad) cree mas o menos columnas, tambien debo agregar las imagenes en matriz cartas para revolverlas con random shuffle 

root = tk.Tk()
root.geometry("900x900")
root.config(bg="#EB9401")

cardWidth = 115
cardHeight =int(cardWidth * 7 / 5)
tiempo = 100
texto_tiempo = tk.StringVar()
texto_tiempo.set("time has no been set yet")

matriz_botones = []
matriz_cartas = []
eleccion = []



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
        root.after(1000, actualizar_temporizador, tiempo, tiempo_cronometro)
    else:
        texto_tiempo.set("¡Tiempo terminado!")

#Esta funcion es diseñada para las cartas y su ubicacion
def generarTablero(dificultad):
    #Temporizador
    lbl_tiempo = tk.Label(root, textvariable=texto_tiempo, font=("Lucida Console", 18, "bold"),bg="#EB9401", fg="white")
    lbl_tiempo.pack(pady=5)
    
    frame_grid = tk.Frame(root)
    frame_grid.pack(pady=(20, 0))

    for columna in range(0,dificultad):
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


def menu():
    #para mostrar en pantalla el nivel de dificultad que seleccione el jugador:
    difiSelect=tk.StringVar()
    difiSelect.set('Medio')
    diff=tk.IntVar()
    diff.set(4)
    
    timeSelect=tk.StringVar()
    timeSelect.set("Ilimitado")
    time=tk.IntVar()
    time.set(-1)
    #funciones para cada botton de dificultad para que al presionarlos cambie el texto de forma dinámica de (difiSelect)
    def selecFacil():
        difiSelect.set('Fácil')
        diff.set(2)
    def selecMedio():
        difiSelect.set('Medio')
        diff.set(4)
    def selecDificil():
        difiSelect.set('Difícil')
        diff.set(6)

    def timeIlim():
        timeSelect.set('Ilimitado')
        time.set(-1)

    def time1():
        timeSelect.set('1 minuto')
        time.set(60)
    
    def time2():
        timeSelect.set('2 minutos')
        time.set(120)
        
    def time5():
        timeSelect.set('5 minutos')
        time.set(300)

    def comenzarPartida():
        for elemento in root.winfo_children():
            elemento.pack_forget() #hacemos que cada cosa dentro del menú se quite
        t = time.get()
        d = diff.get()
        actualizar_temporizador(t,0)
        generarTablero(d)

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
    frame_time=tk.Label(root, text='SELECCIONA EL TIEMPO:', font=('Lucida Console',16,'bold'), bg='#EB9401', fg='Black')
    frame_time.pack(pady=5)
    selected_time= tk.Label(root, textvariable=timeSelect, font=('Lucida Console',16,'bold'), bg='#EB9401', fg='Black')
    selected_time.pack()
    frame_time=tk.Frame(root, bg='#EB9401')
    frame_time.pack(pady=10)

    #botón de tiempo ilimitado
    btnIlimitado=tk.Button(frame_time, text='Ilimitado', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white", command=timeIlim)
    
    #ubicación tiempo ilimitado
    btnIlimitado.grid(row=0, column=0, padx=8)
    
    #boton de tiempo 1 minuto
    btn1=tk.Button(frame_time, text='1 minuto', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white",command=time1)
    
    #ubicación tiempo 1 minuto
    btn1.grid(row=0, column=1, padx=8)
    
    #boton de tiempo 2 minutos
    btn2=tk.Button(frame_time, text='2 minutos', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white",command=time2)
    
    #ubicación de tiempo 2 minutos
    btn2.grid(row=0, column=2, padx=8)
    
    #boton de tiempo 5 minutos
    btn5=tk.Button(frame_time, text='5 minutos', font=('Lucida Console',16), width=10, bg="#BD2600",activebackground="#911F03",fg="white",command=time5)
    
    #ubicación de tiempo 5 minutos
    btn5.grid(row=0, column=3, padx=8)
    
    boton_iniciar.pack(pady=20) #lo puse aquí porque quería que el botón saliera de último (solo por estética), esto corresponde a la linea 51

menu()
root.mainloop()


