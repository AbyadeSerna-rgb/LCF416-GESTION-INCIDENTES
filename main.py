#1 CLASE USUARIO
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre

    def resumen(self):
        return f"Usuario {self.id}: {self.nombre}"

#2 CLASE PADRE INCIDENTE
class Incidente:
    def __init__(self, id_incidente, descripcion, gravedad):
        self.id = id_incidente
        self.descripcion = descripcion
        self.gravedad = gravedad
        self._estado = "Abierto"
        self.responsable = None

    #Propiedad de gravedad con validación
    @property
    def gravedad(self):
        return self._gravedad

    @gravedad.setter
    def gravedad(self, valor):
        gravedades_validas = ["Critica", "Alta", "Media", "Baja"]

        if valor not in gravedades_validas:
            raise ValueError(
                "La gravedad debe ser Critica, Alta, Media o Baja"
            )
        self._gravedad = valor

    @property
    def estado(self):
        return self._estado

    def reabrir(self):
        self._estado = "Abierto"
        print(f"EL INCIDENTE {self.id} HA SIDO REABIERTO")

    def cerrar(self):
        self._estado = "Cerrado"
        print(f"El incidente {self.id} ha sido cerrado.")

    def asignar_responsable(self, usuario):
        if not isinstance(usuario, Usuario):
            print("Error: el responsable debe ser un usuario válido.")
            return

        self.responsable = usuario
        print(f"El incidente {self.id} fue asignado a {usuario.nombre}.")

    #Reporte gral
    def generar_reporte(self):
        if self.responsable is None:
            nombre_responsable = "Sin responsable"
        else:
            nombre_responsable = self.responsable.nombre

        return (
            f"ID: {self.id} | "
            f"Descripción: {self.descripcion} | "
            f"Gravedad: {self.gravedad} | "
            f"Estado: {self.estado} | "
            f"Responsable: {nombre_responsable}"
        )

    def resumen(self):
        return self.generar_reporte()

#3 CLASE HIJA: INCIDENTE MALWARE
class IncidenteMalware(Incidente):
    def __init__(self, id_incidente, descripcion, gravedad, familia):
        super().__init__(id_incidente, descripcion, gravedad)
        self.familia = familia

    def generar_reporte(self):
        reporte = super().generar_reporte()
        return reporte + f" | Familia de malware: {self.familia}"

#4 CLASE HIJA: INCIDENTE ACCESO
class IncidenteAcceso(Incidente):
    def __init__(
        self, id_incidente, descripcion, gravedad,
        usuario_afectado, intentos_detectados
    ):
        super().__init__(id_incidente, descripcion, gravedad)
        self.usuario_afectado = usuario_afectado
        self.intentos_detectados = intentos_detectados

    def generar_reporte(self):
        reporte = super().generar_reporte()
        return (
            reporte
            + f" | Usuario afectado: {self.usuario_afectado}"
            + f" | Intentos detectados: {self.intentos_detectados}"
        )

#5 CLASE NOTIFICADOR
class Notificador:
    def enviar(self, incidente):
        print("\n--- NOTIFICACIÓN ---")
        print(f"Incidente: {incidente.id}")
        print(f"Descripción: {incidente.descripcion}")

        if incidente.responsable is not None:
            print(f"Responsable: {incidente.responsable.nombre}")
        else:
            print("Responsable: Sin asignar")

        print(f"Estado: {incidente.estado}")
        print("Notificación de cierre enviada.")
        print("--------------------")

