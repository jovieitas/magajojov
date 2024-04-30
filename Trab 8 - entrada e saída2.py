def imprimir_informacoes(nome, idade, cidade, sep=' - ', end='\n'):
    print(f"Nome: {nome}{sep}Idade: {idade}{sep}Cidade: {cidade}!", end=end)
imprimir_informacoes("Joana", 21, "Niterói")
def calcular_operacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return
    
    print(f"O resultado de {num1} {operacao} {num2} é {resultado}.")

# Chamar a função para calcular uma operação
calcular_operacao()
def listar_itens_compras():
    itens = input("Digite os itens da lista de compras, separados por vírgula: ").split(',')
    for i, item in enumerate(itens, start=1):
        print(f"Item {i}: {item.strip()}")

# Chamar a função para listar os itens de compras
listar_itens_compras()
def converter_celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

# Chamar a função para converter a temperatura de Celsius para Fahrenheit
converter_celsius_para_fahrenheit()
def solicitar_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome ou 'sair' para sair: ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)
    
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Chamar a função para solicitar nomes e imprimir
solicitar_nomes()



    
