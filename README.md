
python robo_visitas_com_log.py

import requests
import time
import random

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
        
        if response.status_code == 200:
            print(f"[{contador}] Visita enviada com sucesso!")
        else:
            print(f"[{contador}] Código de status: {response.status_code}")
        
        contador += 1
        time.sleep(random.randint(4, 10))  # Intervalo aleatório entre visitas

    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(10)
