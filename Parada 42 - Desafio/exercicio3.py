cod = input("Digite o código do produto: ")
nome = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))

total = qtd * preco

print("------------------------")
print(f"CÓDIGO: {cod}")
print(f"NOME: {nome}")
print(f"QUANTIDADE: {qtd}")
print(f"PREÇO UNITÁRIO: {preco}")
print("------------------------")
print(f"O total da compra foi de: R${total}")