def comparar_numeros(a, b):
    if a > b:
        print(f"{a} é maior que {b}.")
    elif a < b:
        print(f"{a} é menor que {b}.")
    else:
        print(f"{a} é igual a {b}.")

def verificar_tres_iguais(a, b, c):
    if a == b == c:
        print(f"{a}, {b} e {c} são iguais.")
    else:
        print(f"{a}, {b} e {c} não são iguais.")

def operacoes_booleanas(a, b):
    print(f"Negação de {a}: {not a}")
    print(f"Negação de {b}: {not b}")
    print(f"Conjunção de {a} e {b}: {a and b}")
    print(f"Disjunção de {a} e {b}: {a or b}")

def verificar_idade_entre18_e_30(idade):
    if 18 <= idade <= 30:
        print(f"A idade {idade} está entre 18 e 30 anos.")
    else:
        print(f"A idade {idade} não está entre 18 e 30 anos.")