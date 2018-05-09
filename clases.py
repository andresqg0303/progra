#Clases

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
#_____________________________________________________

#Juego
#Atriibutos:
# Nivel: int
# Matriz: list
# Score: int
# Timer: int
# Cantidad de barras: int
# Jugadores (PVP o PVC): boolean

#Métodos:
#set_bola()
#set_barra()
#set_nivel()
#set_score()
#set_player()
#get_time()
#set_time()
#game_over()


class Juego:
    nivel = 1
    Matriz = []
    Score: 0
    Timer = 0
    Cantidad de barras = 1
    PVP = True

    
    barra = None
    bola = None

    def set_Barra(self, color,tamaño,velocidad,posicion):
        self.barra = barra

    def set_Bola(self, color,tamaño,velocidad,posicion):
        self.bola = bola

    def set_nicel(self):
        #Definir

    def set_score(self):
        #Definir

    def set_player(self):
        #Definir

    def get_time(self):
        #Definir

    def set_time(self):
        #Definir

    def game_over(self):
        #Definir





















        
    

    
