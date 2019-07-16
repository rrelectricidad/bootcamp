print(2+2)
print(8*8+6/10)
print(8*8)
print("hola mundo"*6)
print("hola"*6)
print("holaaa"*5)# programa
print("hola",2, "que")
#Ej. Crear un variable nombre y una variable EDAD 
# Con sus Nombres y edades y despues imprimir
#Hola, me llamo ----- y tengo----- anos
nombre = "Ruben"
Edad = 28
print("hola mi nombre es",nombre, "y tengo",Edad)
Profesion = "electrcista"
ciudad = "caaguazu"
#Ej. Crear una lista datos que en en primer lugar este tu nombre
# y en la segnda posicion este tu edad 
# Imprimir "hola me llamo ---- , y tengo ----anos"
Datos= ["Ruben",28]
print("hola mi nombre es ",Datos[0], "y tengo", Datos[1],"anos")
Datos.append("Electricista") #Como agreagar informacion a una lista datos.append

#como crear una lista [,"",]
print(Datos)
# Como imprimir una lista copleta -print(nombre de la lista)
Datos.pop()
print(Datos)
Datos.pop()
print(Datos)

#Como eliminar datos- datos.pop()- print(datos)
# len- dimension de de listas
Datos= ["Ruben",28,1,2,3,3,3,3,7,8,6,0]
#necesito = [zapato , medias , camisas , toallas]
final = 12
print("La lista de Datos tiene",len(Datos),"elementos")
# ej. imprimir el ultimo elemento de una lista que no sabemos cuantos elementos tiene
print(final)
########### bucles/ loops/ciclos

def comico(yo,vos):
    variar= yo + vos
    return variar

print(comico(4,16))

def comico2(yo , vos):
    variar= yo - vos
    return variar

print(comico2(20,6))
print(comico(4,8))

def parrafo(juan , jef):
    literal= juan * jef
    return literal
print(parrafo(15,6))



