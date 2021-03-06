#encoding:UTF-8
#David Salvador Ruiz Roa
#Music Hero

from Graphics import*
from random import randint
from Myro import*

gravedad = 40

v = Window("Fisica",800,600)
fondo = makePicture("fondo2.jpg")
fondo.x = 400
fondo.y = 280
fondo.draw(v)

v.mode = "physics"
v.setBackground(Color("black"))

#Leer Archivo Marcador
def leerArchivo():
    entrada = open("marcador.txt","r") #read
    linea = entrada.readline() #lee "Marcado\nr"
    valor = entrada.readline() #puntos "150\n"
    valor = valor[0:len(valor)-1]
    puntos = int(valor)
    entrada.close()
    return puntos

#Banderas

juego = 1
tipoDeJuegoIzquierda = 0
tipoDeJuegoDerecha= 0


#Letras

A = Text((10+25,565),"Q")
A.color = Color("white")
A.bodyType = "static"

S = Text((70+25,565),"S")
S.color = Color("white")
S.bodyType = "static"

D = Text((130+25,565),"D")
D.color = Color("white")
D.bodyType = "static"

F = Text((190+25,565),"F")
F.color = Color("white")
F.bodyType = "static"

H = Text((560+25,565),"H")
H.color = Color("white")
H.bodyType = "static"

J = Text((620+25,565),"J")
J.color = Color("white")
J.bodyType = "static"

K = Text((680+25,565),"K")
K.color = Color("white")
K.bodyType = "static"

L = Text((740+25,565),"L")
L.color = Color("white")
L.bodyType = "static"

#BOTONES


ambas = Button((375,520),"Ambas")
ambas.draw(v)
derecha = Button((500,520),"Derecha")
derecha.draw(v)
izquierda = Button((250,520),"Izquierda")
izquierda.draw(v)
salirBtn = Button((365,350),"Salir del Juego")
sb = SpeechBubble((300, 475), (500, 515), "Elige la(s) columnas", (300, 515))
sb.color = Color("Black")
sb.bodyType = "static"
sb.draw(v)




def habilitarAmbas(btn,e):
    global tipoDeJuegoIzquierda, tipoDeJuegoDerecha, juego
    print("Se han seleccionado Ambas columnas")
    tipoDeJuegoIzquierda = 0
    tipoDeJuegoDerecha = 8
    juego = 1
    sb.undraw()
    play("a1.wav")
    desdibujarLetras()
    
def habilitarDerecha(btn,e):
    global tipoDeJuegoIzquierda, tipoDeJuegoDerecha, juego
    print("Se ha seleccionado la columna Derecha")
    tipoDeJuegoIzquierda = 5
    tipoDeJuegoDerecha = 8
    juego = 1
    sb.undraw()
    play("b1.wav")
    desdibujarLetras()

def habilitarIzquierda(btn,e):
    global tipoDeJuegoIzquierda, tipoDeJuegoDerecha, juego
    print("Se ha seleccionado la columna Izuiqerda Izquierda")
    tipoDeJuegoIzquierda = 0
    tipoDeJuegoDerecha = 4
    juego = 1
    sb.undraw()
    play("c1.wav")
    desdibujarLetras()

def desdibujarLetras():
    A.undraw()
    S.undraw()
    D.undraw()
    F.undraw()
    H.undraw()
    J.undraw()
    K.undraw()
    L.undraw()
    
def salirDelJuego(btn,e):
    v.close()
    
salirBtn.connect("click",salirDelJuego)
ambas.connect("click",habilitarAmbas)
derecha.connect("click",habilitarDerecha)
izquierda.connect("click",habilitarIzquierda)

#Puntaje

puntaje = 50
score = 0

#Texto

titulo = Text((400,-100),"Music Hero")
titulo.color = Color("White")
titulo.draw(v)

mayor = leerArchivo() 

highScore = Text((400,565),"High Score = " + str(mayor))
highScore.color = Color("Black")
highScore.bodyType = "static"

scoret = Text((400,450),"Score = 0")
scoret.color = Color("White")
scoret.bodyType = "static"

puntajet = Text((400,200),"Puntos de vida 50")
puntajet.color = Color("White")

