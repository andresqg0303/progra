import time
import random

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

# _____________________________________________________

# Juego
# Atributos:
# nivel: int
# matriz: tuple
# score: int
# timer: int
# barras: int
# Jugadores (PVP o PVC): boolean
# tamanoMatriz: list

# Metodos:
# Start()
# set_nivel()
# set_score1()
# set_nivel()
# set_score2()
# set_player()
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
    def get_time(self):
        return self.timer
    def get_score(self):
        return (self.score1,self.score2)
    def update(self):
        self.matriz= Matriz
    def cronometro(self):
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
        if score1-2>=score2 and score1 >= 10:
            self.win1 += 1
            self.nivel += 1
        elif score2-2>=score1 and score2 >= 10:
            self.win2 += 1
            self.nivel += 1
    def game_over(self):
        if self.PVC== False:
            if self.nivel >= 3 and self.win1 >= 2:
                return ("Player 1 won")
            elif self.nivel >= 3 and self.win2 >= 2:
                return ("Player 2 won")
#__________________________________________________________________________________________________________________


#Barra
#Atributos:
# tolor: tuple
# tamano: tuple
# velocidad: int
# posicion: tuple
#Metodos:
# GetPos()
# SetPos()
# GetSpeed()
# GerColor()
# GetTamano()
# MoverBarra()
# ColocarBarras()

class Barra:
    def __init__(self, color= (255,255,255),tamano= 9,velocidad= 7,posicion= (0,8)):
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
    def SetPos(self,nuevaPos_Tuple_):
        self.posicion= nuevaPos_Tuple_
    def MoverBarra(self,moverY):
        
        for i in range(self.posicion[1], self.posicion[1]+self.tamano,1):
            Matriz[i][0] += 1
    def colocarBarras(self):
        for i in range(self.posicion[1], self.posicion[1]+self.tamano,1):
            Matriz[i][0] += 1
#___________________________________________________________

#Bola

#Atributos:
# Color: tuple
# Tamano: tuple
# Velocidad: int
# Posicion: tuple
#Metodos:
# GetPos()
# GetSpeed()
# GerColor()
# GetTamano()
# Mover()

class Bola:
    color= (0, 0, 0)
    tamano= (20,20)
    velocidad= 20
    posicion= ''

    def __init__(self, color,tamano,velocidad,posicion):
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

    def Mover(self):
        pass



















        
    

    
