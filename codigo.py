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
# set_nivel()
# set_score1()
# set_nivel()
# set_score2()
# set_player()
# get_player()
# get_score()
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
    def set_nivel(self,level):
        self.nivel = level
    def set_score1(self):
        self.score1 +=1
    def set_score2(self):
        self.score2 +=1
    def get_matriz(self):
        return self.matriz
    def set_player(self,modo):
        self.PVC = modo
    def get_player(self):
        return self.PVC
    def get_time(self):
        return self.timer
    def get_score(self):
        return (self.score1,self.score2)
    def update(self):
        for i in range(self.tamanoMatriz[0]):
            print(" ")
            for j in range(self.tamanoMatriz[1]):
                Posi = self.matriz[i][j]
                if type(Posi) != type(0):
                    print(Posi, " ", end="")
                    continue
                print (Posi, "  ", end="")
        print(" ")
    def cronometro(self):
        self.timer= 0
        while self.timer >= 0:
            self.timer += 1
            time.sleep(1)
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
#Metodos:
# GetPos()
# SetPos()
# GetSpeed()
# GetColor()
# GetTamano()
# moverBarra()
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

class Bola:
    def __init__(self, color= (255,255,255),tamano= (20,20),velocidad= 3,posicion=[12,19]):
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
    def colocar(self):
        Matriz[self.posicion[0]][self.posicion[1]]= 1
    def Mover(self,MoverX,MoverY):
        Matriz[self.posicion[0]][self.posicion[1]] = 0
        self.posicion[0] += MoverX
        self.posicion[1] += MoverY
        self.colocar()

"""_____________________________________________________________________________________________________________________
_______________________________________________Código de Juego__________________________________________________________
________________________________________________________________________________________________________________________"""
pygame.init()
fps= pygame.time.Clock()
Game = Juego()
Inicio= True
Paleta1= Barra()
Paleta2= Barra(posicion= [8,39])
Paleta3= Barra(tamano=3, posicion= [14,0])
Paleta4= Barra(tamano=3, posicion= [14,39])


Width= 800
Height= 500

root= pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pong")


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

Menu= pygame.image.load("Menu.jpg")

def ObjetosTexto(text, font):
    SuperficieTexto = font.render(text, True, Black)
    return SuperficieTexto, SuperficieTexto.get_rect()

def Boton(msg,x,y,w,h,ic,ac,command= None):
    global Inicio
    mouse = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(root, ac,(x,y,w,h))
        if click[0] == 1 and command == "PVC":
            Game.set_player(True)
            Inicio= False
            mainloop()
        elif click[0] == 1 and command == "PVP":
            Game.set_player(False)
            Inicio = False
            mainloop()
    else:
        pygame.draw.rect(root, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = ObjetosTexto(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    root.blit(textSurf, textRect)

def VisualObjetos():
    for i in range(0,len(Matriz),1):
        for j in range(0,len(Matriz[0]),1):
            if Matriz[i][j]==1:
                if j== 0 or j== 39:
                    pygame.draw.rect(root,White,(j*20,i*20,20,20))
                if 0<j<39:
                    pygame.draw.circle(root,White,(j*20,i*20),10,20)

def mainMenu():
    while Inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton1 = Boton("PVP",355,240,100,50,LightGrey, Grey,"PVP")
        Boton2= Boton("PVC", 355, 320, 100, 50, LightGrey, Grey,"PVC")
        pygame.display.update()
        fps.tick(60)

def mainloop():
    Winner = False
    Nivel1= True
    Nivel2= False
    Nivel3= False
    Vector1= 0
    Vector2= 0
    Movimiento= False
    while not Winner:
        while Nivel1:
            Paleta1.colocarBarra()
            Paleta2.colocarBarra()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Paleta1.SetPos([8,0])
                    Paleta2.SetPos([8,39])
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    Movimiento= True
                    if event.key == pygame.K_w and Paleta1.GetPos()[0] > 0:
                        Paleta1.moverBarra(-1)
                    elif event.key == pygame.K_s and Paleta1.GetPos()[0]*20 < Height-(Paleta1.GetTamano()*20) :
                        Paleta1.moverBarra(1)
                    elif Game.get_player() == False:
                        if event.key == pygame.K_UP and Paleta2.GetPos()[0] > 0:
                            Paleta2.moverBarra(-1)
                        if event.key == pygame.K_DOWN and Paleta2.GetPos()[0] * 20 < Height- (Paleta2.GetTamano() * 20):
                            Paleta2.moverBarra(1)
            root.fill(Blue)
            VisualObjetos()
            pygame.display.update()
            fps.tick(60)
        while Nivel2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            root.fill(Blue)
            pygame.display.update()
            fps.tick(60)
        while Nivel3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            root.fill(Blue)
            pygame.display.update()
            fps.tick(60)

mainMenu()


