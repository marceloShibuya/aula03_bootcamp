nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        #nome = input("Digite seu nome: ")
        nome = "Marcelo"

        if len(nome) == 0:
            raise ValueError("O campo não pode estar vazio")
        elif any(char.isdigit() for char in nome):
            raise ValueError("Nome inválido, não pode ser digito")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

while not salario_valido:
    try:
        #salario = float(input("Digite o seu salário: "))
        salario = 1000.00

        if salario <= 0:
            raise ValueError("O salário não pode ser menor ou igual a zero")
        else:
            print("Salário válido:", salario)
            salario_valido = True
    except ValueError as e:
        print(e)   

while bonus_valido is not True:
    try:
        #bonus = float(input("Digite o seu bônus: "))
        bonus = 2.0

        if bonus <= 0:
            raise ValueError("O bônus não pode ser menor ou igual a zero")
        else:
            print("Bônus válido:", salario)
            bonus_valido = True
    except ValueError as e:
        print(e)             


print(f'O funcionário {nome}, recebe o salário de R$ {salario:.2f} com o bônus de {bonus}')


