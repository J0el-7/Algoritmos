def informacoes_pessoais():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura em metros: "))

    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura} metros")

def dobrar_valor(valor):
    return valor * 2

def variaveis_dependentes():
    a = 10
    b = a + 5

    print(f"Valor de a: {a}")
    print(f"Valor de b (a + 5): {b}")
