def operacoes_basicas(a, b):

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = None if b == 0 else a / b  # Evita divisão por zero
    
    return (soma, subtracao, multiplicacao, divisao)

def potencia_e_raiz(a, b):

    potencia = a ** b
    raiz = a ** 0.5
    return (potencia, raiz)

def aplicar_desconto(preco, desconto):
    valor_final = preco - (preco * 0.10)
    return valor_final

def resto_divisao(a, b):
    if b == 0:
        return None  # Evita divisão por zero
    return a % b