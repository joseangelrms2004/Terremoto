class Region:
    def __init__(self, nombre, costo, dolor):
        self.nombre = nombre
        self.costo = costo  # Matriz de costos
        self.dolor = dolor  # Matriz de pérdidas humanas

    def cargar_datos(self, archivo):
        #Cargar datos desde un archivo 
        pass

    def modificar_datos(self, i, j, nuevo_costo, nuevo_dolor):
        self.costo[i][j] = nuevo_costo
        self.dolor[i][j] = nuevo_dolor

    def estimar_consecuencias(self, epicentro, intensidad):
        total_costo = 0
        total_dolor = 0
        #Calcular el rango afectado por el terremoto
        for x in range(max(0, epicentro[0] - intensidad), min(len(self.costo), epicentro[0] + intensidad + 1)):
            for y in range(max(0, epicentro[1] - intensidad), min(len(self.costo[0]), epicentro[1] + intensidad + 1)):
                if abs(epicentro[0] - x) + abs(epicentro[1] - y) <= intensidad:
                    total_costo += self.costo[x][y]
                    total_dolor += self.dolor[x][y]
        return total_costo, total_dolor

    def mostrar_region(self):
        #Mostrar las matriz de costos y dolores
        pass

def menu():
    while True:
        print("1. Carga o Modificación de Datos")
        print("2. Estimación de Consecuencias")
        print("3. Estimación de Zonas de Riesgo")
        print("4. Mostrar Región Geográfica")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            #Lógica para cargar o modificar datos
            pass
        elif opcion == '2':
            #Lógica para estimar consecuencias
            pass
        elif opcion == '3':
            #Lógica para estimar zonas de riesgo
            pass
        elif opcion == '4':
            #Lógica para mostrar la región geográfica
            pass
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    # Inicializar la región y cargar datos desde archivo
    region = Region("Nombre de la Región", [], [])
    menu()