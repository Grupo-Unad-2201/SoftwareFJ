from datetime import datetime

import re

COSTO_SALA = 6000
COSTO_EQUIPO = 10000
COSTO_ASESORIA = 30000

from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id):
        self._id = id  # aqui realizo encapsulacion
        
        
    @abstractmethod
    def mostrar_info(self):
        pass
    
    


class Cliente(Entidad):
    def __init__(self, id, nombre, correo):
        super().__init__(id)
        
        if not nombre:
            raise ValueError("El nombre no puede estar vacio")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise ValueError("Correo electrónico inválido")
        
        self._nombre = nombre
        self._correo = correo

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo
    
    def __str__(self):
        return f"{self._nombre} - {self._correo}"
    
    
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
        super().__init__("sala", COSTO_SALA)
        
        if tiempo <= 0:
            raise ValueError("El tiempo deber ser mayor a 0 (Cero)")
        self.tiempo = tiempo
        
    def calcular_costo(self):
        return self.costo_inicial * self.tiempo
    
    def descripcion(self):
        return f"Reserva de sala por {self.tiempo} horas"
    
# segundo servicio Alquiler de equipo

class AlquilerEquipo(Servicio):
    def __init__(self, dias):
        super().__init__("Equipo", COSTO_EQUIPO)
        
        if dias <= 0:
            raise ValueError("Los Dias debe ser mayor a 0 (cero)")
            
        self.dias = dias
        
    def calcular_costo(self):
         return self.costo_inicial * self.dias
     
    def descripcion(self):
         return f"Alquiler por {self.dias} dias. "
     
     

class Asesoria(Servicio):
    def __init__(self, horas):
        super().__init__("Asesoria", COSTO_ASESORIA)
        
        if horas <= 0:
            raise ValueError("Las Horas deben ser mayor a 0 (cero)")
        
        self.horas = horas
        
    def calcular_costo(self):
        return self.costo_inicial * self.horas
    
    def descripcion (self):
        return f"Asesoria por {self.horas} horas" 
    
# Realizamos una clase llamada reserve
class Reserva:
    def __init__(self, cliente, servicio):
        if not isinstance (cliente, Cliente):
            raise TypeError("Cliente inválido")
        
        if not isinstance (servicio, Servicio):
             raise TypeError("Servicio inválido")
         
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"
         
    def confirmar(self):
        self.estado = "Confirmada"
        
    def cancelar(self):
        self.estado = "Cancelada"
    
    def procesar(self):
        try:
            costo = self.servicio.calcular_costo()
            self.confirmar()
            return f"Reserva confirmada. Costo: {costo}"
        except Exception as e:
            self.estado = "Error"
            raise RuntimeError("Error al procesar reserva") from e

#Creamos un sistema de Logs

def guardar_logs(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")

# Nueva función

def crear_reserva(cliente, servicio):
    try:
        reserva = Reserva(cliente, servicio)
        sistema.agregar_reserva(reserva)
        print(reserva.procesar())
        return reserva
    except Exception as e:
        guardar_logs(str(e))        

#En este espacio realizo el manejo de excepciones

# Sistema central de reservas
class SistemaReservas:
    def __init__(self):
        self.clientes = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def mostrar_reservas(self):
        print("\n--- ESTADO DE RESERVAS ---")
        for r in self.reservas:
            print(f"Cliente: {r.cliente.nombre} | Servicio: {r.servicio.nombre} | Estado: {r.estado}")


sistema = SistemaReservas() 
           
#Cliente válido
try:
    cliente1 = Cliente(1, "Isaac", "isamnkat@gmail.com")
    sistema.agregar_cliente(cliente1)
    
except Exception as e:
    guardar_logs(str(e))
    
#Cliente inválido
try:
    cliente_error = Cliente(2, "", "correo_mal")
except Exception as e:
    guardar_logs("Error cliente: " + str(e))
    
# Salas reservadas válidas

try:
    s1 = SalaReservada(2)
    crear_reserva(cliente1, s1)

except Exception as e:
    guardar_logs(str(e))
    
#Equipos reservados válidos
    
try:
    s2 = AlquilerEquipo(3)
    crear_reserva(cliente1, s2)
    
except Exception as e:
    guardar_logs(str(e) )   
    
# Equipos con reservas inválidas

try:
    s3 = SalaReservada(-1)
    r3 = Reserva(cliente1, s3)
    print(r3.procesar())
except Exception as e:
    guardar_logs("Error servicio: " + str (e))
    
#Servicio inválido equipos con cero dias

try:
    s4 = AlquilerEquipo(0)
    r4 = Reserva(cliente1, s4)
    print(r4.procesar())
except Exception as e:
    guardar_logs("Error servicio: "+ str(e))
    
#Mostrar Reservas

sistema.mostrar_reservas()