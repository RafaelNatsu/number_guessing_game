# Number Guessing Game

## Descrição

O **Number Guessing Game** é um jogo interativo baseado em terminal onde o jogador tenta adivinhar um número secreto gerado aleatoriamente. Você pode escolher entre diferentes níveis de dificuldade, cada um com uma quantidade limitada de tentativas. O jogo oferece feedback após cada tentativa e salva a pontuação ao final.

---

## Funcionalidades

- Escolha entre **três níveis de dificuldade**:
  - **Fácil**: 10 tentativas
  - **Médio**: 5 tentativas
  - **Difícil**: 1 tentativa
- Feedback interativo para cada tentativa, informando se o número secreto é maior ou menor.
- Salvamento automático da pontuação em um arquivo JSON (`game_scores.txt`).
- Estrutura modular com foco em organização e boas práticas de programação.

---

## Estrutura do Projeto

```plaintext
number_guessing_game/
│
├── src/                        # Código principal do jogo
│   ├── __init__.py
│   ├── main.py                 # Entrada principal do programa
│   ├── game_ui.py              # Interação com o usuário
│   ├── game_config.py          # Configurações e níveis de dificuldade
│   ├── game_storage.py         # Salva pontuação
│   ├── game_manager.py         # Lógica principal do jogo
│
├── test/                       # Testes unitários e de integração
│   ├── __init__.py
│   ├── test_game_config.py
│   ├── test_game_manager.py
│   ├── test_game_ui.py
│   ├── test_game_storage.py
│
├── game.txt                    # Arquivo onde as pontuações são salvas
├── README.md                   # Documentação do projeto
```

---

## Como Jogar

1. Clone este repositório:
   ```bash
   git clone https://github.com/RafaelNatsu/number_guessing_game.git
   cd number_guessing_game
   ```

2. Inicie o jogo:
   ```bash
   python game.py
   ```

---
## Exemplos de Uso

### Escolhendo o nível de dificuldade
- O jogo solicitará que você escolha entre os níveis Fácil, Médio e Difícil. 
  ```plaintext
  Please select the difficulty level:
  1. Easy (10 chances)
  2. Medium (5 chances)
  3. Hard (1 chance)
  ```

### Fazendo um palpite
- Após cada tentativa, você receberá um feedback:
  ```plaintext
  Enter your guess: 50
  Incorrect! The number is greater than 50.
  Attempts remaining: 4
  ```

---

## Tecnologias Utilizadas

- **Python 3.10+**
- Estrutura modular e boas práticas de programação orientada a objetos.

## Autor

- **[RafaelNatsu](https://github.com/RafaelNatsu)**

---

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT) - sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo.

---