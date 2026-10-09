import unittest

from tienda.precios import aplicar_descuento, cambio, precio_con_iva, total_ticket


class TestPrecios(unittest.TestCase):
    def test_iva_general(self):
        self.assertEqual(precio_con_iva(100), 121.0)

    def test_iva_superreducido_pan(self):
        self.assertEqual(precio_con_iva(1.20, "superreducido"), 1.25)

    def test_iva_tipo_desconocido(self):
        with self.assertRaises(ValueError):
            precio_con_iva(10, "lujo")

    def test_descuento(self):
        self.assertEqual(aplicar_descuento(80, 25), 60)

    def test_descuento_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            aplicar_descuento(80, 120)

    def test_total_ticket(self):
        self.assertEqual(total_ticket([(1.25, 4), (3.10, 2), (0.85, 3)]), 13.75)

    def test_total_ticket_vacio(self):
        self.assertEqual(total_ticket([]), 0)

    def test_cambio_con_centimos(self):
        # 20 € para pagar 13,75 €: el cambio es 6,25 € → 5 + 1 + 0,20 + 0,05
        self.assertEqual(cambio(20, 13.75), [5, 1, 0.2, 0.05])

    def test_cambio_redondeo(self):
        # 0,30 € para pagar 0,10 €: dos monedas de 10 céntimos, no un error de coma flotante
        self.assertEqual(cambio(0.30, 0.10), [0.2])


if __name__ == "__main__":
    unittest.main()
