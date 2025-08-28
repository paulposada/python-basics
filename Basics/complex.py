# La j en los números complejos representa la unidad imaginaria, que matemáticamente se define como j² = -1.¿Por qué 'j' y no 'i'?En matemáticas tradicionalmente se usa i, pero Python usa j porque:

# En ingeniería eléctrica se usa 'j' para evitar confusión con 'i' (que representa corriente)
# Python sigue esta convención de ingeniería
# Evita conflictos con variables llamadas 'i' (muy comunes en programación)
# Solo existe la letra 'j'No hay más letras para números complejos en Python. Solo puedes usar:

# j o J (ambas funcionan igual)

# Estos darán error:
# 3 + 4i    # NameError: name 'i' is not defined
# 3 + 4k    # NameError: name 'k' is not defined
# 3 + 4*i   # Solo si tienes una variable 'i' definida

# Formas válidas de escribir números complejos
complejo1 = 3 + 4j      # Usando j minúscula
complejo2 = 3 + 4J      # Usando J mayúscula (igual resultado)
complejo3 = 2j          # Solo parte imaginaria
complejo4 = 5 + 0j      # Solo parte real (pero sigue siendo complex)
complejo5 = 0 + 1j      # Equivale a la unidad imaginaria

print(complejo1)  # (3+4j)
print(complejo2)  # (3+4j) - mismo resultado
print(complejo3)  # 2j
print(complejo4)  # (5+0j)
print(complejo5)  # 1j

# Verificar que j² = -1
unidad_imaginaria = 1j
print(unidad_imaginaria ** 2)  # (-1+0j)

# Formas alternativas de crear números complejos
complejo6 = complex(3, 4)      # complex(real, imaginario)
complejo7 = complex("3+4j")    # Desde string

print(complejo6)  # (3+4j)
print(complejo7)  # (3+4j)

# Acceder a las partes
numero = 3 + 4j
print(f"Parte real: {numero.real}")      # 3.0
print(f"Parte imaginaria: {numero.imag}")  # 4.0
print(f"Conjugado: {numero.conjugate()}")  # (3-4j)
print(f"Módulo: {abs(numero)}")          # 5.0


a = 3 + 4j
b = 1 + 2j

print(f"Suma: {a + b}")           # (4+6j)
print(f"Resta: {a - b}")          # (2+2j)
print(f"Multiplicación: {a * b}") # (-5+10j)
print(f"División: {a / b}")       # (2.2-0.4j)
print(f"Potencia: {a ** 2}")      # (-7+24j)