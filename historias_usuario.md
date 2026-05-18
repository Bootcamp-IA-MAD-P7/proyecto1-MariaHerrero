<<<<<<< HEAD
# 📋 Historias de Usuario
=======
# 🚕 Historias de Usuario — TAXÍMETRO MHS
>>>>>>> feature/tests-tarifas

---

# HU-01 — Iniciar trayecto

## Prioridad

Alta

## Descripción

<<<<<<< HEAD
Como taxista
quiero iniciar un trayecto
para comenzar a calcular automáticamente la tarifa del viaje.

## Criterios de aceptación

* El sistema debe permitir iniciar una nueva carrera.
* El estado inicial del taxi debe ser "parado".
* El contador de tiempo debe comenzar automáticamente.
* No debe permitirse iniciar dos trayectos simultáneos.
=======
Como conductor del taxi,
quiero poder iniciar una carrera,
para comenzar el cálculo del trayecto.

## Criterios de aceptación

* El sistema debe permitir iniciar un trayecto mediante el comando `inicio`
* El trayecto debe comenzar en estado `parado`
* El sistema debe impedir iniciar dos trayectos simultáneamente
>>>>>>> feature/tests-tarifas

---

# HU-02 — Cambiar estado del taxi

## Prioridad

Alta

## Descripción

<<<<<<< HEAD
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
=======
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
>>>>>>> feature/tests-tarifas

## Prioridad

Alta

## Descripción

<<<<<<< HEAD
Como taxista
quiero visualizar la tarifa en tiempo real
para conocer el importe acumulado durante el trayecto.

## Criterios de aceptación

* El sistema debe mostrar la tarifa actual tras cada cambio de estado.
* La tarifa debe calcularse automáticamente.
* Debe aplicarse una tarifa distinta según el estado del taxi.
=======
Como conductor,
quiero calcular automáticamente el precio del trayecto,
para conocer el importe final del viaje.

## Criterios de aceptación

* La tarifa debe calcularse según:

  * tiempo parado
  * tiempo en movimiento
* Debe mostrarse el importe final al finalizar el trayecto
>>>>>>> feature/tests-tarifas

---

# HU-04 — Finalizar trayecto

## Prioridad

Alta

## Descripción

<<<<<<< HEAD
Como taxista
quiero finalizar un trayecto
para mostrar el importe total al cliente.

## Criterios de aceptación

* El sistema debe calcular el total del viaje.
* Debe mostrarse un resumen del trayecto.
* El sistema debe reiniciar las variables para permitir un nuevo viaje.

---

# HU-05 — Mostrar resumen del día
=======
Como conductor,
quiero finalizar un trayecto,
para cerrar el viaje y generar el resumen final.

## Criterios de aceptación

* El sistema debe permitir finalizar un trayecto mediante `findetrayecto`
* Debe mostrarse un resumen del viaje
* Las variables deben reiniciarse automáticamente

---

# HU-05 — Mostrar historial de trayectos
>>>>>>> feature/tests-tarifas

## Prioridad

Media

## Descripción

<<<<<<< HEAD
Como taxista
quiero visualizar un resumen diario
para conocer mis ingresos y estadísticas de trabajo.
=======
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
>>>>>>> feature/tests-tarifas

## Criterios de aceptación

* El sistema debe mostrar:

  * número de trayectos
  * ingresos totales
<<<<<<< HEAD
  * media por trayecto
* El resumen debe actualizarse automáticamente tras cada viaje.

---

# HU-06 — Guardar historial de trayectos
=======
* El resumen debe ejecutarse mediante `resumen_dia`

---

# HU-07 — Configurar precio del combustible
>>>>>>> feature/tests-tarifas

## Prioridad

Alta

## Descripción

<<<<<<< HEAD
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
=======
Como conductor,
quiero introducir el precio actual del combustible,
para ajustar correctamente las tarifas.

## Criterios de aceptación

* El sistema debe solicitar el precio del combustible al iniciar
* Debe utilizarse para calcular las tarifas
* El sistema debe validar que el valor introducido sea numérico

---

# HU-08 — Mostrar tarifa en tiempo real
>>>>>>> feature/tests-tarifas

## Prioridad

Media

## Descripción

<<<<<<< HEAD
Como taxista
quiero consultar el historial de trayectos
para revisar viajes anteriores desde el programa.

## Criterios de aceptación

* El sistema debe mostrar el contenido del historial.
* Debe gestionarse el caso en el que no exista historial previo.
* La información debe mostrarse de forma legible.

---

# HU-08 — Configurar precio del combustible
=======
Como conductor,
quiero visualizar la tarifa en tiempo real,
para conocer el importe acumulado durante el trayecto.

## Criterios de aceptación

* El sistema debe mostrar la tarifa actual al cambiar de estado
* Debe actualizarse automáticamente

---

# HU-09 — Validar comandos incorrectos
>>>>>>> feature/tests-tarifas

## Prioridad

Media

## Descripción

<<<<<<< HEAD
Como usuaria
quiero introducir el precio del combustible
para adaptar las tarifas a la situación actual.

## Criterios de aceptación

* El sistema debe solicitar el precio al iniciar el programa.
* El precio debe utilizarse en el cálculo de tarifas.
* Solo deben aceptarse valores numéricos válidos.

---

# HU-09 — Registrar logs del sistema
=======
Como usuario,
quiero recibir mensajes de error claros cuando escriba comandos incorrectos,
para utilizar correctamente el sistema.

## Criterios de aceptación

* El sistema debe detectar comandos inválidos
* Debe mostrar una lista de comandos válidos

---

# HU-10 — Ejecutar pruebas automáticas
>>>>>>> feature/tests-tarifas

## Prioridad

Media

## Descripción

<<<<<<< HEAD
Como desarrolladora
quiero registrar eventos importantes mediante logs
para detectar errores y realizar seguimiento del funcionamiento del sistema.

## Criterios de aceptación

* El sistema debe registrar:
=======
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
>>>>>>> feature/tests-tarifas

  * inicio de trayecto
  * cambios de estado
  * finalización de viaje
  * cierre del programa
<<<<<<< HEAD
* Los logs deben guardarse en un archivo `.log`.

---

# HU-10 — Implementar tests automáticos
=======
* Los logs deben incluir fecha y hora

---

# HU-12 — Generación de ticket visual
>>>>>>> feature/tests-tarifas

## Prioridad

Media

## Descripción

<<<<<<< HEAD
Como desarrolladora
quiero implementar tests automáticos
para asegurar el correcto funcionamiento de las funciones principales.

## Criterios de aceptación

* Deben existir tests para el cálculo de tarifas.
* Los tests deben ejecutarse mediante `unittest`.
* El sistema debe superar correctamente todas las pruebas.
=======
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
>>>>>>> feature/tests-tarifas
