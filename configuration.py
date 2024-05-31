from countdown import countdown
from colorama import init, Fore, Style

init(autoreset=True)

def configuration():
    print(Fore.GREEN + '-------------------------------------------------------------------------------------------------------------------------------------------')
    print(Fore.YELLOW + Style.BRIGHT + "\nPokerGame\n")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Configs default: \nPlayer Name: 'player1' \nBot Name: 'Bot' \nFichas Iniciais: 1000")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nSe deseja usar as configurações default digite 0 \nPara usar configurações personalizadas digite 1\n")
    choice = int(input('Escolha: '))
    print(Fore.CYAN + Style.BRIGHT + "\nConfigurations\n")
    countdown(1)
    while True:
        if 0 <= choice <= 1:
            if choice == 0:
                name = "Player 1"
                bot_name = "Bot"
                chips = 1000
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Configs Default aplicadas")
                break
            else: 
                name = input(Fore.MAGENTA + "Digite o seu nome: " + Fore.RESET)
                countdown(1)

                bot_name = input(Fore.MAGENTA + "Digite um nome para o bot: " + Fore.RESET)
                countdown(1)

                chips = None
                while chips is None:
                    input_value = input(Fore.MAGENTA + "Digite a quantidade de fichas que você e o bot começarão: " + Fore.RESET)
                    try:
                        chips = float(input_value)
                    except ValueError:
                        print(Fore.RED + f'"{input_value}" não é um número!!')
                        print(Fore.YELLOW + 'Tente novamente!')
                    finally:
                        countdown(1) 
                break
        else:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Escolha fora dos parâmetros, tente novamente!!")
            countdown(1)

    print(Fore.GREEN + Style.BRIGHT + "\nConfigurações concluídas! Vamos começar o jogo!")
    print()
    countdown(1)
    
    return name, bot_name, chips