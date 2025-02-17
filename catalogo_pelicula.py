from pelicula import Pelicula #Lalamos la función pelicula
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
    def agregar_pelicula(self, nombre):
        """ Agrega una película al catálogo en el archivo de texto"""
        with open(self.ruta_archivo, "a") as file:
            file.write(nombre + "\n" )
    def listar_peliculas(self, nombre):
        """ Listar todas las películas del catálogo, que estén guardadas en el archivo .txt"""
        with open(self.ruta_archivo, "r") as file: #Se abre el archivo en modo lectura
            pelis = file.readlines() #Guarda todas las línea del archivo en una lista
            return [pelicula.strip() for pelicula in pelis]
    def eliminar_peliculas(self, nombre):
        """ Elimina el archivo .txt en el que se crearon las películas"""
        os.path.exists(self.ruta_archivo)
        os.remove(self.ruta_archivo)
        print("Archivo Eliminado")