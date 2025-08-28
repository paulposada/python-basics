# ===================================================================
# ERROR 1: No usar entornos virtuales ni requirements
# ===================================================================

print("=== ERROR 1: Entornos virtuales y dependencias ===")

"""
❌ PROBLEMAS COMUNES:
- Instalar paquetes directamente en el sistema: pip install requests
- No documentar dependencias
- "Funciona en mi máquina" pero no en otras
- Conflictos de versiones entre proyectos

✅ SOLUCIÓN CORRECTA:

# Crear entorno virtual
python -m venv mi_proyecto_env

# Activar (Linux/Mac)
source mi_proyecto_env/bin/activate

# Activar (Windows)
mi_proyecto_env\Scripts\activate

# Instalar dependencias
pip install requests==2.28.1

# Generar requirements.txt
pip freeze > requirements.txt

# En otro lugar, instalar desde requirements
pip install -r requirements.txt

EJEMPLO DE requirements.txt:
requests==2.28.1
flask==2.2.2
python-dotenv==0.19.2
"""

print("Siempre usa entornos virtuales para cada proyecto!")

print("\n" + "="*60)

# ===================================================================
# ERROR 2: No entender [key] vs .get(key, default)
# ===================================================================

print("=== ERROR 2: Acceso a diccionarios ===")

usuario = {
    'nombre': 'Juan',
    'edad': 30,
    'email': 'juan@email.com'
}

# ❌ INCORRECTO - Puede causar KeyError
try:
    telefono = usuario['telefono']  # ¡CRASH! KeyError
except KeyError:
    telefono = None
print(f"Teléfono (forma mala): {telefono}")

# ✅ CORRECTO - Usar .get() con valor por defecto
telefono = usuario.get('telefono', 'No disponible')
print(f"Teléfono (forma buena): {telefono}")

# Ejemplos prácticos
config = {'debug': True, 'port': 8000}

# ❌ INCORRECTO - Código frágil
def configurar_servidor_mal():
    try:
        debug_mode = config['debug']
        puerto = config['port']
        host = config['host']  # ¡Puede fallar!
        timeout = config['timeout']  # ¡Puede fallar!
    except KeyError as e:
        print(f"Falta configuración: {e}")
        return None

# ✅ CORRECTO - Código robusto
def configurar_servidor_bien():
    debug_mode = config.get('debug', False)
    puerto = config.get('port', 3000)
    host = config.get('host', 'localhost')
    timeout = config.get('timeout', 30)
    
    return {
        'debug': debug_mode,
        'port': puerto, 
        'host': host,
        'timeout': timeout
    }

configurar_servidor_mal()
servidor_config = configurar_servidor_bien()
print(f"Configuración del servidor: {servidor_config}")

# Cuándo usar cada uno:
# - dict[key]: Cuando SABES que la key existe o QUIERES que falle si no existe
# - dict.get(key, default): Cuando la key es opcional

print("\n" + "="*60)

# ===================================================================
# ERROR 3: try/except demasiado amplio
# ===================================================================

print("=== ERROR 3: try/except demasiado amplio ===")

# ❌ INCORRECTO - try/except demasiado amplio
def procesar_datos_mal(archivo, multiplicador):
    try:
        # Abrir archivo
        with open(archivo, 'r') as f:
            datos = f.read()
        
        # Parsear datos
        numeros = [int(x.strip()) for x in datos.split(',')]
        
        # Procesar
        resultado = []
        for num in numeros:
            calculado = num * multiplicador
            resultado.append(calculado)
            
        # Guardar resultado
        with open('resultado.txt', 'w') as f:
            f.write(','.join(map(str, resultado)))
            
        return resultado
        
    except Exception as e:  # ¡Demasiado amplio!
        print(f"Algo salió mal: {e}")
        return []

