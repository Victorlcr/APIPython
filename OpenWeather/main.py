import requests

def obter_clima(*coordenadas, **params):
    # Caso base sem coordenadas pra processar
    if not coordenadas:
        return []

    # Recebe a coordenada de cada iteração
    atual = coordenadas[0]
    restante = coordenadas[1:]

    # URL dinâmica com os dados fornecidos
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={atual['lat']}&lon={atual['lon']}"
    for chave, valor in params.items():
            url += f"&{chave}={valor}"

    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        # Chama a função para empilhar as outras localidades
        adicionais = obter_clima(*restante, **params)
        # Converter de Kelvin pra Celsius
        temperatura = dados['main'].get('temp') - 273.15

        return [{
            'cidade': dados.get('name', 'Desconhecida'),
            'temp': round(temperatura, 1),
            'condicao': dados['weather'][0].get('description', 'Sem dados')
        }] + adicionais

# Localidades escolhidas para observar o clima
coordenadas = (
    {'lat': -23.157823, 'lon': -47.058063},
    {'lat': -23.189286, 'lon': -46.889119},
    {'lat': -23.550650, 'lon': -46.633382}
)
# Parâmetros para compor URL
resultados = obter_clima(
    *coordenadas,
    appid='c45d3c6ddf7e2baa0fc7c1b35522dbd4',
    unit='metric',
    lang='pt'
)
# Amostra dos principais dados metereológicos
for clima in resultados:
    print(f"{clima['cidade']}: {clima['temp']}ºC, {clima['condicao'].capitalize()}")
