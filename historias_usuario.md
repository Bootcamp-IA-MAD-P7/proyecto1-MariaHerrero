# 🚕 Historias de Usuario — TAXÍMETRO MHS

---

# HU-01 — Iniciar trayecto

## Prioridad

Alta

## Descripción

Como conductor del taxi,
quiero poder iniciar una carrera,
para comenzar el cálculo del trayecto.

## Criterios de aceptación

* El sistema debe permitir iniciar un trayecto mediante el comando `inicio`
* El trayecto debe comenzar en estado `parado`
* El sistema debe impedir iniciar dos trayectos simultáneamente

---

# HU-02 — Cambiar estado del taxi

## Prioridad

Alta

## Descripción

Como conductor,
quiero cambiar el estado del taxi entre parado y moviéndonos,
para calcular correctamente el precio del trayecto.

## Criterios de aceptación

* El sistema debe permitir cambiar entre:

  * `parado`
  * `moviendonos`
* Debe registrarse el tiempo acumulado de cada estado
* El sistema debe mostrar el estado actual

---

# HU-03 — Calcular tarifa del trayecto

## Prioridad

Alta

## Descripción

Como conductor,
quiero calcular automáticamente el precio del trayecto,
para conocer el importe final del viaje.

## Criterios de aceptación

* La tarifa debe calcularse según:

  * tiempo parado
  * tiempo en movimiento
* Debe mostrarse el importe final al finalizar el trayecto

---

# HU-04 — Finalizar trayecto

## Prioridad

Alta

## Descripción

Como conductor,
quiero finalizar un trayecto,
para cerrar el viaje y generar el resumen final.

## Criterios de aceptación

* El sistema debe permitir finalizar un trayecto mediante `findetrayecto`
* Debe mostrarse un resumen del viaje
* Las variables deben reiniciarse automáticamente

---

# HU-05 — Mostrar historial de trayectos

## Prioridad

Media

## Descripción

Como usuario,
quiero consultar el historial de trayectos realizados,
para revisar viajes anteriores.

## Criterios de aceptación

* El sistema debe guardar los trayectos en `historial.txt`
* Debe incluir:

  * fecha
  * tiempos
  * importe
* El historial debe visualizarse mediante el comando `historial`

---

# HU-06 — Mostrar resumen del día

## Prioridad

Media

## Descripción

Como conductor,
quiero visualizar los ingresos acumulados del día,
para controlar mis ganancias.

## Criterios de aceptación

* El sistema debe mostrar:

  * número de trayectos
  * ingresos totales
* El resumen debe ejecutarse mediante `resumen_dia`

---

# HU-07 — Configurar precio del combustible

## Prioridad

Alta

## Descripción

Como conductor,
quiero introducir el precio actual del combustible,
para ajustar correctamente las tarifas.

## Criterios de aceptación

* El sistema debe solicitar el precio del combustible al iniciar
* Debe utilizarse para calcular las tarifas
* El sistema debe validar que el valor introducido sea numérico

---

# HU-08 — Mostrar tarifa en tiempo real

## Prioridad

Media

## Descripción

Como conductor,
quiero visualizar la tarifa en tiempo real,
para conocer el importe acumulado durante el trayecto.

## Criterios de aceptación

* El sistema debe mostrar la tarifa actual al cambiar de estado
* Debe actualizarse automáticamente

---

# HU-09 — Validar comandos incorrectos

## Prioridad

Media

## Descripción

Como usuario,
quiero recibir mensajes de error claros cuando escriba comandos incorrectos,
para utilizar correctamente el sistema.

## Criterios de aceptación

* El sistema debe detectar comandos inválidos
* Debe mostrar una lista de comandos válidos

---

# HU-10 — Ejecutar pruebas automáticas

## Prioridad

Media

## Descripción

Como desarrolladora,
quiero implementar pruebas automáticas,
para verificar el correcto funcionamiento del sistema.

## Criterios de aceptación

* El proyecto debe incluir tests unitarios
* Deben probarse funciones principales:

  * cálculo de tarifas
  * tarifa en vivo
  * simulación de trayecto

---

# HU-11 — Registro de actividad mediante logs

## Prioridad

Alta

## Descripción

Como desarrolladora,
quiero registrar eventos importantes del sistema,
para revisar el funcionamiento de la aplicación y detectar errores.

## Criterios de aceptación

* El sistema debe generar un archivo `taximetro.log`
* Deben registrarse:

  * inicio de trayecto
  * cambios de estado
  * finalización de viaje
  * cierre del programa
* Los logs deben incluir fecha y hora

---

# HU-12 — Generación de ticket visual

## Prioridad

Media

## Descripción

Como usuario,
quiero visualizar un ticket organizado al finalizar el trayecto,
para consultar claramente la información del viaje.

## Criterios de aceptación

* El ticket debe mostrar:

  * combustible
  * tiempo parado
  * tiempo movimiento
  * importe total
* Debe mostrarse con formato visual en consola

---

# HU-13 — Simulación automática del sistema

## Prioridad

Media

## Descripción

Como desarrolladora,
quiero disponer de una demo automática del proyecto,
para mostrar fácilmente el funcionamiento completo del sistema.

## Criterios de aceptación

* La demo debe simular un trayecto completo
* Debe mostrar:

  * movimientos
  * cálculo de tarifa
  * resumen final
  * historial
* Debe ejecutarse desde un archivo independiente
