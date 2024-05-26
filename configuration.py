from countdown import countdown


def configuration():
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print()
    print('PokerGame')
    print()
    print('Configurations')
    countdown(1)
    name = input('Digite o seu nome: ')
    countdown(1)
    bot_name = input('Digite um nome para o bot: ')
    countdown(1)
    chips = None
    while chips is None:
        input_value = input('Digite a quantidade de fichas que você e o bot começarão: ')
        try:
            chips = float(input_value)
        except ValueError:
            print(f'"{input_value}" não é um número!!')
            print('Tente novamente!')
        finally:
            countdown(1) 
    
    return name, bot_name, chips
