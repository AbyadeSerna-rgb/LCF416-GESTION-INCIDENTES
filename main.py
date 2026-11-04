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
        gravedades_validas = ["Critica", "Alta", "Media", "Baja"]

        if gravedad not in gravedades_validas:
            raise ValueError("La gravedad debe ser Critica, Alta, Media o Baja.")
        
        self.id = id_incidente
        self.descripcion = descripcion
        self.gravedad = gravedad
        self.estado = estado
        self.responsable = None

    def asignar_responsable(self, usuario):
        if not isinstance(usuario, Usuario):
            print("Error: el responsable debe ser un usuario válido.")
            return

        self.responsable = usuario
        print(f"El incidente {self.id} fue asignado a {usuario.nombre}.")
    
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
        print(f"Incidente: {incidente.id}")
        print(f"Descripción: {incidente.descripcion}")

        if incidente.responsable is not None:
            print(f"Responsable: {incidente.responsable.nombre}")
        else:
            print("Responsable: Sin asignar")

        print(f"Estado: {incidente.estado}")
        print("Notificación de cierre enviada.")
        print("--------------------")

#4 CLASE GESTOR DE INCIDENTES
class GestorIncidentes:
    def __init__(self):
        self.incidentes = []

    def registrar_incidente(self, incidente):
        if not isinstance(incidente, Incidente):
            print("Error: se debe registrar un incidente válido")
            return

        for existense in self.incidentes:
            if existense.id == incidente.id:
                print(f"Error: el ID {incidente.id} ya está registrado.")
                return
            
        self.incidentes.append(incidente)
        print(f"Incidente {incidente.id} registrado correctamente.")

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
    incidente1 = Incidente(101, "Intento de phishing", "Alta")
    incidente2 = Incidente(102, "Acceso sospechoso al sistema", "Media")
    incidente3 = Incidente(103, "Antivirus desactualizado", "Baja")
    incidente4 = Incidente(104, "Ataque de ransonware", "Critica")
    incidente5 = Incidente(105, "Intento de acceso no autorizado", "Alta")
    incidente6 = Incidente(106, "Software desactualizado", "Baja")

    #Crear el gestor
    gestor = GestorIncidentes()
    #Registrar los incidentes
    gestor.registrar_incidente(incidente1)
    gestor.registrar_incidente(incidente2)
    gestor.registrar_incidente(incidente3)
    gestor.registrar_incidente(incidente4)
    gestor.registrar_incidente(incidente5)
    gestor.registrar_incidente(incidente6)

    print("\n--- PRUEBA DE VALIDACION DE GRAVEDAD ---")
    print("ESTOY EJECUTANDO LA PRUEBA DE VALIDACION")
    try: 
        prueba_valida = Incidente(107, "Prueba de seguridad", "Alta")
        print("Incidente válido creado correctamente")

        prueba_invalida = Incidente(108, "Prueba de seguridad", "Urgente")
        print("Incidente inválido creado")

    except ValueError as error:
        print(f"Error detectado: {error}")
    print("FIN DE LA PRUEBA")            

    #Comprobar IDs duplicados
    incidente_duplicado = Incidente(
        101, "Otro intento de phishing", "Alta"
    )

    gestor.registrar_incidente(incidente_duplicado)

    #Comprobar conteo por gravedad
    print("\n--- CONTEO POR GRAVEDAD ---")
    print(gestor.contar_por_gravedad())

    #Comprobar eliminación e independencia
    print("\n--- PRUEBA DE AGREGACIÓN ---")

    retirado = gestor.quitar_incidente(102)

    print("\nIncidentes restantes: ")
    gestor.consultar_incidentes()

    print("\nComprobar que el objeto sigue existiendo:")
    print(retirado.resumen())

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
