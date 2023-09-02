def lendo_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def somar_acima_da_diagonal(matriz):
    soma = 0
    for i in range(3):
        for j in range(i+1, 3):
            soma += matriz[i][j]
    return soma

print("Digite os elementos da matriz 3x3:")
matriz = lendo_matriz()

meu_resultado = somar_acima_da_diagonal(matriz)

print("A soma dos elementos acima da diagonal principal é:", meu_resultado)