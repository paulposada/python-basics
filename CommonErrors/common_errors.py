# Un malentendido de cómo funcionan las = y las referencias. Piensan que hace copias, y que reasignar referencias en funciones va a afectar al argumento pasado.
# Usa argumentos por defecto mutables sin entender por qué casi siempre es una mala idea.
# No cierra los recursos cuando termina con ellos/no usa with para gestionar recursos cuando with es apropiado.
# Usa list comprehensions para hacer efectos secundarios en vez de para producir una lista.
# No sigue PEP8 ni ninguna guía de estilo consistentemente.
# Usa except: sin entender por qué es tan peligroso.
#     Y, atrapa excepciones pero no maneja el error correctamente.
# Usa for i in range(len(coll)): en vez de for elem in coll: cuando lo segundo es más apropiado.

# ===================================================================
# ERROR 1: Malentender cómo funcionan las asignaciones y referencias
# ===================================================================

print("=== ERROR 1: Referencias vs Copias ===")

# ❌ INCORRECTO - Malentendido común
lista_original = [1, 2, 3]
lista_copia = lista_original  # ¡NO es una copia!
lista_copia.append(4)
print(f"Original después de 'copia': {lista_original}")  # [1, 2, 3, 4] ¡Cambió!

# ✅ CORRECTO - Hacer copias reales
lista_original = [1, 2, 3]
lista_copia_real = lista_original.copy()  # o lista_original[:]
lista_copia_real.append(4)
print(f"Original con copia real: {lista_original}")  # [1, 2, 3] ¡No cambió!

# ❌ INCORRECTO - Pensar que reasignar en funciones afecta el original
def intento_modificar_mal(numero, lista):
    numero = 100  # ¡Esto NO modifica el original!
    lista = [100, 200]  # ¡Esto tampoco!

x = 10
mi_lista = [1, 2, 3]
intento_modificar_mal(x, mi_lista)
print(f"Después de función mal: x={x}, lista={mi_lista}")  # No cambiaron

# ✅ CORRECTO - Modificar el contenido, no reasignar
def modificar_bien(lista):
    lista.append(100)  # Modifica el contenido
    lista[0] = 999     # Modifica elemento existente

mi_lista = [1, 2, 3]
modificar_bien(mi_lista)
print(f"Después de función bien: {mi_lista}")  # [999, 2, 3, 100]

print("\n" + "="*60)

# ===================================================================
# ERROR 2: Argumentos por defecto mutables
# ===================================================================

print("=== ERROR 2: Argumentos por defecto mutables ===")

# ❌ INCORRECTO - Argumento mutable por defecto
def agregar_mal(elemento, lista=[]):  # ¡PELIGRO!
    lista.append(elemento)
    return lista

print(agregar_mal(1))  # [1]
print(agregar_mal(2))  # [1, 2] ¡La misma lista!
print(agregar_mal(3))  # [1, 2, 3] ¡Sigue creciendo!

