import requests

menu = True

def coin_price():
    main = True
    print('Insira a abreviação da moeda, ex : EUR, USD, BTC')
    while main:
        coin = input('Moeda: ').upper()
        request =  requests.get('http://economia.awesomeapi.com.br/json/last/'+ coin +'-BRL')
        while not request:
            print('Ocorreu um erro, insira uma moeda válida')
            coin = input('Moeda: ')
            request =  requests.get('http://economia.awesomeapi.com.br/json/last/'+ coin +'-BRL')
        else:
            json = request.json()
            print('Compra: R$ {:.5}'.format(json[coin]['bid']))
            print('Venda: R$ {:.5}'.format(json[coin]['ask']))
            print('Máximo(Dia): R$ {:.5}'.format(json[coin]['high']))
            print('Mínimo(Dia): R$ {:.5}'.format(json[coin]['low']))
            print('')
            next = int(input('''[1] Nova moeda
[2] Voltar
'''))
            while not 0 < next < 3:
                print('Insira uma opção válida')
                next = int(input('''[1] Nova moeda
[2] Voltar
'''))     
            if next == 1:
                pass
            else:
                break


def coin_converter():
    main = True
    print('Insira a abreviação da moeda, ex : EUR, USD, BTC')
    while main:
        coin1 = input('Moeda 1: ').upper()
        coin2 = input('Moeda 2: ').upper()
        price = float(input('Valor a ser convertido: '))
        request = requests.get('http://economia.awesomeapi.com.br/json/last/'+ coin1 + '-' + coin2)
        while not request:
            print('Ocorreu um erro, a converão não pode ser realizada ou foram inseridas moedas inválidas')
            coin1 = input('Moeda 1: ').upper()
            coin2 = input('Moeda 2: ').upper()
            price = float(input('Valor a ser convertido: '))
            request = requests.get('http://economia.awesomeapi.com.br/json/last/'+ coin1+ '-' + coin2)
        else:
            json = request.json()
            bid = float(json[coin1]['bid'])
            print(coin1, 'para', coin2)
            print(price, coin1, '=', '{:.5}'.format(price*bid), coin2)
            print('')
            next = int(input('''[1] Nova moeda
[2] Voltar
'''))
            while not 0 < next < 3:
                print('Insira uma opção válida')
                next = int(input('''[1] Converter novamente
    [2] Voltar
    '''))     
            if next == 1:
                pass
            else:
                break


while menu:
    option = int(input('''[1] Cotação atual da Moeda
[2] Converter Moedas
[3] Moedas disponíveis
[4] Sair
'''))
    while not 0 < option < 6:
        print('Insira uma opção válida')
        option = int(input('''[1] Cotação atual da Moeda
[2] Converter Moedas
[3] Moedas disponíveis
[4] Sair
'''))
    if option == 1:
        coin_price()
    if option == 2:
        coin_converter()
    if option == 3:
        print('='*21)
        print('   Lista de Moedas  ')
        print('='*21)
        coins = open('coins.txt', 'r', encoding='utf-8')
        for linha in coins:
            coin = linha.strip()
            print(coin)
        print('')
    if option == 4:
        break
