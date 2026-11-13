# Ciclo de vida del software – Clase 11

## 1. Proyecto
**Sistema de Gestión de Incidentes de Ciberseguridad**
El ciclo de vida del software permite organizar las actividades necesarias para desarrollar, probar, entregar y mantener un sistema. Para este proyecto se utiliza como referencia la mejora que permite consultar los incidentes abiertos ordenados por nivel de gravedad.

## 2. Modelo de desarrollo seleccionado
Se seleccionó el modelo **iterativo e incremental** debido a que el proyecto ya cuenta con una estructura desarrollada en clases anteriores y se busca agregar nuevas funcionalidades de manera gradual, este modelo permite implementar una mejora, probarla y realizar ajustes antes de continuar con otras funcionalidades, también facilita detectar errores sin tener que modificar todo el sistema.

## 3. Etapas del ciclo de vida
| Etapa | Actividad realizada | Responsable simulado | Evidencia | Riesgo |
|---|---|---|---|---|
| Necesidad / análisis | Identificar la necesidad de consultar primero los incidentes de mayor gravedad. | Analista del sistema | Descripción del problema y actores. | No comprender correctamente la necesidad del usuario. |
| Requisitos | Definir que solo se deben mostrar incidentes abiertos, ordenados por gravedad. | Analista del sistema | `requisitos_clase11.md` | Establecer requisitos ambiguos o incompletos. |
| Diseño | Definir la lógica de filtrado y ordenamiento sin modificar la colección original. | Diseñador del sistema | Descripción del algoritmo y estructura de clases existente. | Diseñar una solución que afecte el funcionamiento anterior. |
| Implementación | Desarrollar el método `pendientes_priorizados()` utilizando Python. | Desarrollador | Código fuente y commit en Git. | Introducir errores en el método o alterar la lista original. |
| Pruebas | Comprobar el orden de prioridad, los estados, las listas vacías y la estabilidad del orden. | Tester | `test_priorizacion.py` y resultados de ejecución. | No contemplar casos límite o situaciones incorrectas. |
| Entrega | Preparar los documentos, el código y las pruebas para su revisión mediante GitHub. | Responsable de entrega | Repositorio y Pull Request. | Entregar archivos incompletos o pruebas fallidas. |
| Mantenimiento | Corregir errores y agregar mejoras futuras sin afectar las funcionalidades existentes. | Equipo de desarrollo | Historial de cambios y nuevas pruebas. | Que una modificación futura provoque errores en otras partes del sistema. |

## 4. Aplicación del modelo al proyecto
El desarrollo se realiza de manera incremental porque cada clase agrega conocimientos y mejoras al sistema existente.
En esta etapa se incorporó la consulta de incidentes pendientes priorizados. El proceso consistió en:
1. Analizar la necesidad de organizar los incidentes por gravedad.
2. Definir los requisitos y criterios de aceptación.
3. Diseñar la lógica de filtrado y ordenamiento.
4. Implementar el método `pendientes_priorizados()`.
5. Crear pruebas para verificar su funcionamiento.
6. Documentar los cambios y preparar su revisión en GitHub.

## 5. Riesgos generales y prevención
- **Errores de lógica:** ejecutar pruebas que comprueben diferentes niveles de gravedad y estados.
- **Pérdida de información:** utilizar `sorted()` para generar una nueva lista sin modificar la colección original.
- **Regresiones:** ejecutar las pruebas anteriores junto con las nuevas.
- **Documentación incompleta:** mantener actualizados los archivos de documentación y registrar los cambios mediante commits.

## 6. Conclusión
El ciclo de vida permite organizar el desarrollo del sistema desde la identificación de una necesidad hasta su mantenimiento. El modelo iterativo e incremental es adecuado para este proyecto porque permite agregar funcionalidades de forma gradual, comprobar su funcionamiento y conservar las características desarrolladas anteriormente.