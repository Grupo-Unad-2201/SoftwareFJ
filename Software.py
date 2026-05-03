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
            
            
#creacion de los 3 servicios
#Utilizacion de Herencia y polimorfismo

class SalaReservada(Servicio):
    def __init__(self, tiempo):
        super().__init__("sala", 6000)
        self.tiempo = tiempo
        
    def calcular_costo(self):
        return self.costo_inicial * self.tiempo
    
    def descripcion(self):
        return f"Reserva de sala por {self.tiempo} horas"
    
# segundo servicio Alquiler de equipo

class Equiposalquilado(Servicio):
    def __init__(self, dias):
        super().__init__("Equipo", 10000)
        self.dias = dias
        
    def calculcar_costo(self):
         return self.costo_inicial * self.dias
     
    def descripcion(self):
         return f"Alquiler por {self.tiempo} dias. "
     
     
class Asesorias(Servicio):
    def __init__(sel, tiempo):
        super().__init__("Asesorias", 20000)
        self.tiempo = tiempo
        
    def calcular_costo(self):
        return self.costo_inicial * self.tiempo
    
    def descripcion (Self):
        return f"Asesorias por {self.tiempo} horas"

class Asesoria(Servicio):
    def __init__(self, horas):
        super().__init__("Asesoria", 30000)
        self.horas = horas
        
    def calcular_costo(self):
        return self.costo_inicial * self.horas
    
    def descripcion (self):
        return f"Asesoria por {self.horas} horas" 
    
   