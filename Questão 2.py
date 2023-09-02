def função_vetor(seu_tamanho):
    vetor = []
    for i in range(seu_tamanho):
        valores = int(input(f"Digite o valor para a posição {i}: "))
        vetor.append(valores)
    return vetor

def calculo_da_diferença(vetor_a, vetor_b):
    vetor_c = []
    for i in range(len(vetor_a)):
        diferenca = vetor_a[i] - vetor_b[i]
        vetor_c.append(diferenca)
    return vetor_c

def mostrar_vetor(vetor):
    print("Vetor:", vetor)

tamanho_vetor = 10

print("\t Preenchendo o vetor A \t")
vetor_a = função_vetor(tamanho_vetor)

print("\t Preenchendo o vetor B \t")
vetor_b = função_vetor(tamanho_vetor)

vetor_c = calculo_da_diferença(vetor_a, vetor_b)

print("\t Vetor C (C = A - B) \t")
mostrar_vetor(vetor_c)
