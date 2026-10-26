"""Calculadora de terminal para praticar os fundamentos de Python."""

from math import isfinite


def ler_numero(mensagem):
    while True:
        try:
            # Aceita tanto 2.5 quanto 2,5 na entrada.
            numero = float(input(mensagem).strip().replace(",", "."))
            if isfinite(numero):
                return numero
            print("Digite um número finito.")
        except ValueError:
            print("Entrada inválida. Digite um número, como 10 ou 2,5.")


def main():
    print("Olá! Hoje iremos aprender a calcular.")

    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Calculadora encerrada. Até logo!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Escolha 0, 1, 2, 3 ou 4.")
            continue

        primeiro = ler_numero("Digite o primeiro número: ")
        segundo = ler_numero("Digite o segundo número: ")

        if opcao == "1":
            resultado = primeiro + segundo
            simbolo = "+"
        elif opcao == "2":
            resultado = primeiro - segundo
            simbolo = "-"
        elif opcao == "3":
            resultado = primeiro * segundo
            simbolo = "*"
        else:
            if segundo == 0:
                print("Não é possível dividir por zero.")
                continue
            resultado = primeiro / segundo
            simbolo = "/"

        if not isfinite(resultado):
            print("Resultado fora do limite numérico. Tente valores menores.")
            continue

        print(f"Resultado: {primeiro} {simbolo} {segundo} = {resultado}")


if __name__ == "__main__":
    main()
