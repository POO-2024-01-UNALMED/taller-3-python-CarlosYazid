

class Marca:

    # Construct

    def __init__(self, nombre : str) -> None:
        self.__nombre = nombre
    
    # Getters and Setters

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre : str) -> None:
        self.__nombre = nombre
    
    pass

# Anti - copy: Carlos Yazid Padilla