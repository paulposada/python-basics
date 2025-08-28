"""
Decoradores de retry y manejo de errores: retry
"""
import functools
import time

def retry(max_intentos: int = 3, delay: float = 1.0, excepciones: tuple = (Exception,)):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ultimo_error = None
            for intento in range(max_intentos):
                try:
                    return func(*args, **kwargs)
                except excepciones as e:
                    ultimo_error = e
                    if intento < max_intentos - 1:
                        print(f"Intento {intento + 1} falló: {e}. Reintentando en {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"Todos los intentos fallaron.")
            raise ultimo_error
        return wrapper
    return decorador

@retry(max_intentos=3, delay=0.5, excepciones=(ConnectionError, TimeoutError))
def operacion_inestable(probabilidad_fallo: float = 0.7) -> str:
    import random
    if random.random() < probabilidad_fallo:
        raise ConnectionError("Fallo de conexión simulado")
    return "Operación exitosa"


# Prueba del retry
try:
    resultado = operacion_inestable()
    print(resultado)
except Exception as e:
    print(f"Falló después de todos los intentos: {e}")

print("\n" + "="*60)