nome_valido = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        if len(nome) == 0:
            raise ValueError("O campo não pode estar vazio")
        elif any(char.isdigit() for char in nome):
            raise ValueError("Nome inválido, não pode ser digito")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)
