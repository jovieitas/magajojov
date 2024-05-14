def buscar_nome_por_numero():
    nome_arquivo = input("Por favor, informe o nome do arquivo de exemplo (com extensão): ")
    try:
        numero = int(input("Por favor, informe um número: "))
    except ValueError:
        print("Número inválido. Por favor, informe um número inteiro.")
        return

    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        
        if 1 <= numero <= len(linhas):
            nome = linhas[numero - 1].strip()
            print(f"O nome correspondente ao número {numero} é: {nome}")
        else:
            print(f"Número fora do intervalo. O arquivo contém {len(linhas)} linhas.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o nome do arquivo e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

# Chamando a função
buscar_nome_por_numero()







