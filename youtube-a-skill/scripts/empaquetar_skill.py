#!/usr/bin/env python3
"""
empaquetar_skill.py - comprueba una carpeta de skill y la convierte en un
archivo .skill listo para «Guardar habilidad». Solo biblioteca estándar.

Comprueba
  - que existe SKILL.md con cabecera YAML entre dos líneas «---»
  - que name va en minúsculas, números y guiones, como mucho 64 caracteres,
    y coincide con el nombre de la carpeta
  - que description existe y no pasa de 1024 caracteres
  - que la cabecera solo usa campos admitidos (name, description, license,
    allowed-tools, metadata)
  - que no hay archivos ocultos ni cachés de Python dentro

Uso
  python3 empaquetar_skill.py CARPETA_DE_LA_SKILL [--salida DIRECTORIO]
"""

import argparse
import os
import re
import sys
import zipfile

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

CAMPOS = {"name", "description", "license", "allowed-tools", "metadata"}


def cabecera(texto):
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", texto, re.S)
    if not m:
        raise ValueError("SKILL.md debe empezar con una cabecera entre dos líneas «---».")
    campos, actual = {}, None
    for linea in m.group(1).splitlines():
        if not linea.strip():
            continue
        if not linea.startswith((" ", "\t")):
            clave, _, valor = linea.partition(":")
            actual = clave.strip()
            campos[actual] = valor.strip()
        elif actual:
            campos[actual] = (campos[actual] + " " + linea.strip()).strip()
    for k, v in campos.items():
        v = re.sub(r"^[>|][-+]?\s*", "", v)
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        campos[k] = v
    return campos


def comprobar(carpeta):
    errores = []
    nombre = os.path.basename(os.path.normpath(carpeta))
    ruta = os.path.join(carpeta, "SKILL.md")
    if not os.path.isfile(ruta):
        return [f"No existe {ruta}"]
    try:
        c = cabecera(open(ruta, encoding="utf-8").read())
    except ValueError as e:
        return [str(e)]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", c.get("name", "")) or len(c.get("name", "")) > 64:
        errores.append(f"name «{c.get('name')}» debe ir en minúsculas, números y guiones (máx. 64).")
    elif c["name"] != nombre:
        errores.append(f"name «{c['name']}» no coincide con la carpeta «{nombre}».")
    if not c.get("description"):
        errores.append("Falta description.")
    elif len(c["description"]) > 1024:
        errores.append(f"description tiene {len(c['description'])} caracteres (máx. 1024).")
    extra = set(c) - CAMPOS
    if extra:
        errores.append(f"Campos no admitidos en la cabecera: {', '.join(sorted(extra))}. Muévelos a metadata.")
    return errores


def empaquetar(carpeta, salida):
    carpeta = os.path.normpath(carpeta)
    nombre = os.path.basename(carpeta)
    destino = os.path.join(salida, nombre + ".skill")
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, dirs, archivos in os.walk(carpeta):
            dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d != "__pycache__")
            for a in sorted(archivos):
                if a.startswith(".") or a.endswith(".pyc"):
                    continue
                completo = os.path.join(raiz, a)
                z.write(completo, os.path.join(nombre, os.path.relpath(completo, carpeta)))
    with zipfile.ZipFile(destino) as z:
        if z.testzip() is not None:
            raise RuntimeError("El archivo .skill ha salido dañado.")
        n = len(z.namelist())
    return destino, n


def main():
    ap = argparse.ArgumentParser(description="Comprueba y empaqueta una skill en .skill")
    ap.add_argument("carpeta")
    ap.add_argument("--salida", default=".")
    a = ap.parse_args()
    errores = comprobar(a.carpeta)
    if errores:
        print("NO SE PUEDE EMPAQUETAR:\n  - " + "\n  - ".join(errores), file=sys.stderr)
        sys.exit(1)
    os.makedirs(a.salida, exist_ok=True)
    destino, n = empaquetar(a.carpeta, a.salida)
    print(f"Listo: {destino} ({n} archivos)")


if __name__ == "__main__":
    main()
