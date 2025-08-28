# ¿Por qué las tuplas son inmutables?
# Rendimiento: Son más rápidas que las listas para acceso
# Seguridad: No se pueden modificar accidentalmente
# Hashable: Pueden usarse como claves en diccionarios
# Thread-safe: Seguras en programación concurrente
# Cuándo usar cada una:
# Usa tuplas cuando los datos no deben cambiar (coordenadas, configuraciones, registros)
# Usa listas cuando necesites modificar, insertar o eliminar elementos


# Las tuplas mantienen el orden
tupla1 = (1, 2, 3)
tupla2 = (3, 2, 1)
print(tupla1 == tupla2)  # False - el orden importa

# Acceso por índice
mi_tupla = ('a', 'b', 'c', 'd')
print(mi_tupla[0])   # 'a'
print(mi_tupla[2])   # 'c'
print(mi_tupla[-1])  # 'd' (último elemento)

# El orden se mantiene en iteraciones
for elemento in mi_tupla:
    print(elemento)  # Siempre imprime: a, b, c, d

# Slicing también respeta el orden
print(mi_tupla[1:3])  # ('b', 'c')


mi_tupla = (1, 2, 3)

# Estos intentos fallarán:
# mi_tupla.append(4)        # ERROR: AttributeError
# mi_tupla[0] = 10          # ERROR: TypeError
# mi_tupla.insert(1, 5)     # ERROR: AttributeError
# del mi_tupla[0]           # ERROR: TypeError


# Crear una nueva tupla
tupla_original = (1, 2, 3)
# "Insertar" al final
nueva_tupla = tupla_original + (4,)
print(nueva_tupla)  # (1, 2, 3, 4)

# "Insertar" en una posición específica
tupla_original = (1, 2, 3)
nueva_tupla = tupla_original[:1] + (1.5,) + tupla_original[1:]
print(nueva_tupla)  # (1, 1.5, 2, 3)


# Convertir a lista y modificar
tupla_original = (1, 2, 3)
lista_temporal = list(tupla_original)
lista_temporal.insert(1, 1.5)  # Insertar en posición 1
nueva_tupla = tuple(lista_temporal)
print(nueva_tupla)  # (1, 1.5, 2, 3)


# Usar desempaquetado
tupla_original = (1, 2, 3)
# "Insertar" al inicio
nueva_tupla = (0,) + tupla_original
print(nueva_tupla)  # (0, 1, 2, 3)

# "Insertar" en el medio usando desempaquetado
a, b, c = tupla_original
nueva_tupla = (a, 1.5, b, c)
print(nueva_tupla)  # (1, 1.5, 2, 3)