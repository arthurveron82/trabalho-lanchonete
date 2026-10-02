def exibir_cardapio():
    """Exibe o cardápio com os produtos disponíveis."""
    print("\n" + "=" * 35)
    print("         CARDÁPIO DA LANCHONETE      ")
    print("=" * 35)
    print("Código | Produto         | Preço")
    print("-" * 35)
    print("  1    | Hambúrguer      | R$ 15.00")
    print("  2    | Cheeseburger    | R$ 18.00")
    print("  3    | Batata Frita    | R$ 10.00")
    print("  4    | Refrigerante    | R$  6.00")
    print("  5    | Suco Natural    | R$  8.00")
    print("=" * 35)


def obter_preco_produto(codigo):
    """Retorna o preço do produto com base no código informado.
    Retorna -1.0 se o código for inválido.
    """
    match codigo:
        case "1":
            return 15.00
        case "2":
            return 18.00
        case "3":
            return 10.00
        case "4":
            return 6.00
        case "5":
            return 8.00
        case _:
            return -1.0


def obter_nome_produto(codigo):
    """Retorna o nome do produto correspondente ao código."""
    match codigo:
        case "1":
            return "Hambúrguer"
        case "2":
            return "Cheeseburger"
        case "3":
            return "Batata Frita"
        case "4":
            return "Refrigerante"
        case "5":
            return "Suco Natural"
        case _:
            return "Desconhecido"


def calcular_desconto(total_original):
    """Calcula a taxa e o valor do desconto com base no valor total da compra."""
    if total_original >= 100.0:
        percentual = 10
        valor_desconto = total_original * 0.10
    elif total_original >= 50.0:
        percentual = 5
        valor_desconto = total_original * 0.05
    else:
        percentual = 0
        valor_desconto = 0.0

    return percentual, valor_desconto


def obter_forma_pagamento():
    """Solicita e valida a forma de pagamento selecionada pelo cliente."""
    opcao_valida = False
    forma = ""

    while not opcao_valida:
        print("\nFormas de Pagamento:")
        print("1. Dinheiro")
        print("2. PIX")
        print("3. Cartão")
        opcao = input("Escolha a forma de pagamento (1-3): ")

        match opcao:
            case "1":
                forma = "Dinheiro"
                opcao_valida = True
            case "2":
                forma = "PIX"
                opcao_valida = True
            case "3":
                forma = "Cartão"
                opcao_valida = True
            case _:
                print("[ERRO] Opção de pagamento inválida! Tente novamente.")

    return forma


def exibir_resumo(nome_cliente, total_original, percentual, valor_desconto, valor_final, forma_pagamento):
    """Apresenta o resumo final do pedido de forma organizada."""
    print("\n" + "=" * 40)
    print("           RESUMO DO PEDIDO             ")
    print("=" * 40)
    print(f"Cliente:            {nome_cliente}")
    print(f"Valor Original:     R$ {total_original:.2f}")
    print(f"Desconto Aplicado:  {percentual}%")
    print(f"Valor do Desconto:  R$ {valor_desconto:.2f}")
    print(f"Valor Final:        R$ {valor_final:.2f}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print("=" * 40)
    print("Obrigado pela preferência! Volte sempre.")


def main():
    print("========================================")
    print("  BEM-VINDO AO SISTEMA DE ATENDIMENTO   ")
    print("========================================")

    nome_cliente = input("Digite o nome do cliente: ")

    total_compra = 0.0
    continuar = "s"

    while continuar == "s" or continuar == "sim":
        exibir_cardapio()
        codigo = input("Digite o código do produto desejado: ")
        preco = obter_preco_produto(codigo)

        if preco == -1.0:
            print("[ERRO] Código de produto inválido! Nenhum produto foi adicionado.")
        else:
            nome_prod = obter_nome_produto(codigo)
            qtd_str = input(f"Digite a quantidade de '{nome_prod}': ")

            if qtd_str.isdigit() and int(qtd_str) > 0:
                quantidade = int(qtd_str)
                subtotal = preco * quantidade
                total_compra = total_compra + subtotal
                print(f"[SUCESSO] Adicionado: {quantidade}x {nome_prod} = R$ {subtotal:.2f}")
                print(f"Total acumulado até agora: R$ {total_compra:.2f}")
            else:
                print("[ERRO] Quantidade inválida! Deve ser um número inteiro positivo.")

        continuar = input("\nDeseja adicionar outro produto? (s/n): ").lower()

    if total_compra == 0:
        print("\nNenhum item foi adicionado ao pedido. Atendimento encerrado.")
    else:
        percentual, valor_desconto = calcular_desconto(total_compra)
        valor_final = total_compra - valor_desconto
        forma_pagamento = obter_forma_pagamento()

        exibir_resumo(
            nome_cliente,
            total_compra,
            percentual,
            valor_desconto,
            valor_final,
            forma_pagamento
        )


if __name__ == "__main__":
    main()