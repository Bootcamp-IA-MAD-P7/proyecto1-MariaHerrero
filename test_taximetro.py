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


# Este test nos comprueba la tarifa en vivo #

def test_tarifa_en_vivo():

    resultado = tarifa_en_vivo(10, 20, 2)

    esperado = (10 * 0.02 * 2) + (20 * 0.05 * 2)

    assert resultado == esperado

# Este test comprueba que ocurre cuando la tarifa es 0 #
def test_tarifa_cero():

    resultado = calcula_tarifa(0, 0, 2)

    assert resultado == 0


# Este test nos comprueba que ocurre cuando todo el tiempo estamos en parado#
def test_solo_parado():

    resultado = calcula_tarifa(10, 0, 2)

    esperado = 10 * 0.02 * 2

    assert resultado == esperado

# Este test nos comprueba el flujo completo #
def test_flujo_completo():


    # Datos simulados del trayecto

    tiempo_parado = 10
    tiempo_movimiento = 20
    precio_combustible = 2

# Calculamos tarifa
    tarifa_total = calcula_tarifa(
    tiempo_parado,
    tiempo_movimiento,
    precio_combustible
    )

# Simulamos ingresos del día
    ingresos_dia = [tarifa_total]

# Comprobaciones principales
    assert tarifa_total > 0
    assert len(ingresos_dia) == 1

# Verificamos cálculo esperado
    esperado = (
    tiempo_parado * 0.02 * precio_combustible
    + tiempo_movimiento * 0.05 * precio_combustible
    )

    assert tarifa_total == esperado

# Mostrar información simulada
    print("\n🚕 TEST END TO END COMPLETADO")
    print(f"⛽ Combustible: €{precio_combustible}")
    print(f"🟡 Tiempo parado: {tiempo_parado}s")
    print(f"🟢 Tiempo movimiento: {tiempo_movimiento}s")
    print(f"💰 Tarifa total: €{tarifa_total:.2f}")

    print("\n📊 RESUMEN DEL DÍA")
    print(f"💵 Ingresos: €{sum(ingresos_dia):.2f}")

    print("\n📄 HISTORIAL SIMULADO")
    print("Trayecto guardado correctamente")









if __name__ == "__main__":
    unittest.main()