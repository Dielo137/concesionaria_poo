from concesionaria import Concesionaria

from vehiculo import Auto, Moto, Camion



if __name__ == "__main__":

    print(" Iniciando sistema de la concesionaria...")


    mi_concesionaria = Concesionaria()

    print(" Creando e instanciando vehículos...")

    auto_1 = Auto("Toyota", "Corolla", 20000, 4)
    moto_1 = Moto("Honda", "CBR500R", 15000, "500cc")
    camion_1 = Camion("Volvo", "FH16", 75000, "20000kg")
    auto_2 = Auto("Tesla", "Model 3", 45000, 4)


    print("Agregando vehículos al catálogo...")
    mi_concesionaria.agregar_vehiculo(auto_1)
    mi_concesionaria.agregar_vehiculo(moto_1)
    mi_concesionaria.agregar_vehiculo(camion_1)
    mi_concesionaria.agregar_vehiculo(auto_2)


    mi_concesionaria.mostrar_catalogo()


    print("Probando el encapsulamiento (setter)...")
    print(f"Precio original del Tesla: ${auto_2.get_precio()}")
    

    print("Intentando poner precio -500...")
    auto_2.set_precio(-500) 
    

    print("Cambiando precio a 48000...")
    auto_2.set_precio(48000)
    print(f"Nuevo precio del Tesla: ${auto_2.get_precio()}")


    mi_concesionaria.mostrar_catalogo()

    print("\n Sistema finalizado.")