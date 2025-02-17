from pelicula import Pelicula
from catalogo_pelicula import CatalogoPelicula

print("Bienvenida al Catálogo de Películas 📽️🍿")
nombre_cat = input("Ingrese el nombre del catálogo de películas (Ej: Películas Romáticas): ").strip()
ruta = input("Ingrese el nombre de la ruta que quiere que tenga el catálogo (Ej: pelis_romanticas):  ")
catalogo = CatalogoPelicula(nombre_cat, ruta)

#Creación de un bucle while, para que se siga repitiendo el catálogo hasta que el usuario elija salir
while True:
    #Creación del menú interactivo
    print("Menú de opciones 🎬")
    print("1.  Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")    

    opcion = input("Seleccione una opción (1-4): ").strip()

    #Opción 1: 
    if opcion == "1":
        print("Ha elegido agregar una nueva película al catálogo 🍿")
        nombre_pelicula = input("Ingrese el nombre de la película: ").strip()
        nueva_peli = Pelicula(nombre_pelicula) #Crea el objetivo tipo película
        catalogo.agregar_pelicula(nueva_peli)  # Agregar la película al catálogo
        print(f"La película {nombre_pelicula} ha sido agregada con éxito 💚")
        #Se agregó una nueva película, creando un objeto desde Pelicula. Posteriormente, se usó el método 
        #agregar_pelicula para agregar el nombre de la peli al archivo .txt creado en CatálogoPelicula
    
    elif opcion == "2":
        print("Ha elegido listar las películas 🎬")
        peliculas = catalogo.listar_peliculas() #Se obtiene la lista de películas 
        if peliculas:
            print("\nPelículas en el catálogo: ")
            for i, peli in enumerate(peliculas, start=1):
                print(f"{i}. {peli}")
        else:
            print(peliculas)
        #Aquí se usa el método de listar películas que se creó en catalogo_pelicula. En el if se analiza si 
        #películas está vacío o no. Al usar listar_peliculas(), nos debe de dar una lista, ya que a´si lo definimos
        #El for enumerate nos ayuda a enumerar y posteriormente imprimir de forma ordenada cada peli de la lista
    
    elif opcion == "3":
        print(f"Ha elegido eliminar el catálogo de películas '{nombre_cat}' 🚫") 
        sure = input("¿Estás segura que deseas continuar? (S/N): ").strip().lower()
        if sure == "s":
            catalogo.eliminar_peliculas()
        elif sure =="n":
            print("El catálogo de películas no ha sido eliminado ⛔")
        else: 
            print("Sólo acepto una 's' o una 'n' por respuesta. Vuelve a intentarlo")
    #Se agregó un if antes de eliminar el archivo para asegurarque que el usuario realmente quería eliminarlo y no fue un
    #error. 

    elif opcion == "4":
        print("Ha elegido salir del programa. Gracias por usar el catálogo. ¡Hasta luego! 🥰")
        break 
    #Se sale del bucle while y se cierra el programa

    else:
        print("Opción no válida. Ingrese un número que corresponda a las opciones del catálogo (1-4): ")
