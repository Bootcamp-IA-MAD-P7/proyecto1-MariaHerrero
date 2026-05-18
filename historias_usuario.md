# 📋 Historias de Usuario

---

# HU-01 — Iniciar trayecto

## Prioridad

Alta

## Descripción

Como taxista
quiero iniciar un trayecto
para comenzar a calcular automáticamente la tarifa del viaje.

## Criterios de aceptación

* El sistema debe permitir iniciar una nueva carrera.
* El estado inicial del taxi debe ser "parado".
* El contador de tiempo debe comenzar automáticamente.
* No debe permitirse iniciar dos trayectos simultáneos.

---

# HU-02 — Cambiar estado del taxi

## Prioridad

Alta

## Descripción

Como taxista
quiero indicar si el taxi está parado o en movimiento
para calcular correctamente la tarifa del trayecto.

## Criterios de aceptación

* El sistema debe aceptar los estados:

  * `parado`
  * `moviendonos`
* El cambio de estado debe actualizar el tiempo acumulado.
* El sistema debe mostrar el estado actual del taxi.

---

# HU-03 — Calcular tarifa en tiempo real

## Prioridad

Alta

## Descripción

Como taxista
quiero visualizar la tarifa en tiempo real
para conocer el importe acumulado durante el trayecto.

## Criterios de aceptación

* El sistema debe mostrar la tarifa actual tras cada cambio de estado.
* La tarifa debe calcularse automáticamente.
* Debe aplicarse una tarifa distinta según el estado del taxi.

---

# HU-04 — Finalizar trayecto

## Prioridad

Alta

## Descripción

Como taxista
quiero finalizar un trayecto
para mostrar el importe total al cliente.

## Criterios de aceptación

* El sistema debe calcular el total del viaje.
* Debe mostrarse un resumen del trayecto.
* El sistema debe reiniciar las variables para permitir un nuevo viaje.

---

# HU-05 — Mostrar resumen del día

## Prioridad

Media

## Descripción

Como taxista
quiero visualizar un resumen diario
para conocer mis ingresos y estadísticas de trabajo.

## Criterios de aceptación

* El sistema debe mostrar:

  * número de trayectos
  * ingresos totales
  * media por trayecto
* El resumen debe actualizarse automáticamente tras cada viaje.

---

# HU-06 — Guardar historial de trayectos

## Prioridad

Alta

## Descripción

Como taxista
quiero guardar el historial de trayectos
para consultar viajes realizados anteriormente.

## Criterios de aceptación

* El sistema debe guardar cada trayecto en un archivo `.txt`.
* Debe almacenarse:

  * fecha
  * tiempo parado
  * tiempo en movimiento
  * tarifa total
* El historial debe mantenerse aunque el programa se cierre.

---

# HU-07 — Consultar historial

## Prioridad

Media

## Descripción

Como taxista
quiero consultar el historial de trayectos
para revisar viajes anteriores desde el programa.

## Criterios de aceptación

* El sistema debe mostrar el contenido del historial.
* Debe gestionarse el caso en el que no exista historial previo.
* La información debe mostrarse de forma legible.

---

# HU-08 — Configurar precio del combustible

## Prioridad

Media

## Descripción

Como usuaria
quiero introducir el precio del combustible
para adaptar las tarifas a la situación actual.

## Criterios de aceptación

* El sistema debe solicitar el precio al iniciar el programa.
* El precio debe utilizarse en el cálculo de tarifas.
* Solo deben aceptarse valores numéricos válidos.

---

# HU-09 — Registrar logs del sistema

## Prioridad

Media

## Descripción

Como desarrolladora
quiero registrar eventos importantes mediante logs
para detectar errores y realizar seguimiento del funcionamiento del sistema.

## Criterios de aceptación

* El sistema debe registrar:

  * inicio de trayecto
  * cambios de estado
  * finalización de viaje
  * cierre del programa
* Los logs deben guardarse en un archivo `.log`.

---

# HU-10 — Implementar tests automáticos

## Prioridad

Media

## Descripción

Como desarrolladora
quiero implementar tests automáticos
para asegurar el correcto funcionamiento de las funciones principales.

## Criterios de aceptación

* Deben existir tests para el cálculo de tarifas.
* Los tests deben ejecutarse mediante `unittest`.
* El sistema debe superar correctamente todas las pruebas.
