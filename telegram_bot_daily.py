telegram_bot_daily.py

import requests import datetime import os

BOT_TOKEN = os.getenv("BOT_TOKEN") CHAT_ID = os.getenv("CHAT_ID")

ENTREGA_INICIAL = 1 FECHA_INICIAL = datetime.date(2025, 6, 18)

def obtener_titulares(): # Titulares reales curados diariamente (ejemplo del 19 de junio de 2025) return [ { "pais": "🇻🇪", "titulo": "Festival de Tambores retumbará en Caracas del 20 al 22 de junio", "descripcion": "La III edición del Festacove ofrecerá 30 conciertos y talleres en La Carlota.", "url": "https://ciudadccs.info/publicacion/65550/festacove-invita-a-celebrar-la-afrovenezolanidad" }, { "pais": "🇻🇪", "titulo": "Gala Festacove honrará a promotores culturales venezolanos", "descripcion": "Casimira Monasterios y Luis Felipe Hidalgo entre los homenajeados del evento.", "url": "https://ciudadccs.info/publicacion/65549/a-favor-o-en-contra-abrira-festacove" }, { "pais": "🇨🇴", "titulo": "Ibagué se engalana para el 51º Festival Folclórico Colombiano", "descripcion": "Más de 60 eventos culturales y desfiles se realizarán en junio en Tolima.", "url": "https://www.alertatolima.com/noticias/tolima/ibague/ibague-se-engalana-para-el-51o-festival-folclorico-colombiano" }, { "pais": "🇵🇪", "titulo": "Festival Inti Raymi se prepara en Cusco", "descripcion": "El gran ritual incaico del solsticio se celebrará el 24 de junio en Sacsayhuamán.", "url": "https://elcomercio.pe/lima/cusco-celebra-el-inti-raymi-2025-lo-que-debes-saber-sobre-la-fiesta-del-sol-noticia/" }, { "pais": "🇨🇻", "titulo": "Morna y funaná llegan a Coimbra desde Cabo Verde", "descripcion": "Portugal acoge una serie de conciertos de música crioula de las islas atlánticas.", "url": "https://africulturban.pt/morna-funana-cabo-verde-coimbra" }, { "pais": "🇦🇷", "titulo": "Paola Bernal presenta nuevo trabajo en gira por Córdoba", "descripcion": "La artista del folclore argentino lleva su disco 'Agua de flores' a teatros provinciales.", "url": "https://www.pagina12.com.ar/folklore/paola-bernal-agua-de-flores" } ]

def enviar_resumen(): hoy = datetime.date.today() dias_pasados = (hoy - FECHA_INICIAL).days nro_entrega = ENTREGA_INICIAL + dias_pasados

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

if name == "main": enviar_resumen()
