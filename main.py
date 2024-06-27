
numero = int(input("Digite um número inteiro: "))

if isinstance(numero,int):
    if numero < 0:
        print("O número é menor que 0")
    elif numero >= 1 and numero <= 10:
        print("O número é entre 1 a 10")
    else:
        print("O número é maior do que 10")
else:
    exit

