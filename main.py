import datetime

# 1. ESCUDO: Para que el programa no se cierre si hay errores
class ErrorSoftwareFJ(Exception):
    pass
from abc import ABC, abstractmethod

# 1. CLASE CLIENTE (Con datos protegidos y validaciones robustas)
class Cliente:
    def __init__(self, nombre, cedula):
        # Validación estricta según el Anexo 3
        if not nombre.strip() or not cedula.strip():
            raise ErrorSoftwareFJ("Datos de cliente incompletos.")
        
        self.__nombre = nombre  # Encapsulamiento (Dato privado)
        self.__cedula = cedula  # Encapsulamiento (Dato privado)

    def obtener_nombre(self):
        return self.__nombre

# 2. CHISMOSO: Para anotar los fallos en un bloc de notas
def registrar_log(mensaje):
    with open("sistema_logs.txt", "a") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] ERROR: {mensaje}\n")

# 3. EL PROGRAMA
def iniciar_sistema():
    try:
        print("--- SISTEMA SOFTWARE FJ - TRABAJO DE JAVIER ---")
        while True:
            nombre = input("Escriba el nombre del cliente: ").strip()
            
            if nombre.replace(" ", "").isalpha() and len(nombre) > 2:
                print(f"✅ Cliente {nombre} registrado correctamente.")
                break

        else:  registrar_log(f"Nombre inválido: {nombre}")
        print("❌ ERROR: El nombre solo debe contener letras.")
            
            # --- VALIDACIÓN DE CÉDULA (JAVIER) ---
        while True:
            cedula = input("Escriba la cédula del cliente: ").strip()
            if cedula.isdigit() and 7 <= len(cedula) <= 10:
                print(f"✅ Cédula {cedula} registrada correctamente.")
                break
            
            else:
                registrar_log(f"Cédula inválida: {cedula}")
                print("❌ ERROR: La cédula debe ser solo números (entre 7 y 10 dígitos).")
        # --- PUENTE DE CONEXIÓN ---
        print(f"\nRegistro exitoso para {nombre}")
        
        try:
            menu_servicios()
        except Exception as e:
            registrar_log(f"error en menú servicios: {e}")
            print("❌ error al cargar servicios.")
        
    except ErrorSoftwareFJ as e:
        print(f"Hubo un error: {e}")
        registrar_log(str(e))
    except Exception as e:
        print(f"Falla del sistema: {e}")
        registrar_log(f"Falla crítica: {e}")
    finally:
        print("Proceso terminado.")

if __name__ == "__main__":
    iniciar_sistema()
 
#============================================================
# CLASE ABSTRACTA SERVICIO
#============================================================
# Uso ABC para indicar que será una plantilla de la que heredarán los demás servicios
class Servicio(ABC):     
    # Indico que todo servicio que herede de esta clase deberá implementar su propia forma de calcular costos
    @abstractmethod 
    def calcular_costo(self):
        pass
    
     # Indico que cada servicio deberá poder describirse mostrando información sobre lo que ofrece
    @abstractmethod
    def describir(self):
        pass
    
     # Indico que cada servicio deberá validar que los datos recibidos sean correctos
    @abstractmethod
    def validar_parametros(self):
        pass
    
#------------------------------------------------------------
# CLASE ReservaSala que hereda de Servicio 
#------------------------------------------------------------
class ReservaSala(Servicio):
    # Inicializo los datos principales del servicio y valido que la información ingresada sea correcta.
    def __init__ (self, nombre, costo_por_hora):
        self.nombre = nombre
        self.costo_por_hora = costo_por_hora
        self.validar_parametros()
    
    # Calculo el costo total de la reserva según las horas solicitadas
    def calcular_costo(self, horas):
        if not isinstance(horas, (int, float)):
            raise ErrorSoftwareFJ("Las horas deben ser un valor numérico.")
        
        if horas <= 0:
            raise ErrorSoftwareFJ("Las horas deben ser mayores que cero.")
        return self.costo_por_hora * horas
    
    # Muestro una descripción del servicio de reserva de salas
    def describir(self):
        return f"Servicio de reserva de sala: {self.nombre}"
    
    # Valido que los datos del servicio sean correctos
    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorSoftwareFJ("El nombre del servicio no es válido.")
        
        if not isinstance(self.costo_por_hora, (int, float)):
            raise ErrorSoftwareFJ("El costo debe ser numérico.")
        
        if self.costo_por_hora <= 0:
            raise ErrorSoftwareFJ("El costo por hora debe ser mayor que cero.")
        
#------------------------------------------------------------    
# CLASE AlquilerEquipos que hereda de Servicio
#------------------------------------------------------------
class AlquilerEquipos(Servicio):
    # Inicializo los datos principales del servicio y valido que la información ingresada sea correcta.
    def __init__(self, nombre, costo_por_dia):
        self.nombre = nombre
        self.costo_por_dia = costo_por_dia
        self.validar_parametros()
        
    # Calculo el costo total del alquiler según los días solicitados
    def calcular_costo(self, dias):
        if not isinstance(dias, (int, float)):
            raise ErrorSoftwareFJ("Los días deben ser un valor numérico.")
        
        if dias <= 0:
            raise ErrorSoftwareFJ("Los días deben ser mayores que cero.")
        return self.costo_por_dia * dias
    
    # Muestro una descripción del servicio de alquiler de equipos
    def describir(self):
        return f"Servicio de alquiler de equipos: {self.nombre}"
    
    # Valido que los datos del servicio sean correctos
    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorSoftwareFJ("El nombre del servicio no es válido.")
        
        if not isinstance(self.costo_por_dia, (int, float)):
            raise ErrorSoftwareFJ("El costo debe ser numérico.")
        
        if self.costo_por_dia <= 0:
            raise ErrorSoftwareFJ("El costo por día debe ser mayor que cero.")
    
