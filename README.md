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

---

# ▶️ Cómo ejecutar el proyecto

## Ejecutar aplicación principal

```bash
python taximetroMHS.py
```

---

## Ejecutar tests

```bash
python -m unittest test_taximetro.py
```

---

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

