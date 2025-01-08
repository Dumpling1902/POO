class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    vida = 0
    defensa = 0
#Variable del constructor vacío de la clase
mi_personaje = Personaje()
#Modificando los valores de los atributos
mi_personaje.nombre = "Liam"
mi_personaje.fuerza = 20
print("El nombre del personaje es", mi_personaje.nombre)
print("La fuerza del personaje es", mi_personaje.fuerza)