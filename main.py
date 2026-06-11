continuar = True
while continuar is True:
    print("Deseja continuar? (s/n)")
    resposta = input()
    if resposta.lower() == "s":
        print("Continuando...")
    elif resposta.lower() == "n":
        print("Encerrando...")
        continuar = False
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
    print("Mamamamammama")