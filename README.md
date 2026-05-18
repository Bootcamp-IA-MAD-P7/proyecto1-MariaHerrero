
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

---

# ▶️ Cómo ejecutar el proyecto

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

## 2. Entrar en carpeta

```bash
cd taximetro_MariaH
```

## 3. Ejecutar programa

```bash
python taximetroMHS.py
```

---

# 🧪 Ejecutar tests

```bash
python -m unittest test_taximetro.py
```

---

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
