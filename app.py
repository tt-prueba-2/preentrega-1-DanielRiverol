# Lista para almacenar los productos
producto = []


# Función principal para el sistema de inventario
def main():
    # Variable de control para el bucle del menú
    opcion = 0

    # Bucle para mostrar el menú hasta que el usuario elija salir
    while opcion != 3:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        # Solicitar la opción al usuario
        opcion = int(input("Seleccioná una opción: "))

        if opcion == 1:
            # Agregar un nuevo producto
            nombre = input("Ingresá el nombre del producto: ")
            cantidad = int(input("Ingresá la cantidad del producto: "))

            # Agregar el producto a la lista como una tupla (nombre, cantidad)
            productos.append([nombre, cantidad])
            print("Producto agregado con éxito.")

       
        
      
        else:
            print("Opción inválida, por favor intentá de nuevo.")

    # Mensaje final
    print("Programa finalizado.")


if __name__ == "__main__":
    main()
