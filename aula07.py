nome = input ("Informe o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
media = round(media, 2)

if media >= 7:
    print(f"O aluno {nome} foi reprovado com a média das notas {media}")
else:
    print(f"O aluno {nome} foi aprovado com a média das notas {media} ")