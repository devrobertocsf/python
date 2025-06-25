# Projeto ainda em desenvolvimento.
# Funcionalidades básicas implementadas.
# Planejo adicionar tratamento de erros, funções e melhorias.

import time

cardapio = {
    1: { "nome": "X-Burguer", "preco": 10.00},
    2: {"nome": "X-Salada", "preco": 11.50},
    3: {"nome": "X-Tudo", "preco": 13.00},
    4: {"nome": "Batata Média", "preco": 6.00},
    5: {"nome": "Suco De Laranja", "preco": 10.00},
    6: {"nome": "Refrigerante", "preco": 4.50},
    7: {"nome": "Água", "preco": 3.00}
}

print("========== BEM VINDO À LANCHONETE DO ZÉ ==========")

pedido = []
total = []

while True:
    for id, produto in cardapio.items():
        print(f"[{id}] {produto['nome']} R${produto['preco']:.2f}")
    print("[0] Finalizar pedido")
    print("[999] Remover último item")

    opcao = int(input("Digite o ID do produto: "))
    
    if opcao in cardapio:
        pedido.append(cardapio[opcao]['nome'])
        total.append(cardapio[opcao]['preco'])

    elif opcao == 999:
        if pedido and total:
            item_removido = pedido.pop()
            preco_removido = total.pop()
            print(f"Removido: {item_removido} (R${preco_removido:.2f})")
        else:
            print("Nenhum item para remover.")

    elif opcao == 0:
        break

    else:
        print("Opção inválida.")

print("\nPedido finalizado:")
print(pedido)
print(f"Total: R$ {sum(total):.2f}")
