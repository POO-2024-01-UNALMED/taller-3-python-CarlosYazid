
from televisores.tv import TV
from typing import Callable

class Control:

    # Control Methods

    def enlazar(self, tv : TV) -> None:
        tv.setControl(self)
        self.__tv = tv

    # Tv Methods

    def turnOff(self):
        self.__tv.turnOff()
    
    def turnOn(self):
        self.__tv.turnOn()

    def canalUp(self):
        self.__tv.canalUp()

    def canalDown(self):
        self.__tv.canalDown()

    def volumenUp(self):
        self.__tv.volumenUp()

    def volumenDown(self):
        self.__tv.volumenDown()

    def setCanal(self, canal : int):
        self.__tv.setCanal(canal)

    def setVolumen(self, volumen : int):
        self.__tv.setVolumen(volumen)

    # Getters and Setters

    def getTv(self) -> TV:
        return self.__tv
    
    def setTv(self, tv : TV) -> None:
        self.__tv = tv

    pass