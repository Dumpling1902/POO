class Personaje:
    #Atributos de la clase

    def __init__(self,nombre,fuerza,inteligencia,vida,defensa):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__vida = vida
        self.__defensa = defensa

    def atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Vida:", self.__vida)
        print("-Defensa:", self.__defensa)

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "Ha muerto")

    def dañar(self,enemigo):
        return self.__fuerza - enemigo.__defensa 

    def atacar(self,enemigo):
        daño = self.dañar(enemigo) 
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "Ha realizado", daño, "Punto de daño a", enemigo.__nombre)
        print("Vida de", enemigo.__nombre, "es", enemigo.__vida)

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self,fuerza):
        if fuerza < 0:
            print ("Error, has puesto un valor negativo")
        else:
            self.__fuerza = fuerza

#Variable del constructor vacío de la clase
mi_personaje = Personaje("Liam", 70, 60, 80, 50) #nombre,fuerza,inteligencia,vida,defensa
mi_enemigo = Personaje ("Michael", 60,90,100,40)
#Prueba 4. ¿Acceso a morir?
mi_personaje.atacar(mi_enemigo)

#Prueba 7. Getters and setters
#print(mi_personaje.get_fuerza())
#mi_personaje.setfuerza(-100)
#print(mi_personaje.getfuerza())
mi_personaje._Personaje__fuerza = 10
mi_personaje.atributos()

#Prueba 1. Sin acceso al atributo fuerza
mi_personaje.fuerza=10
mi_personaje.atributos()



#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()

#print("El nombre del personaje es", mi_personaje.__nombre)
#print("La fuerza del personaje es", mi_personaje.__fuerza)