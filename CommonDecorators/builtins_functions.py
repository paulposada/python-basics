"""
Funciones built-in útiles: zip, enumerate, map, filter, reduce, any, all, etc.
"""
from functools import reduce

# zip - Combinar iterables
nombres = ['Ana', 'Bob', 'Carlos']
edades = [25, 30, 35]
ciudades = ['Madrid', 'Barcelona', 'Sevilla']

# Crear diccionarios de personas
personas = [
    dict(zip(['nombre', 'edad', 'ciudad'], persona_data))
    for persona_data in zip(nombres, edades, ciudades)
]

print("Personas creadas con zip:")
for persona in personas:
    print(f"  {persona}")

# enumerate - Índice y valor
print("\nEnumerate con inicio personalizado:")
tareas = ['Diseñar', 'Implementar', 'Probar', 'Desplegar']
for i, tarea in enumerate(tareas, start=1):
    print(f"  Paso {i}: {tarea}")

# map, filter, reduce - Programación funcional
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map - Transformar
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Cuadrados: {cuadrados}")

# filter - Filtrar
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")

# reduce - Reducir a un solo valor
suma_total = reduce(lambda x, y: x + y, numeros)
print(f"Suma total: {suma_total}")

# any, all - Evaluación de condiciones
print(f"¿Algún número es mayor a 8? {any(n > 8 for n in numeros)}")
print(f"¿Todos son menores a 20? {all(n < 20 for n in numeros)}")

print("\n" + "="*60)

print("\n7. FUNCIONES DE INTROSPECCIÓN")

# vars() - Variables de objeto
class Ejemplo:
    def __init__(self):
        self.atributo1 = "valor1"
        self.atributo2 = "valor2"

obj = Ejemplo()
print(f"Variables del objeto: {vars(obj)}")

# dir() - Atributos y métodos disponibles
print(f"Métodos de string disponibles: {[m for m in dir(str) if not m.startswith('_')][:5]}...")

# hasattr, getattr, setattr - Manipulación dinámica de atributos
if hasattr(obj, 'atributo1'):
    valor = getattr(obj, 'atributo1')
    print(f"Valor obtenido dinámicamente: {valor}")

setattr(obj, 'nuevo_atributo', 'nuevo_valor')
print(f"Después de setattr: {vars(obj)}")

# callable() - Verificar si es callable
print(f"¿Es 'print' callable? {callable(print)}")
print(f"¿Es '123' callable? {callable('123')}")

print("\n" + "="*60)

print("\n8. FUNCIONES DE ORDENAMIENTO Y AGRUPACIÓN")

from itertools import groupby
from operator import itemgetter, attrgetter

# sorted con key personalizada
estudiantes = [
    {'nombre': 'Ana', 'edad': 22, 'nota': 8.5},
    {'nombre': 'Bob', 'edad': 24, 'nota': 7.2},
    {'nombre': 'Carlos', 'edad': 23, 'nota': 9.1},
    {'nombre': 'Diana', 'edad': 22, 'nota': 8.8}
]

# Ordenar por múltiples criterios
print("Estudiantes ordenados por edad, luego por nota (desc):")
estudiantes_ordenados = sorted(
    estudiantes, 
    key=lambda x: (x['edad'], -x['nota'])  # Nota negativa para orden descendente
)

for est in estudiantes_ordenados:
    print(f"  {est['nombre']}: {est['edad']} años, nota {est['nota']}")

# itemgetter para ordenamiento más eficiente
print("\nOrdenados por nota (usando itemgetter):")
por_nota = sorted(estudiantes, key=itemgetter('nota'), reverse=True)
for est in por_nota:
    print(f"  {est['nombre']}: {est['nota']}")

# groupby - Agrupar elementos
print("\nAgrupados por edad:")
estudiantes_por_edad = sorted(estudiantes, key=itemgetter('edad'))
for edad, grupo in groupby(estudiantes_por_edad, key=itemgetter('edad')):
    nombres = [est['nombre'] for est in grupo]
    print(f"  {edad} años: {', '.join(nombres)}")

print("\n" + "="*60)

print("\n9. FUNCIONES DE itertools - COMBINATORIAS")

from itertools import combinations, permutations, product, chain, islice

# combinations - Combinaciones
colores = ['rojo', 'verde', 'azul']
print("Combinaciones de 2 colores:")
for combo in combinations(colores, 2):
    print(f"  {combo}")

# product - Producto cartesiano
tallas = ['S', 'M', 'L']
print("\nProducto cartesiano (colores × tallas):")
for producto in list(product(colores[:2], tallas[:2])):  # Limitado para output
    print(f"  {producto}")

# chain - Concatenar iterables
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
concatenada = list(chain(lista1, lista2, lista3))
print(f"\nListas concatenadas: {concatenada}")

# islice - Slice de iterables
print("Primeros 5 números pares:")
numeros_pares = (x for x in range(100) if x % 2 == 0)
primeros_5_pares = list(islice(numeros_pares, 5))
print(f"  {primeros_5_pares}")

print("\n" + "="*60)