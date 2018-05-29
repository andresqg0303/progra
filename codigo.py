"""_______________________________________________________________________________________________________________________________
____________________________________________________PONG__________________________________________________________________________
__________________________________________________________________________________________________________________________________"""
#Importes
import pygame
import time
from tkinter import *

#________________________________________________________________________________________________________________________________
#_______________________________________________TABLERO__________________________________________________________________________

        # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
Matriz= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

""" Forma en la que se ve la matriz. Es una matriz binaria en la que los 0's en el juego se ven reflejados en la interfaz como
color azul, los unos en la columna 0 y la columna 39 se colocan como cuadros blancos y en el resto de posiciones si tienen un
uno se vulve una bola"""

""" ______________________________________________________________________________________________________________________________
_________________________________________________________CLASES___________________________________________________________________
__________________________________________________________________________________________________________________________________"""

"""Juego"""
# Atributos:
# nivel: int
# matriz: tuple
# score1: int
# score2: int
# barras: int
# Jugadores (PVP o PVC): boolean
# tamanoMatriz: list

# Metodos:
# get_nivel()
# set_score1()
# set_score2()
# get_score1()
# get_score2()
# restart_Score()
# restartGameAux()
# set_player()
# get_player()
# get_score()
# get_barras()
# set_barras()
# get_win1()
# get_win2()
# winner()
# game_over()
# creaMatriz()

class Juego:
    def __init__(self,matriz=Matriz,nivel=1,PVC=True,barras=1,score1=0,score2=0,tamanoMatriz=(25,40)):
        self.matriz = matriz
        self.tamanoMatriz= tamanoMatriz
        self.nivel = nivel
        self.PVC = PVC
        self.barras = barras
        self.score1 = score1
        self.score2 = score2
        self.win1 = 0
        self.win2 = 0
    def show(self):
        mostrar= ""
        for i in range(self.tamanoMatriz[0]):
            mostrar += "    "
            for j in range(self.tamanoMatriz[1]):
                Posi = self.matriz[i][j]
                if type(Posi) != type(0):
                    mostrar += str(Posi) + "    "
                    continue
                mostrar += str(Posi) + "    "
            mostrar += "\n"
        return mostrar
    def get_nivel(self): #Retorna el nivel en el que se está
        return self.nivel
    def set_score1(self): #Aumenta en 1 el score 1
        self.score1 += 1
    def set_score2(self): #Aumenta en 1 el score 2
        self.score2 +=1
    def restart_Score(self): #Reinicia las puntuaciones a 0
        self.score1 = 0
        self.score2 = 0
    def restartGameAux(self): #Reinicia las puntuaciones y la cantidad de niveles ganados a 0
        self.score1 = 0
        self.score2 = 0
        self.win1 = 0
        self.win2 = 0
    def set_barras(self,Cantidad): #Define la cantidad de barras, ya sea 1 o 2
        self.barras= Cantidad
    def get_barras(self): #Retorna la cantidad de barras en el juego
        return self.barras
    def set_player(self,modo): #Define si se juega contra otro jugador o contra la maquina
        self.PVC = modo
    def get_player(self): # Retorna si es Player vs Player o Player vs CPU
        return self.PVC
    def get_score1(self): # Retorna el score 1
        return self.score1
    def get_score2(self):# Retorna el score 2
        return self.score2
    def get_win1(self):# Retorna la cantidad de veces que ha ganado el jugador 1
        return self.win1
    def get_win2(self):# Retorna la cantidad de veces que ha ganado el jugador 2 o el CPU
        return self.win2
    def creaMatriz(self): #Crea la matriz dependiendo del tamaño que uno defina
        self.matriz= []
        for i in range(0,self.tamanoMatriz[0],1):
            temp= []
            for n in range(0,self.tamanoMatriz[1],1):
                temp+= [0]
            self.matriz+= [temp]
    def winner(self): #Aumenta el nivel y la cantidad de veces ganadas de nivel en nivel
        if self.score1-1 >= self.score2 and self.score1 >= 7:
            self.win1 += 1
            self.nivel += 1
        elif self.score2-1 >= self.score1 and self.score2 >= 7:
            self.win2 += 1
            self.nivel += 1
    def game_over(self): #Retorna un string que dice quien ganó el juego
        if self.PVC== False:
            if self.nivel > 3 and self.win1 >= 2:
                return ("Player 1 won")
            elif self.nivel > 3 and self.win2 >= 2:
                return ("Player 2 won")
        if self.PVC== True:
            if self.nivel > 3 and self.win1 >= 2:
                return ("Player 1 won")
            elif self.nivel > 3 and self.win2 >= 2:
                return ("CPU won")
#_______________________________________________________________________________________________________________________

"""Barra"""
#Atributos:
# tamano: int
# posicion: list
#Metodos:
# GetPos()
# SetPos()
# GetTamano()
# SetTamano()
# moverBarra()
# SetTamano()
# colocarBarra()
# moverBarra()

class Barra:
    def __init__(self,tamano= 9,posicion=[8,0]):
        self.tamano = tamano
        self.posicion = posicion
    def GetPos(self): #Retorna la posicion superior de la barra
        return self.posicion
    def GetTamano(self): #Retorna el tamaño de la barra
        return self.tamano
    def SetTamano(self,Nuevo): #Define el tamaño de la barra
        for i in range(0,25,1): #Borra todos los ceros y define la nueva cantidad de unos
            for j in range(0,40,1):
                Matriz[i][j]= 0
        self.tamano = Nuevo
    def SetPos(self,nuevaPos_Lista_): #Define la posicion inicial
        self.posicion= nuevaPos_Lista_
    def colocarBarra(self): #Coloca los unos correspondientes a la barra en la matriz en la matriz
        for i in range(self.posicion[0], self.posicion[0]+self.tamano,1):
            j= self.posicion[1]
            Matriz[i][j]= 1
    def moverBarra(self,moverY): #Mueve el origen de la barra y en base a eso borra los unos y coloca los nuevos unos por el movimiento
        for i in range(self.posicion[0], self.posicion[0]+self.tamano,1):
            j= self.posicion[1]
            Matriz[i][j]= 0
        self.posicion[0] += moverY
        self.colocarBarra()
