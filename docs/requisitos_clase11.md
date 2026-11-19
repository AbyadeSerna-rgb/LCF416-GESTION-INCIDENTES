# Requisitos – Clase 11

## 1. Nombre del proyecto
Sistema de Gestión de Incidentes de Ciberseguridad.

## 2. Necesidad identificada
El sistema registra incidentes de ciberseguridad, pero cuando existen varios pendientes es necesario identificar cuáles requieren atención primero.
La nueva función permitirá consultar los incidentes abiertos y organizarlos de acuerdo con su gravedad, para facilitar la atención de los casos más importantes.

## 3. Actor y necesidad
**Operador:** necesita consultar los incidentes pendientes para atenderlos según su nivel de gravedad.
**Supervisor:** necesita visualizar los incidentes prioritarios para dar seguimiento a su atención.
**Administrador:** se encarga de mantener la gestión general del sistema.
La función de priorización atenderá principalmente la necesidad del operador.

## 4. Alcance
La función `pendientes_priorizados()` permitirá consultar los incidentes cuyo estado sea `Abierto` y ordenarlos de acuerdo con la siguiente prioridad:
1. Critica
2. Alta
3. Media
4. Baja
Cuando dos o más incidentes tengan la misma gravedad, se conservará el orden en el que fueron registrados.
La consulta devolverá una lista nueva, sin modificar la colección original ni alterar los objetos registrados.
**Fuera del alcance:** enviar notificaciones externas, consultar servicios de terceros o modificar automáticamente la gravedad de los incidentes.

## 5. Requisitos funcionales
| ID | Requisito | Forma de comprobar |
|---|---|---|
| RF-01 | El sistema deberá consultar únicamente los incidentes con estado `Abierto`. | Registrar incidentes abiertos y cerrados y comprobar el resultado. |
| RF-02 | El sistema deberá ordenar los incidentes por gravedad: Critica, Alta, Media y Baja. | Comparar el orden obtenido con la prioridad establecida. |
| RF-03 | El sistema deberá conservar el orden de registro cuando dos incidentes tengan la misma gravedad. | Registrar incidentes con igual gravedad y comparar su posición. |
| RF-04 | El sistema deberá devolver una lista nueva sin modificar la colección original. | Comparar la colección antes y después de la consulta. |

## 6. Requisitos no funcionales
| ID | Requisito | Forma de comprobar |
|---|---|---|
| RNF-01 | La función deberá implementarse utilizando Python y las estructuras de datos de la biblioteca estándar. | Revisar el código fuente. |
| RNF-02 | La consulta deberá mantener el funcionamiento de las clases y relaciones existentes del proyecto. | Ejecutar las pruebas anteriores y las nuevas en conjunto. |

## 7. Historias de usuario
**Historia 1 – Operador**
Como operador, quiero consultar los incidentes abiertos ordenados por gravedad para atender primero los que requieren mayor prioridad.
**Historia 2 – Supervisor**
Como supervisor, quiero visualizar los incidentes pendientes en orden de prioridad para facilitar el seguimiento de su atención.

## 8. Criterios de aceptación
**CA-01. Exclusión de incidentes cerrados**
Dado un conjunto de incidentes abiertos y cerrados, cuando se consulte la priorización, entonces únicamente aparecerán los incidentes abiertos.
**CA-02. Orden por gravedad**
Dado un incidente Critica y otro Media, ambos abiertos, cuando se consulte la priorización, entonces el incidente Critica aparecerá primero.
**CA-03. Conservación del orden en empates**
Dado dos incidentes Alta registrados en distinto momento, cuando se consulte la priorización, entonces conservarán su orden de registro.
**CA-04. Resultado vacío**
Dada una colección sin incidentes abiertos, cuando se consulte la priorización, entonces el sistema devolverá una lista vacía.
**CA-05. Conservación de la colección original**
Dada la colección original de incidentes, cuando se consulte la priorización, entonces su contenido y orden permanecerán sin modificaciones.

## 9. Conclusión
La incorporación de la función de priorización permitirá organizar la consulta de incidentes pendientes de acuerdo con su gravedad. La definición de requisitos y criterios de aceptación establece las condiciones que debe cumplir la mejora y permite comprobar su funcionamiento mediante pruebas.