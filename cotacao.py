
import requests
URL = 'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
req = requests.get(URL)
dados_recebidos = req.json()
print(dados_recebidos)
if req.status_code == 200:
    dados = req.json()
    print ('Moedas')
    print (dados['USDBRL']["name"])
    print ('Valor de compra em Reais')
    print (dados['USDBRL']["bid"])
    print ('Atualizado em')
    print (dados['USDBRL']["create_date"])
    print ('\n')
    print ('Moedas')
    print (dados['EURBRL']["name"])
    print ('Valor de compra em Reais')
    print (dados['EURBRL']["bid"])
    print ('Atualizado em')
    print (dados['EURBRL']["create_date"])
    print ('\n')
    print ('Moedas')
    print (dados['BTCBRL']["name"])
    print ('Valor de compra em Reais')
    print (dados['BTCBRL']["bid"])
    print ('Atualizado em')
    print (dados['BTCBRL']["create_date"])
    print ('\n')
    print ('Link para vericar nomenclaturas das chaves')
    print ('https://docs.awesomeapi.com.br/api-de-moedas')

if req.status_code == 404:
    print('Não encontrado')