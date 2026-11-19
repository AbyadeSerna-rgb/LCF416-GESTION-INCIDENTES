import csv
from pathlib import Path

class ExportadorCSV:
    CAMPOS = ("folio", "tipo", "gravedad", "estado")

    def construir_filas(self, incidentes):
        from main import IncidenteMalware, IncidenteAcceso
        filas = []
        for incidente in incidentes:
            if isinstance(incidente, IncidenteMalware):
                tipo = "Malware"
            elif isinstance(incidente, IncidenteAcceso):
                tipo = "Acceso"
            else:
                tipo = getattr(incidente, "tipo", "General")

            filas.append({
                "folio": f"INC-{incidente.id}",
                "tipo": tipo,
                "gravedad": incidente.gravedad,
                "estado": incidente.estado
            })

        return filas

    def exportar(self, incidentes, destino):
        destino = Path(destino)

        filas = self.construir_filas(incidentes)

        with destino.open(
            "w", encoding="utf-8-sig", newline=""
        ) as archivo:
            escritor = csv.DictWriter(
                archivo, fieldnames=self.CAMPOS
            )
            escritor.writeheader()
            escritor.writerows(filas)

        return destino