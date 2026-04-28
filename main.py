import datetime

# 1. ESCUDO: Para que el programa no se cierre si hay errores
class ErrorSoftwareFJ(Exception):
    pass

# 2. CHISMOSO: Para anotar los fallos en un bloc de notas
def registrar_log(mensaje):
    with open("log_errores.txt", "a") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] ERROR: {mensaje}\n")

# 3. EL PROGRAMA
def iniciar_sistema():
    try:
        print("--- SISTEMA SOFTWARE FJ - TRABAJO DE JAVIER ---")
        nombre = input("Escriba el nombre del cliente: ")
        
        if not nombre.strip():
            raise ErrorSoftwareFJ("No escribió ningún nombre.")
            
        print(f"Cliente {nombre} registrado correctamente.")

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