#Notas

listaNotas = []

y11 = 540
y22 = 590
y33 = -10

nota1m = RoundedRectangle((10,y11),(60,y22),10)
nota2m = RoundedRectangle((70,y11),(120,y22),10)
nota3m = RoundedRectangle((130,y11),(180,y22),10)
nota4m = RoundedRectangle((190,y11),(240,y22),10)

riel1 = RoundedRectangle((10,y33),(60,y22),10)
riel2 = RoundedRectangle((70,y33),(120,y22),10)
riel3 = RoundedRectangle((130,y33),(180,y22),10)
riel4 = RoundedRectangle((190,y33),(240,y22),10)
    
nota5m = RoundedRectangle((560,y11),(610,y22),10)
nota6m = RoundedRectangle((620,y11),(670,y22),10)
nota7m = RoundedRectangle((680,y11),(730,y22),10)
nota8m = RoundedRectangle((740,y11),(790,y22),10)

riel5 = RoundedRectangle((560,y33),(610,y22),10)
riel6 = RoundedRectangle((620,y33),(670,y22),10)
riel7 = RoundedRectangle((680,y33),(730,y22),10)
riel8 = RoundedRectangle((740,y33),(790,y22),10)

nota1m.bodyType = "static"
nota2m.bodyType = "static"
nota3m.bodyType = "static"
nota4m.bodyType = "static"
nota5m.bodyType = "static"
nota6m.bodyType = "static"
nota7m.bodyType = "static"
nota8m.bodyType = "static"

riel1.bodyType = "static"
riel2.bodyType = "static"
riel3.bodyType = "static"
riel4.bodyType = "static"
riel5.bodyType = "static"
riel6.bodyType = "static"
riel7.bodyType = "static"
riel8.bodyType = "static"

nota1m.fill = Color("Grey")
nota2m.fill = Color("Grey")
nota3m.fill = Color("Grey")
nota4m.fill = Color("Grey")
nota5m.fill = Color("Grey")
nota6m.fill = Color("Grey")
nota7m.fill = Color("Grey")
nota8m.fill = Color("Grey")

riel1.fill = None
riel2.fill = None
riel3.fill = None
riel4.fill = None
riel5.fill = None
riel6.fill = None
riel7.fill = None
riel8.fill = None

riel1.outline = Color("Blue")
riel2.outline = Color("Yellow")
riel3.outline = Color("Red")
riel4.outline = Color("Lime")
riel5.outline = Color("Lime")
riel6.outline = Color("Yellow")
riel7.outline = Color("Red")
riel8.outline = Color("Blue")

def dibujarRieles():
    riel1.draw(v)
    riel2.draw(v)
    riel3.draw(v)
    riel4.draw(v)
    riel5.draw(v)
    riel6.draw(v)
    riel7.draw(v)
    riel8.draw(v)

def dibujarNotasm():
    nota1m.draw(v)
    nota2m.draw(v)
    nota3m.draw(v)
    nota4m.draw(v)
    nota5m.draw(v)
    nota6m.draw(v)
    nota7m.draw(v)
    nota8m.draw(v)
    
def dibujarLetras():
    #Letras sobre las teclas
    A.draw(v)
    S.draw(v)
    D.draw(v)
    F.draw(v)
    H.draw(v)
    J.draw(v)
    K.draw(v)
    L.draw(v)
    
   
def sonido():
    azar = randint(1,13)
    
    if azar == 1:
        play("a1.wav")
    if azar == 2:
        play("a1s.wav")
    if azar == 3:
        play("b1.wav")
    if azar == 4:
        play("c1.wav")
    if azar == 5:
        play("c1s.wav")
    if azar == 6:
        play("c2.wav")
    if azar == 7:
        play("d1.wav")
    if azar == 8:
        play("d1s.wav")
    if azar == 9:
        play("e1.wav")
    if azar == 10:
        play("f1.wav")
    if azar == 11:
        play("f1s.wav")
    if azar == 12:
        play("g1.wav")
    if azar == 13:
        play("g1s.wav")

def ejecutarColision():
    global puntajet, puntaje, scoret, score
    sonido()
    puntaje += 1
    puntajet.text = "Puntos de vida: " + str(puntaje)
    score += 1
    scoret.text = "Score = " + str(score)
    
