import requests
from bs4 import BeautifulSoup

url = "https://www.booking.com/searchresults.pt-br.html?label=gen173nr-10CAEoggI46AdIM1gEaCCIAQGYATO4ARnIAQzYAQPoAQH4AQGIAgGoAgG4AvTpp8gGwAIB0gIkNTc2OTU0ODYtMjUxZi00OTg4LTliZDItNWUxNTBiYjk3ODMw2AIB4AIB&aid=304142&checkin=2025-11-28&checkout=2025-12-01&dest_id=-639568&dest_type=city&order=popularity&group_adults=5&req_adults=5&no_rooms=1&group_children=0&req_children=0"

response = requests.get(URL, timeout=10)
response.raise_for_status()

print("Requisição bem-sucedida! Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

hoteis = soup.find_all("div", {"data-testid": "property-card"})

for hotel in hoteis:
    nome = hotel.find("div", {"data-testid": "title"})
    preco = hotel.find("span", {"data-testid": "price-and-discounted-price"})
    nota = hotel.find("div", {"aria-hidden": "true", "class": "f63b14ab7a dff2e52086"})
    avaliacoes = hotel.find("div", {"class": "fff1944c52 fb14de7f14 eaa8455879"})

    dados.append({
        "nome": nome.get_text(strip=True) if nome else None,
        "preco": preco.get_text(strip=True) if preco else None,
        "nota": nota.get_text(strip=True) if nota else None,
        "avaliacoes": avaliacoes.get_text(strip=True) if avaliacoes else None
    })


for d in dados:
    print(f"Hotel: {d['nome']}")
    print(f"Preço: {d['preco']}")
    print(f"Nota: {d['nota']}")
    print(f"Avaliações: {d['avaliacoes']}")
    print("-" * 60)