# ✅ CORRECTO - try/except específicos
def procesar_datos_bien(archivo, multiplicador):
    # Leer archivo con manejo específico
    try:
        with open(archivo, 'r') as f:
            datos = f.read()
    except FileNotFoundError:
        print(f"Archivo {archivo} no encontrado")
        return []
    except PermissionError:
        print(f"Sin permisos para leer {archivo}")
        return []
    
    # Parsear datos con manejo específico
    try:
        numeros = [int(x.strip()) for x in datos.split(',')]
    except ValueError as e:
        print(f"Error al convertir datos a números: {e}")
        return []
    
    # Procesar (sin try/except porque no hay operaciones riesgosas)
    resultado = []
    for num in numeros:
        calculado = num * multiplicador
        resultado.append(calculado)
    
    # Guardar con manejo específico
    try:
        with open('resultado.txt', 'w') as f:
            f.write(','.join(map(str, resultado)))
    except PermissionError:
        print("Sin permisos para escribir archivo resultado")
        # Pero devolvemos el resultado calculado anyway
    
    return resultado

print("El try/except debe ser específico y granular")

print("\n" + "="*60)

# ===================================================================
# ERROR 4: No crear modelos de datos
# ===================================================================

print("=== ERROR 4: Falta de modelos de datos ===")

# ❌ INCORRECTO - Usar diccionarios y listas para todo
def procesar_usuario_mal(usuario_data):
    # ¿Qué campos tiene usuario_data? ¿Cuáles son requeridos?
    # ¿Qué tipo de datos son? ¡No lo sabemos!
    
    nombre = usuario_data.get('nombre', '')
    edad = usuario_data.get('edad', 0)
    email = usuario_data.get('email', '')
    
    # Lógica de validación repetida en muchos lugares
    if not nombre or not email:
        return None
    
    if edad < 0 or edad > 150:
        return None
        
    # ¿Qué devolvemos? ¿Otro diccionario? ¿Una tupla?
    return {
        'nombre_completo': nombre.title(),
        'edad_valida': edad,
        'email_limpio': email.lower().strip()
    }

# ✅ CORRECTO - Usar clases/dataclasses como modelos
from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    """Modelo de datos para un usuario."""
    nombre: str
    edad: int
    email: str
    telefono: Optional[str] = None
    
    def __post_init__(self):
        """Validación automática después de crear el objeto."""
        if not self.nombre or not self.email:
            raise ValueError("Nombre y email son requeridos")
        
        if self.edad < 0 or self.edad > 150:
            raise ValueError("Edad debe estar entre 0 y 150")
        
        # Normalizar datos
        self.nombre = self.nombre.strip().title()
        self.email = self.email.strip().lower()
    
    def es_mayor_de_edad(self) -> bool:
        """Método de negocio."""
        return self.edad >= 18
    
    def obtener_info_contacto(self) -> dict:
        """Obtener información de contacto."""
        contacto = {'email': self.email}
        if self.telefono:
            contacto['telefono'] = self.telefono
        return contacto

# Uso del modelo
try:
    usuario = Usuario(
        nombre="  juan pérez  ",
        edad=25,
        email="  JUAN@EMAIL.COM  "
    )
    print(f"Usuario creado: {usuario}")
    print(f"¿Es mayor de edad? {usuario.es_mayor_de_edad()}")
    print(f"Contacto: {usuario.obtener_info_contacto()}")
except ValueError as e:
    print(f"Error al crear usuario: {e}")

# Ejemplo con Enum para estados
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"

@dataclass
class Pedido:
    id: int
    usuario: Usuario
    productos: list
    estado: EstadoPedido = EstadoPedido.PENDIENTE
    
    def cambiar_estado(self, nuevo_estado: EstadoPedido):
        """Cambiar estado del pedido con validación."""
        if self.estado == EstadoPedido.CANCELADO:
            raise ValueError("No se puede cambiar estado de pedido cancelado")
        self.estado = nuevo_estado

print("\n" + "="*60)

# ===================================================================
# ERROR 5: No entender paquetes y __init__.py
# ===================================================================

print("=== ERROR 5: Paquetes y __init__.py ===")

"""
❌ ESTRUCTURA INCORRECTA:
mi_proyecto/
    main.py
    utilidades.py
    configuracion.py
    modelos.py
    # Todo en un solo directorio, sin organización

✅ ESTRUCTURA CORRECTA:
mi_proyecto/
    main.py
    requirements.txt
    README.md
    mi_proyecto/
        __init__.py
        config/
            __init__.py
            settings.py
        models/
            __init__.py
            usuario.py
            pedido.py
        utils/
            __init__.py
            helpers.py
            validators.py
        api/
            __init__.py
            routes.py

EJEMPLO DE __init__.py:
"""

