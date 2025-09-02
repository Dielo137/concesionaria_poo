class Vehiculo:

    def __init__ (self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El valor debe ser un numero positivo")
    
    def descripcion(self):
        return f"Vehiculo marca {self.marca}, modelo {self.modelo}"
    

class Auto(Vehiculo):
    
    def __init__(self,marca,modelo,precio,puertas):
        super().__init__(marca,modelo,precio)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto marca {self.marca}, modelo {self.modelo}, con {self.puertas}"
    
class Moto(Vehiculo):

    def __init__(self,marca,modelo,precio,cilindrada):
        super().__init__(marca,modelo,precio)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Moto marca {self.marca}, modelo {self.modelo}, con {self.cilindrada}"
    
class Camion(Vehiculo):

    def __init__(self,marca,modelo,precio,capacidad_carga):
        super().__init__(marca,modelo,precio)
        self.capacidad_carga = capacidad_carga

    def descripcion(self):
        return f"Camion marca {self.marca}, modelo {self.modelo}, con {self.capacidad_carga}"