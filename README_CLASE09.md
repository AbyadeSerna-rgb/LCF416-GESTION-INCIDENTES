# Gestión de Incidentes de Ciberseguridad
## Versión 3 - Herencia y Polimorfismo

### Descripción
Sistema desarrollado en Python para administrar incidentes
de ciberseguridad mediante programación orientada a objetos.

### Clases principales

- Usuario: representa a los responsables de los incidentes.
- Incidente: clase padre que contiene los atributos y métodos generales.
- IncidenteMalware: representa incidentes relacionados con malware.
- IncidenteAcceso: representa incidentes de acceso no autorizado.
- GestorIncidentes: administra el registro y seguimiento de incidentes.
- Notificador: permite enviar notificaciones sobre incidentes.

### Conceptos de POO implementados

- Herencia.
- Polimorfismo.
- Encapsulamiento.
- Propiedades con @property y @setter.
- Validación de atributos.
- Agregación.
- Asociación.
- Dependencia.

### Validaciones

- Gravedad permitida: Critica, Alta, Media y Baja.
- Estado inicial: Abierto.
- Cierre y reapertura de incidentes.
- Rechazo de identificadores duplicados.

### Pruebas

Archivo: test_incidentes.py

Pruebas realizadas:
- T01: Reporte de malware.
- T02: Reporte de acceso.
- T03: Polimorfismo.
- T04: Gravedad inválida.
- T05: Cierre y reapertura.
- T06: Identificadores duplicados.

### Ejecución

Ejecutar el programa:

py main.py

Ejecutar las pruebas:

py -m unittest -v

### Tecnologías

- Python 3.14.3
- Git
- GitHub