#------------------------------------------------------------
# CLASE Asesoria que hereda de Servicio 
#------------------------------------------------------------
class Asesoria(Servicio):
    # Inicializo los datos principales del servicio y valido que la información ingresada sea correcta.
    def __init__(self,nombre, tarifa_por_sesion):
        self.nombre = nombre
        self.tarifa_por_sesion = tarifa_por_sesion
        self.validar_parametros()
    
    # Calculo el costo total de la asesoría según las sesiones solicitadas
    def calcular_costo(self, sesiones):
        if not isinstance(sesiones, (int, float)):
            raise ErrorSoftwareFJ("Las sesiones deben ser un valor numérico.")
        
        if sesiones <= 0:
            raise ErrorSoftwareFJ("Las sesiones deben ser mayores que cero.")
        return self.tarifa_por_sesion * sesiones
    
    # Muestro una descripción del servicio de asesoría
    def describir(self):
        return f"Servicio de asesorías especializadas: {self.nombre}"
    
    # Valido que los datos del servicio sean correctos
    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorSoftwareFJ("El nombre del servicio no es válido.")
        
        if not isinstance(self.tarifa_por_sesion, (int, float)):
            raise ErrorSoftwareFJ("La tarifa por sesión debe ser numérica.")
        
        if self.tarifa_por_sesion <= 0:
            raise ErrorSoftwareFJ("La tarifa por sesión debe ser mayor que cero.")

import logging
from datetime import datetime

# CONFIGURACION DEL LOG
logging.basicConfig(
    filename="sistema_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# EXCEPCIONES PERSONALIZADAS
class ReservaError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass


# CLASE RESERVA
class Reserva:

    ESTADOS_VALIDOS = ["Pendiente", "Confirmada", "Cancelada", "Procesada"]

    def __init__(self, cliente, servicio, duracion):

        try:
            if cliente is None:
                raise ValueError("El cliente no puede ser nulo")

            if servicio is None:
                raise ValueError("El servicio no puede ser nulo")

            if duracion <= 0:
                raise ValueError("La duración debe ser mayor a cero")

            self.__cliente = cliente
            self.__servicio = servicio
            self.__duracion = duracion
            self.__estado = "Pendiente"
            self.__fecha = datetime.now()

            logging.info("Reserva creada correctamente")

        except Exception as e:
            logging.error(f"Error al crear reserva: {e}")
            raise ReservaError("No se pudo crear la reserva") from e

    # GETTERS
    @property
    def estado(self):
        return self.__estado

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    # CONFIRMAR RESERVA
    def confirmar(self):

        try:
            if self.__estado == "Cancelada":
                raise ReservaError(
                    "No se puede confirmar una reserva cancelada"
                )

            self.__estado = "Confirmada"

            logging.info("Reserva confirmada correctamente")

        except Exception as e:
            logging.error(f"Error al confirmar reserva: {e}")
            print("Error:", e)

    # CANCELAR RESERVA
    def cancelar(self):

        try:
            if self.__estado == "Procesada":
                raise ReservaError(
                    "No se puede cancelar una reserva procesada"
                )

            self.__estado = "Cancelada"

            logging.info("Reserva cancelada")

        except Exception as e:
            logging.error(f"Error al cancelar reserva: {e}")
            print("Error:", e)

    # PROCESAR RESERVA
    def procesar(self):

        try:
            if self.__estado != "Confirmada":
                raise ReservaError(
                    "La reserva debe estar confirmada"
                )

            costo = self.__servicio.calcular_costo(
                self.__duracion
            )

            self.__estado = "Procesada"

            logging.info(
                f"Reserva procesada correctamente. Total: ${costo}"
            )

            print("Reserva procesada correctamente")
            print(f"Costo total: ${costo}")

        except ServicioNoDisponibleError as e:
            logging.error(f"Servicio no disponible: {e}")

        except Exception as e:
            logging.error(f"Error al procesar reserva: {e}")
            print("Error:", e)

        finally:
            print("Proceso de reserva finalizado")

class Serviciocosto:

    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    # CALCULO BASICO
    def calcular_costo(self, duracion):
        return self.precio_base * duracion

    # CALCULO CON IMPUESTO
    def calcular_costo_impuesto(self, duracion, impuesto):

        subtotal = self.precio_base * duracion

        return subtotal + (subtotal * impuesto)

    # CALCULO CON DESCUENTO
    def calcular_costo_descuento(self, duracion, descuento):

        subtotal = self.precio_base * duracion

        return subtotal - descuento

    # CALCULO COMPLETO
    def calcular_costo_total(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        subtotal = self.precio_base * duracion

        total = subtotal + (subtotal * impuesto) - descuento

        return total