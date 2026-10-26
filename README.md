# Calculadora em Python

Atividade de Coding: calculadora com interação pelo terminal, desenvolvida para praticar lógica de programação e versionamento com Git e GitHub.

## Evolução do exercício

O exercício inicial, feito em sala, recebia um número para somar com 10 e outro para subtrair 1. Esta versão permite escolher uma das quatro operações e informar os dois números.

## Funcionalidades

- Soma, subtração, multiplicação e divisão.
- Números inteiros, negativos e decimais.
- Entrada decimal com ponto ou vírgula.
- Menu que permite realizar várias contas e sair com a opção 0.
- Mensagens para opção inválida, entrada não numérica e divisão por zero.
- Rejeição de valores não finitos e de resultados fora do limite numérico.

## Como executar no VS Code

1. Instale Python 3, caso ainda não esteja instalado.
2. Abra esta pasta no VS Code: Arquivo > Abrir Pasta.
3. Abra Terminal > Novo Terminal.
4. Execute `py main.py` no Windows. Se sua instalação usa `python`, execute `python main.py`.
5. Escolha uma operação e digite os dois números, pressionando Enter após cada resposta.

O projeto usa apenas a biblioteca padrão do Python. Não requer instalação de pacotes adicionais.

## Exemplo

```text
Escolha uma opção: 1
Digite o primeiro número: 3
Digite o segundo número: 10
Resultado: 3.0 + 10.0 = 13.0
```

## Algoritmo em pseudocódigo

```text
INÍCIO
    exibir saudação
    REPETIR
        exibir menu e ler opção
        SE opção for sair: encerrar
        SE opção não existir: informar erro e voltar ao menu
        ler dois números, repetindo a leitura se forem inválidos
        SE operação for soma: somar
        SENÃO SE for subtração: subtrair
        SENÃO SE for multiplicação: multiplicar
        SENÃO:
            SE segundo número for zero: informar erro e voltar ao menu
            dividir
        verificar se o resultado está dentro do limite numérico
        exibir resultado ou mensagem de erro
    ATÉ escolher sair
FIM
```

## Entendendo o código

| Recurso | Aplicação |
|---|---|
| `print()` | Mostra o menu e os resultados. |
| `input()` | Recebe o texto digitado no terminal. |
| Variáveis | Associam nomes à opção, aos números e ao resultado. |
| `float()` | Converte texto em número para fazer contas. |
| `if`, `elif`, `else` | Escolhem a operação e verificam condições. |
| `while` | Repete o menu e a leitura de números inválidos. |
| `break` | Encerra o laço do menu. |
| `continue` | Volta ao início do laço. |
| `def` | Define funções para organizar o programa. |
| `return` | Devolve o número lido pela função. |
| `try/except ValueError` | Trata entradas que não podem ser convertidas em número. |
| `isfinite()` | Verifica se um valor é finito. |

`ler_numero()` recebe uma mensagem, pede um número e devolve um valor válido. `main()` controla o menu e os cálculos. A condição `if __name__ == "__main__"` inicia o programa quando o arquivo é executado diretamente.

## Roteiro de conferência

| Operação | Entrada | Resultado esperado |
|---|---|---|
| Soma | 3 e 10 | 13 |
| Subtração | 2 e 1 | 1 |
| Multiplicação | -3 e 4 | -12 |
| Divisão | 10 e 4 | 2.5 |
| Soma decimal | 2,5 e 1.5 | 4 |
| Divisão por zero | 8 e 0 | Mensagem de erro e retorno ao menu |
| Entrada inválida | abc | Nova solicitação de número |
| Opção inválida | 9 | Mensagem e retorno ao menu |
| Sair | 0 | Programa encerrado |

## Limitação

O tipo `float` pode apresentar pequenas aproximações, como em `0.1 + 0.2`. Esta é uma calculadora didática, sem histórico persistente.
