produto = input("Informe o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

resultado = preco * quantidade
resultado = round(resultado, 2)
print (resultado)

if resultado >= 100:
    print (f"O produto {produto} é muito caro")
elif resultado >= 60 and resultado <= 99:
    print (f"O preço do produto {produto} está normal ")
else:
    print (f"O produto {produto} está muito barato")
