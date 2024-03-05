import requests

City_name = input('Digite a sua cidade: ')

API_KEY = "98d38496801a7ab800fd108be3843458"

link = f'https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={API_KEY}&lang=pt_br'
requisicao = requests.get(link)

requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15

print(f'O tempo da sua cidade está {descricao} e com a temperatura de {round(temperatura, 2)}°C')
