"""
Decoradores de logging y debugging: log_calls
"""
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_calls(func):
    """Loggea todas las llamadas a la función."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        logger.info(f"Llamando {func.__name__}({all_args})")
        try:
            resultado = func(*args, **kwargs)
            logger.info(f"{func.__name__} retornó: {repr(resultado)}")
            return resultado
        except Exception as e:
            logger.error(f"{func.__name__} lanzó excepción: {e}")
            raise
    return wrapper

@log_calls
def dividir(a: float, b: float) -> float:
    return a / b

# Prueba con logging
resultado = dividir(10, 2)
try:
    dividir(10, 0)  # Genera excepción loggeada
except ZeroDivisionError:
    pass

print("\n" + "="*60)