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