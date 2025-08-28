# TIPOS NUMÉRICOS
print("=== TIPOS NUMÉRICOS ===")

# int - Números enteros
entero = 42
entero_negativo = -17
entero_cero = 0
print(f"int: {entero}, {entero_negativo}, {entero_cero}")
print(f"Tipo: {type(entero)}")

# float - Números decimales
decimal = 3.14
decimal_negativo = -0.5
notacion_cientifica = 2e3  # 2000.0
print(f"float: {decimal}, {decimal_negativo}, {notacion_cientifica}")
print(f"Tipo: {type(decimal)}")

# complex - Números complejos
complejo1 = 3 + 4j
complejo2 = complex(1, -2)  # 1 - 2j
print(f"complex: {complejo1}, {complejo2}")
print(f"Tipo: {type(complejo1)}")

# TIPOS DE TEXTO
print("\n=== TIPOS DE TEXTO ===")

# str - Cadenas de texto
texto1 = "Hola mundo"
texto2 = 'Python es genial'
texto3 = """Este es un
texto multilínea"""
texto4 = f"Interpolación: {entero}"
print(f"str: {repr(texto1)}, {repr(texto2)}")
print(f"Texto multilínea: {repr(texto3)}")
print(f"F-string: {texto4}")
print(f"Tipo: {type(texto1)}")

# TIPOS BOOLEANOS
print("\n=== TIPOS BOOLEANOS ===")

# bool - Valores booleanos
verdadero = True
falso = False
resultado_comparacion = 5 > 3
print(f"bool: {verdadero}, {falso}, {resultado_comparacion}")
print(f"Tipo: {type(verdadero)}")

# TIPOS DE SECUENCIA
print("\n=== TIPOS DE SECUENCIA ===")

# list - Listas mutables
lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c']
lista_mixta = [1, 'texto', True, 3.14]
lista_vacia = []
print(f"list: {lista1}")
print(f"Lista mixta: {lista_mixta}")
print(f"Tipo: {type(lista1)}")

# Demostrar mutabilidad
lista1.append(6)
print(f"Después de append: {lista1}")

# tuple - Tuplas inmutables
tupla1 = (1, 2, 3, 4, 5)
tupla2 = ('x', 'y', 'z')
tupla_unitaria = (42,)  # Coma necesaria para tupla de un elemento
tupla_sin_parentesis = 1, 2, 3  # También es válido
tupla_vacia = ()
print(f"tuple: {tupla1}")
print(f"Tupla unitaria: {tupla_unitaria}")
print(f"Sin paréntesis: {tupla_sin_parentesis}")
print(f"Tipo: {type(tupla1)}")

# range - Secuencias numéricas
rango1 = range(5)  # 0 a 4
rango2 = range(1, 10, 2)  # 1, 3, 5, 7, 9
print(f"range: {list(rango1)}")  # Convertir a lista para mostrar
print(f"range con paso: {list(rango2)}")
print(f"Tipo: {type(rango1)}")

# TIPOS DE MAPEO
print("\n=== TIPOS DE MAPEO ===")

# dict - Diccionarios
diccionario1 = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
diccionario2 = {1: 'uno', 2: 'dos', 3: 'tres'}
dict_vacio = {}
dict_comprehension = {x: x**2 for x in range(5)}
print(f"dict: {diccionario1}")
print(f"Dict con keys numéricas: {diccionario2}")
print(f"Dict comprehension: {dict_comprehension}")
print(f"Tipo: {type(diccionario1)}")

# TIPOS DE CONJUNTO
print("\n=== TIPOS DE CONJUNTO ===")

# set - Conjuntos mutables
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {'a', 'b', 'c'}
conjunto_desde_lista = set([1, 2, 2, 3, 3, 4])  # Elimina duplicados
conjunto_vacio = set()  # No usar {} que crea dict vacío
print(f"set: {conjunto1}")
print(f"Desde lista (sin duplicados): {conjunto_desde_lista}")
print(f"Tipo: {type(conjunto1)}")

