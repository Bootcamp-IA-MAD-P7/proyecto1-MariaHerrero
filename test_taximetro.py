import unittest

from taximetroMHS import calcula_tarifa


class TestTaximetro(unittest.TestCase):
#Este test nos comprueba que la tarifa funciona correctamente #
    def test_calcula_tarifa(self):

        resultado = calcula_tarifa(10, 20, 1.5)

        esperado = (10 * (0.02 * 1.5)) + (20 * (0.05 * 1.5))

        self.assertEqual(resultado, esperado)

# Este test nos comprueba que la tarifa parado funciona correctamente #
    def test_tarifa_solo_parado(self):

        resultado = calcula_tarifa(10, 0, 1.5)

        esperado = 10 * (0.02 * 1.5)

        self.assertEqual(resultado, esperado)



if __name__ == "__main__":
    unittest.main()