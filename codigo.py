"""_______________________________________________________________________________________________________________________________
____________________________________________________PONG__________________________________________________________________________
__________________________________________________________________________________________________________________________________"""
#Importes
import pygame
import random
import time
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

""" ______________________________________________________________________________________________________________________________
_________________________________________________________CLASES___________________________________________________________________
__________________________________________________________________________________________________________________________________"""

"""Juego"""
# Atributos:
# nivel: int
# matriz: tuple
# score1: int
# score2: int
# timer: int
# barras: int
# Jugadores (PVP o PVC): boolean
# tamanoMatriz: list

# Metodos:
# Start()
# Update()
# get_nivel()
# set_score1()
# set_nivel()
# set_score2()
# set_player()
# get_player()
# get_score()
# get_barras()
# set_barras()
# get_time()
# set_time()
# winner()
# game_over()
# cronometro()
# creaMatriz()

class Juego:
    win1= 0
    win2= 0
    def __init__(self,matriz=Matriz,nivel=1,PVC=True,barras=1,timer=0,score1=0,score2=0,tamanoMatriz=(25,40)):
        self.matriz = matriz
        self.tamanoMatriz= tamanoMatriz
        self.nivel = nivel
        self.PVC = PVC
        self.barras = barras
        self.timer = timer
        self.score1 = score1
        self.score2 = score2
    def start(self):
        for i in range(self.tamanoMatriz[0]):
            print(" ")
            for j in range(self.tamanoMatriz[1]):
                Posi = self.matriz[i][j]
                if type(Posi) != type(0):
                    print(Posi, " ", end="")
                    continue
                print (Posi, "  ", end="")
        print(" ")
    def get_nivel(self):
        return self.nivel
    def set_score1(self):
        self.score1 +=1
    def restart_Score(self):
        self.score1 = 0
        self.score2 = 0
    def set_score2(self):
        self.score2 +=1
    def get_matriz(self):
        return self.matriz
    def set_barras(self,Cantidad):
        self.barras= Cantidad
    def get_barras(self):
        return self.barras
    def set_player(self,modo):
        self.PVC = modo
    def get_player(self):
        return self.PVC
    def get_time(self):
        return self.timer
    def get_score1(self):
        return self.score1
    def get_score2(self):
        return self.score2
    def creaMatriz(self):
        self.matriz= []
        for i in range(0,self.tamanoMatriz[0],1):
            temp= []
            for n in range(0,self.tamanoMatriz[1],1):
                temp+= [0]
            self.matriz+= [temp]
    def getMatriz(self):
        return self.matriz
    def winner(self):
        if self.score1-2>=self.score2 and self.score1 >= 10:
            self.win1 += 1
            self.nivel += 1
        elif self.score2-2>=self.score1 and self.score2 >= 10:
            self.win2 += 1
            self.nivel += 1

    def game_over(self):
        if self.PVC== False:
            if self.nivel > 3 and self.win1 >= 2:
                return ("Player 1 won")
            elif self.nivel > 3 and self.win2 >= 2:
                return ("Player 2 won")
#_______________________________________________________________________________________________________________________

"""Barra"""
#Atributos:
# color: tuple
# tamano: int
# velocidad: int
# posicion: list
# origen: lista
#Metodos:
# GetPos()
# SetPos()
# GetSpeed()
# GetColor()
# GetTamano()
# moverBarra()
# SetTamano()
# colocarBarra()

class Barra:
    def __init__(self, color= (255,255,255),tamano= 9,velocidad= 7,posicion= [8,0]):
        self.color = color
        self.tamano = tamano
        self.velocidad = velocidad
        self.posicion = posicion
    def GetColor(self):
        return self.color
    def GetSpeed(self):
        return self.velocidad
    def GetPos(self):
        return self.posicion
    def GetTamano(self):
        return self.tamano
    def SetTamano(self,nuevo):
        for i in range(self.posicion[0], self.posicion[0]+self.tamano,1):
            j= self.posicion[1]
            Matriz[i][j]= 0
        self.tamano = nuevo
    def SetPos(self,nuevaPos_Lista_):
        self.posicion= nuevaPos_Lista_
    def colocarBarra(self):
        for i in range(self.posicion[0], self.posicion[0]+self.tamano,1):
            j= self.posicion[1]
            Matriz[i][j]= 1
    def moverBarra(self,moverY):
        for i in range(self.posicion[0], self.posicion[0]+self.tamano,1):
            j= self.posicion[1]
            Matriz[i][j]= 0
        self.posicion[0] += moverY
        self.colocarBarra()
