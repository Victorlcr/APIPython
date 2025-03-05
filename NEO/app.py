import requests

def obter_url_base(data, api_key):
    # Cria e retorna a URL para a consulta da NASA API.
    return f"https://api.nasa.gov/neo/rest/v1/feed?start_date={data['inicio']}&end_date={data['fim']}&api_key={api_key}"

def obter_resposta(url):
    # Faz a requisição à NASA API e retorna a resposta JSON se for bem-sucedida.
    resposta = requests.get(url)
    if resposta.status_code != 200:
        print(resposta.status_code)
        exit()
    return resposta.json()

def processar_asteroide(asteroide):
    # Processa os dados de um asteroide e retorna as informações relevantes.
    nome = asteroide['name']
    diametro_max = round(asteroide['estimated_diameter']['kilometers']['estimated_diameter_max'], 2)
    perigoso = 'Sim' if asteroide['is_potentially_hazardous_asteroid'] else 'Não'
    return nome, diametro_max, perigoso

def processar_aproximacao(dado_aproximado):
    # Processa os dados de aproximação do asteroide e retorna informações relevantes.
    velocidade_kmh = round(float(dado_aproximado['relative_velocity']['kilometers_per_hour']), 2)
    distancia_km = round(float(dado_aproximado['miss_distance']['kilometers']), 2)
    orbita = dado_aproximado['orbiting_body']
    return velocidade_kmh, distancia_km, orbita

def exibir_asteroide_proximo(nome, diametro_max, km_por_h, distancia_km, perigoso):
    # Exibe as informações do asteroide em risco de aproximação com a Terra.
    asteroides_proximos = {
        'Nome': nome,
        'Diâmetro Máx.': diametro_max,
        'Velocidade Km/h': km_por_h,
        'Distância Min.': distancia_km,
        'Potencialmente perigoso': perigoso
    }
    print(asteroides_proximos)

def main():
    # Função principal que executa o processo de consulta e exibição dos dados de asteroides próximos.
    data = {'inicio': '2025-03-01', 'fim': '2025-03-02'}
    api_key = 'jiZiJZT1wN1ppmR6mwtzeJYnbcnTGEnpc2Ls2EWZ'

    url = obter_url_base(data, api_key)
    resposta = obter_resposta(url)

    for data, asteroides in resposta['near_earth_objects'].items():
        for asteroide in asteroides:
            nome, diametro_max, perigoso = processar_asteroide(asteroide)
            dados_aproximados = asteroide['close_approach_data']
            
            for dado_aproximado in dados_aproximados:
                km_por_h, distancia_km, orbita = processar_aproximacao(dado_aproximado)
                
                if orbita == 'Earth':  # Considera apenas os asteroides que se aproximam da Terra
                    exibir_asteroide_proximo(nome, diametro_max, km_por_h, distancia_km, perigoso)

if __name__ == "__main__":
    main()
