"""
Ejemplo real de clase con decoradores múltiples
"""
import functools
import time
from datetime import datetime
from performance_decorators import medir_tiempo
from logging_decorators import log_calls
from retry_decorators import retry

class GestorAPI:
    def __init__(self, base_url: str, max_reintentos: int = 3):
        self.base_url = base_url
        self.max_reintentos = max_reintentos
        self._cache = {}
        self._request_count = 0

    @property
    def request_count(self) -> int:
        return self._request_count

    @medir_tiempo
    @log_calls
    @retry(max_intentos=3)
    def hacer_peticion(self, endpoint: str):
        self._request_count += 1
        import random
        if random.random() < 0.3:
            raise ConnectionError("Fallo de red simulado")
        return {
            'status': 'success',
            'data': f'Datos de {endpoint}',
            'timestamp': datetime.now().isoformat()
        }

    @functools.lru_cache(maxsize=64)
    def obtener_configuracion(self, tipo: str):
        time.sleep(0.1)
        return {
            'tipo': tipo,
            'configuracion': f'Config para {tipo}',
            'version': '1.0'
        }

# Usar la clase
gestor = GestorAPI("https://api.ejemplo.com")

try:
    # Petición con todos los decoradores activos
    resultado = gestor.hacer_peticion("usuarios")
    print(f"Resultado: {resultado['status']}")
    
    # Cache en acción
    config1 = gestor.obtener_configuracion("produccion")
    config2 = gestor.obtener_configuracion("produccion")  # Desde cache
    
    print(f"Peticiones realizadas: {gestor.request_count}")
    print(f"Cache info: {gestor.obtener_configuracion.cache_info()}")
    
except Exception as e:
    print(f"Error final: {e}")

print("\n" + "="*60)