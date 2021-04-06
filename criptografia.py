# Criptografia

def Criptografia():
    numero = input('Digite o número a ser criptografado: ')

    while (int(numero) < 1000 or int(numero) > 10000):
        numero = input("Entrada inválida! Informe o número criptografado de 4 digitos: ")

    primeiro = (int(numero[0])+6)%10
    segundo = (int(numero[1])+6)%10
    terceiro = (int(numero[2])+6)%10
    quarto = (int(numero[3])+6)%10

    aux = primeiro
    primeiro = terceiro
    terceiro = aux
    aux = segundo
    segundo = quarto
    quarto = aux

    print("O número criptografado é: ",primeiro ,segundo ,terceiro ,quarto)

Criptografia()