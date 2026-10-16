#!/usr/bin/env python3
"""
transcribir.py - saca la transcripción de un vídeo de YouTube sin claves, sin
cuentas y sin instalar nada: solo Python 3 y su biblioteca estándar.

Cómo lo hace
  1. Pregunta a YouTube por el vídeo haciéndose pasar por varias apps oficiales
     (la de visores VR, iOS, Android y la web móvil). La primera que devuelva
     subtítulos gana.
  2. Elige la pista: primero la del idioma pedido (por defecto, el original del
     vídeo), y dentro de un idioma, la manual antes que la automática.
  3. Descarga los subtítulos y los devuelve como texto, con marcas de tiempo.

Cuándo falla
  YouTube bloquea a menudo las IP de servidores en la nube (centros de datos)
  con un «confirma que no eres un bot». Desde un ordenador de casa suele
  funcionar. Si falla, el script sale con código 3 y explica el plan B: copiar
  la transcripción desde YouTube y pegarla, que siempre funciona y es gratis.

Uso
  python3 transcribir.py URL_O_ID
  python3 transcribir.py URL_O_ID --idioma es
  python3 transcribir.py URL_O_ID --json            # texto + metadatos en JSON
  python3 transcribir.py URL_O_ID -o video.md       # guarda en Markdown
  python3 transcribir.py --pegado texto.txt         # limpia una transcripción pegada a mano
  python3 transcribir.py --json3 subs.json3         # convierte un archivo json3 ya descargado

Códigos de salida
  0 bien · 1 entrada no válida · 2 el vídeo no tiene subtítulos · 3 YouTube bloqueó la petición
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

PLAYER = "https://www.youtube.com/youtubei/v1/player?prettyPrint=false"
CLIENTES = [
    ("ANDROID_VR", {"clientName": "ANDROID_VR", "clientVersion": "1.62.27", "deviceMake": "Oculus",
                    "deviceModel": "Quest 3", "androidSdkVersion": 32, "osName": "Android",
                    "osVersion": "12L"},
     "com.google.android.apps.youtube.vr.oculus/1.62.27 (Linux; U; Android 12L; eureka-user Build/SQ3A.220605.009.A1) gzip"),
    ("IOS", {"clientName": "IOS", "clientVersion": "20.10.4", "deviceMake": "Apple",
             "deviceModel": "iPhone16,2", "osName": "iPhone", "osVersion": "18.3.2.22D82"},
     "com.google.ios.youtube/20.10.4 (iPhone16,2; U; CPU iOS 18_3_2 like Mac OS X;)"),
    ("ANDROID", {"clientName": "ANDROID", "clientVersion": "20.10.38", "androidSdkVersion": 30,
                 "osName": "Android", "osVersion": "11"},
     "com.google.android.youtube/20.10.38 (Linux; U; Android 11) gzip"),
    ("MWEB", {"clientName": "MWEB", "clientVersion": "2.20250311.03.00"},
     "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Mobile/15E148 Safari/604.1"),
]
NAVEGADOR = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

PLAN_B = """\
YouTube ha bloqueado la petición (suele pasar desde servidores en la nube).
Plan B, gratis (elige uno):
  A. Una web de transcripciones, desde el navegador del móvil o del ordenador:
     abre youtubetotranscript.com o tactiq.io/tools/youtube-transcript, pega el
     enlace del vídeo, pulsa el botón para generar y copia el texto.
  B. En el ordenador, en YouTube: debajo del vídeo pulsa «...más» y luego
     «Mostrar transcripción»; selecciona el texto con el ratón y cópialo.
     (En la app del móvil no se puede copiar.)
  C. Si Claude tiene acceso a tu Chrome, que abra el vídeo y lea la transcripción.
