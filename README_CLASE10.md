# Ejercicio 12. Integración de relaciones entre clases

En el proyecto Gestión de Incidentes de Ciberseguridad se integraron cuatro tipos de relaciones entre clases:

## 1 Asociación: Usuario e Incidente ##

La clase Incidente mantiene una referencia a un objeto Usuario mediante el atributo `responsable`. Esto permite asignar un responsable a cada incidente.

# 2 Agregación: GestorIncidentes e Incidente 

La clase GestorIncidentes administra una colección de objetos Incidente mediante una lista. Los incidentes pueden registrarse y retirarse del gestor sin que necesariamente dejen de existir como objetos.

# 3 Herencia: Incidente, IncidenteMalware e IncidenteAcceso

Las clases IncidenteMalware e IncidenteAcceso heredan los atributos y métodos de la clase Incidente. También sobrescriben el método `generar_reporte()` para agregar información específica de cada tipo de incidente.

# 4 Dependencia: GestorIncidentes y Notificador

La clase GestorIncidentes utiliza un objeto Notificador como parámetro del método `cerrar_incidente()`. El notificador se utiliza temporalmente para enviar una notificación cuando un incidente es cerrado.

# Conclusión

La integración de estas relaciones permite organizar el proyecto, reutilizar código, administrar objetos y separar responsabilidades entre las clases.