#_______________________________________________________________________________________________________________________
"""Bola"""
#Atributos:
# Tamano: tuple
# Posicion: lista
#Metodos:
# GetPos()
# GetTamano()
# colocar()
# Mover()
# posInicial()
class Bola:
    def __init__(self,tamano= (20,20),posicion=[12,20]):
        self.tamano = tamano
        self.posicion = posicion
    def GetPos(self): #Retorna la posicion de la bola en la matriz
        return self.posicion
    def GetTamano(self): # Retorna el tamaño de la matriz
        return self.tamano
    def posInicial(self): #Regresa la bola a la posicion inicial
        Matriz[self.posicion[0]][self.posicion[1]] = 0
        self.posicion= [12,20]
    def colocar(self): #Coloca el 1 que representa la bola en la matriz
        Matriz[self.posicion[0]][self.posicion[1]] = 1
    def Mover(self,MoverX,MoverY): #Convierte el anterior uno en la matriz a un cero y luego cambia la posicion
        Matriz[self.posicion[0]][self.posicion[1]] = 0
        self.posicion[1] += MoverX
        self.posicion[0] += MoverY
        self.colocar() #y coloca un uno en la nueva posicion
#_______________________________________________________________________________________________________________________
"""Trampolines"""
#Atributos:
# tamano: int
# posicion: list
#Metodos:
# GetPos()
# SetPos()
# GetTamano()
# SetTamano()
# colocarTramp()

class Trampolin:
    def __init__(self,tamano= 3,posicion=[8,0]):
        self.tamano = tamano
        self.posicion = posicion
    def GetPos(self): #Retorna la posicion superior del trampolin
        return self.posicion
    def GetTamano(self): #Retorna el tamaño del trampolin
        return self.tamano
    def SetTamano(self,Nuevo): #Define el tamaño del trampolin
        for i in range(0,25,1): #Borra todos los ceros y define la nueva cantidad de unos
            for j in range(0,40,1):
                Matriz[i][j]= 0
        self.tamano = Nuevo
    def SetPos(self,nuevaPos_Lista_): #Define la posicion inicial
        self.posicion= nuevaPos_Lista_
    def colocarTramp(self): #Coloca los unos correspondientes a los trampolines en la matriz en la matriz
        for i in range(self.posicion[0], self.posicion[0]+self.tamano,1):
            j= self.posicion[1]
            Matriz[i][j]= 1
    def borraTramp(self):
        for i in range(self.posicion[0],self.posicion[0] + self.tamano + 1, 1): #Borra todos los ceros y define la nueva cantidad de unos
            Matriz[i][self.posicion[1]]= 0
"""_____________________________________________________________________________________________________________________
_______________________________________________Código de Juego__________________________________________________________
________________________________________________________________________________________________________________________"""
pygame.init() #Inicia pygame
#Variables______________________________________________________________________________________________________________
fps= pygame.time.Clock() #Reloj interno del juego
Game = Juego() #Define la instancia del juego
#Variables que activan pantallas
Inicio= True
Inicio2= False
Mode= False
Mode2= False
Mode3= False
Winner= False
practica1 = True
#Instancias de las paletas
Paleta1= Barra()
Paleta2= Barra(posicion= [8,39])
Paleta3= Barra(posicion= [])
Paleta4= Barra(posicion= [])
#Instancia de la bola
Balon= Bola()
#Instancias de los Trampolines
"""#Nivel 1
Tramp1= Trampolin(posicion=[6,19])
Tramp2= Trampolin(posicion=[16,19])
#Nivel 2
Tramp3= Trampolin(posicion=[4,22])
Tramp4= Trampolin(posicion=[11,18])
Tramp5= Trampolin(posicion=[19, 22])
#Nivel 3
Tramp6= Trampolin(posicion=[3,18])
Tramp7= Trampolin(posicion=[8,22])
Tramp8= Trampolin(posicion=[14,18])
Tramp9= Trampolin(posicion=[20,22])"""

#Nivel 1
Tramp1= Trampolin(posicion=[5,19],tamano=4)
Tramp2= Trampolin(posicion=[16,19],tamano=4)
#Nivel 2
Tramp3= Trampolin(posicion=[4,19])
Tramp4= Trampolin(posicion=[11,19])
Tramp5= Trampolin(posicion=[19,19])
#Nivel 3
Tramp6= Trampolin(posicion=[3,19])
Tramp7= Trampolin(posicion=[8,19])
Tramp8= Trampolin(posicion=[14,19])
Tramp9= Trampolin(posicion=[20,19])

Trampolines= [[Tramp1,Tramp2],[Tramp3,Tramp4,Tramp5],[Tramp6,Tramp7,Tramp8,Tramp9]]

#Vectores de movimiento de la bola
VectorBolax= -1
VectorBolay= -1
#Activación de los niveles
Nivel1= True
Nivel2= False
Nivel3= False
#Movimiento de la barra controlada por la máquina
CPU= 1

#Música de fondo del menú

#Tamaño de Pantalla
Width= 800
Height= 500

#Pantalla
root= pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pong")#Titulo de la pantalla


#Colores________________________________________________________________________________________________________________
Black= (0, 0, 0)
White= (255, 255, 255)
Grey= (130, 130, 130)
LightGrey= (200,200,200)
Blue= (29, 49, 86)
LightBlue=  (130, 159, 255)
Orange= (255, 139, 54)
Red= (174, 24, 24)
Green= (2, 184, 5)
Yellow= (250, 195, 15)
#_______________________________________________________________________________________________________________________
#Hace repeticion de teclas lo que permite repeticion continua de teclas
pygame.key.set_repeat(1,30)