def guardarMarcador():
    anteriores = leerArchivo()
    if score > anteriores :
        salida = open("marcador.txt","w")
        salida.write("marcador\n")
        salida.write(str(score) + "\n")
        salida.close()

def atenderTeclado(v,e):
    global puntajet,puntaje,scoret,score
    vida = 0
    
    y1 = 530
    y2 = 600
    
    if e.key == "a":                                        #Colisión de A
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 60 and ancho >= 10:
                    nota1m.fill = Color("Blue")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "s":                                        #Colisión de S
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 120 and ancho >= 70:
                    nota2m.fill = Color("Yellow")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "d":                                        #Colisión de D 
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 180 and ancho >= 130:
                    nota3m.fill = Color("Red")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "f":                                        #Colisión de F 
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 240 and ancho >= 190:
                    nota4m.fill = Color("Lime")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "h":                                        #Colisión de H        parte 2
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 610 and ancho >= 560:
                    nota5m.fill = Color("Lime")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "j":                                        #Colisión de J 
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 670 and ancho >= 620:
                    nota6m.fill = Color("Yellow")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "k":                                        #Colisión de K 
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 730 and ancho >= 680:
                    nota7m.fill = Color("Red")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
    if e.key == "l":                                        #Colisión de L 
        for n in listaNotas:
            ancho = n.x
            alto = n.y
            if alto <= y2 and alto >= y1:
                if ancho <= 790 and ancho >= 710:
                    nota8m.fill = Color("Blue")
                    ejecutarColision()
                    n.undraw()
                    listaNotas.remove(n)
                    
def verificarNotas():
    global juego, puntaje, puntajet
    for n in listaNotas:
        if n.y >= 630:
            puntaje -= 3
            puntajet.text = "Puntos de vida: " + str(puntaje)
            n.undraw()
            listaNotas.remove(n)
        if puntaje <= 0:
            juego = 0
            gameover = Text((400,300),"Game Over")
            gameover.color = Color("white")
            gameover.draw(v)
            guardarMarcador()
            #salirBtn.draw(v)

def crearNotas():
    if len(listaNotas)<100:
        azar = randint(tipoDeJuegoIzquierda,tipoDeJuegoDerecha)                                            #Modo de juego
        
        x = 0
        y = -25
        
        color = "White"
            
        if azar == 1:
            x = 34
            color = "Blue"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 2:
            x = 94
            color = "Yellow"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 3:
            x = 154
            color = "Red"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 4:
            x = 214
            color = "Lime"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 5:
            x = 584
            color = "Lime"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 6:
            x = 644
            color = "Yellow"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 7:
            x = 704
            color = "Red"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)
        if azar == 8:
            x = 764
            color = "Blue"
            n = Circle((x,y),25)
            n.fill = Color(color)
            n.draw(v)
            listaNotas.append(n)

def main():
    global gravedad
    piso = RoundedRectangle((10,550),(790,580),10)
    piso.bodyType = "static"
    piso.fill = Color("White")
    piso.draw(v)
    
    puntajet.draw(v)
    scoret.draw(v)
    highScore.draw(v)
    dibujarRieles()
    dibujarNotasm()
    dibujarLetras()
    
    tiempo = 0
    LIMITE = 1
    
    while juego == 1:
        v.step(0.034)
        tiempo += 0.1
        verificarNotas()
        onKeyPress(atenderTeclado)
        if tiempo>= LIMITE:
            tiempo = 0
            LIMITE -= 0.002                                         #Velocidad de oleada
            crearNotas()
            gravedad += .5
            v.gravity = Vector (0,gravedad)
            nota5m.fill = Color("Grey")
            nota6m.fill = Color("Grey")
            nota7m.fill = Color("Grey")
            nota8m.fill = Color("Grey")
            nota1m.fill = Color("Grey")
            nota2m.fill = Color("Grey")
            nota3m.fill = Color("Grey")
            nota4m.fill = Color("Grey")
            if LIMITE <= 0.990:
                titulo.bodyType = "static"
                puntajet.bodyType = "static"
                
v.run(main)