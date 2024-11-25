# Treembo Marketplace - Pruebas Unitarias

Este repositorio contiene una simulación del marketplace de Treembo y pruebas unitarias diseñadas para validar su funcionalidad usando **pytest** en entornos Windows con herramientas como **PowerShell** y **VS Code**.
---
Estructura del proyecto

treembo-marketplace-tests/
├── models/                   
│   ├── __init__.py
│   ├── marketplace.py       
│
├── tests/                    
│   ├── __init__.py
│   ├── test_marketplace.py   
│
├── requirements.txt          
├── README.md                 


---

## **Requisitos**

Antes de comenzar, asegúrate de tener instalado:

- **Python** (versión 3.8 o superior)
  - Descarga e instala desde [python.org](https://www.python.org/downloads/). Asegúrate de marcar la casilla **"Add Python to PATH"** durante la instalación.
- **pip** (incluido con Python).

---

## **Instalación en Windows**

### **1. Clonar el repositorio**

1. Abre **PowerShell** en tu computadora.
2. Clona el repositorio usando Git:
   ```powershell
   git clone https://github.com/wichoiscoding/treembo-unit-tests.git/
   cd treembo-unit-tests

3. Instala las dependencias
   pip install -r requirements.txt

4. Ejecucion (desde la raiz)
   pytest