#Imagenes para fondos
Menu= pygame.image.load("Menu.jpg")
End= pygame.image.load("GameOver.jpg")
Fondo= pygame.image.load("Fondo.jpg")

def muestreMatriz():
    ventana= Tk()
    ventana.title("Matriz")
    ventana.minsize(734, 395)
    ventana.maxsize(734, 395)
    ventana.resizable(width= NO, height= NO)
    Cv= Canvas(ventana, width= 800, height= 600, bg="#203864" )
    Cv.place(x=-2,y=-1)
    Matrix= Label(Cv, text= Game.show(), bg="#203864", fg= "white")
    Matrix.place(x=0,y=2)
    ventana.mainloop()
def ObjetosTexto(text, font): #Renderiza los textos con el color y su fuente
    SuperficieTexto = font.render(text, True, White)
    return SuperficieTexto, SuperficieTexto.get_rect()
def Boton(msg,x,y,w,h,ic,ac,command= None): #Define Botones
    global Inicio
    global Mode
    global Winner
    global Mode2
    global Mode3
    mouse = pygame.mouse.get_pos() #Me informa la posicion del mouse
    click= pygame.mouse.get_pressed() #Dice si algo se clicó
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #Comprueba que la posicion del mouse este dentro del boton
        pygame.draw.rect(root, ac,(x,y,w,h))
        #Estas siguientes lineas definen las distintas acciones dependiendo del boton
        if click[0] == 1 and command == "PVC":
            Game.set_player(True)
            Inicio = False
            time.sleep(0.2)
            Mode = True
            Modo()
        elif click[0] == 1 and command == "PVP":
            Game.set_player(False)
            Inicio = False
            time.sleep(0.2)
            Mode = True
            Modo()
        elif click[0] == 1 and command == "Pract":
            Inicio = False
            time.sleep(0.2)
            Mode2 = True
            Modo2()
        elif click[0] == 1 and command == "1PA":
            Game.set_barras(1)
            Mode = False
            Mode3 = True
            time.sleep(0.2)
            selectTrampolin()
        elif click[0] == 1 and command == "2PA":
            Game.set_barras(2)
            Mode = False
            Mode3= True
            time.sleep(0.2)
            selectTrampolin()
        elif click[0] == 1 and command == "Trampolin":
            Mode3 = False
            LoopObstaculos()
        elif click[0] == 1 and command == "Normal":
            Mode3 = False
            mainloop()
        elif click[0] == 1 and command == "1PA1":
            Game.set_barras(1)
            Mode2 = False
            modop()
        elif click[0] == 1 and command == "2PA1":
            Game.set_barras(2)
            Mode2 = False
            modop()
        elif click[0] == 1 and command == "Restart":
            Winner = False
            Game.restartGameAux()
            Inicio= True
            mainMenu()
        elif click[0] == 1 and command == "Pause":
            muestreMatriz()
        elif click[0] == 1 and command == "Quit":
            Winner = False
            pygame.quit()
            quit()
    else: #Coloca los botones con un color de no activo y coloca el texto a cada boton
        pygame.draw.rect(root, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = ObjetosTexto(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    root.blit(textSurf, textRect)
def VisualObjetos(): #Dinuja en la pantalla los ceros de la matriz ya sea como barras o la bola
    for i in range(0,len(Matriz),1):
        for j in range(0,len(Matriz[0]),1):
            if Matriz[i][j]==1:
                if j== 0 or j== 39:
                    pygame.draw.rect(root,White,(j*20,i*20,20,20))
                if 0<j<39 and Balon.GetPos() == [i,j]:
                    pygame.draw.circle(root,White,(j*20,i*20),15,15)
                if 0<j<39 and Balon.GetPos() != [i,j]:
                    pygame.draw.rect(root, LightBlue, (j * 20, i * 20, 20, 20))
def Puntuaciones(texto,lado): #Muestra las puntuaciones en la pantalla y recibe el texto y un numero que define el lado
    smallText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = ObjetosTexto(texto, smallText)
    TextRect.center = ((Height/10)*lado,(Width/20))
    root.blit(TextSurf, TextRect)
    pygame.display.update()
def Mensajes(texto): #Recibe un texto y lo convierte en un mensaje en pantalla
    smallText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = ObjetosTexto(texto, smallText)
    TextRect.center = ((400),(300))
    root.blit(TextSurf, TextRect)
    pygame.display.update()
def MoverBola(Velocidad):#Mueve la bola segun los vectores y recibe un argumento de velocidad que es la cantidad de tiempo que duerme
    Balon.Mover(VectorBolax, VectorBolay)#la funcion
    time.sleep(Velocidad)
def ColPract():    #Colisión en paredes para el modo práctica
    global VectorBolay
    global VectorBolax
    Posicion= Balon.GetPos()
    PosPa1= Paleta1.GetPos()
    PosPa3 = Paleta3.GetPos()
    if Posicion[0] == 0: #Si toca en el techo invierte el desplazamiento
        VectorBolay *= -1
    elif Posicion[0] == 24: #Si toca el suelo invierte el desplazamiento
        VectorBolay *= -1
    elif Posicion[1] == 39:
        VectorBolax *=-1
    elif Posicion[1]==0:
        Balon.posInicial()
        VectorBolax *= -1
        VectorBolay *= -1
def Colision(): #Define las coliciones con las distintas paredes
    global VectorBolay
    global VectorBolax
    Posicion= Balon.GetPos()
    PosPa1= Paleta1.GetPos()
    PosPa2 = Paleta2.GetPos()
    PosPa3 = Paleta3.GetPos()
    PosPa4 = Paleta4.GetPos()
    if Posicion[0] == 0: #Si toca en el techo invierte el desplazamiento
        VectorBolay *= -1
    elif Posicion[0] == 24: #Si toca el suelo invierte el desplazamiento
        VectorBolay *= -1
def ColPal2():  #Colisión paletas para modo práctica
    global VectorBolay
    global VectorBolax
    Posicion= Balon.GetPos()
    PosPa1= Paleta1.GetPos()
    PosPa3 = Paleta3.GetPos()
    if Game.get_barras() == 1:# Si la cantidad de paletas es 1
        #PALETA 1_____________________________________________________________
        #Define las coliciones con la paleta, ya sea que choque en la parte superior de la paleta, la del medio o la inferior
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano()/3 > Posicion[0] >= PosPa1[0]:
            VectorBolax = 1
            VectorBolay = -1
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+(Paleta1.GetTamano()*2)/3 > Posicion[0] >= PosPa1[0]+Paleta1.GetTamano()/3:
            VectorBolax = 1
            VectorBolay = 0
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano() > Posicion[0] >= PosPa1[0]+(Paleta1.GetTamano()*2)/3:
            VectorBolax= 1
            VectorBolay= 1
    if Game.get_barras() == 2: #Si hay 2 paletas por lado
        #PALETA 1______________________________________________________________
        # Define las coliciones con la paleta, ya sea que choque en la parte superior de la paleta, la del medio o la inferior
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano()/3 > Posicion[0] >= PosPa1[0]:
            VectorBolax = 1
            VectorBolay = -1
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+(Paleta1.GetTamano()*2)/3 > Posicion[0] >= PosPa1[0]+Paleta1.GetTamano()/3:
            VectorBolax = 1
            VectorBolay = 0
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano() > Posicion[0] >= PosPa1[0]+(Paleta1.GetTamano()*2)/3:
            VectorBolax= 1
            VectorBolay= 1
        #PALETA 3_____________________________________________________________________________________________
        if Posicion[1] == PosPa3[1]+1 and PosPa3[0]+Paleta3.GetTamano()/3 > Posicion[0] >= PosPa3[0]:
            VectorBolax = 1
            VectorBolay = -1
        if Posicion[1] == PosPa3[1]+1 and PosPa3[0]+(Paleta3.GetTamano()*2)/3 > Posicion[0] >= PosPa3[0]+Paleta3.GetTamano()/3:
            VectorBolax = 1
            VectorBolay = 0
        if Posicion[1] == PosPa3[1]+1 and PosPa3[0]+Paleta3.GetTamano() > Posicion[0] >= PosPa3[0]+(Paleta3.GetTamano()*2)/3:
            VectorBolax= 1
            VectorBolay= 1
def ColPal():   #Define la colisión con las paletas
    global VectorBolay
    global VectorBolax
    Posicion= Balon.GetPos()
    PosPa1= Paleta1.GetPos()
    PosPa2 = Paleta2.GetPos()
    PosPa3 = Paleta3.GetPos()
    PosPa4 = Paleta4.GetPos()
    if Game.get_barras() == 1:# Si la cantidad de paletas es 1
        #PALETA 1_____________________________________________________________
        #Define las coliciones con la paleta, ya sea que choque en la parte superior de la paleta, la del medio o la inferior
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano()/3 > Posicion[0] >= PosPa1[0]:
            VectorBolax = 1
            VectorBolay = -1
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+(Paleta1.GetTamano()*2)/3 > Posicion[0] >= PosPa1[0]+Paleta1.GetTamano()/3:
            VectorBolax = 1
            VectorBolay = 0
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano() > Posicion[0] >= PosPa1[0]+(Paleta1.GetTamano()*2)/3:
            VectorBolax= 1
            VectorBolay= 1
        #PALETA 2_____________________________________________________________
        if Posicion[1] == PosPa2[1]-1 and PosPa2[0]+Paleta2.GetTamano()/3 > Posicion[0] >= PosPa2[0]:
            VectorBolax = -1
            VectorBolay = -1
        if Posicion[1] == PosPa2[1]-1 and PosPa2[0]+(Paleta2.GetTamano()*2)/3 > Posicion[0] >= PosPa2[0]+Paleta2.GetTamano()/3:
            VectorBolax = -1
            VectorBolay = 0
        if Posicion[1] == PosPa2[1]-1 and PosPa2[0]+Paleta2.GetTamano() > Posicion[0] >= PosPa2[0]+(Paleta2.GetTamano()*2)/3:
            VectorBolax= -1
            VectorBolay= 1
    if Game.get_barras() == 2: #Si hay 2 paletas por lado
        #PALETA 1______________________________________________________________
        # Define las coliciones con la paleta, ya sea que choque en la parte superior de la paleta, la del medio o la inferior
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano()/3 > Posicion[0] >= PosPa1[0]:
            VectorBolax = 1
            VectorBolay = -1
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+(Paleta1.GetTamano()*2)/3 > Posicion[0] >= PosPa1[0]+Paleta1.GetTamano()/3:
            VectorBolax = 1
            VectorBolay = 0
        if Posicion[1] == PosPa1[1]+1 and PosPa1[0]+Paleta1.GetTamano() > Posicion[0] >= PosPa1[0]+(Paleta1.GetTamano()*2)/3:
            VectorBolax= 1
            VectorBolay= 1
        #PALETA 2_____________________________________________________________
        if Posicion[1] == PosPa2[1]-1 and PosPa2[0]+Paleta2.GetTamano()/3 > Posicion[0] >= PosPa2[0]:
            VectorBolax = -1
            VectorBolay = -1
        if Posicion[1] == PosPa2[1]-1 and PosPa2[0]+(Paleta2.GetTamano()*2)/3 > Posicion[0] >= PosPa2[0]+Paleta2.GetTamano()/3:
            VectorBolax = -1
            VectorBolay = 0
        if Posicion[1] == PosPa2[1]-1 and PosPa2[0]+Paleta2.GetTamano() > Posicion[0] >= PosPa2[0]+(Paleta2.GetTamano()*2)/3:
            VectorBolax= -1
            VectorBolay= 1
        #PALETA 3_____________________________________________________________________________________________
        if Posicion[1] == PosPa3[1]+1 and PosPa3[0]+Paleta3.GetTamano()/3 > Posicion[0] >= PosPa3[0]:
            VectorBolax = 1
            VectorBolay = -1
        if Posicion[1] == PosPa3[1]+1 and PosPa3[0]+(Paleta3.GetTamano()*2)/3 > Posicion[0] >= PosPa3[0]+Paleta3.GetTamano()/3:
            VectorBolax = 1
            VectorBolay = 0
        if Posicion[1] == PosPa3[1]+1 and PosPa3[0]+Paleta3.GetTamano() > Posicion[0] >= PosPa3[0]+(Paleta3.GetTamano()*2)/3:
            VectorBolax= 1
            VectorBolay= 1
        #PALETA 4_____________________________________________________________
        if Posicion[1] == PosPa4[1]-1 and PosPa4[0]+Paleta4.GetTamano()/3 > Posicion[0] >= PosPa4[0]:
            VectorBolax = -1
            VectorBolay = -1
        if Posicion[1] == PosPa4[1]-1 and PosPa4[0]+(Paleta4.GetTamano()*2)/3 > Posicion[0] >= PosPa4[0]+Paleta4.GetTamano()/3:
            VectorBolax = -1
            VectorBolay = 0
        if Posicion[1] == PosPa4[1]-1 and PosPa4[0]+Paleta4.GetTamano() > Posicion[0] >= PosPa4[0]+(Paleta4.GetTamano()*2)/3:
            VectorBolax= -1
            VectorBolay= 1
def ColTramp():
    global VectorBolay
    global VectorBolax
    Pos= Balon.GetPos()
    if Game.get_nivel() == 1:
        #Tramp1__________________________________________________________________________________________________
        if Pos[1]== Tramp1.GetPos()[1] - 1 and Tramp1.GetPos()[0]-1<Pos[0]< Tramp1.GetPos()[0]+Tramp1.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp1.GetPos()[1] + 1 and Tramp1.GetPos()[0]-1<Pos[0]< Tramp1.GetPos()[0]+Tramp1.GetTamano()+1:
            VectorBolax = 1
        #Tramp2__________________________________________________________________________________________________
        if Pos[1]== Tramp2.GetPos()[1] - 1 and Tramp2.GetPos()[0]-1<Pos[0]< Tramp2.GetPos()[0]+Tramp2.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp2.GetPos()[1] + 1 and Tramp2.GetPos()[0]-1<Pos[0]< Tramp2.GetPos()[0]+Tramp2.GetTamano()+1:
            VectorBolax = 1
    if Game.get_nivel() == 2:
        #Tramp3__________________________________________________________________________________________________
        if Pos[1]== Tramp3.GetPos()[1] - 1 and Tramp3.GetPos()[0]-1<Pos[0]< Tramp3.GetPos()[0]+Tramp3.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp3.GetPos()[1] + 1 and Tramp3.GetPos()[0]-1<Pos[0]< Tramp3.GetPos()[0]+Tramp3.GetTamano()+1:
            VectorBolax = 1
        #Tramp4__________________________________________________________________________________________________
        if Pos[1]== Tramp4.GetPos()[1] - 1 and Tramp4.GetPos()[0]-1<Pos[0]< Tramp4.GetPos()[0]+Tramp4.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp4.GetPos()[1] + 1 and Tramp4.GetPos()[0]-1<Pos[0]< Tramp4.GetPos()[0]+Tramp4.GetTamano()+1:
            VectorBolax = 1
        # Tramp5__________________________________________________________________________________________________
        if Pos[1]== Tramp5.GetPos()[1] - 1 and Tramp5.GetPos()[0]-1<Pos[0]< Tramp5.GetPos()[0]+Tramp5.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp5.GetPos()[1] + 1 and Tramp5.GetPos()[0]-1<Pos[0]< Tramp5.GetPos()[0]+Tramp5.GetTamano()+1:
            VectorBolax = 1
    if Game.get_nivel() == 3:
        # Tramp6__________________________________________________________________________________________________
        if Pos[1]== Tramp6.GetPos()[1] - 1 and Tramp6.GetPos()[0]-1<Pos[0]< Tramp6.GetPos()[0]+Tramp6.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp6.GetPos()[1] + 1 and Tramp6.GetPos()[0]-1<Pos[0]< Tramp6.GetPos()[0]+Tramp6.GetTamano()+1:
            VectorBolax = 1
        # Tramp7__________________________________________________________________________________________________
        if Pos[1]== Tramp7.GetPos()[1] - 1 and Tramp7.GetPos()[0]-1<Pos[0]< Tramp7.GetPos()[0]+Tramp7.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp7.GetPos()[1] + 1 and Tramp7.GetPos()[0]-1<Pos[0]< Tramp7.GetPos()[0]+Tramp7.GetTamano()+1:
            VectorBolax = 1
        # Tramp8__________________________________________________________________________________________________
        if Pos[1]== Tramp8.GetPos()[1] - 1 and Tramp8.GetPos()[0]-1<Pos[0]< Tramp8.GetPos()[0]+Tramp8.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp8.GetPos()[1] + 1 and Tramp8.GetPos()[0]-1<Pos[0]< Tramp8.GetPos()[0]+Tramp8.GetTamano()+1:
            VectorBolax = 1
        # Tramp9__________________________________________________________________________________________________
        if Pos[1]== Tramp9.GetPos()[1] - 1 and Tramp9.GetPos()[0]-1<Pos[0]< Tramp9.GetPos()[0]+Tramp9.GetTamano()+1:
            VectorBolax = -1
        if Pos[1]== Tramp9.GetPos()[1] + 1 and Tramp9.GetPos()[0]-1<Pos[0]< Tramp9.GetPos()[0]+Tramp9.GetTamano()+1:
            VectorBolax = 1
def Puntuacion(): #Suma las puntuaciones a cada lado y regresa la bola al centro usando los metodos de las clases
    global VectorBolax
    global VectorBolay
    Posicion = Balon.GetPos()
    if Posicion[1]==0:
        Balon.posInicial()
        Game.set_score2()
        VectorBolax *= -1
        VectorBolay *= -1
    if Posicion[1]==39:
        Balon.posInicial()
        Game.set_score1()
        VectorBolax *= -1
        VectorBolay *= -1
    Puntuaciones(str(Game.get_score1()),7)
    Puntuaciones(str(Game.get_score2()),9)
def Win(): #Aumenta cada nivel y al final dice quien ganó la partida
    global Nivel1
    global Nivel2
    global Nivel3
    global Winner
    if Game.get_nivel()==2:
        Nivel1= False
        Nivel2= True
        Nivel3= False
    if Game.get_nivel()==3:
        Nivel1= False
        Nivel2= False
        Nivel3= True
    if Game.get_nivel()==4:
        Nivel1= False
        Nivel2= False
        Nivel3= False
        Winner= True
        GameOver()
def mainMenu():
    while Inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton1 = Boton("2 Players", 355, 280, 100, 50, LightGrey, Grey, "PVP")
        Boton2 = Boton("1 Player", 355, 210, 100, 50, LightGrey, Grey, "PVC")
        Boton5 = Boton("Training",355,350,100,50, LightGrey, Grey,"Pract")
        pygame.display.update()
        fps.tick(60)
def Modo(): #Crea pantalla para escoger 1 jugador o dos jugadores
    while Mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton3 = Boton("2 Paletas", 355, 310, 100, 50, LightGrey, Grey, "2PA")
        Boton4 = Boton("1 Paleta", 355, 240, 100, 50, LightGrey, Grey, "1PA")
        pygame.display.update()
        fps.tick(60)
def Modo2():
    while Mode2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton6 = Boton("2 Paletas", 355, 310, 100, 50, LightGrey, Grey, "2PA1")
        Boton7 = Boton("1 Paleta", 355, 240, 100, 50, LightGrey, Grey, "1PA1")
        pygame.display.update()
        fps.tick(60)
def selectTrampolin():
    while Mode3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton8 = Boton("Simple", 355, 240, 100, 50, LightGrey, Grey, "Normal")
        Boton9 = Boton("Trampolines", 345, 310, 120, 50, LightGrey, Grey, "Trampolin")
        pygame.display.update()
        fps.tick(60)
def GameOver(): #Crea una pantalla que indica el final del juego y tiene un boton de reiniciar y uno de cerrar el juego
    while Winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(End, (0, 0))
        Mensajes(Game.game_over())
        #Boton(msg,x,y,w,h,ic,ac)
        Boton1 = Boton("Restart", 100, 400, 100, 50, LightGrey, Grey, "Restart")
        Boton2 = Boton("Quit", 600, 400, 100, 50, LightGrey, Grey, "Quit")
        pygame.display.update()
        fps.tick(60)
def nivel(Nivel): #Crea una pantalla cada vez que se inicia un nivel indicando cual es
    root.fill(Blue)
    Mensajes("Nivel "+str(Nivel))
    pygame.display.update()
    fps.tick(60)
    time.sleep(2)
def MovimientoCPU(Velocidad): #Define el movimiento de la computadora al jugar en modo 1 jugador y mientras menor sea el argumento
    #Velocidad mayor será la velocidad de la barra
    if Game.get_barras()== 1:
        if Balon.GetPos()[1] >= 30:
            if Balon.GetPos()[0] < Paleta2.GetPos()[0]:
                if Paleta2.GetPos()[0] > 0:
                    Paleta2.moverBarra(-1)
                    time.sleep(Velocidad)
            elif Balon.GetPos()[0] > Paleta2.GetPos()[0] + Paleta2.GetTamano()-1:
                if Paleta2.GetPos()[0] + Paleta2.GetTamano() < 24:
                    Paleta2.moverBarra(1)
                    time.sleep(Velocidad)
    elif Game.get_barras() == 2:
        if Balon.GetPos()[1] >= 30:
            if Balon.GetPos()[0] < Paleta2.GetPos()[0]:
                if Paleta2.GetPos()[0] > 0:
                    Paleta2.moverBarra(-1)
                    Paleta4.moverBarra(-1)
                    time.sleep(Velocidad)
            if Balon.GetPos()[0] > Paleta4.GetPos()[0] + Paleta4.GetTamano()-1:
                if Paleta4.GetPos()[0] + Paleta4.GetTamano() < 24:
                    Paleta2.moverBarra(1)
                    Paleta4.moverBarra(1)
                    time.sleep(Velocidad)

def modop():#Modo Práctica
    global practica1
    pygame.mixer.music.stop() 
    if Game.get_barras() == 1:
        Paleta1.SetPos([8, 0])
    if Game.get_barras() == 2:
        Paleta1.SetPos([2, 0])
        Paleta3.SetPos([14, 0])
    while practica1:
        if Game.get_barras() == 1:
            Paleta1.colocarBarra()
            MoverBola(0.04)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    Paleta1.SetPos([8,0])
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0 : 
                         Paleta1.moverBarra(-1)
                    elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20): 
                         Paleta1.moverBarra(1)
            root.blit(Fondo, (0, 0)) 
            VisualObjetos()
            Boton1 = Boton("Volver", 680, 10, 90, 30, LightGrey, Grey, "Restart")
            Pausa = Boton("Inspector", 680, 440, 100, 30, LightGrey, Grey, "Pause")
            pygame.display.update()
            fps.tick(60) 
            ColPract()
            ColPal2()
        elif Game.get_barras() == 2: 
            MoverBola(0.04)
            Paleta1.colocarBarra()
            Paleta3.colocarBarra()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Paleta1.SetPos([8, 0])
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                        Paleta1.moverBarra(-1)
                        Paleta3.moverBarra(-1)
                    elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                        Paleta1.moverBarra(1)
                        Paleta3.moverBarra(1)
            root.blit(Fondo, (0, 0))
            VisualObjetos()
            Boton1 = Boton("Volver", 680, 10, 90, 30, LightGrey, Grey, "Restart")
            Pausa = Boton("Inspector", 680, 440, 100, 30, LightGrey, Grey, "Pause")
            pygame.display.update() 
            fps.tick(60) 
            ColPract()
            ColPal2()

def mainloop(): #Loop principal que maneja la mayoria del juego
    global Winner
    global Nivel1
    global Nivel2
    global Nivel3
    global CPU
    while not Winner:
        #Para la música al salirse del menú
        #Estos dos if definen las posiciones de las paletas
        if Game.get_barras() == 1 and Game.get_nivel() == 1:
            Paleta1.SetPos([8, 0])
            Paleta2.SetPos([8, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 1:
            Paleta1.SetPos([2, 0])
            Paleta2.SetPos([2, 39])
            Paleta3.SetPos([14, 0])
            Paleta4.SetPos([14, 39])
        Game.restart_Score() #Hace las puntuaciones 0
        nivel(1)#Muestra la pantalla de nivel 1
        while Nivel1: #Nivel 1
            if Game.get_barras() == 1: #Si es con una sola paleta
                Puntuacion()
                MoverBola(0.04)
                #Se colocan ambas paletas
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                if Game.get_player() == True: #Si se juega contra la maquina se inicia la funcion de control de maquina
                    MovimientoCPU(0.055)
                for event in pygame.event.get():#Toma los eventos de teclas y mouse ademas de posicion de este
                    if event.type == pygame.QUIT: #Define la utilidad de la x en el juego
                        Paleta1.SetPos([8,0])
                        Paleta2.SetPos([8,39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN: #Detecta cuando se presiona una tecla
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0 : #Movimiento hacia arriba
                            #Impide que la barra salga de la pantalla
                            Paleta1.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20): #Movimiento hacia abajo
                            # Impide que la barra salga de la pantalla
                            Paleta1.moverBarra(1)
                        if Game.get_player() == False: #Si se juegan dos jugadores hace lo mismo que las lineas de arribas pero para la
                            #paleta 2
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                Game.winner() #Detecta los ganadores del nive1 1
                Colision()
                ColPal()
                root.blit(Fondo, (0, 0)) #Coloca el fondo
                VisualObjetos() #Muestra los objetos
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update() #Actualiza la página
                fps.tick(60) #Define la velocidad del reloj interno del juego
            elif Game.get_barras() == 2: #Es lo mismo que la parte superior excepto porque es con dos barras
                Puntuacion()
                MoverBola(0.04)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.06)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                            Paleta3.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                            Paleta3.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                                Paleta4.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta4.GetPos()[0] * 20 < Height - (Paleta4.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                                Paleta4.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
        Game.restart_Score() #Reinicia puntuacion para el nivel 2
        if Game.get_nivel()==2: #Define el tamaño de las paletas en el nivel 2
            Paleta1.SetTamano(6)
            Paleta2.SetTamano(6)
            Paleta3.SetTamano(6)
            Paleta4.SetTamano(6)
        if Game.get_barras() == 1 and Game.get_nivel() == 2: #Define las posiciones de las paletas si solo es una por lado
            Paleta1.SetPos([9, 0])
            Paleta2.SetPos([9, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 2: #Define las posiciones de las paletas si son dos por lado
            Paleta1.SetPos([3, 0])
            Paleta2.SetPos([3, 39])
            Paleta3.SetPos([14, 0])
            Paleta4.SetPos([14, 39])
        nivel(2) #Muestra la pantalla de nivel 2
        while Nivel2: #Hace lo mismo que el nivel uno solo que aumenta velocidades de las barras del CPU y velocidad de la bola
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.03)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.045)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8,0])
                        Paleta2.SetPos([8,39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0 :
                            Paleta1.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20):
                            Paleta1.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.035)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.05)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                            Paleta3.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                            Paleta3.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                                Paleta4.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta4.GetPos()[0] * 20 < Height - (Paleta4.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                                Paleta4.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
        Game.restart_Score()
        if Game.get_barras() == 1 and Game.get_nivel() == 3:#Define las posiciones de las paletas si solo es una por lado
            Paleta1.SetPos([11, 0])
            Paleta2.SetPos([11, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 3:#Define las posiciones de las paletas si son dos por lado
            Paleta1.SetPos([3, 0])
            Paleta2.SetPos([3, 39])
            Paleta3.SetPos([10, 0])
            Paleta4.SetPos([10, 39])
        if Game.get_nivel()==3: #Define el tamaño de las barras para el nivel 3
            Paleta1.SetTamano(3)
            Paleta2.SetTamano(3)
            Paleta3.SetTamano(3)
            Paleta4.SetTamano(3)
        nivel(3)
        while Nivel3: #Hace lo mismo que el nivel 2 solo que aumenta velocidades de las barras del CPU y velocidad de la bola
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.03)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.035)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8,0])
                        Paleta2.SetPos([8,39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20):
                            Paleta1.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.03)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.04)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                            Paleta3.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                            Paleta3.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                                Paleta4.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta4.GetPos()[0] * 20 < Height - (Paleta4.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                                Paleta4.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
def LoopObstaculos():
    global Winner
    global Nivel1
    global Nivel2
    global Nivel3
    global CPU
    while not Winner:
        # Para la música al salirse del menú
        # Estos dos if definen las posiciones de las paletas
        if Game.get_barras() == 1 and Game.get_nivel() == 1:
            Paleta1.SetPos([8, 0])
            Paleta2.SetPos([8, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 1:
            Paleta1.SetPos([2, 0])
            Paleta2.SetPos([2, 39])
            Paleta3.SetPos([14, 0])
            Paleta4.SetPos([14, 39])
        Tramp6.borraTramp()
        Tramp7.borraTramp()
        Tramp8.borraTramp()
        Tramp9.borraTramp()
        Game.restart_Score()  # Hace las puntuaciones 0
        nivel(1)  # Muestra la pantalla de nivel 1
        while Nivel1:  # Nivel 1
            Tramp1.colocarTramp()
            Tramp2.colocarTramp()
            if Game.get_barras() == 1:  # Si es con una sola paleta
                Puntuacion()
                MoverBola(0.04)
                # Se colocan ambas paletas
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                if Game.get_player() == True:  # Si se juega contra la maquina se inicia la funcion de control de maquina
                    MovimientoCPU(0.055)
                for event in pygame.event.get():  # Toma los eventos de teclas y mouse ademas de posicion de este
                    if event.type == pygame.QUIT:  # Define la utilidad de la x en el juego
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:  # Detecta cuando se presiona una tecla
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:  # Movimiento hacia arriba
                            # Impide que la barra salga de la pantalla
                            Paleta1.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0] * 20 < Height - (
                                Paleta1.GetTamano() * 20):  # Movimiento hacia abajo
                            # Impide que la barra salga de la pantalla
                            Paleta1.moverBarra(1)
                        if Game.get_player() == False:  # Si se juegan dos jugadores hace lo mismo que las lineas de arribas pero para la
                            # paleta 2
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height - (
                                    Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                Game.winner()  # Detecta los ganadores del nive1 1
                Colision()
                ColPal()
                ColTramp()
                root.blit(Fondo, (0, 0))  # Coloca el fondo
                VisualObjetos()  # Muestra los objetos
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()  # Actualiza la página
                fps.tick(60)  # Define la velocidad del reloj interno del juego
            elif Game.get_barras() == 2:  # Es lo mismo que la parte superior excepto porque es con dos barras
                Puntuacion()
                MoverBola(0.04)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.06)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                            Paleta3.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                            Paleta3.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                                Paleta4.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta4.GetPos()[0] * 20 < Height - (
                                    Paleta4.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                                Paleta4.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                ColTramp()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
        Game.restart_Score()  # Reinicia puntuacion para el nivel 2
        if Game.get_nivel() == 2:  # Define el tamaño de las paletas en el nivel 2
            Paleta1.SetTamano(6)
            Paleta2.SetTamano(6)
            Paleta3.SetTamano(6)
            Paleta4.SetTamano(6)
        if Game.get_barras() == 1 and Game.get_nivel() == 2:  # Define las posiciones de las paletas si solo es una por lado
            Paleta1.SetPos([9, 0])
            Paleta2.SetPos([9, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 2:  # Define las posiciones de las paletas si son dos por lado
            Paleta1.SetPos([3, 0])
            Paleta2.SetPos([3, 39])
            Paleta3.SetPos([14, 0])
            Paleta4.SetPos([14, 39])
        Tramp1.borraTramp()
        Tramp2.borraTramp()
        nivel(2)  # Muestra la pantalla de nivel 2
        while Nivel2:# Hace lo mismo que el nivel uno solo que aumenta velocidades de las barras del CPU y velocidad de la bola
            Tramp3.colocarTramp()
            Tramp4.colocarTramp()
            Tramp5.colocarTramp()
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.04)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.045)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0] * 20 < Height - (Paleta1.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height - (
                                    Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                ColTramp()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.04)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.05)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                            Paleta3.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                            Paleta3.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                                Paleta4.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta4.GetPos()[0] * 20 < Height - (
                                    Paleta4.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                                Paleta4.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                ColTramp()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
        Game.restart_Score()
        if Game.get_barras() == 1 and Game.get_nivel() == 3:  # Define las posiciones de las paletas si solo es una por lado
            Paleta1.SetPos([11, 0])
            Paleta2.SetPos([11, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 3:  # Define las posiciones de las paletas si son dos por lado
            Paleta1.SetPos([3, 0])
            Paleta2.SetPos([3, 39])
            Paleta3.SetPos([10, 0])
            Paleta4.SetPos([10, 39])
        if Game.get_nivel() == 3:  # Define el tamaño de las barras para el nivel 3
            Paleta1.SetTamano(3)
            Paleta2.SetTamano(3)
            Paleta3.SetTamano(3)
            Paleta4.SetTamano(3)
        Tramp3.borraTramp()
        Tramp4.borraTramp()
        Tramp5.borraTramp()
        nivel(3)
        while Nivel3:  # Hace lo mismo que el nivel 2 solo que aumenta velocidades de las barras del CPU y velocidad de la bola
            Tramp6.colocarTramp()
            Tramp7.colocarTramp()
            Tramp8.colocarTramp()
            Tramp9.colocarTramp()
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.037)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.035)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0] * 20 < Height - (Paleta1.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height - (
                                    Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                ColTramp()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.037)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
                if Game.get_player() == True:
                    MovimientoCPU(0.04)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8, 0])
                        Paleta2.SetPos([8, 39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                            Paleta1.moverBarra(-1)
                            Paleta3.moverBarra(-1)
                        elif event.key == pygame.K_s and Paleta3.GetPos()[0] * 20 < Height - (Paleta3.GetTamano() * 20):
                            Paleta1.moverBarra(1)
                            Paleta3.moverBarra(1)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-1)
                                Paleta4.moverBarra(-1)
                            elif event.key == pygame.K_DOWN and Paleta4.GetPos()[0] * 20 < Height - (
                                    Paleta4.GetTamano() * 20):
                                Paleta2.moverBarra(1)
                                Paleta4.moverBarra(1)
                Game.winner()
                Colision()
                ColPal()
                ColTramp()
                root.blit(Fondo, (0, 0))
                VisualObjetos()
                Win()
                Pausa = Boton("Inspector", 600, 440, 95, 30, LightGrey, Grey, "Pause")
                pygame.display.update()
                fps.tick(60)

mainMenu() #Se corre el menu de inicio al correr el programa
