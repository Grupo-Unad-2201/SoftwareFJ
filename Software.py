from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id):
        self. _id = id  # aqui realizo encapsulacion
        
        
    @abstractmethod
    def mostrar_info(self):
        pass
    
    


class Cliente(Entidad):
    def __init__(self, id, nombre, correo):
        super().__init__(id)
        
        if not nombre:
            raise valueError("El nombre no puede estar vacio")
        
        if "@" not in correo:
            raise valueError("Correo Electronico invalido invalido ")
        
        self._nombre = nombre
        self._correo = correo
        
    def mostrar_info(self):
        return f"Cliente: {self._nombre}, correo: {self._correo}"
    
    
#Clase Abstracta de servicio

class Servicio(ABC):
    def __init__(self, nombre, costo_inicial):
        self.nombre = nombre
        self.costo_inicial = costo_inicial
        
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass
            