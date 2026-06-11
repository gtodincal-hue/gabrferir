
# função

def cadastrar_produtos():
    produtos = []#lista vazia

    n = int(input("Quantos produtos deseja cadastrar? "))#quantos produtos o cliente vai cadastrar

    for i in range(n):
        print(f"\nProduto {i+1}")# f deixa em string e o mais 1 faz o produto começar de 1 ao invés de começar de 0
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))

        produto = {#dicionario do produto
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }

        produtos.append(produto)# adiciona o produto na lista produtos, no final da lista

    return produtos# retorna a lista de produtos cadastrados





def buscar_produto(produtos, nome):# busca o produto na lista de produtos cadastrados
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():# compara o nome do produto com o nome digitado pelo cliente
            return produto
    return None# se o produto não for encontrado, retorna None





def calcular_desconto(total):# calcula o desconto 
    if total >= 1000:
        return total * 0.15
    elif total >= 500 and total < 1000:
        return total * 0.10
    elif total >= 200 and total < 500:
        return total * 0.05
    else:
        return 0





def realizar_venda(produtos):# realiza a venda, calcula o total, desconto e total final
    cliente = input("\nNome do cliente: ")
    
    carrinho = []  # lista de produtos comprados
    total = 0      # acumulador

    while True:
        nome_prod = input("\nProduto (ou 'fim' para encerrar): ")

        if nome_prod.lower() == "fim":# se o cliente digitar "fim", encerra a compra
            break

        produto = buscar_produto(produtos, nome_prod)# busca o produto na lista de produtos cadastrados

        if produto:
            qtd = int(input("Quantidade: "))# quantidade do produto que o cliente deseja comprar

            if qtd <= produto["estoque"]:
                subtotal = qtd * produto["preco"]
                total += subtotal  # acumulador, coloca o subtotal no total

                produto["estoque"] -= qtd

                item = {
                    "nome": produto["nome"],
                    "qtd": qtd,
                    "subtotal": subtotal
                }

                carrinho.append(item)

                print("Produto adicionado!")
            else:
                print("Estoque insuficiente!")# se a quantidade desejada for maior que o estoque disponível, mostra mensagem de estoque insuficiente
        else:
            print("Produto não encontrado!")# se o produto não for encontrado na lista de produtos cadastrados, mostra mensagem de produto não encontrado

        continuar = input("Deseja continuar comprando? (S/N): ")
        if continuar.upper() == "N":
            break

    desconto = calcular_desconto(total)
    total_final = total - desconto

    return cliente, carrinho, total, desconto, total_final



# prorograma

produtos = cadastrar_produtos()

cliente, carrinho, total, desconto, total_final = realizar_venda(produtos)# realiza a venda e retorna o cliente, carrinho, total, desconto e total final

print("\n===== RESUMO DA COMPRA =====")
print("Cliente:", cliente)

print("\nProdutos comprados:")
for item in carrinho:
    print(f"{item['nome']} - Qtd: {item['qtd']} - Subtotal: R${item['subtotal']:.2f}")# exibe o nome do produto, quantidade e subtotal de cada item comprado

print("\nTotal:", total)
print("Desconto:", desconto)
print("Total final:", total_final)