<<<<<<< HEAD

# 🚕 Taxímetro MHS

Proyecto desarrollado en Python como simulador de un taxímetro mediante una interfaz de línea de comandos (CLI).

El programa permite iniciar trayectos, calcular tarifas en tiempo real, guardar históricos de viajes y mostrar estadísticas del día.

---

# 📌 Funcionalidades

## ✅ Nivel esencial

* Iniciar trayectos
* Calcular tarifa mientras el taxi está parado
* Calcular tarifa mientras el taxi está en movimiento
* Finalizar trayectos mostrando el total
* Permitir múltiples trayectos sin cerrar el programa

---

## ✅ Funcionalidades implementadas

### 🚕 Gestión de trayectos

* Inicio y finalización de carreras
* Cambio de estado:

  * `parado`
  * `moviendonos`

### 💰 Tarifas dinámicas

* Tarifa configurable según el precio del combustible
* Cálculo automático:

  * Taxi parado → 0.02€/seg
  * Taxi en movimiento → 0.05€/seg

### 📊 Resumen del día

* Total ganado
* Número de trayectos
* Media por trayecto

### 📄 Historial de trayectos

* Guardado automático en fichero `.txt`
* Registro con fecha y hora

### 📝 Logs

* Registro de eventos importantes:

  * Inicio de trayecto
  * Cambio de estado
  * Finalización
  * Cierre del programa

### ✅ Tests unitarios

* Tests automáticos usando `unittest`
* Verificación del cálculo de tarifas

---
# 📋 Historias de usuario

## 📋 Documentación adicional

- Historias de usuario: `historias_usuario.md`




# 🛠️ Tecnologías utilizadas

* Python
* Git
* GitHub
* Logging
* Unittest
=======
# 🚕 TAXÍMETRO MHS

Aplicación desarrollada en Python que simula el funcionamiento de un taxímetro real desde consola.

El proyecto permite iniciar trayectos, calcular tarifas en tiempo real, registrar historiales, generar tickets, visualizar ingresos diarios y almacenar logs de actividad.

---

# 📌 Descripción del proyecto

Este proyecto ha sido desarrollado como parte del bootcamp de programación Full Stack e Inteligencia Artificial.

El objetivo principal es aplicar conceptos fundamentales de programación utilizando Python:

* funciones,
* estructuras condicionales,
* bucles,
* manejo de archivos,
* testing,
* logs,
* control de versiones con Git y GitHub.

El programa simula el comportamiento de un taxímetro real mediante comandos desde terminal.

---

# ⚙️ Funcionalidades principales

## 🚕 Gestión de trayectos

* Inicio de carrera
* Cambio de estado:

  * parado
  * moviéndonos
* Finalización de trayecto
* Reinicio automático de variables tras finalizar un viaje

---

## 💰 Cálculo de tarifas

El precio del trayecto se calcula teniendo en cuenta:

* tiempo parado
* tiempo en movimiento
* precio del combustible

Tarifas base:

* Parado → 0.02 €/segundo
* Movimiento → 0.05 €/segundo

---

## ⛽ Precio del combustible

El usuario puede introducir el precio actual del combustible al iniciar el programa.

El sistema incluye validación de entrada para evitar errores si se introducen valores no numéricos.

---

## 📄 Historial de trayectos

Cada trayecto finalizado se almacena automáticamente en:

```text
historial.txt
```

Incluyendo:

* fecha,
* duración,
* tiempo parado,
* tiempo en movimiento,
* importe total.

---

## 📊 Resumen del día

El sistema muestra:

* total ganado durante el día,
* ingresos acumulados.

---

## 🎫 Ticket de viaje

Al finalizar un trayecto se genera un ticket visual con:

* combustible,
* tiempo parado,
* tiempo movimiento,
* importe final.

---

## 📝 Sistema de logs

El proyecto incluye un sistema de logs utilizando el módulo `logging`.

Los eventos se almacenan en:

```text
taximetro.log
```

Se registran acciones como:

* inicio de trayecto,
* cambios de estado,
* cierre de programa,
* finalización de viajes.

---

## 🎞️ Animación de tarifa final

El proyecto incluye una animación sencilla en consola que muestra el cálculo progresivo de la tarifa final.

---

# 🧪 Testing

El proyecto incluye pruebas unitarias utilizando `unittest`.

Archivo de tests:

```text
test_taximetro.py
```

Se realizan pruebas sobre:

* cálculo de tarifas,
* tarifa en vivo,
* trayectos simulados,
* flujo completo básico del sistema.

---

# 🚕 Demo automática

El proyecto incluye una simulación automática completa:

```text
demo_taximetro.py
```

Esta demo permite visualizar:

* trayecto completo,
* cálculo de tarifa,
* historial,
* resumen final,

sin necesidad de introducir comandos manualmente.

Para ejecutarla:

```bash
python demo_taximetro.py
```
>>>>>>> feature/tests-tarifas

---

# ▶️ Cómo ejecutar el proyecto

<<<<<<< HEAD
## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

## 2. Entrar en carpeta

```bash
cd taximetro_MariaH
```

## 3. Ejecutar programa
=======
## Ejecutar aplicación principal
>>>>>>> feature/tests-tarifas

```bash
python taximetroMHS.py
```

---

<<<<<<< HEAD
# 🧪 Ejecutar tests
=======
## Ejecutar tests
>>>>>>> feature/tests-tarifas

```bash
python -m unittest test_taximetro.py
```

---

<<<<<<< HEAD
# 💻 Comandos disponibles

| Comando       | Función              |
| ------------- | -------------------- |
| inicio        | Iniciar trayecto     |
| parado        | Taxi detenido        |
| moviendonos   | Taxi en movimiento   |
| findetrayecto | Finalizar trayecto   |
| resumen_dia   | Mostrar estadísticas |
| historial     | Mostrar historial    |
| salir         | Cerrar programa      |

---

# 🧹 Buenas prácticas implementadas

* Clean Code
* Constantes globales
* Separación de responsabilidades
* Reutilización de funciones
* Uso de ramas feature en Git

---

# 👩‍💻 Autora

María Herrero Sánchez

Proyecto desarrollado durante el bootcamp de programación y desarrollo en Python.
=======
# 📂 Estructura del proyecto

```text
taximetro_MariaH/
│
├── taximetroMHS.py
├── test_taximetro.py
├── demo_taximetro.py
├── historial.txt
├── taximetro.log
├── README.md
└── .gitignore
```

---

# 🛠️ Tecnologías utilizadas

* Python 3
* Git
* GitHub
* VS Code
* unittest
* logging

---

# 🌱 Metodología de trabajo

El proyecto se ha desarrollado utilizando:

* ramas feature,
* commits incrementales,
* control de versiones con Git,
* documentación técnica,
* historias de usuario.

---

# 👩‍💻 Autor

Proyecto desarrollado por:

**María Herrero Sánchez**

Bootcamp Factoria F5 Promocion 7 🚀

>>>>>>> feature/tests-tarifas
