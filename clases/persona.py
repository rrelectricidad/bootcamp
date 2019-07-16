class persona:
    edad = 0
    def __init__(self , un_npombre):
        self.mi_nombre = un_npombre
        print("Hola naci , me llamo, y soy un genio" , self.mi_nombre)
    def cumple(self):
        self.edad = self.edad + 1

pepe = persona("pepito")
pepa = persona("pepita")
genio = persona("Ruben")
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)