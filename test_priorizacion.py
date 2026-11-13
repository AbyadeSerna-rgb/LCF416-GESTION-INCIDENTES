import unittest
from main import Incidente, GestorIncidentes

class TestPriorizacion(unittest.TestCase):
    #T07: Ordenar por gravedad
    def test_ordenar_por_gravedad(self):
        gestor = GestorIncidentes()

        gestor.registrar_incidente(Incidente(1, "Falla", "Baja"))
        gestor.registrar_incidente(Incidente(2, "Virus", "Critica"))
        gestor.registrar_incidente(Incidente(3, "Acceso", "Alta"))
        gestor.registrar_incidente(Incidente(4, "Error", "Media"))

        resultado = gestor.pendientes_priorizados()

        ids = [incidente.id for incidente in resultado]

        self.assertEqual(ids, [2, 3, 4, 1])

    #T08: Excluir incidentes cerrados
    def test_excluir_cerrados(self):
        gestor = GestorIncidentes()

        incidente1 = Incidente(1, "Falla", "Alta")
        incidente2 = Incidente(2, "Virus", "Critica")

        gestor.registrar_incidente(incidente1)
        gestor.registrar_incidente(incidente2)

        incidente2.cerrar()

        resultado = gestor.pendientes_priorizados()

        ids = [incidente.id for incidente in resultado]

        self.assertEqual(ids, [1])

    #T09: Lista vacía
    def test_lista_vacia(self):
        gestor = GestorIncidentes()

        resultado = gestor.pendientes_priorizados()

        self.assertEqual(resultado, [])

    #T10: Conservar orden en caso de empate
    def test_orden_estable(self):
        gestor = GestorIncidentes()

        gestor.registrar_incidente(Incidente(1, "Primero", "Alta"))
        gestor.registrar_incidente(Incidente(2, "Segundo", "Alta"))
        gestor.registrar_incidente(Incidente(3, "Tercero", "Alta"))

        resultado = gestor.pendientes_priorizados()

        ids = [incidente.id for incidente in resultado]

        self.assertEqual(ids, [1, 2, 3])

    #T11: No modificar la lista original
    def test_no_modificar_lista_original(self):
        gestor = GestorIncidentes()

        gestor.registrar_incidente(Incidente(1, "Falla", "Baja"))
        gestor.registrar_incidente(Incidente(2, "Virus", "Critica"))
        gestor.registrar_incidente(Incidente(3, "Acceso", "Alta"))

        lista_original = gestor.incidentes.copy()
        gestor.pendientes_priorizados()
        self.assertEqual(gestor.incidentes, lista_original)

if __name__ == "__main__":
    unittest.main()