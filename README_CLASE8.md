# Actividad 8 – Agregación y jerarquía

## Objetivo
Implementar la agregación de incidentes mediante la clase `GestorIncidentes`, permitiendo administrar objetos `Incidente` creados de manera independiente.

## Funcionalidades implementadas

- **Validación de gravedad:** acepta únicamente Critica, Alta, Media y Baja.
- **Registro de incidentes:** permite agregar incidentes al gestor.
- **Validación de duplicados:** evita registrar dos incidentes con el mismo ID.
- **Eliminación de incidentes:** permite retirar un incidente del gestor sin destruir el objeto original.
- **Conteo por gravedad:** muestra cuántos incidentes existen de cada nivel.

## Pruebas realizadas

1. Registro de seis incidentes ficticios.
2. Intento de registrar un ID duplicado.
3. Conteo de incidentes por gravedad.
4. Eliminación de un incidente y comprobación de que el objeto sigue existiendo.
5. Intento de crear un incidente con una gravedad no permitida.

## Resultados esperados

- Los IDs duplicados son rechazados.
- Las gravedades se contabilizan correctamente.
- El incidente eliminado deja de pertenecer al gestor, pero el objeto continúa disponible mediante su referencia externa.
- Las gravedades no permitidas generan un error de validación.

## Archivo principal

Las funcionalidades y pruebas se encuentran implementadas en `main.py`.