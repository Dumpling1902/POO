class Personaje:
    #Atributos de la clase
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa

    def atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Vida:", self.vida)
        print("-Defensa:", self.defensa)

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    def dañar(self,enemigo):
        return self.fuerza - enemigo.defensa if self.fuerza > enemigo.defensa else 0

    def atacar(self,enemigo):
        daño = self.dañar(enemigo) 
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "Punto de daño a", enemigo.nombre)
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de", enemigo.nombre, "es", enemigo.vida) 

#Creando clase Guerrero que hereda de su clase padre "Personaje"
class Guerrero (Personaje):
    #Sobreescribir el constructor 
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa,espada):
        #Llamar a la clase padre
        super().__init__(nombre,fuerza,inteligencia,vida,defensa)
        self.espada = espada

    #Pedirle al usuario escoger un arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de plata, daño 10. (2) Espada de bronce, daño 8"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")

    #Sobreescirbir método
    def atributos(self):
       super().atributos()
       print("-Espada:", self.espada)

    #Sobreescirbir el cálculo de daño
    def dañar(self, enemigo):
        return self.fuerza * self.espada -enemigo.defensa

#Creando clase Mago que hereda de su clase padre "Personaje"
class Mago (Personaje):
    #Sobreescribir el constructor 
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa,libro):
        #Llamar a la clase padre
        super().__init__(nombre,fuerza,inteligencia,vida,defensa)
        self.libro = libro

    #Sobreescirbir método
    def atributos(self):
       super().atributos()
       print("-Libro:", self.libro)

    #Sobreescirbir el cálculo de daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro -enemigo.defensa

liam = Personaje ("Liam", 20, 15, 100, 10)
hercules = Guerrero("Hércules", 20,15,100,10,5)
michael = Mago ("Michael", 20,15,100,10,5)
#Imprimir atributos antes del ataque
liam.atributos()
hercules.atributos()
michael.atributos()
#Ataques
liam.atacar(hercules)
hercules.atacar(michael)
michael.atacar(liam)
#hercules.cambiar_arma()
#hercules.atributos()
#print (hercules.espada)

#Imprimir atributos antes del ataque
liam.atributos()
hercules.atributos()
michael.atributos()



#Variable del constructor vacío de la clase
#mi_personaje = Personaje("Liam", 70, 60, 80, 50)
#mi_enemigo = Personaje ("Michael", 60,90,100,40)
#print(mi_personaje.dañar(mi_enemigo))

#print(mi_personaje.esta_vivo())
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()
#print("El nombre del personaje es", mi_personaje.nombre)
#print("La fuerza del personaje es", mi_personaje.fuerza)