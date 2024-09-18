def calcular_media(notas):
    if not notas:
        return 0
    soma = sum(notas)
    media = soma / len(notas)
    return media

def main():
    n = int(input("Digite o número de notas: "))
    
    notas = []

    for i in range(n):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    
    print(f"A média aritmética das notas é: {media:.2f}")

if __name__ == "__main__":
    main()