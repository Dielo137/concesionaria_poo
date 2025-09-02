from vehiculo import Vehiculo, Auto, Moto, Camion

class Concesionaria:
    def __init__(self):
        
        self.vehiculos = []

    def agregar_vehiculo(self,vehiculo):
        
        self.vehiculos.append(vehiculo)
        print(f" {vehiculo.marca} {vehiculo.modelo} agregado al catalogo")

    def mostrar_catalogo(self):

            print("---  Catálogo de la Concesionaria  ---")
            
            if not self.vehiculos:
                print("El catálogo está vacio. Añade algunos vehiculos")
                return 

            total_inventario = 0

            for v in self.vehiculos:

                print(f"- {v.descripcion()} | Precio: ${v.get_precio()}")
                

                total_inventario += v.get_precio()

            print("------------------------------------------")

            print(f" Valor total del inventario: ${total_inventario}")