
PokerGame
=========

Este projeto é uma implementação simples de um jogo de poker em Python, desenvolvido para fins educacionais e de prática em programação orientada a objetos.

Visão Geral
-----------
O PokerGame simula uma partida básica de poker, permitindo que múltiplos jogadores participem, com funcionalidades como distribuição de cartas, apostas e determinação do vencedor com base nas mãos.

Estrutura do Projeto
--------------------
O projeto é composto pelos seguintes arquivos principais:

- card.py: Define a classe `Card`, representando uma carta individual com naipe e valor.
- deck.py: Contém a classe `Deck`, responsável por criar e embaralhar o baralho.
- player.py: Implementa a classe `Player`, que gerencia as informações e ações de cada jogador.
- game.py: Controla a lógica principal do jogo, incluindo o fluxo das rodadas e regras.
- main.py: Ponto de entrada do programa, onde o jogo é iniciado.
- configuration.py: Armazena configurações e constantes utilizadas no jogo.
- countdown.py: Possivelmente gerencia contadores regressivos para ações temporizadas.
- UMLClassDiagram.png: Diagrama UML ilustrando a estrutura e relacionamentos entre as classes.

Como Executar
-------------
1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Clone este repositório:

   git clone https://github.com/graminea/PokerGame.git

3. Navegue até o diretório do projeto:

   cd PokerGame

4. Execute o jogo:

   python main.py

Notas
-----
- Este projeto é uma versão inicial e pode ser expandido com funcionalidades adicionais, como interface gráfica, suporte a diferentes variantes de poker e melhorias na lógica de apostas.
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
