"""
Decoradores de validación y control de acceso: requiere_autenticacion, validar_tipos
"""
import functools
from datetime import datetime
from typing import Dict

def requiere_autenticacion(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        usuario_autenticado = kwargs.get('usuario_id') is not None
        if not usuario_autenticado:
            raise PermissionError(f"Acceso denegado a {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def validar_tipos(**tipos):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for nombre, tipo_esperado in tipos.items():
                if nombre in kwargs:
                    valor = kwargs[nombre]
                    if not isinstance(valor, tipo_esperado):
                        raise TypeError(
                            f"{nombre} debe ser {tipo_esperado.__name__}, "
                            f"recibió {type(valor).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorador

@requiere_autenticacion
@validar_tipos(edad=int, nombre=str)
def crear_perfil(nombre: str, edad: int, usuario_id: int = None) -> Dict:
    return {
        'nombre': nombre,
        'edad': edad,
        'usuario_id': usuario_id,
        'creado_en': datetime.now()
    }


# Uso exitoso
perfil = crear_perfil(nombre="Juan", edad=30, usuario_id=123)
print(f"Perfil creado: {perfil.get('nombre')}, Edad: {perfil.get('edad')}, Usuario ID: {perfil.get('usuario_id')}")

#Uso no exitoso Acceso Denegado
try:
    crear_perfil(nombre="Ana", edad=30, usuario_id=None) 
except Exception as e:
    print(f"Error: {e}")

#Uso no exitoso Tipo Incorrecto
try:
    crear_perfil(nombre="Ana", edad="treinta", usuario_id=456)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60)