# ✅ CORRECTO - Usar None y crear nueva lista
def agregar_bien(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

print(agregar_bien(1))  # [1]
print(agregar_bien(2))  # [2] ¡Nueva lista!
print(agregar_bien(3))  # [3] ¡Cada llamada es independiente!

# Otro ejemplo común con diccionarios
# ❌ INCORRECTO
def crear_config_mal(clave, valor, config={}):  # ¡PELIGRO!
    config[clave] = valor
    return config

config1 = crear_config_mal('a', 1)
config2 = crear_config_mal('b', 2)
print(f"Config1: {config1}")  # {'a': 1, 'b': 2} ¡Compartido!
print(f"Config2: {config2}")  # {'a': 1, 'b': 2} ¡El mismo!

# ✅ CORRECTO
def crear_config_bien(clave, valor, config=None):
    if config is None:
        config = {}
    config[clave] = valor
    return config

print("\n" + "="*60)

# ===================================================================
# ERROR 3: No cerrar recursos / No usar 'with'
# ===================================================================

print("=== ERROR 3: Gestión de recursos ===")

# ❌ INCORRECTO - No cerrar archivos
def leer_archivo_mal(nombre):
    archivo = open(nombre, 'r')
    contenido = archivo.read()
    # ¡Olvida cerrar el archivo!
    return contenido

# ❌ LIGERAMENTE MEJOR - Cerrar manualmente (pero puede fallar)
def leer_archivo_regular(nombre):
    archivo = open(nombre, 'r')
    try:
        contenido = archivo.read()
        return contenido
    finally:
        archivo.close()  # Al menos se cierra

# ✅ CORRECTO - Usar 'with'
def leer_archivo_bien(nombre):
    with open(nombre, 'r') as archivo:
        contenido = archivo.read()
        return contenido
    # El archivo se cierra automáticamente

# Ejemplo práctico (simulado)
import tempfile
import os

# Crear archivo temporal para demostrar
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
    temp.write("Contenido de ejemplo")
    temp_name = temp.name

# ✅ CORRECTO - Múltiples archivos con 'with'
def procesar_archivos_bien(archivo1, archivo2):
    with open(archivo1, 'r') as f1, open(archivo2, 'w') as f2:
        contenido = f1.read()
        f2.write(contenido.upper())

# Limpiar archivo temporal
os.unlink(temp_name)

print("\n" + "="*60)

# ===================================================================
# ERROR 4: List comprehensions para efectos secundarios
# ===================================================================

print("=== ERROR 4: List comprehensions mal usadas ===")

numeros = [1, 2, 3, 4, 5]

# ❌ INCORRECTO - Usar list comprehension solo por efectos secundarios
resultados_ignorados = [print(f"Número: {n}") for n in numeros]
print(f"Lista resultante inútil: {resultados_ignorados}")  # [None, None, ...]

# ✅ CORRECTO - Usar for loop para efectos secundarios
print("Forma correcta:")
for numero in numeros:
    print(f"Número: {numero}")

# ✅ CORRECTO - List comprehension para crear lista
cuadrados = [n**2 for n in numeros]
print(f"Cuadrados: {cuadrados}")

# ❌ INCORRECTO - Modificar lista externa en comprehension
lista_externa = []
# ¡Confuso y poco legible!
basura = [lista_externa.append(n*2) for n in numeros]

# ✅ CORRECTO - Ser explícito
lista_externa = []
for n in numeros:
    lista_externa.append(n*2)

print("\n" + "="*60)

# ===================================================================
# ERROR 5: No seguir PEP8 / Estilo inconsistente
# ===================================================================

print("=== ERROR 5: Problemas de estilo (PEP8) ===")

# ❌ INCORRECTO - Estilo inconsistente
def funcionMal(primerArgumento,segundoArgumento=None):
    if segundoArgumento==None:
        variable_muy_larga_con_nombre_malo=primerArgumento*2
        return variable_muy_larga_con_nombre_malo
    else:
        return primerArgumento+segundoArgumento

# ✅ CORRECTO - Siguiendo PEP8
def funcion_bien(primer_argumento, segundo_argumento=None):
    """Función que sigue las convenciones de PEP8."""
    if segundo_argumento is None:
        resultado = primer_argumento * 2
        return resultado
    else:
        return primer_argumento + segundo_argumento

# Más ejemplos de PEP8:
# ❌ INCORRECTO
lista_mal_espaciada=[1,2,3,4,5]
diccionario_mal={'clave1':'valor1','clave2':'valor2'}

# ✅ CORRECTO
lista_bien_espaciada = [1, 2, 3, 4, 5]
diccionario_bien = {'clave1': 'valor1', 'clave2': 'valor2'}

# ❌ INCORRECTO - Líneas muy largas
cadena_muy_larga = "Esta es una cadena extremadamente larga que definitivamente excede los 79 caracteres recomendados por PEP8"

# ✅ CORRECTO - Dividir líneas largas
cadena_bien_dividida = (
    "Esta es una cadena extremadamente larga que se ha dividido "
    "correctamente para cumplir con PEP8"
)

print("\n" + "="*60)

# ===================================================================
# ERROR 6: Uso peligroso de except
# ===================================================================

print("=== ERROR 6: Manejo peligroso de excepciones ===")

# ❌ INCORRECTO - except: sin especificar
def operacion_peligrosa(a, b):
    try:
        resultado = a / b
        return resultado
    except:  # ¡PELIGROSO! Atrapa TODO
        return 0  # ¿Qué pasó? ¿División por cero? ¿TypeError? ¿KeyboardInterrupt?

# ✅ CORRECTO - Ser específico con las excepciones
def operacion_segura(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return None

print(f"Operación peligrosa: {operacion_peligrosa(10, 0)}")
print(f"Operación segura: {operacion_segura(10, 0)}")

# ❌ INCORRECTO - Atrapar pero no manejar
def leer_archivo_mal_manejo(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass  # ¡Silencia el error sin manejarlo!

# ✅ CORRECTO - Manejar apropiadamente
def leer_archivo_buen_manejo(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Archivo {archivo} no encontrado")
        return ""
    except PermissionError:
        print(f"Sin permisos para leer {archivo}")
        return ""
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise  # Re-lanza si no sabemos qué hacer

print("\n" + "="*60)

# ===================================================================
# ERROR 7: for i in range(len()) innecesario
# ===================================================================

print("=== ERROR 7: Iteración innecesariamente complicada ===")

frutas = ['manzana', 'banana', 'cereza', 'durazno']

# ❌ INCORRECTO - Usar índices cuando no es necesario
print("Forma incorrecta:")
for i in range(len(frutas)):
    print(f"Fruta: {frutas[i]}")

# ✅ CORRECTO - Iterar directamente
print("\nForma correcta:")
for fruta in frutas:
    print(f"Fruta: {fruta}")

# ✅ CORRECTO - Cuando SÍ necesitas el índice
print("\nCuando sí necesitas el índice:")
for i, fruta in enumerate(frutas):
    print(f"Posición {i}: {fruta}")

# ❌ INCORRECTO - Modificar lista durante iteración por índice
numeros = [1, 2, 3, 4, 5, 6]
print(f"\nLista original: {numeros}")

# Esto puede causar problemas
numeros_copia = numeros.copy()
for i in range(len(numeros_copia)):
    if numeros_copia[i] % 2 == 0:
        numeros_copia.pop(i)  # ¡Problemático! Los índices cambian

# ✅ CORRECTO - Varias formas mejores
numeros = [1, 2, 3, 4, 5, 6]

# Opción 1: List comprehension
impares_solo = [n for n in numeros if n % 2 != 0]
print(f"Solo impares (comprehension): {impares_solo}")

# Opción 2: filter
impares_filter = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Solo impares (filter): {impares_filter}")

# Opción 3: Iterar sobre copia si necesitas modificar original
numeros_modificable = [1, 2, 3, 4, 5, 6]
for numero in numeros_modificable.copy():
    if numero % 2 == 0:
        numeros_modificable.remove(numero)
print(f"Original modificado: {numeros_modificable}")

print("\n" + "="*60)
