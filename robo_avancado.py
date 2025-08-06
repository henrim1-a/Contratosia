
import requests
import time
import random
from datetime import datetime

def carregar_links():
    try:
        with open("links.txt", "r") as f:
            return [linha.strip() for linha in f.readlines() if linha.strip()]
    except FileNotFoundError:
        print("❌ Arquivo 'links.txt' não encontrado.")
        return []

def carregar_proxies():
    try:
        with open("proxies.txt", "r") as f:
            return [linha.strip() for linha in f.readlines() if linha.strip()]
    except FileNotFoundError:
        return []

def menu():
    print("==== ROBÔ DE TRÁFEGO ILIMITADO ====")
    print("1. Iniciar envio de visitas")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def enviar_visitas(links, proxies):
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
        for link in links:
            proxy = random.choice(proxies) if proxies else None
            proxy_dict = {"http": proxy, "https": proxy} if proxy else None
            headers = {"User-Agent": random.choice(user_agents)}
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                response = requests.get(link, headers=headers, proxies=proxy_dict, timeout=10)
                if response.status_code == 200:
                    msg = f"[{contador}] ✔️ Visita OK em {link} - {agora}\n"
                else:
                    msg = f"[{contador}] ❌ Erro {response.status_code} em {link} - {agora}\n"
            except Exception as erro:
                msg = f"[{contador}] ⚠️ Falha em {link} - {erro} - {agora}\n"

            print(msg.strip())
            with open("log_visitas.txt", "a") as f:
                f.write(msg)
            contador += 1
            time.sleep(random.randint(4, 10))

if __name__ == "__main__":
    opcao = menu()
    if opcao == "1":
        links = carregar_links()
        if not links:
            print("⚠️ Nenhum link encontrado. Adicione links no arquivo links.txt")
        else:
            proxies = carregar_proxies()
            enviar_visitas(links, proxies)
    else:
        print("Saindo...")