Pega el texto en el chat y se sigue exactamente igual."""


class Bloqueado(Exception):
    pass


class SinSubtitulos(Exception):
    pass


def video_id(valor):
    valor = valor.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", valor):
        return valor
    m = re.search(r"(?:v=|/shorts/|/embed/|/live/|youtu\.be/|/v/)([A-Za-z0-9_-]{11})", valor)
    if not m:
        raise ValueError(f"No encuentro el identificador del vídeo en: {valor}")
    return m.group(1)


def _post(url, cuerpo, agente, timeout=20):
    req = urllib.request.Request(url, data=json.dumps(cuerpo).encode(), headers={
        "Content-Type": "application/json", "User-Agent": agente, "Accept-Language": "es-ES,es;q=0.9"})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def _get(url, agente=NAVEGADOR, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": agente, "Accept-Language": "es-ES,es;q=0.9"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")


def reproductor(vid):
    """Devuelve (respuesta_del_reproductor, cliente, agente) del primer cliente que dé subtítulos."""
    motivos = []
    sin_subs = None
    for nombre, cliente, agente in CLIENTES:
        try:
            d = _post(PLAYER, {"context": {"client": dict(cliente, hl="es", gl="ES")}, "videoId": vid}, agente)
        except urllib.error.HTTPError as e:
            motivos.append(f"{nombre}: HTTP {e.code}")
            continue
        except Exception as e:  # red, tiempo de espera...
            motivos.append(f"{nombre}: {e}")
            continue
        estado = d.get("playabilityStatus", {})
        pistas = d.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", [])
        if pistas:
            return d, nombre, agente
        if estado.get("status") == "OK":
            sin_subs = d                      # el vídeo se ve, pero sin subtítulos con este cliente
        motivos.append(f"{nombre}: {estado.get('status')} {estado.get('reason', '')}".strip())
    if sin_subs is not None:
        raise SinSubtitulos("El vídeo existe pero no tiene subtítulos (ni manuales ni automáticos).")
    raise Bloqueado("; ".join(motivos))


def elegir_pista(pistas, idioma=None):
    if not idioma:
        # Sin idioma pedido, el original del vídeo: es el de la pista automática,
        # porque YouTube solo genera subtítulos automáticos en el idioma hablado.
        auto = [p for p in pistas if p.get("kind") == "asr"]
        idioma = auto[0].get("languageCode", "").split("-")[0] if auto else None

    def clave(p):
        lang = p.get("languageCode", "")
        auto = p.get("kind") == "asr"
        prefer = 0 if idioma and lang.split("-")[0] == idioma else 1
        return (prefer, auto)
    return sorted(pistas, key=clave)[0]


def segmentos_json3(datos):
    segs = []
    for ev in datos.get("events", []):
        if "segs" not in ev:
            continue
        texto = "".join(s.get("utf8", "") for s in ev["segs"]).replace("\n", " ").strip()
        if texto:
            segs.append({"inicio": ev.get("tStartMs", 0) / 1000, "texto": texto})
    return segs


def segmentos_xml(xml):
    import html
    segs = []
    for m in re.finditer(r'<(?:text|p)[^>]*?(?:start="([\d.]+)"|t="(\d+)")[^>]*>(.*?)</(?:text|p)>', xml, re.S):
        inicio = float(m.group(1)) if m.group(1) else int(m.group(2)) / 1000
        texto = html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).replace("\n", " ").strip()
        if texto:
            segs.append({"inicio": inicio, "texto": texto})
    return segs


def descargar_pista(pista, agente):
    base = re.sub(r"&fmt=[^&]+", "", pista["baseUrl"])
    try:
        return segmentos_json3(json.loads(_get(base + "&fmt=json3", agente)))
    except Exception:
        return segmentos_xml(_get(base, agente))


def transcribir(valor, idioma=None):
    vid = video_id(valor)
    d, cliente, agente = reproductor(vid)
    pistas = d["captions"]["playerCaptionsTracklistRenderer"]["captionTracks"]
    pista = elegir_pista(pistas, idioma)
    segs = descargar_pista(pista, agente)
    if not segs:
        raise Bloqueado("La pista de subtítulos llegó vacía (YouTube suele hacer esto cuando sospecha de un bot).")
    det = d.get("videoDetails", {})
    return {
        "video_id": vid,
        "url": f"https://www.youtube.com/watch?v={vid}",
        "titulo": det.get("title"),
        "canal": det.get("author"),
        "duracion_s": int(det.get("lengthSeconds") or 0) or None,
        "visualizaciones": int(det.get("viewCount") or 0) or None,
        "idioma": pista.get("languageCode"),
        "automatico": pista.get("kind") == "asr",
        "idiomas_disponibles": sorted({p.get("languageCode") for p in pistas}),
        "via": cliente,
        "segmentos": segs,
    }


def limpiar_pegado(texto):
    """Convierte lo que se copia de «Mostrar transcripción» en segmentos.

    YouTube lo copia alternando líneas de tiempo («0:03», «1:02:15») y de texto.
    Si no hay marcas de tiempo, se devuelve el texto tal cual en un segmento.
    """
    segs, actual = [], None
    for linea in (l.strip() for l in texto.splitlines()):
        if not linea:
            continue
        m = re.fullmatch(r"(?:(\d+):)?(\d{1,2}):(\d{2})", linea)
        if m:
            h, mi, s = m.groups()
            actual = {"inicio": int(h or 0) * 3600 + int(mi) * 60 + int(s), "texto": ""}
            segs.append(actual)
        elif actual is not None:
            actual["texto"] = (actual["texto"] + " " + linea).strip()
        else:
            segs.append({"inicio": None, "texto": linea})
    return [s for s in segs if s["texto"]]


def hms(seg):
    if seg is None:
        return "--:--"
    seg = int(seg)
    h, r = divmod(seg, 3600)
    m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def texto_corrido(segs):
    return re.sub(r"\s+", " ", " ".join(s["texto"] for s in segs)).strip()


def a_markdown(r):
    lineas = [f"# {r.get('titulo') or r.get('video_id') or 'Transcripción'}", ""]
    for k, etiqueta in (("canal", "Canal"), ("url", "Enlace"), ("idioma", "Idioma de los subtítulos")):
        if r.get(k):
            lineas.append(f"- {etiqueta}: {r[k]}")
    if r.get("automatico") is not None:
        lineas.append(f"- Subtítulos: {'automáticos' if r['automatico'] else 'manuales'}")
    if r.get("duracion_s"):
        lineas.append(f"- Duración: {hms(r['duracion_s'])}")
    lineas += ["", "## Transcripción", ""]
    bloque, inicio = [], None
    for s in r["segmentos"]:
        if inicio is None:
            inicio = s["inicio"]
        bloque.append(s["texto"])
        if len(" ".join(bloque)) > 400:
            lineas += [f"[{hms(inicio)}] " + " ".join(bloque), ""]
            bloque, inicio = [], None
    if bloque:
        lineas += [f"[{hms(inicio)}] " + " ".join(bloque), ""]
    return "\n".join(lineas)


def main():
    ap = argparse.ArgumentParser(description="Transcripción de un vídeo de YouTube, gratis y sin instalar nada.")
    ap.add_argument("video", nargs="?", help="enlace de YouTube o identificador de 11 caracteres")
    ap.add_argument("--idioma", help="código de idioma preferido (es, en...). Por defecto, el del vídeo")
    ap.add_argument("--pegado", help="archivo con una transcripción copiada a mano de YouTube")
    ap.add_argument("--json3", help="archivo json3 de subtítulos ya descargado")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    ap.add_argument("-o", "--salida", help="guardar el resultado en este archivo (Markdown, o JSON con --json)")
    a = ap.parse_args()

    try:
        if a.pegado:
            r = {"segmentos": limpiar_pegado(open(a.pegado, encoding="utf-8").read()), "via": "pegado"}
        elif a.json3:
            r = {"segmentos": segmentos_json3(json.load(open(a.json3, encoding="utf-8"))), "via": "json3"}
        elif a.video:
            r = transcribir(a.video, a.idioma)
        else:
            ap.error("indica un enlace de YouTube, --pegado o --json3")
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except SinSubtitulos as e:
        print(f"SIN SUBTÍTULOS: {e}\nPlan B: si el vídeo tiene audio en un idioma que entiendas, "
              "describe o resume tú lo que dice y se trabaja con eso.", file=sys.stderr)
        sys.exit(2)
    except Bloqueado as e:
        print(f"BLOQUEADO: {e}\n\n{PLAN_B}", file=sys.stderr)
        sys.exit(3)

    r["palabras"] = len(texto_corrido(r["segmentos"]).split())
    salida = json.dumps(r, ensure_ascii=False, indent=1) if a.json else a_markdown(r)
    if a.salida:
        open(a.salida, "w", encoding="utf-8").write(salida)
        print(f"Guardado en {a.salida} ({r['palabras']} palabras, vía {r['via']})", file=sys.stderr)
    else:
        print(salida)


if __name__ == "__main__":
    main()
