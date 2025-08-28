def mostrar_tipos_dados():
    inteiro = 10
    ponto_flutuante = 10.5
    texto = "Olá, mundo!"

    print(f"Tipo de dado de {inteiro}: {type(inteiro)}")
    print(f"Tipo de dado de {ponto_flutuante}: {type(ponto_flutuante)}")
    print(f"Tipo de dado de {texto}: {type(texto)}")

def mostrar_parte_inteira():
    numero = float(input("Digite um número: "))
    parte_inteira = int(numero)
    print(f"A parte inteira de {numero} é {parte_inteira}.")

def converter_string_para_inteiro():
    texto = input("Digite um número inteiro: ")
    inteiro = int(texto)
    print(f"O número inteiro é: {inteiro}")

def mostrar_tipo_booleano():
    verdadeiro = True
    falso = False
    print(f"Tipo de dado de {verdadeiro}: {type(verdadeiro)}")
    print(f"Tipo de dado de {falso}: {type(falso)}")