import csv
import tempfile
import unittest
from pathlib import Path

from main import (
    Incidente,
    IncidenteMalware,
    IncidenteAcceso,
    GestorIncidentes
)

from exportador_csv import ExportadorCSV

class TestExportadorCSV(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorIncidentes()

        self.i1 = Incidente(1, "Critico", "Critica")
        self.i2 = Incidente(2, "Alta 1", "Alta")
        self.i3 = Incidente(3, "Alta 2", "Alta")
        self.i4 = Incidente(4, "Media", "Media")
        self.i5 = Incidente(5, "Baja", "Baja")

        for incidente in [
            self.i1, self.i2, self.i3, self.i4, self.i5
        ]:
            self.gestor.registrar_incidente(incidente)

        self.exportador = ExportadorCSV()

    def leer_csv(self, ruta):
        with ruta.open(
            encoding="utf-8-sig", newline=""
        ) as archivo:
            return list(csv.DictReader(archivo))

    #P-01: Filtrado de incidentes cerrados
    def test_filtrado(self):
        self.i5.cerrar()

        pendientes = self.gestor.pendientes_priorizados()

        self.assertEqual(len(pendientes), 4)
        self.assertNotIn(self.i5, pendientes)

    #P-02: Orden de prioridad
    def test_prioridad(self):
        pendientes = self.gestor.pendientes_priorizados()

        gravedades = [
            i.gravedad for i in pendientes
        ]

        self.assertEqual(
            gravedades,
            ["Critica", "Alta", "Alta", "Media", "Baja"]
        )

    #P-03: Orden estable en empates
    def test_orden_estable(self):
        pendientes = self.gestor.pendientes_priorizados()

        ids = [i.id for i in pendientes]

        self.assertEqual(ids, [1, 2, 3, 4, 5])

    #P-04: Lista vacía
    def test_lista_vacia(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "vacio.csv"

            self.exportador.exportar([], ruta)

            with ruta.open(
                encoding="utf-8-sig", newline=""
            ) as archivo:
                lector = csv.reader(archivo)
                filas = list(lector)

            self.assertEqual(
                filas,
                [["folio", "tipo", "gravedad", "estado"]]
            )

    #P-05: Comas y acentos
    def test_comas_acentos(self):
        incidente = Incidente(
            6, "Descripción ficticia", "Alta"
        )

        incidente.tipo = "Correo, phishing"

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "acentos.csv"

            self.exportador.exportar([incidente], ruta)

            filas = self.leer_csv(ruta)

            self.assertEqual(
                filas[0]["tipo"],
                "Correo, phishing"
            )

    #P-06: No modificar objetos ni colección
    def test_no_mutacion(self):
        original = list(self.gestor.incidentes)

        estados = [
            i.estado for i in self.gestor.incidentes
        ]

        gravedades = [
            i.gravedad for i in self.gestor.incidentes
        ]

        pendientes = self.gestor.pendientes_priorizados()

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "reporte.csv"

            self.exportador.exportar(pendientes, ruta)

        self.assertEqual(
            self.gestor.incidentes, original
        )

        self.assertEqual(
            [i.estado for i in self.gestor.incidentes],
            estados
        )

        self.assertEqual(
            [i.gravedad for i in self.gestor.incidentes],
            gravedades
        )

if __name__ == "__main__":
    unittest.main()