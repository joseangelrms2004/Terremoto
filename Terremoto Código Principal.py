class Region:
    def __init__(self, nombre, costo, dolor):
        self.nombre = nombre
        self.costo = costo  # Matriz de costos
        self.dolor = dolor  # Matriz de pérdidas humanas
    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as file:
                lines = file.readlines()
                # Leer la primera línea que contiene el nombre de la región
                self.costo = []
                i = 0
                while i < len(lines) and lines[i].strip():  # Mientras la línea no esté vacía
                    self.costo.append([float(val) for val in lines[i].split()])
                    i += 1
                # Saltar la línea en blanco
                i += 1
                # Leer la sección de pérdidas humanas
                self.dolor = []
                while i < len(lines) and lines[i].strip():  # Mientras la línea no esté vacía
                    self.dolor.append([float(val) for val in lines[i].split()])
                    i += 1
                
                print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print(f"Error: El archivo {archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

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
        print(f"Región: {self.nombre}")
        # Mostrar la matriz de costos
        print("\nMatriz de Costos:")
        for fila in self.costo:
            print(" ".join(f"{val:10.2f}" for val in fila))  # Formatear cada valor con 2 decimales
        # Mostrar la matriz de pérdidas humanas
        print("\nMatriz de Pérdidas Humanas:")
        for fila in self.dolor:
            print(" ".join(f"{val:10.2f}" for val in fila))  # Formatear cada valor con 2 decimales

def menu():
    region = Region("Nombre de la Región", [], [])  # Inicializar la región
    while True:
        print("\n--- Menú ---")
        print("1. Cargar Datos")
        print("2. Modificar Datos")
        print("3. Estimar Consecuencias")
        print("4. Mostrar Región")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Opción 1: Cargar datos desde un archivo
            archivo = input("Ingrese el nombre del archivo de datos: ")
            region.cargar_datos(archivo)
        elif opcion == '2':
            # Opción 2: Modificar datos en una posición específica
            try:
                i = int(input("Ingrese la fila a modificar: "))
                j = int(input("Ingrese la columna a modificar: "))
                nuevo_costo = float(input("Ingrese el nuevo costo: "))
                nuevo_dolor = float(input("Ingrese el nuevo dolor: "))
                region.modificar_datos(i, j, nuevo_costo, nuevo_dolor)
                print("Datos modificados exitosamente.")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}. Asegúrese de ingresar valores válidos.")
        elif opcion == '3':
            # Opción 3: Estimar consecuencias de un terremoto
            try:
                epicentro_x = int(input("Ingrese la fila del epicentro: "))
                epicentro_y = int(input("Ingrese la columna del epicentro: "))
                intensidad = int(input("Ingrese la intensidad del terremoto: "))
                costo_total, dolor_total = region.estimar_consecuencias((epicentro_x, epicentro_y), intensidad)
                print(f"\nConsecuencias estimadas:")
                print(f"Costo total: {costo_total:.2f}")
                print(f"Pérdidas humanas totales: {dolor_total:.2f}")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}. Asegúrese de ingresar valores válidos.")
        elif opcion == '4':
            # Opción 4: Mostrar la región (matrices de costos y pérdidas humanas)
            region.mostrar_region()
        elif opcion == '5':
            # Opción 5: Salir del programa
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    # Inicializar la región y cargar datos desde archivo
    region = Region("Nombre de la Región", [], [])
    menu()