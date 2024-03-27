def calcular_soma_e_media(numeros):
    """
    Calcular a soma e a média de uma lista de números.

    Args:
    - numeros (list): Lista de números.

    Returns:
    - tuple: Uma tupla contendo a soma e a média dos números.
    """
    soma_total = sum(numeros)
    media = soma_total / len(numeros)
    return soma_total, media

def substituir_ocorrencias_palavra(lista_palavras, palavra_antiga, palavra_nova):
    """
    Substituir ocorrências de uma palavra por outra em uma lista de palavras.

    Args:
    - lista_palavras (list): Lista de palavras.
    - palavra_antiga (str): Palavra a ser substituída.
    - palavra_nova (str): Nova palavra para substituir a palavra antiga.

    Returns:
    - list: A lista modificada com as palavras substituídas.
    """
    lista_modificada = [palavra.replace(palavra_antiga, palavra_nova) for palavra in lista_palavras]
    return lista_modificada

def gerar_triangulo_asteriscos(num_linhas):
    """
    Gerar um triângulo de asteriscos para o número de linhas informado.

    Args:
    - num_linhas (int): Número de linhas para o triângulo.

    Output:
    - None (imprime o triângulo)
    """
    for i in range(1, num_linhas + 1):
        print("*" * i)

# Exemplo de uso:
numeros = [1, 2, 3, 4]
lista_palavras = ["banana", "morango", "limão"]
num_linhas = 4

soma_resultado, media_resultado = calcular_soma_e_media(numeros)
print("Soma:", soma_resultado)
print("Média:", media_resultado)

lista_modificada = substituir_ocorrencias_palavra(lista_palavras, "banana", "maçã")
print("Lista Modificada:", lista_modificada)

gerar_triangulo_asteriscos(num_linhas)


