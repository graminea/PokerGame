from countdown import countdown
from colorama import init, Fore, Style

init(autoreset=True)

def configuration():
    print(Fore.GREEN + '-------------------------------------------------------------------------------------------------------------------------------------------')
    print(Fore.YELLOW + Style.BRIGHT + "\nPokerGame\n")
    print(Fore.CYAN + Style.BRIGHT + "Configurations")
    print()
    countdown(1)

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

    print(Fore.GREEN + "\nConfigurações concluídas! Vamos começar o jogo!")
    print()
    countdown(1)
    
    return name, bot_name, chips