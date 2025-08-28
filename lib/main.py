# Menu principal para executar listas de exercícios

def executar_lista01():
    import lista01
    print("Executando lista 01...")
    # Chame funções específicas de lista01 aqui

def executar_lista02():
    import lista02
    print("Executando lista 02...")
    # Chame funções específicas de lista02 aqui

def executar_lista03():
    import lista03
    print("Executando lista 03...")
    # Chame funções específicas de lista03 aqui

def executar_lista04():
    import lista04
    print("Executando lista 04...")
    # Chame funções específicas de lista04 aqui

def executar_lista05():
    import lista05
    print("Executando lista 05...")
    # Chame funções específicas de lista05 aqui

if __name__ == "__main__":
    while True:
        print("\nEscolha a lista para executar:")
        print("1 - Lista 01")
        print("2 - Lista 02")
        print("3 - Lista 03")
        print("4 - Lista 04")
        print("5 - Lista 05")
        print("0 - Sair")
        escolha = input("Opção: ")
        if escolha == "1":
            executar_lista01()
        elif escolha == "2":
            executar_lista02()
        elif escolha == "3":
            executar_lista03()
        elif escolha == "4":
            executar_lista04()
        elif escolha == "5":
            executar_lista05()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
