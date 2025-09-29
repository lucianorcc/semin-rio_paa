# ================================================================
# ÁRVORE BINÁRIA DE BUSCA ÓTIMA (Optimal Binary Search Tree - OBST)
# Implementação baseada no livro de Cormen, com comentários
# ================================================================

# Chaves em ordem alfabética:
# Amor < Carro < Xilofone < Zebra
keys = ["Amor", "Carro", "Xilofone", "Zebra"]

# Probabilidades de acesso (sucesso na busca de cada chave)
p = [0.40, 0.30, 0.10, 0.20]
n = len(keys)

# ================================================================
# Passo 1: Inicializar matrizes
# ================================================================
e = [[0.0 for _ in range(n+2)] for _ in range(n+2)]
w = [[0.0 for _ in range(n+2)] for _ in range(n+2)]
root = [[0   for _ in range(n+2)] for _ in range(n+2)]

# ================================================================
# Passo 2: Casos base
# ================================================================

# Este laço percorre todas as chaves da lista "keys".
# No Python, range(1, n+1) gera os números de 1 até n (inclusive).
for i in range(1, n+1):

    # e[i][i] representa o custo esperado de busca de uma árvore que
    # contém apenas a chave "i".
    # Se existe apenas uma chave, ela é a raiz e está no nível 1.
    # O custo nesse caso é simplesmente a probabilidade dessa chave.
    e[i][i] = p[i-1]

    # w[i][i] representa o "peso total" do intervalo [i, i],
    # ou seja, a soma das probabilidades das chaves dentro do intervalo.
    # Como aqui só existe uma chave, o peso é a própria probabilidade.
    w[i][i] = p[i-1]

    # root[i][i] indica qual chave é escolhida como raiz do intervalo [i, i].
    # Se só existe uma chave, a raiz só pode ser ela mesma.
    root[i][i] = i

# ================================================================
# Passo 3: Preencher tabelas
# ================================================================
for l in range(2, n+1):             # l = tamanho do subintervalo
    for i in range(1, n-l+2):       # i = início do intervalo
        j = i + l - 1               # j = fim do intervalo
        e[i][j] = float("inf")      # inicializa com infinito
        w[i][j] = w[i][j-1] + p[j-1]  # soma dos pesos até j

        for k in range(i, j+1):     # testamos cada chave como raiz
            cost = ( (e[i][k-1] if k > i else 0) +
                     (e[k+1][j] if k < j else 0) +
                     w[i][j] )
            if cost < e[i][j]:      # guardamos o menor custo
                e[i][j] = cost
                root[i][j] = k      # registramos quem foi a raiz

# ================================================================
# Passo 4: Reconstrução da árvore com níveis e custo individual
# ================================================================
def build_tree(i, j, nivel=1, parent=None, side=None):
    if i > j:
        return
    r = root[i][j]                  # raiz ótima desse intervalo
    node = keys[r-1]                # nome da chave
    prob = p[r-1]                   # sua probabilidade
    custo_individual = round(prob * nivel, 2)  # custo local = p * profundidade

    if parent is None:
        print(f"Raiz: {node} (nível {nivel}, custo {custo_individual})")
    else:
        print(f"{side} de {parent}: {node} (nível {nivel}, custo {custo_individual})")

    # recursivamente constrói as subárvores esquerda e direita
    build_tree(i, r-1, nivel+1, node, "esquerda")
    build_tree(r+1, j, nivel+1, node, "direita")

# ================================================================
# Passo 5: Exibir resultados
# ================================================================
print("Matriz de custos e[i][j]:")
for row in e[1:n+1]:
    print([round(x,2) if x != float("inf") else "∞" for x in row[1:n+1]])

print("\nMatriz de raízes root[i][j]:")
for row in root[1:n+1]:
    print(row[1:n+1])

print("\nÁrvore ótima:")
build_tree(1, n)

print("\nCusto esperado ótimo =", round(e[1][n], 2))
