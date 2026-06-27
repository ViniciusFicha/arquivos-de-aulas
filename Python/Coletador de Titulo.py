import requests
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Python_(linguagem_de_programação)"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
} 

try:
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    titulo_da_pagina = soup.title.text

    print(f"O título da página é: {titulo_da_pagina}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    print("Verifique sua conexão com a internet ou se a URL está correta.")