# bst_words_interactive_commented.py
# Exemplo didático: Árvore Binária de Busca (BST) com pausas interativas
# Conjunto de palavras: Bola, Amor, Casa, Carro, Fruta, Gato
# ------------------------------------------------------------
# Este código mostra como a BST é construída, como funciona a
# inserção, a busca e as travessias, e ainda conta o custo
# (número de comparações ou visitas) de cada operação.
# ------------------------------------------------------------

from typing import Optional, Tuple

# ============================================================
# Classe Node
# Representa cada nó da árvore.
# Exemplo: Node("Bola") cria um nó com a chave "Bola".
# ============================================================
class Node:
    def __init__(self, key: str):
        self.key: str = key
        self.left: Optional['Node'] = None   # filho à esquerda (chaves menores)
        self.right: Optional['Node'] = None  # filho à direita (chaves maiores)

    def __repr__(self):
        return f"Node({self.key!r})"


# ============================================================
# Função insert
# Insere uma nova palavra na BST.
# Retorna a raiz da árvore e o custo (nº de comparações).
# Exemplo: inserir "Amor" depois de "Bola" → 2 comparações.
# ============================================================
def insert(root: Optional[Node], key: str) -> Tuple[Node, int]:
    cost = 0
    if root is None:
        return Node(key), 1  # custo 1 (checou raiz vazia)

    cur = root
    while True:
        cost += 1
        if key < cur.key:
            # Palavra é menor → segue para a esquerda
            if cur.left is None:
                cur.left = Node(key)
                cost += 1  # comparação final ao inserir
                break
            else:
                cur = cur.left
        elif key > cur.key:
            # Palavra é maior → segue para a direita
            if cur.right is None:
                cur.right = Node(key)
                cost += 1
                break
            else:
                cur = cur.right
        else:
            # Palavra já existe → não insere duplicatas
            break
    return root, cost


# ============================================================
# Função search
# Busca uma palavra na BST.
# Retorna (nó encontrado ou None, custo em comparações).
# Exemplo: buscar "Fruta" percorre Bola → Casa → Fruta (3 passos).
# ============================================================
def search(root: Optional[Node], key: str) -> Tuple[Optional[Node], int]:
    cur = root
    cost = 0
    while cur is not None:
        cost += 1
        if key == cur.key:
            return cur, cost
        elif key < cur.key:
            cur = cur.left
        else:
            cur = cur.right
    return None, cost


# ============================================================
# Travessia inorder
# Visita nós na ordem crescente (alfabética).
# Exemplo: ['Amor', 'Bola', 'Carro', 'Casa', 'Fruta', 'Gato'].
# Custo = nº de visitas.
# ============================================================
def inorder(root: Optional[Node], visit, cost=0) -> int:
    if root:
        cost = inorder(root.left, visit, cost)
        visit(root)
        cost += 1
        cost = inorder(root.right, visit, cost)
    return cost


# ============================================================
# Travessia preorder
# Visita raiz antes dos filhos.
# Útil para salvar/serializar a árvore.
# ============================================================
def preorder(root: Optional[Node], visit, cost=0) -> int:
    if root:
        visit(root)
        cost += 1
        cost = preorder(root.left, visit, cost)
        cost = preorder(root.right, visit, cost)
    return cost


# ============================================================
# Travessia postorder
# Visita filhos antes da raiz.
# Útil para remover todos os nós da árvore.
# ============================================================
def postorder(root: Optional[Node], visit, cost=0) -> int:
    if root:
        cost = postorder(root.left, visit, cost)
        cost = postorder(root.right, visit, cost)
        visit(root)
        cost += 1
    return cost


# ============================================================
# Função pretty_print
# Imprime a árvore em formato hierárquico.
# Exemplo esperado com as palavras:
# `- Bola
#    |- Amor
#    `- Casa
#       |- Carro
#       `- Fruta
#          `- Gato
# ============================================================
def pretty_print(root: Optional[Node], indent: str = "", last: bool = True):
    if root is None:
        return
    print(indent, "`- " if last else "|- ", root.key, sep="")
    indent += "   " if last else "|  "
    if root.left or root.right:
        if root.left:
            pretty_print(root.left, indent, False if root.right else True)
        else:
            print(indent + "|- " + "∅")  # ∅ = vazio
        if root.right:
            pretty_print(root.right, indent, True)


# ============================================================
# Programa principal (main)
# Constrói a árvore com as palavras dadas,
# mostra as inserções passo a passo,
# depois imprime travessias e buscas.
# ============================================================
if __name__ == "__main__":
    words_insert_order = ["Bola", "Amor", "Casa", "Carro", "Fruta", "Gato"]

    root = None
    print("Inserções na ordem:", words_insert_order)
    input("Pressione Enter para começar as inserções...")

    # Inserção interativa
    for w in words_insert_order:
        root, cost = insert(root, w)
        print(f"Inserido {w} com custo {cost}")
        pretty_print(root)
        input("Pressione Enter para continuar...")

    print("\nEstrutura final da árvore BST:")
    pretty_print(root)
    input("\nPressione Enter para iniciar as travessias...")

    # Travessias com custo
    inorder_list = []
    cost_in = inorder(root, lambda n: inorder_list.append(n.key))
    print("In-order (ordenado):", inorder_list, f"(custo {cost_in})")
    input("Pressione Enter...")

    pre_list = []
    cost_pre = preorder(root, lambda n: pre_list.append(n.key))
    print("Pre-order:", pre_list, f"(custo {cost_pre})")
    input("Pressione Enter...")

    post_list = []
    cost_post = postorder(root, lambda n: post_list.append(n.key))
    print("Post-order:", post_list, f"(custo {cost_post})")
    input("Pressione Enter...")

    # Buscas interativas
    print("\nBuscas de exemplo:")
    for q in ["Fruta", "Xingar", "Amor", "Gato"]:
        node, cost = search(root, q)
        if node:
            print(f"Busca por '{q}': encontrada (custo {cost})")
        else:
            print(f"Busca por '{q}': não encontrada (custo {cost})")
        input("Pressione Enter para próxima busca...")
   