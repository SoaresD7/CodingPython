idade = int(input("Digite sua idade: "))
resp = input ("Possui CNH? SIM OU NÃO: ")

resp = resp.lower()
check = True if resp == "sim" else False
print (check)

if idade >= 18:
    if check:
        print ("Você pode dar um rolê de bibi, marcha no progresso")
    else:
        print ("Você não pode dar um rolê de bibi, night night")
else:
    print ("Você não tem idade vagabundo, vai estudar no SENAI")