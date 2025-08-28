Estos son errores más avanzados pero igual de importantes. Te explico cada uno:Estos errores son **críticos para código profesional**. Te explico la importancia de cada uno:

## Los más críticos para producción:

### 1. **Manejo de secretos**
```python
# ❌ NUNCA hagas esto
API_KEY = "sk-1234567890abcdef"  # Hardcodeado en el código

# ✅ Usa variables de entorno
import os
API_KEY = os.getenv('API_KEY')
```

### 2. **Entornos virtuales**
Sin ellos tienes:
- Conflictos de dependencias
- "Funciona en mi máquina" pero no en otras
- Imposibilidad de reproducir el entorno

### 3. **Type hints**
```python
# Sin types: ¿Qué espera? ¿Qué devuelve?
def procesar(datos):
    return datos.split(',')

# Con types: Cristalino
def procesar(datos: str) -> List[str]:
    return datos.split(',')
```

## Los que más afectan mantenibilidad:

### 1. **Modelos de datos**
Sin modelos = bugs inevitables:
```python
# ❌ ¿Qué campos tiene? ¿Cuáles son opcionales?
usuario = {'nombre': 'Juan', 'edad': 30}

# ✅ Claro y validado
@dataclass
class Usuario:
    nombre: str
    edad: int
```

### 2. **Try/except granular**
```python
# ❌ ¿Qué falló? ¿Por qué?
try:
    # 50 líneas de código
except Exception:
    pass

# ✅ Específico y manejable
try:
    resultado = operacion_riesgosa()
except ValueError as e:
    logger.error(f"Valor inválido: {e}")
    return None
```

## Herramientas que debes usar YA:

1. **black** - Formateo automático
2. **flake8** - Detectar errores
3. **mypy** - Verificar types
4. **pre-commit** - Hooks de git
5. **python-dotenv** - Variables de entorno

## Configuración básica recomendada:

**requirements-dev.txt:**
```
black
flake8
mypy
pre-commit
python-dotenv
pytest
```

**pyproject.toml:**
```toml
[tool.black]
line-length = 88

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
```