#_______________________________________________________________________________________________________________________
"""Bola"""
#Atributos:
# Color: tuple
# Tamano: tuple
# Velocidad: int
# Posicion: lista
#Metodos:
# GetPos()
# GetSpeed()
# GerColor()
# GetTamano()
# colocar()
# Mover()
# posInicial()
class Bola:
    def __init__(self, color= (255,255,255),tamano= (20,20),velocidad= 3,posicion=[12,20]):
        self.color = color
        self.tamano = tamano
        self.velocidad = velocidad
        self.posicion = posicion
    def GetColor(self):
        return self.color
    def GetSpeed(self):
        return self.velocidad
    def GetPos(self):
        return self.posicion
    def GetTamano(self):
        return self.tamano
    def posInicial(self):
        Matriz[self.posicion[0]][self.posicion[1]] = 0
        self.posicion= [12,20]
    def colocar(self):
        Matriz[self.posicion[0]][self.posicion[1]] = 1
    def Mover(self,MoverX,MoverY):
        Matriz[self.posicion[0]][self.posicion[1]] = 0
        self.posicion[1] += MoverX
        self.posicion[0] += MoverY
        self.colocar()

"""_____________________________________________________________________________________________________________________
_______________________________________________Código de Juego__________________________________________________________
________________________________________________________________________________________________________________________"""
pygame.init()
#Variables______________________________________________________________________________________________________________
fps= pygame.time.Clock()
Game = Juego()
Inicio= True
Mode= False
Winner= False
Paleta1= Barra()
Paleta2= Barra(posicion= [8,39])
Paleta3= Barra(posicion= [])
Paleta4= Barra(posicion= [])
Balon= Bola()
VectorBolax= 1
VectorBolay= 1
Nivel1= True
Nivel2= False
Nivel3= False



#Tamaño de Pantalla
Width= 800
Height= 500

root= pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pong")

#Colores________________________________________________________________________________________________________________
Black= (0, 0, 0)
White= (255, 255, 255)
Grey= (130, 130, 130)
LightGrey= (200,200,200)
Blue= (29, 49, 86)
LightBlue=  (49, 69, 106)
Orange= (255, 139, 54)
Red= (174, 24, 24)
Green= (2, 184, 5)
Yellow= (250, 195, 15)
#_______________________________________________________________________________________________________________________

pygame.key.set_repeat(1,40)

Menu= pygame.image.load("Menu.jpg")

def ObjetosTexto(text, font):
    SuperficieTexto = font.render(text, True, White)
    return SuperficieTexto, SuperficieTexto.get_rect()
