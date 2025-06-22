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
print("==========BEM VINDO A LANCHONETE DO ZÉ==========")
# time.sleep(2)
pedido = []
total = []
while True:
  for id,produto in cardapio.items():
    print(f"[{id}] {produto['nome']} R${produto['preco']:.2f}")
  print("[0] Finalizar pedido")
  opçao = int(input("Digite o ID do produto: "))
  if opçao in cardapio:
    pedido.append(cardapio[opçao]['nome'])
    total.append(cardapio[opçao]['preco'])
  if opçao == 0:
    break
print("\nPedido finalizado (projeto em andamento):")
print(pedido)
print(f"Total: R$ {sum(total):.2f}")

 
