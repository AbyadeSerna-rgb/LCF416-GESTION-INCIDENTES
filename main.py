#1 CLASE USUARIO
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre

    def resumen(self):
        return f"Usuario {self.id}: {self.nombre}"

#2 CLASE INCIDENTE
class Incidente:
    def __init__(self, id_incidente, descripcion, gravedad, estado="Abierto"):
        self.id = id_incidente
        self.descripcion = descripcion
        self.gravedad = gravedad
        self.estado = estado
        self.responsable = None

    def asignar_responsable(self, usuario):
        self.responsable = usuario
        print(
            f"El incidente {self.id} fue asignado a "
            f"{usuario.nombre}."
        )

    def cerrar(self):
        self.estado = "Cerrado"
        print(f"El incidente {self.id} ha sido cerrado.")

    def resumen(self):
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

#3 CLASE NOTIFICADOR
class Notificador:
    def enviar(self, incidente):
        print("\n--- NOTIFICACIÓN ---")
        print(
            f"Se notificó el cierre del incidente "
            f"{incidente.id}: {incidente.descripcion}"
        )
        print("--------------------")

#4 CLASE GESTOR DE INCIDENTES
class GestorIncidentes:
    def __init__(self):
        self.incidentes = []

    def registrar_incidente(self, incidente):
        self.incidentes.append(incidente)
        print(f"Incidente {incidente.id} registrado correctamente.")

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

    def cerrar_incidente(self, incidente, notificador):
        if incidente in self.incidentes:
            incidente.cerrar()
            notificador.enviar(incidente)
        else:
            print("El incidente no está registrado.")

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    #Crear dos usuarios
    usuario1 = Usuario(1, "Ana")
    usuario2 = Usuario(2, "Luis")

    #Crear tres incidentes
    incidente1 = Incidente(
        101, "Intento de phishing", "Alta"
    )

    incidente2 = Incidente(
        102, "Acceso sospechoso al sistema", "Media"
    )

    incidente3 = Incidente(
        103, "Antivirus desactualizado", "Baja"
    )

    #Crear el gestor
    gestor = GestorIncidentes()
    #Registrar los incidentes
    gestor.registrar_incidente(incidente1)
    gestor.registrar_incidente(incidente2)
    gestor.registrar_incidente(incidente3)
    #Asignar responsables
    gestor.asignar_responsable(incidente1, usuario1)
    gestor.asignar_responsable(incidente2, usuario2)
    #Consultar los incidentes
    gestor.consultar_incidentes()
    #Crear el notificador
    notificador = Notificador()
    #Cerrar un incidente y enviar notificación
    gestor.cerrar_incidente(incidente1, notificador)
    #Consultar nuevamente para comprobar el cambio
    gestor.consultar_incidentes()