def Boton(msg,x,y,w,h,ic,ac,command= None):
    global Inicio
    global Mode
    mouse = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(root, ac,(x,y,w,h))
        if click[0] == 1 and command == "PVC":
            Game.set_player(True)
            Inicio= False
            time.sleep(0.1)
            Mode = True
            Modo()
        elif click[0] == 1 and command == "PVP":
            Game.set_player(False)
            Inicio = False
            time.sleep(0.1)
            Mode = True
            Modo()
        elif click[0] == 1 and command == "1PA":
            Game.set_barras(1)
            Mode = False
            mainloop()
        elif click[0] == 1 and command == "2PA":
            Game.set_barras(2)
            Mode = False
            mainloop()
    else:
        pygame.draw.rect(root, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = ObjetosTexto(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    root.blit(textSurf, textRect)
def VisualObjetos():
    for i in range(0,len(Matriz),1):
        for j in range(0,len(Matriz[0]),1):
            if Matriz[i][j]==1:
                if j== 0 or j== 39:
                    pygame.draw.rect(root,White,(j*20,i*20,20,20))
                if 0<j<39:
                    pygame.draw.circle(root,White,(j*20,i*20),15,15)
def Mensajes(texto,lado):
    smallText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = ObjetosTexto(texto, smallText)
    TextRect.center = ((Height/10)*lado,(Width/20))
    root.blit(TextSurf, TextRect)
    pygame.display.update()
def MoverBola(Velocidad):
    Balon.Mover(VectorBolax, VectorBolay)
    time.sleep(Velocidad)
def Colision():
    global VectorBolay
    global VectorBolax
    Posicion= Balon.GetPos()
    PosPa1= Paleta1.GetPos()
    PosPa2 = Paleta2.GetPos()
    PosPa3 = Paleta3.GetPos()
    PosPa4 = Paleta4.GetPos()
    if Posicion[0] == 0:
        VectorBolay *= -1
    elif Posicion[0] == 24:
        VectorBolay *= -1
    if Game.get_barras() == 1:
        #PALETA 1_____________________________________________________________
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
    if Game.get_barras() == 2:
        #PALETA 1______________________________________________________________
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
def Puntuacion():
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
    Mensajes(str(Game.get_score1()),7)
    Mensajes(str(Game.get_score2()),9)
def Win():
    global Nivel1
    global Nivel2
    global Nivel3
    if Game.get_nivel()==2:
        Nivel1= False
        Nivel2= True
        Nivel3= False
    if Game.get_nivel()==3:
        Nivel1= False
        Nivel2= False
        Nivel3= True
def mainMenu():
    while Inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton1 = Boton("2 Players", 355, 320, 100, 50, LightGrey, Grey, "PVP")
        Boton2 = Boton("1 Player", 355, 240, 100, 50, LightGrey, Grey, "PVC")
        pygame.display.update()
        fps.tick(60)
def Modo():
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
def mainloop():
    global Winner
    global Nivel1
    global Nivel2
    global Nivel3
    while not Winner:
        if Game.get_barras() == 1 and Game.get_nivel() == 1:
            Paleta1.SetPos([8, 0])
            Paleta2.SetPos([8, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 1:
            Paleta1.SetPos([2, 0])
            Paleta2.SetPos([2, 39])
            Paleta3.SetPos([14, 0])
            Paleta4.SetPos([14, 39])
        Game.restart_Score()
        while Nivel1:
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.07)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8,0])
                        Paleta2.SetPos([8,39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0 :
                            Paleta1.moverBarra(-2)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20):
                            Paleta1.moverBarra(2)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-2)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(2)
                Game.winner()
                Colision()
                root.fill(Blue)
                VisualObjetos()
                Win()
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.07)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
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
                root.fill(Blue)
                VisualObjetos()
                Win()
                pygame.display.update()
                fps.tick(60)
        Game.restart_Score()
        if Game.get_nivel()==2:
            Paleta1.SetTamano(6)
            Paleta2.SetTamano(6)
            Paleta3.SetTamano(6)
            Paleta4.SetTamano(6)
        if Game.get_barras() == 1 and Game.get_nivel() == 2:
            Paleta1.SetPos([9, 0])
            Paleta2.SetPos([9, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 2:
            Paleta1.SetPos([3, 0])
            Paleta2.SetPos([3, 39])
            Paleta3.SetPos([14, 0])
            Paleta4.SetPos([14, 39])
        while Nivel2:
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.055)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8,0])
                        Paleta2.SetPos([8,39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0 :
                            Paleta1.moverBarra(-2)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20):
                            Paleta1.moverBarra(2)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-2)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(2)
                Game.winner()
                Colision()
                root.fill(Blue)
                VisualObjetos()
                Win()
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.055)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
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
                root.fill(Blue)
                VisualObjetos()
                Win()
                pygame.display.update()
                fps.tick(60)
        Game.restart_Score()
        if Game.get_barras() == 1 and Game.get_nivel() == 3:
            Paleta1.SetPos([11, 0])
            Paleta2.SetPos([11, 39])
        if Game.get_barras() == 2 and Game.get_nivel() == 3:
            Paleta1.SetPos([8, 0])
            Paleta2.SetPos([8, 39])
            Paleta3.SetPos([10, 0])
            Paleta4.SetPos([10, 39])
        if Game.get_nivel()==3:
            Paleta1.SetTamano(3)
            Paleta2.SetTamano(3)
            Paleta3.SetTamano(3)
            Paleta4.SetTamano(3)
        while Nivel3:
            if Game.get_barras() == 1:
                Puntuacion()
                MoverBola(0.04)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Paleta1.SetPos([8,0])
                        Paleta2.SetPos([8,39])
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0 :
                            Paleta1.moverBarra(-2)
                        elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20):
                            Paleta1.moverBarra(2)
                        if Game.get_player() == False:
                            if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                                Paleta2.moverBarra(-2)
                            elif event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                                Paleta2.moverBarra(2)
                Game.winner()
                Colision()
                root.fill(Blue)
                VisualObjetos()
                Win()
                pygame.display.update()
                fps.tick(60)
            elif Game.get_barras() == 2:
                Puntuacion()
                MoverBola(0.04)
                Paleta1.colocarBarra()
                Paleta2.colocarBarra()
                Paleta3.colocarBarra()
                Paleta4.colocarBarra()
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
                root.fill(Blue)
                VisualObjetos()
                Win()
                pygame.display.update()
                fps.tick(60)

mainMenu()

