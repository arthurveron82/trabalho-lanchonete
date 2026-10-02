# Sistema de Atendimento e Pedidos de Lanchonete

**Estudantes:** Arthur Veron e Enzo Formigone
**Disciplina:** Algoritmos e Programação
**Linguagem:** Python

## Descrição do Projeto
Este projeto consiste em um sistema simples de atendimento e realização de pedidos para uma lanchonete, desenvolvido em Python. O objetivo principal é demonstrar o domínio de conceitos fundamentais da programação estruturada sem o uso de estruturas de dados avançadas (como listas ou dicionários).

## Funcionalidades Principais
- **Identificação do Cliente:** Registro do nome do cliente no início do atendimento.
- **Apresentação do Cardápio:** Exibição interativa de 5 produtos com seus respectivos códigos e preços.
- **Acumulação de Pedidos:** Possibilidade de selecionar múltiplos itens e quantidades em uma mesma sessão.
- **Validação de Entradas:** Tratamento de códigos de produtos inválidos e quantidades incorretas.
- **Cálculo Automático de Descontos:**
  - Compras inferiores a R$ 50,00: sem desconto (0%).
  - Compras de R$ 50,00 a R$ 99,99: 5% de desconto.
  - Compras iguais ou superiores a R$ 100,00: 10% de desconto.
- **Escolha da Forma de Pagamento:** Suporte para Dinheiro, PIX ou Cartão com validação.
- **Resumo Final:** Impressão detalhada do pedido com valor original, desconto, valor final e forma de pagamento.

## Como Executar o Programa
1. Certifique-se de ter o **Python 3** instalado no computador.
2. Abra o terminal no diretório do projeto.
3. Execute o comando:
   ```bash
   python main.py
   ```