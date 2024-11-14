from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Inicializa o WebDriver
driver = webdriver.Chrome()

try:
    # URL da página SteamDB com promoções
    url = "https://steamdb.info/sales/"
    
    # Acessa a página
    driver.get(url)
    time.sleep(5)  # Espera alguns segundos para garantir o carregamento completo da página
    
    # Localiza os primeiros 100 jogos na tabela
    jogos = driver.find_elements(By.CSS_SELECTOR, "tr.app")[:100]  # Limita a 100 jogos
    
    # Lista para armazenar os dados brutos de cada jogo
    dados_brutos = []
    
    # Extrai e armazena os dados brutos de cada jogo
    for i, jogo in enumerate(jogos, start=1):
        texto_bruto = jogo.text  # Mantém os dados brutos sem substituições ou alterações
        dados_brutos.append({
            "Jogo": i,
            "Dados Brutos": texto_bruto
        })
    
    # Salva os dados brutos no arquivo JSON
    with open("dados_brutos_100.json", mode="w", encoding="utf-8") as arquivo_json:
        json.dump(dados_brutos, arquivo_json, ensure_ascii=False, indent=4)
        
    print("Dados brutos dos 100 primeiros jogos salvos em 'dados_brutos_100.json' com sucesso.")

except Exception as e:
    print("Erro ao extrair dados:", e)

finally:
    # Fecha o navegador
    driver.quit()