# frozenset - Conjuntos inmutables
frozen1 = frozenset([1, 2, 3, 4])
frozen2 = frozenset('abcd')
print(f"frozenset: {frozen1}")
print(f"Frozenset desde string: {frozen2}")
print(f"Tipo: {type(frozen1)}")

# TIPOS ESPECIALES
print("\n=== TIPOS ESPECIALES ===")

# NoneType - Ausencia de valor
nulo = None
print(f"NoneType: {nulo}")
print(f"Tipo: {type(nulo)}")

# bytes - Secuencias inmutables de bytes
bytes1 = b'hello'
bytes2 = bytes([65, 66, 67])  # ABC en ASCII
bytes3 = 'español'.encode('utf-8')
print(f"bytes: {bytes1}")
print(f"Desde lista: {bytes2}")
print(f"Desde string: {bytes3}")
print(f"Tipo: {type(bytes1)}")

# bytearray - Secuencias mutables de bytes
bytearray1 = bytearray(b'hello')
bytearray2 = bytearray([65, 66, 67])
print(f"bytearray: {bytearray1}")
print(f"Tipo: {type(bytearray1)}")

# Demostrar mutabilidad
bytearray1[0] = 72  # Cambiar 'h' por 'H'
print(f"Después de modificar: {bytearray1}")

# TIPOS DE FUNCIÓN
print("\n=== TIPOS DE FUNCIÓN ===")

# function - Funciones definidas por el usuario
def mi_funcion(x, y):
    """Función de ejemplo"""
    return x + y

print(f"function: {mi_funcion}")
print(f"Tipo: {type(mi_funcion)}")
print(f"Resultado: {mi_funcion(3, 4)}")

# builtin_function_or_method - Funciones integradas
print(f"builtin function: {len}")
print(f"Tipo: {type(len)}")
print(f"Resultado: {len('hello')}")

# method - Métodos de objetos
lista_ejemplo = [1, 2, 3]
metodo_append = lista_ejemplo.append
print(f"method: {metodo_append}")
print(f"Tipo: {type(metodo_append)}")

# VERIFICACIÓN DE TIPOS
print("\n=== VERIFICACIÓN DE TIPOS ===")

# Usando type()
print(f"type(42): {type(42)}")
print(f"type('hello'): {type('hello')}")

# Usando isinstance() - más recomendado
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance('hello', str): {isinstance('hello', str)}")
print(f"isinstance([1,2,3], (list, tuple)): {isinstance([1,2,3], (list, tuple))}")

# CONVERSIONES ENTRE TIPOS
print("\n=== CONVERSIONES ENTRE TIPOS ===")

numero_str = "123"
numero_int = int(numero_str)
numero_float = float(numero_str)
print(f"String a int: '{numero_str}' -> {numero_int}")
print(f"String a float: '{numero_str}' -> {numero_float}")

lista_a_tupla = tuple([1, 2, 3])
tupla_a_lista = list((4, 5, 6))
print(f"Lista a tupla: {lista_a_tupla}")
print(f"Tupla a lista: {tupla_a_lista}")

string_a_lista = list("Python")
lista_a_string = ''.join(['P', 'y', 't', 'h', 'o', 'n'])
print(f"String a lista: {string_a_lista}")
print(f"Lista a string: {lista_a_string}")

# CASOS ESPECIALES Y CURIOSIDADES
print("\n=== CASOS ESPECIALES ===")

# Todo en Python es un objeto
print(f"Tipo de type: {type(type)}")
print(f"Tipo de None: {type(type(None))}")

# Los números muy grandes siguen siendo int en Python 3
numero_grande = 123456789012345678901234567890
print(f"Número grande: {numero_grande}")
print(f"Tipo: {type(numero_grande)}")

# Las operaciones pueden cambiar el tipo
division_entera = 10 // 3  # int
division_decimal = 10 / 3  # float
print(f"División entera: {division_entera} (tipo: {type(division_entera)})")
print(f"División decimal: {division_decimal} (tipo: {type(division_decimal)})")