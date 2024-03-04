# lê o código do produto, a quantidade e o preço de cada
# separa cada uma das informações
prod1 = input().split()
prod2 = input().split()

# calcula o subtotal e o total do carrinho

tot_prod1 = int(prod1[1]) * float(prod1[2])
tot_prod2 = int(prod2[1]) * float(prod2[2])
valor_total = tot_prod1 + tot_prod2

# printa o total a ser pago
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
