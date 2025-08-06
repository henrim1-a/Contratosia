
import requests
import time
import random
from datetime import datetime

url = "https://contratos-ia.my.canva.site/pagina-de-vendas-para-contratos-ia"

user_agents = [
    "Mozilla/5.0 (Linux; Android 10)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

contador = 1

while True:
    try:
        headers = {
            "User-Agent": random.choice(user_agents)
        }

        response = requests.get(url, headers=headers, timeout=10)

        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if response.status_code == 200:
            msg = f"[{contador}] ✔️ Visita OK - {agora}\n"
        else:
            msg = f"[{contador}] ❌ Erro {response.status_code} - {agora}\n"

        print(msg.strip())

        # Salvar no arquivo de log
        with open("log_visitas.txt", "a") as f:
            f.write(msg)

        contador += 1
        time.sleep(random.randint(4, 10))  # Intervalo aleatório

    except Exception as erro:
        msg = f"[{contador}] ⚠️ Falha - {erro} - {agora}\n"
        print(msg.strip())
        with open("log_visitas.txt", "a") as f:
            f.write(msg)
        time.sleep(10)
