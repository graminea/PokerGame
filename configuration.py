from countdown import countdown
from colorama import init, Fore, Style

init(autoreset=True)

'''
def configuration():
    print(Fore.GREEN + '-------------------------------------------------------------------------------------------------------------------------------------------')
    print(Fore.YELLOW + Style.BRIGHT + "\nPokerGame\n")
    countdown(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Configs default: \nPlayer Name: 'player1' \nBot Name: 'Bot' \nFichas Iniciais: 1000")
    countdown(1)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\nSe deseja usar as configurações default digite 0 \nPara usar configurações personalizadas digite 1\n")
    countdown(1)
    while True:
        choice = None
        while choice is None:
            choice_input = input('Escolha: ')
            try:
                choice = int(choice_input)
            except ValueError:
                print(Fore.RED + f'"{choice_input}" não é um número!!')
                print(Fore.YELLOW + 'Tente Novamente')
            finally:
                countdown(1)
        if 0 <= choice <= 1:
            print(Fore.CYAN + Style.BRIGHT + "\nConfigurations\n")
            countdown(1)
            if choice == 0:
                name = "Player 1"
                bot_name = "Bot"
                chips = 1000
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Configs Default aplicadas")
                break
            else: 
                while True:
                    name = input(Fore.MAGENTA + "Digite o seu nome: " + Fore.RESET)
                    countdown(1)

                    bot_name = input(Fore.MAGENTA + "Digite um nome para o bot: " + Fore.RESET)
                    countdown(1)

                    if name == bot_name:
                        print(Fore.RED + '\nNomes iguais!!\nOs nomes devem ser diferentes. Tente novamente!!\n')
                        countdown(1)
                    else:
                        break

                chips = None
                while chips is None:
                    print(Fore.MAGENTA + 'Valor mínimo: 500 fichas')
                    input_value = input(Fore.MAGENTA + "Digite a quantidade de fichas que você e o bot começarão: " + Fore.RESET)
                    try:
                        chips = float(input_value)
                        if chips <= 500:
                            print(Fore.RED + '\nValor mínimo de fichas é de 500\nTente novamente!\n')
                            countdown(1)
                            chips = None
                    except ValueError:
                        print(Fore.RED + f'"{input_value}" não é um número!!')
                        print(Fore.YELLOW + 'Tente novamente!\n')
                    finally:
                        countdown(1)
                break        
        else:
            print(Fore.RED + Style.BRIGHT + "Escolha fora dos parâmetros, tente novamente!!\n")
            countdown(1)

    print(Fore.GREEN + Style.BRIGHT + "\nConfigurações concluídas! Vamos começar o jogo!")
    print()
    countdown(1)
    
    return name, bot_name, chips
'''

def configuration():
    name = 'player1'
    bot_name = 'Bot'
    chips = 1000
    return name, bot_name, chips
