import requests
import datetime
import os

# Configuración
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GNEWS_API_KEY = "e92b6cd7710b45a677d22d056e10e0f1"

# Inicial: fecha de inicio del conteo de entregas
ENTREGA_INICIAL = 1
FECHA_INICIAL = datetime.date(2025, 6, 18)

# Palabras clave y parámetros por idioma
CONSULTAS = [
    {"q": "música folclórica OR música tradicional OR folklore", "lang": "es", "country": "ve"},
    {"q": "música folclórica OR música tradicional OR folklore", "lang": "es", "country": "co"},
    {"q": "música popular OR folclore", "lang": "pt", "country": "br"},
    {"q": "musique traditionnelle OR folklore", "lang": "fr", "country": "fr"},
    {"q": "musica tradizionale OR folklore", "lang": "it", "country": "it"},
    {"q": "música tradicional OR festival OR folklore", "lang": "es", "country": "ar"},
    {"q": "musique africaine OR folklore", "lang": "fr", "country": "sn"},
    {"q": "música cabo-verdiana OR morna OR funaná", "lang": "pt", "country": "cv"},
]

def obtener_titulares():
    titulares = []
    hace_24h = (datetime.datetime.utcnow() - datetime.timedelta(hours=24)).isoformat("T") + "Z"

    for consulta in CONSULTAS:
        params = {
            "q": consulta["q"],
            "lang": consulta["lang"],
            "country": consulta["country"],
            "token": GNEWS_API_KEY,
            "max": 2,
            "from": hace_24h
        }
        res = requests.get("https://gnews.io/api/v4/search", params=params)
        if res.status_code == 200:
            datos = res.json()
            for article in datos.get("articles", []):
                titulo = article["title"]
                descripcion = article.get("description") or ""
                if len(descripcion) > 300:
                    descripcion = descripcion[:297] + "..."
                titulares.append({
                    "pais": f"🌍",
                    "titulo": titulo.strip(),
                    "descripcion": descripcion.strip(),
                    "url": article["url"]
                })
        else:
            print(f"Error con consulta {consulta['country']}: {res.status_code}")
    return titulares[:8]

def enviar_resumen():
    hoy = datetime.date.today()
    dias_pasados = (hoy - FECHA_INICIAL).days
    nro_entrega = ENTREGA_INICIAL + dias_pasados
    fecha_str = hoy.strftime("%d/%m/%y")
    numero = f"2025-{nro_entrega:03d}"

    titulares = obtener_titulares()

    mensaje = f"🎶 *Resumen de folclore RCA – {fecha_str} – Nº {numero}*\n"
    for i, item in enumerate(titulares, start=1):
        mensaje += f"\n{i}. {item['pais']} *{item['titulo']}*\n"
        mensaje += f"📰 {item['descripcion']}\n"
        mensaje += f"🔗 {item['url']}\n"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    })

if __name__ == "__main__":
    enviar_resumen()