# En models/__init__.py
"""
from .usuario import Usuario
from .pedido import Pedido, EstadoPedido

# Permite importar así: from models import Usuario, Pedido
# En lugar de: from models.usuario import Usuario

__all__ = ['Usuario', 'Pedido', 'EstadoPedido']
"""

# En config/__init__.py
"""
from .settings import DATABASE_URL, DEBUG_MODE

# Configuración centralizada
__version__ = '1.0.0'
"""

print("Los __init__.py definen qué se puede importar de un paquete")

print("\n" + "="*60)

# ===================================================================
# ERROR 6: Scripts sin if __name__ == "__main__"
# ===================================================================

print("=== ERROR 6: Scripts sin if __name__ == '__main__' ===")

# ❌ INCORRECTO - Código que se ejecuta al importar
def calcular_factorial(n):
    if n <= 1:
        return 1
    return n * calcular_factorial(n - 1)

def main_mal():
    # Este código se ejecuta SIEMPRE, incluso al importar
    numero = 5
    resultado = calcular_factorial(numero)
    print(f"Factorial de {numero} es {resultado}")

# main_mal()  # ¡Se ejecutaría al importar este módulo!

# ✅ CORRECTO - Solo ejecutar si es el script principal
def main_bien():
    """Función principal del script."""
    numero = 5
    resultado = calcular_factorial(numero)
    print(f"Factorial de {numero} es {resultado}")

if __name__ == "__main__":
    # Solo se ejecuta si corremos este archivo directamente
    # No se ejecuta si importamos este módulo
    main_bien()

"""
¿Por qué es importante?

1. REUTILIZACIÓN: Puedes importar funciones sin ejecutar el script
2. TESTING: Los tests pueden importar funciones sin efectos secundarios  
3. MODULARIDAD: El código es más modular y reutilizable

Ejemplo de uso:
# archivo: mi_script.py
def utilidad_importante():
    return "algo útil"

if __name__ == "__main__":
    # Solo corre si ejecutas: python mi_script.py
    print("Ejecutando como script principal")

# En otro archivo:
from mi_script import utilidad_importante  # No ejecuta el print
resultado = utilidad_importante()
"""

print("\n" + "="*60)

# ===================================================================
# ERROR 7: Falta de type hints y mal uso de scope
# ===================================================================

print("=== ERROR 7: Type hints y scope ===")

# ❌ INCORRECTO - Sin tipos, variables globales
contador_global = 0  # Variable global (malo)

def procesar_lista_mal(lista):
    global contador_global  # Modifica estado global
    contador_global += 1
    
    resultado = []
    for item in lista:
        # ¿Qué tipo es item? ¿Qué devuelve la función? ¡No sabemos!
        if item > 5:
            resultado.append(item * 2)
    return resultado

# ✅ CORRECTO - Con type hints y scope apropiado
from typing import List, Optional, Dict, Any

