"""
Context managers y manejo de recursos
"""
from contextlib import contextmanager, suppress
import tempfile
import os

@contextmanager
def cambiar_directorio_temporal(nuevo_dir):
    directorio_original = os.getcwd()
    try:
        os.makedirs(nuevo_dir, exist_ok=True)
        os.chdir(nuevo_dir)
        yield nuevo_dir
    finally:
        os.chdir(directorio_original)

# Uso del context manager personalizado
with tempfile.TemporaryDirectory() as temp_dir:
    with cambiar_directorio_temporal(temp_dir):
        # Crear archivo temporal
        with open('test.txt', 'w') as f:
            f.write('Contenido temporal')
        
        print(f"Archivos en directorio temporal: {os.listdir('.')}")

# suppress - Suprimir excepciones específicas
print("\nUsando suppress para ignorar errores específicos:")
with suppress(FileNotFoundError):
    os.remove('archivo_que_no_existe.txt')
    print("Archivo eliminado")  # No se ejecuta

print("Continuamos sin problemas después del suppress")

print("\n" + "="*60)