#6 CLASE GESTOR DE INCIDENTES
class GestorIncidentes:
    def __init__(self):
        self.incidentes = []

    def registrar_incidente(self, incidente):
        if not isinstance(incidente, Incidente):
            print("Error: se debe registrar un incidente válido")
            return False

        for existense in self.incidentes:
            if existense.id == incidente.id:
                print(f"Error: el ID {incidente.id} ya está registrado.")
                return False
            
        self.incidentes.append(incidente)
        print(f"Incidente {incidente.id} registrado correctamente.")
        return True

    def quitar_incidente(self, id_incidente):
         for incidente in self.incidentes:
             if incidente.id == id_incidente:
                 self.incidentes.remove(incidente)
                 print(f"Incidente {id_incidente} eliminado del gestor.")
                 return incidente

         print(f"No se encontró el incidente {id_incidente}.")
         return None

    def contar_por_gravedad(self):
        conteo = {
            "Critica": 0,
            "Alta": 0,
            "Media": 0,
            "Baja": 0
        }

        for incidente in self.incidentes:
            conteo[incidente.gravedad] +=1

        return conteo

    def asignar_responsable(self, incidente, usuario):
        if incidente in self.incidentes:
            incidente.asignar_responsable(usuario)
        else:
            print("El incidente no está registrado.")

    def consultar_incidentes(self):
        print("\n===== LISTA DE INCIDENTES =====")

        for incidente in self.incidentes:
            print(incidente.resumen())

        print(f"Total de incidentes registrados: {len(self.incidentes)}")

        print("===============================\n")

    def pendientes_priorizados(self):
        prioridad = {
            "Critica": 0,
            "Alta": 1,
            "Media": 2,
            "Baja": 3
        }

        abiertos = [
            incidente for incidente in self.incidentes
            if incidente.estado == "Abierto"
        ]

        return sorted(
            abiertos, 
            key=lambda incidente: prioridad[incidente.gravedad]
        )

    def cerrar_incidente(self, incidente, notificador):
        if incidente not in self.incidentes:
            print("El incidente no está registrado.")
            return

        if not isinstance(notificador, Notificador):
            print("Error: se necesita un notificador válido.")
            return

        incidente.cerrar()
        notificador.enviar(incidente)

#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    #Crear usuarios
    usuario1 = Usuario(1, "Ana")
    usuario2 = Usuario(2, "Luis")

    #Crear incidentes de diferentes tipos
    incidente1 = Incidente(
        101, "Falla en el servidor", "Media"
    )

    incidente2 = IncidenteMalware(
        102, "Archivo infectado", "Alta", "Ransomware"
    )

    incidente3 = IncidenteAcceso(
        103, "Acceso no autorizado", "Critica", "usuario01", 8
    )

    incidente4 = IncidenteMalware(
        104, "Programa sospechoso", "Baja", "Troyano"
    )

    #Crear gestor
    gestor = GestorIncidentes()

    #Registrar incidentes
    gestor.registrar_incidente(incidente1)
    gestor.registrar_incidente(incidente2)
    gestor.registrar_incidente(incidente3)
    gestor.registrar_incidente(incidente4)

    #Asignar responsables
    gestor.asignar_responsable(incidente1, usuario1)
    gestor.asignar_responsable(incidente2, usuario2)

    #Consultar incidentes: polimorfismo
    print("\n--- REPORTES POLIMÓRFICOS ---")
    gestor.consultar_incidentes()

    #Comprobar gravedad
    print("\n--- VALIDACIÓN DE GRAVEDAD ---")
    try:
        incidente1.gravedad = "Urgente"
    except ValueError as error:
        print(f"Error detectado: {error}")

    #Comprobar cierre y reapertura
    print("\n--- VALIDACIÓN DE ESTADO ---")
    print("Estado inicial:", incidente1.estado)
    incidente1.cerrar()
    print("Estado después de cerrar:", incidente1.estado)
    incidente1.reabrir()
    print("Estado después de reabrir:", incidente1.estado)

    #Comprobar ID duplicado
    print("\n--- VALIDACIÓN DE ID DUPLICADO ---")
    duplicado = Incidente(
        101, "Otro incidente", "Alta"
    )
    gestor.registrar_incidente(duplicado)

    #Conteo por gravedad
    print("\n--- CONTEO POR GRAVEDAD ---")
    print(gestor.contar_por_gravedad())

    #Notificación
    notificador = Notificador()
    gestor.cerrar_incidente(incidente2, notificador)

    #Comprobar eliminación e independencia
    print("\n--- PRUEBA DE AGREGACIÓN ---")
    retirado = gestor.quitar_incidente(103)

    if retirado is not None:
        print("El objeto sigue existiendo:")
        print(retirado.generar_reporte())

    gestor.consultar_incidentes()