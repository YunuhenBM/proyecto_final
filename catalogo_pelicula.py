from pelicula import Pelicula #Llamamos la función pelicula
import os #Importanto el sistema operativo para crear, modificar y eliminar archivos
import re #Importando la paquetería para expresiones regulares

class CatalogoPelicula:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre

        validacion = r"^[a-z0-9_]+$" #La r indica que es una cadena tipo raw, lo que significa que va a tomar literal ese caracter, sin tomar en cuenta que sea especial o no
    
        while not re.match(validacion, ruta_archivo):
            print("El nombre del archivo es inválido")
            print("El archivo no debe contener espacios, mayúsculas, acentos, puntos, ni carácteres especiales")
            ruta_archivo = input("Ingrese un nombre válido")
        self.ruta_archivo = f"{ruta_archivo}.txt"
        #Con el while not nos aseguramos que el usuario ingrese el nombre válido, y no avanzará hasta que lo haga.
    
    def agregar_pelicula(self, pelicula): #pelicula viene de la función pelicula.py
        """ Agrega una película al catálogo en el archivo de texto"""
        with open(self.ruta_archivo, "a") as file:
            file.write(pelicula.get_nombre() + "\n" )
    #Se hizo una función para agregar películas al catálogo, almacenándolas en un archivo 
    # de texto. Se usó un getter (get_nombre()) porque el atributo "__nombre" es privado.
    #Este método permite acceder al archivo.


    def listar_peliculas(self):
        """ Listar todas las películas del catálogo, que estén guardadas en el archivo .txt"""
        try:
            with open(self.ruta_archivo, "r") as file: #Se abre el archivo en modo lectura
                pelis = file.readlines() #Guarda todas las línea del archivo en una lista
                return [pelicula.strip() for pelicula in pelis]
        except FileNotFoundError:
            return "El catálogo está vacío o no existe"
        except Exception as e:
            return f"Error inesperado: {e}"
    #Se realizó una lista de todas las películas dentro del archivo creado. Se usó un with open "r"
    #Para leer el archivo, y un readlines para que devuelva todas las líneas ocmo una lista.
    # Se quitaron los saltos de lína (\n) con un strip() dentro de un for 
    #Se hizo un try-except para evitar que marque error si se usa esa función cuando
    #el catálogo esté vacío o no exista.


    def eliminar_peliculas(self):
        """ Elimina el archivo .txt en el que se crearon las películas"""
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"Archivo {self.ruta_archivo} eliminado con éxito")
        else:
            print("La ruta no existe")
    #Se utilizó un if os.path.exists para comprobar que el archivo exite. Si sí exite,
    # os.remove lo elimina e imprime un mensaje diciento que ya se eliminó.
    #Si no existe, manda un mensaje diciendo que la ruta no exite.