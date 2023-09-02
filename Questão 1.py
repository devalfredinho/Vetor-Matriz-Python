def função_vetor(seu_tamanho):
    vetor = []
    for i in range(seu_tamanho):
        valores = int(input(f"Digite o valor para a posição {i}: "))
        vetor.append(valores)
    return vetor

def executar_função():
    tamanho_vetor = 8
    vetor = função_vetor(tamanho_vetor)

    x = int(input("Digite a posição X (entre 0 e 7): "))
    while not 0 <= x < tamanho_vetor:
        print("Posição X inválida. Digite um valor entre 0 e 7.")
        x = int(input("Digite a posição X (entre 0 e 7): "))

    y = int(input("Digite a posição Y (entre 0 e 7): "))
    while not 0 <= y < tamanho_vetor:
        print("Posição Y inválida. Digite um valor entre 0 e 7.")
        y = int(input("Digite a posição Y (entre 0 e 7): "))

    somar = vetor[x] + vetor[y]

    print(f"A soma dos valores nas posições {x} e {y} é: {somar}")

executar_função()
