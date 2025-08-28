def saudacao_usuario():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Bem-vindo(a) ao nosso sistema.")


def soma_dois_usuario():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é: {soma}")


def mostrar_preco_produto():
    string = input("Digite o nome do produto: ")
    float = float(input("Digite o preço do produto: "))

    print(f"O produto {string} custa R$ {float:.2f}")

def converter_metros_para_centimetros():
    metros = float(input("Digite o valor em metros: "))
    centimetros = metros * 100
    print(f"{metros} metros equivalem a {centimetros} centímetros.")

def mostrar_altura_peso():
    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em kg: "))
    print(f"Sua altura é {altura} metros e seu peso é {peso} kg.")