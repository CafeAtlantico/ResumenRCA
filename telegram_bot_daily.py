# telegram_bot_daily.py
import requests
import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Fecha inicial del primer resumen y número de entrega
ENTREGA_INICIAL = 1
FECHA_INICIAL = datetime.date(2025, 6, 18)

# Simulación de titulares (más adelante puede conectarse a una API o scraping)
def obtener_titulares():
    return [
        {
            "pais": "🇻🇪",
            "titulo": "Fiesta de San Juan en Venezuela reunió a 5 mil tamboreros",
            "descripcion": "Las costas de Aragua y Miranda vibraron con la herencia afrovenezolana.",
            "url": "https://ejemplo.com/sanjuan-venezuela"
        },
        {
            "pais": "🇵🇪",
            "titulo": "Festival Inti Raymi se prepara en Cusco",
            "descripcion": "Autoridades culturales afinan detalles para el ritual incaico del solsticio.",
            "url": "https://ejemplo.com/intiraymi-cusco"
        },
        {
            "pais": "🇨🇻",
            "titulo": "Morna y funaná llegan a Coimbra desde Cabo Verde",
            "descripcion": "Ciclo de música crioula presenta artistas de las islas en Portugal.",
            "url": "https://ejemplo.com/morna-coimbra"
        }
    ]

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

# Para pruebas locales
if _name_ == "_main_":
    enviar_resumen()
