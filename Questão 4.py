def lendo_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz_a, matriz_b):
    resultado = []
    for i in range(3):
        linha = []
        for j in range(3):
            soma = matriz_a[i][j] + matriz_b[i][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado

def subtrair_matrizes(matriz_a, matriz_b):
    resultado = []
    for i in range(3):
        linha = []
        for j in range(3):
            subtracao = matriz_a[i][j] - matriz_b[i][j]
            linha.append(subtracao)
        resultado.append(linha)
    return resultado

def multiplicar_matrizes(matriz_a, matriz_b):
    resultado = []
    for i in range(3):
        linha = []
        for j in range(3):
            produto = sum(matriz_a[i][k] * matriz_b[k][j] for k in range(3))
            linha.append(produto)
        resultado.append(linha)
    return resultado

def exibir_matriz(matriz, titulo):
    print(f"\n{titulo}:")
    for linha in matriz:
        print(linha)

while True:
    print("------------------------------------------------------------------------")
    print("\t Calculadora de Matrizes \t")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        matriz_a = lendo_matriz()
        matriz_b = lendo_matriz()
        resultado = somar_matrizes(matriz_a, matriz_b)
        exibir_matriz(resultado, "SOMA")

    elif opcao == 2:
        matriz_a = lendo_matriz()
        matriz_b = lendo_matriz()
        resultado = subtrair_matrizes(matriz_a, matriz_b)
        exibir_matriz(resultado, "SUBTRAÇÃO")

    elif opcao == 3:
        matriz_a = lendo_matriz()
        matriz_b = lendo_matriz()
        resultado = multiplicar_matrizes(matriz_a, matriz_b)
        exibir_matriz(resultado, "MULTIPLICAÇÃO")

    elif opcao == 4:
        print("Saindo da Calculadora de Matrizes...")
        break

    else:
        print("Opção inválida! Digite uma opção válida (1, 2, 3 ou 4).")