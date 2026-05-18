import time
from taximetroMHS import (
    calcula_tarifa,
    tarifa_en_vivo,
    guardar_historial,
    mostrar_historial
)

def demo_completo():

    print("\n🚕 DEMO COMPLETA TAXÍMETRO MHS")
    print("=" * 50)

    precio_combustible = 2
    print(f"⛽ Combustible: €{precio_combustible}")

    # -----------------------------
    # SIMULACIÓN DE TRAYECTO
    # -----------------------------
    tiempo_parado = 0
    tiempo_movimiento = 0

    print("\n▶ Inicio del trayecto")
    time.sleep(1)

    print("🟡 Taxi parado (5s simulados)")
    time.sleep(1)
    tiempo_parado += 5

    print("🚗 Taxi en movimiento (12s simulados)")
    time.sleep(1)
    tiempo_movimiento += 12

    print("🟡 Taxi parado (3s simulados)")
    time.sleep(1)
    tiempo_parado += 3

    # -----------------------------
    # TARIFA EN VIVO
    # -----------------------------
    print("\n🧮 Calculando tarifa en vivo...")
    tarifa_viva = tarifa_en_vivo(
        tiempo_parado,
        tiempo_movimiento,
        precio_combustible
    )

    print(f"💰 Tarifa en vivo: €{tarifa_viva:.2f}")

    # -----------------------------
    # FINALIZAR TRAYECTO
    # -----------------------------
    print("\n🏁 Finalizando trayecto...")
    time.sleep(1)

    tarifa_total = calcula_tarifa(
        tiempo_parado,
        tiempo_movimiento,
        precio_combustible
    )

    guardar_historial(tiempo_parado, tiempo_movimiento, tarifa_total)

    # -----------------------------
    # RESUMEN DEL VIAJE
    # -----------------------------
    print("\n📊 RESUMEN DEL TRAYECTO")
    print("-" * 30)
    print(f"🟡 Tiempo parado: {tiempo_parado}s")
    print(f"🟢 Tiempo movimiento: {tiempo_movimiento}s")
    print(f"💰 Total: €{tarifa_total:.2f}")

    # -----------------------------
    # HISTORIAL COMPLETO
    # -----------------------------
    print("\n📄 HISTORIAL COMPLETO")
    print("-" * 30)
    mostrar_historial()

    print("\n🚕 DEMO FINALIZADA")

if __name__ == "__main__":
    demo_completo()