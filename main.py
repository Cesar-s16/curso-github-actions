import os
import sys

name = os.getenv("NAME", "Mundo")
mode = os.getenv("MODE", "simple")

print(f"Hola {name}")

if mode == "advanced":
    print("¡Modo avanzado activado!")
    print(f"Ejecutando en: {sys.platform}")