def procesar_numeros_bien(
    numeros: List[int], 
    umbral: int = 5,
    multiplicador: int = 2
) -> List[int]:
    """
    Procesa una lista de números.
    
    Args:
        numeros: Lista de enteros a procesar
        umbral: Valor mínimo para incluir números (default: 5)
        multiplicador: Factor para multiplicar números válidos (default: 2)
    
    Returns:
        Lista de números procesados
        
    Raises:
        ValueError: Si la lista está vacía
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    resultado: List[int] = []
    for numero in numeros:
        if numero > umbral:
            resultado.append(numero * multiplicador)
    
    return resultado

# Ejemplo con clases y types más complejos
class ConfiguradorAPI:
    """Configurador para API con types claros."""
    
    def __init__(self, base_url: str, timeout: int = 30) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self._headers: Dict[str, str] = {}
    
    def agregar_header(self, clave: str, valor: str) -> None:
        """Agrega un header HTTP."""
        self._headers[clave] = valor
    
    def obtener_config(self) -> Dict[str, Any]:
        """Obtiene la configuración completa."""
        return {
            'base_url': self.base_url,
            'timeout': self.timeout,
            'headers': self._headers.copy()
        }
    
    def hacer_peticion(self, endpoint: str) -> Optional[Dict[str, Any]]:
        """Simula una petición HTTP."""
        # En la realidad haría la petición
        print(f"Petición a: {self.base_url}/{endpoint}")
        return {'status': 'ok', 'data': []}

# Uso con types claros
configurador: ConfiguradorAPI = ConfiguradorAPI(
    base_url="https://api.ejemplo.com",
    timeout=60
)
configurador.agregar_header("Authorization", "Bearer token123")

resultado: Optional[Dict[str, Any]] = configurador.hacer_peticion("users")
print(f"Resultado de API: {resultado}")

print("\n" + "="*60)

# ===================================================================
# ERROR 8: Nombres de variables malos
# ===================================================================

print("=== ERROR 8: Nombres de variables ===")

# ❌ INCORRECTO - Nombres terribles
def calcular_mal():
    # Nombres no descriptivos
    d = 10  # ¿Qué es d?
    t = 25  # ¿Qué es t?
    x = d * t  # ¿Qué representa x?
    
    # Inconsistencia de estilo
    primerNumero = 5  # camelCase
    segundo_numero = 3  # snake_case
    TERCERNUMERO = 7  # UPPER_CASE mal usado
    
    # Nombres engañosos
    lista = "no es una lista"  # ¡Es un string!
    numero = [1, 2, 3]  # ¡Es una lista!
    
    return x

# ✅ CORRECTO - Nombres descriptivos y consistentes
def calcular_distancia_bien() -> float:
    """Calcula la distancia recorrida."""
    # Nombres descriptivos
    velocidad_kmh: float = 10.0
    tiempo_horas: float = 2.5
    distancia_km: float = velocidad_kmh * tiempo_horas
    
    # Estilo consistente (snake_case)
    primer_numero: int = 5
    segundo_numero: int = 3
    tercer_numero: int = 7
    
    # Nombres que reflejan el contenido
    numeros_lista: List[int] = [primer_numero, segundo_numero, tercer_numero]
    mensaje_resultado: str = f"Distancia calculada: {distancia_km} km"
    
    print(mensaje_resultado)
    return distancia_km

# Constantes en UPPER_CASE
MAX_INTENTOS: int = 3
TIMEOUT_SEGUNDOS: int = 30
BASE_URL: str = "https://api.ejemplo.com"

# Nombres de clases en PascalCase
class ManejadorConfiguracion:
    """Maneja la configuración de la aplicación."""
    pass

# Nombres de funciones y variables en snake_case
def validar_email_usuario(email: str) -> bool:
    """Valida el formato de un email."""
    return "@" in email and "." in email

resultado_calculo = calcular_distancia_bien()

print("\n" + "="*60)

# ===================================================================
# RESUMEN DE HERRAMIENTAS Y MEJORES PRÁCTICAS
# ===================================================================

print("=== HERRAMIENTAS ESENCIALES ===")

"""
🛠️ ENTORNO DE DESARROLLO:

1. FORMATEADORES:
   - black: Formateo automático de código
   - isort: Organiza imports automáticamente

2. LINTERS:
   - flake8: Encuentra errores de estilo y sintaxis
   - pylint: Análisis más profundo de código
   - mypy: Verificación de type hints

3. ENTORNOS VIRTUALES:
   - venv: Incluido con Python
   - conda: Para ciencia de datos
   - poetry: Gestión moderna de dependencias

4. CONTROL DE VERSIONES:
   - .gitignore apropiado para Python
   - pre-commit hooks para validar código

5. GESTIÓN DE SECRETOS:
   - python-dotenv: Variables de entorno
   - Nunca hardcodear passwords/API keys
   - Usar servicios como HashiCorp Vault

EJEMPLO DE .gitignore:
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
.env
.DS_Store
*.sqlite3
.pytest_cache/
.coverage
dist/
build/
*.egg-info/

EJEMPLO DE .env:
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=tu_api_key_secreta
DEBUG=True
"""

print("Usa estas herramientas para código profesional y mantenible!")