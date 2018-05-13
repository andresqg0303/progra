import time
import random

# _____________________________________________________

# Juego
# Atributos:
# nivel: int
# matriz: list
# score: int
# timer: int
# barras: int
# Jugadores (PVP o PVC): boolean

# Métodos:
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


class Juego:
    matriz= (40,25)
    nivel= 1
    PVC= True
    barras= 1
    timer= 0
    score1= 0
    score2= 0
    win1= 0
    win2= 0
    def __init__(self,matriz,nivel,PVC,barras,timer,score1,score2):
        self.matriz = matriz
        self.nivel = nivel
        self.PVC = PVC
        self.barras = barras
        self.timer = timer
        self.score1 = score1
        self.score2 = score2
    def set_nivel(self,level):
        self.nivel = level
    def set_score1(self):
        self.score1 +=1
    def set_score2(self):
        self.score2 +=1
    def set_player(self,modo):
        self.PVC = modo
    def get_time(self):
        return self.timer
    def get_score(self):
        return (self.score1,self.score2)
    def cronometro(self):
        while self.timer >= 0:
            self.timer += 1
            time.sleep(1)
    def get_matriz(self):
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
# Color: tuple
# Tamaño: tuple
# Velocidad: int
# Posición: tuple
#Métodos:
# GetPos()
# GetSpeed()
# GerColor()
# GetTamaño()
# MoverBarra()

class Barra:
    color= (0, 0, 0)
    tamaño= (180,20)
    velocidad= 10
    posicion= ''

    def __init__(self, color,tamaño,velocidad,posicion):
        self.color = color
        self.tamaño = tamaño
        self.velocidad = velocidad
        self.posicion = posicion

    def GetColor(self):
        return self.color=color
    
    def GetSpeed(self):
        return self.velocidad = velocidad

    def GetPos(self):
        return self.posición = posición

    def GetTamaño(self):
        return self.tamaño = tamaño

    def MoverBarra(self):
        #Definir


#___________________________________________________________

#Bola

#Atributos:
# Color: tuple
# Tamaño: tuple
# Velocidad: int
# Posición: tuple
#Métodos:
# GetPos()
# GetSpeed()
# GerColor()
# GetTamaño()
# Mover()
# Dirección()

class Bola:
    color= (0, 0, 0)
    tamaño= (20,20)
    velocidad= 20
    posicion= ''

    def __init__(self, color,tamaño,velocidad,posicion):
        self.color = color
        self.tamaño = tamaño
        self.velocidad = velocidad
        self.posicion = posicion

    def GetColor(self):
        return self.color=color
    
    def GetSpeed(self):
        return self.velocidad = velocidad

    def GetPos(self):
        return self.posición = posición

    def GetTamaño(self):
        return self.tamaño = tamaño

    def Mover(self):
        #Definir

    def Dirección(self):
        #Definir



















        
    

    
