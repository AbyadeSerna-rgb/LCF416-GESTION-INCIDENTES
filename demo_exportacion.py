from main import(
    Incidente,
    IncidenteMalware,
    IncidenteAcceso,
    GestorIncidentes
)
from exportador_csv import ExportadorCSV

#Crear 5 incidentes 
incidente1 = IncidenteAcceso(
    501, "Acceso sospechoso", "Critica", "usuario01", 5
)

incidente2 = IncidenteMalware(
    502, "Archivo infectado", "Alta", "Troyano"
)

incidente3 = Incidente(
    503, "Correo sospechoso", "Alta"
)

incidente4 = Incidente(
    504, "Falla de seguridad", "Media"
)

incidente5 = IncidenteMalware(
    505, "Software sospechoso", "Baja", "Spyware"
)

#Crear gestor y registrar los incidentes
gestor = GestorIncidentes()
gestor.registrar_incidente(incidente1)
gestor.registrar_incidente(incidente2)
gestor.registrar_incidente(incidente3)
gestor.registrar_incidente(incidente4)
gestor.registrar_incidente(incidente5)

#Cerrar un incidente para verificar el filtrado
incidente5.cerrar()

#Consultar pendientes priorizados
pendientes = gestor.pendientes_priorizados()

print("\n--- INCIDENTES PENDIENTES ---")
for incidente in pendientes:
    print(incidente.generar_reporte())

#Exportar CSV
exportador = ExportadorCSV()
ruta = exportador.exportar(
    pendientes,
    "incidentes_abiertos.csv"
)

print("\nArchivo generado:", ruta)
print("Total de incidentes exportados:", len(pendientes))