import unittest

from main import (
    Incidente,
    IncidenteMalware,
    IncidenteAcceso,
    GestorIncidentes
)

class TestGestionIncidentes(unittest.TestCase):

    #T01: El reporte de malware incluye su familia
    def test_T01_reporte_malware(self):
        incidente = IncidenteMalware(
            1, "Archivo infectado", "Alta", "Ransomware"
        )

        reporte = incidente.generar_reporte()

        self.assertIn("Ransomware", reporte)

    #T02: El reporte de acceso incluye usuario e intentos
    def test_T02_reporte_acceso(self):
        incidente = IncidenteAcceso(
            2, "Acceso sospechoso", "Critica", "cuenta_demo", 8
        )

        reporte = incidente.generar_reporte()

        self.assertIn("cuenta_demo", reporte)
        self.assertIn("8", reporte)

    #T03: Lista heterogénea y polimorfismo
    def test_T03_polimorfismo(self):
        incidentes = [
            Incidente(3, "Falla general", "Media"),
            IncidenteMalware(
                4, "Virus detectado", "Alta", "Troyano"
            ),
            IncidenteAcceso(
                5, "Intento de acceso", "Critica", "cuenta01", 5
            )
        ]

        reportes = [
            incidente.generar_reporte()
            for incidente in incidentes
        ]

        self.assertEqual(len(reportes), 3)
        self.assertIn("Troyano", reportes[1])
        self.assertIn("cuenta01", reportes[2])

    #T04: Una gravedad incorrecta debe generar ValueError
    def test_T04_gravedad_invalida(self):
        with self.assertRaises(ValueError):
            Incidente(6, "Prueba", "Urgente")

    #T05: Cerrar y reabrir cambia el estado
    def test_T05_estado(self):
        incidente = Incidente(7, "Prueba de estado", "Baja")

        self.assertEqual(incidente.estado, "Abierto")

        incidente.cerrar()
        self.assertEqual(incidente.estado, "Cerrado")

        incidente.reabrir()
        self.assertEqual(incidente.estado, "Abierto")

    #T06: El gestor rechaza IDs duplicados
    def test_T06_id_duplicado(self):
        gestor = GestorIncidentes()

        incidente1 = Incidente(8, "Primer incidente", "Alta")
        incidente2 = Incidente(8, "Segundo incidente", "Media")

        self.assertTrue(gestor.registrar_incidente(incidente1))
        self.assertFalse(gestor.registrar_incidente(incidente2))

        self.assertEqual(len(gestor.incidentes), 1)

if __name__ == "__main__":
    unittest.main()