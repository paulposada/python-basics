"""
Decoradores de rendimiento: medir_tiempo, lru_cache, cache
"""
import functools
import time

# Decorador de timing
def medir_tiempo(func):
    """Mide el tiempo de ejecución de una función."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    time.sleep(0.1)
    return sum(range(100000))

resultado = operacion_lenta()
print("\n" + "="*60)

# lru_cache
def fibonacci_optimizado(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_optimizado(n-1) + fibonacci_optimizado(n-2)
fibonacci_optimizado = functools.lru_cache(maxsize=128)(fibonacci_optimizado)

# cache (Python 3.9+)
@functools.cache
def calculo_pesado(n: int) -> int:
    print(f"Calculando para n={n}...")
    return n ** 2 + n ** 3

# Sin cache sería lentísimo para n=40
print(f"Fibonacci(35): {fibonacci_optimizado(35)}")
print(f"Info del cache: {fibonacci_optimizado.cache_info()}")
print("\n" + "="*60)
