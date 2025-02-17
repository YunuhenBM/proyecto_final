class Pelicula:   
    def __init__(self, nombre):
        self.__nombre = nombre
        """ Se inicia la función con un atributo privado (self.__nombre) """
    def __str__(self):
        return self.__nombre
        """ Convierte la salida de nombre en string cuando se imprime el objeto """
        
    def get_nombre(self): #Getter: Me permite acceder a la cadena de texto
        """ Devuelve el nombre de la película, al usar nuestro atributo privado """
        return self.__nombre

    
# Esta clase representa una película y tiene un atributo privado (__nombre).
# Al ser privado, el atributo no puede ser accedido directamente desde fuera de la clase.
# Para permitir el acceso al nombre de la película, se implementa un método getter (get_nombre()).