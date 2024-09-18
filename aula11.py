n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
opcao = int(input("Qual operação você quer fazer: 1.Soma 2.Subtrair 3.Multiplicação 4.Divisão"))
if opcao == 1:
    soma = n1 + n2
    print (f"A soma dos números é: {soma}")
elif opcao == 2:
    sub = n1 - n2
    print (f"A subtração dos números é: {sub}")
elif opcao == 3:
    mult = n1 * n2
    print (f"A multiplicação dos números é: {mult}")
elif opcao == 4:
    div = n1 / n2
    print (f"A divisão dos números é: {div}")
else:
    print ("Opcão inválida")