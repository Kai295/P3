def registrar_propiedad():
    correlativo = input("Ingrese correlativo: ")
    tipo_propiedad = input("Ingrese tipo de propiedad (1 = Casa, 2 = Departamento): ")
    nro_dormitorios = input("Ingrese número de dormitorios: ")
    nro_baños = input("Ingrese número de baños: ")
    precio = input("Ingrese precio: ")

    tipo_propiedad_str = 'Casa' if tipo_propiedad == '1' else 'Departamento'

    
    nueva_propiedad = f"{correlativo},{tipo_propiedad_str},{nro_dormitorios},{nro_baños},{precio}\n"

    
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'a') as file:
        file.write(nueva_propiedad)

    print("Propiedad registrada correctamente.")


def listar_propiedades():
    print("Listado de propiedades:")
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'r') as file:
        for line in file:
            print(line.strip())  

def imprimir_oferta_por_tipo(tipo):
    tipo_propiedad_str = 'Casa' if tipo == '1' else 'Departamento'

    
    output_file = f'PROPIEDADESXTIPO.csv'

    
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if tipo_propiedad_str in line:
                outfile.write(line) 

    print(f"Se ha generado el archivo {output_file} con las propiedades de tipo {tipo_propiedad_str}.")

def main():
    while True:
        print("\nBienvenido a FastHome - Sistema de Gestión de Propiedades Usadas")
        print("1. Registrar propiedad")
        print("2. Listar propiedades")
        print("3. Imprimir oferta de propiedad por tipo")
        print("4. Salir del programa")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            registrar_propiedad()
        elif opcion == '2':
            listar_propiedades()
        elif opcion == '3':
            tipo = input("Ingrese el tipo de propiedad (1 = Casa, 2 = Departamento): ")
            imprimir_oferta_por_tipo(tipo)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")

if __name__ == "__main__":
    main()