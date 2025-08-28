**extremadamente comunes**, especialmente en programadores que vienen de otros lenguajes. Te explico por qué son problemáticos:

## Los más peligrosos:

1. **Referencias mal entendidas**: Causa bugs sutiles y difíciles de encontrar
2. **Argumentos mutables por defecto**: Puede causar comportamiento impredecible 
3. **except: sin especificar**: Puede ocultar errores críticos como KeyboardInterrupt
4. **No cerrar recursos**: Cause memory leaks y problemas de rendimiento

## Los más frecuentes:

- **for i in range(len())**: Se ve en casi todo código de principiantes
- **List comprehensions mal usadas**: Muy común cuando se aprende el concepto
- **PEP8 ignorado**: Hace el código difícil de leer y mantener

## Consejos para evitarlos:

1. **Usa herramientas**: `pylint`, `flake8`, `black` para formateo automático
2. **Lee PEP8**: Es la guía oficial de estilo de Python
3. **Practica con `with`**: Úsalo siempre para recursos
4. **Entiende las referencias**: Python pasa referencias a objetos, no copias
5. **Sé específico con excepciones**: Nunca uses `except:` solo