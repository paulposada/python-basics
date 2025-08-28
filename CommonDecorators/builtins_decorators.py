"""
Decoradores built-in: @property, @staticmethod, @classmethod, @functools.wraps
"""
import functools

# @property - El más usado en clases
class Usuario:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
        self._email = None
    
    @property
    def nombre(self) -> str:
        """Getter para nombre."""
        return self._nombre.title()
    
    @nombre.setter 
    def nombre(self, valor: str) -> None:
        """Setter con validación."""
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self, valor: int) -> None:
        if valor < 0 or valor > 150:
            raise ValueError("Edad debe estar entre 0 y 150")
        self._edad = valor
    
    @property 
    def es_mayor_de_edad(self) -> bool:
        """Propiedad calculada."""
        return self._edad >= 18

# Uso
usuario = Usuario("juan pérez", 25)
print(f"Nombre: {usuario.nombre}")  # Se ejecuta el getter
print(f"¿Mayor de edad? {usuario.es_mayor_de_edad}")
print("\n" + "="*60)

# @staticmethod y @classmethod
class Matematicas:
    PI = 3.14159
    
    @staticmethod
    def sumar(a: float, b: float) -> float:
        """Método estático - no necesita instancia ni clase."""
        return a + b
    
    @classmethod
    def crear_desde_radio(cls, radio: float) -> 'Matematicas':
        """Método de clase - constructor alternativo."""
        instancia = cls()
        instancia.radio = radio
        return instancia
    
    @classmethod
    def obtener_pi(cls) -> float:
        """Acceso a variables de clase."""
        return cls.PI

# Uso
print(f"Suma: {Matematicas.sumar(5, 3)}")  # Sin instancia
math_obj = Matematicas.crear_desde_radio(5.0)  # Constructor alternativo
print(f"PI: {Matematicas.obtener_pi()}")
print("\n" + "="*60)

# @functools.wraps - CRÍTICO para decoradores personalizados
def mi_decorador(func):
    """Decorador que preserve metadatos de la función original."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Terminado: {func.__name__}")
        return resultado
    return wrapper

@mi_decorador
def funcion_importante():
    """Esta es una función muy importante."""
    return "resultado"


print(f"Nombre: {funcion_importante.__name__}")  # Preserva 'funcion_importante'
print(f"Docstring: {funcion_importante.__doc__}")  # Preserva docstring
print("\n" + "="*60)