
from televisores.marca import Marca

class TV:

    # Class Attributes

    __numTV = 0

    # Construct

    def __init__(self, marca : Marca, estado : bool) -> None:
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__volumen = 1
        self.__precio = 500
        self.__control = None
        TV.__numTV += 1

    # Instance Methods
    
    def turnOff(self) -> None: 
        self.__estado = False

    def turnOn(self) -> None:  
        self.__estado = True
    
    def volumenUp(self) -> None:
        self.__volumen += 1 if (self.__volumen < 7) else 0
    
    def volumenDown(self) -> None:
        self.__volumen -= 1 if (self.__volumen > 0) else 0
    
    def canalUp(self) -> None:
        self.__canal += 1 if (self.__canal < 120) else 0
    
    def canalDown(self) -> None:
        self.__canal -= 1 if (self.__canal > 1) else 0
    
    # Getters and Setters
        
        #   Gets
    
    def getMarca(self) -> Marca:
        return self.__marca
    
    def getCanal(self) -> int:
        return self.__canal
    
    def getVolumen(self) -> int:
        return self.__volumen
    
    def getPrecio(self) -> int:
        return self.__precio
    
    def getEstado(self) -> bool:
        return self.__estado
    
    def getControl(self):
        return self.__control
    
        #   Sets
    
    def setMarca(self, marca : Marca) -> None:
        self.__marca = marca
    
    def setCanal(self, canal : int) -> None:
        self.__canal = canal if (canal >= 1 and canal <= 120) else self.__canal
    
    def setVolumen(self, volumen : int) -> None:
        self.__volumen = volumen if (volumen >= 0 and volumen <= 7) else self.__volumen
    
    def setPrecio(self, precio : int) -> None:
        self.__precio = precio
    
    def setControl(self, control) -> None:
        self.__control = control
        control.tv = self
    
    def setEstado(self, estado : bool) -> None:
        self.__estado = estado
    

    # Class Methods
         
    @classmethod
    def getNumTV(cls) -> int:
        return cls.__numTV

    pass