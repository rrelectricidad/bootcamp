class Dino: 
    def __init__(self,un_nombre , una_edad , altura):
        self.nombre = un_nombre
        self.edad = una_edad
        self.altur = altura
        print("que hay")

    def saludar(self):
        print("hola me llamo", self.nombre, "tengo", self.edad, "ano y mido", self.altur, "metros")
    
    # def cortar_altur(sel):
    #     self.altura = self.altur - cntidad_de_altur_a_cortar



vari = Dino( "tirano", 1, "20")


vari.saludar()


