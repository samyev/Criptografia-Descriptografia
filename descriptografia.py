# Descriptografando

from criptografia import Criptografia

def Descriptografia():
  numero = input("Insira o número criptografado de 4 digittos: ")
  
  while (int(numero) < 1000 or int(numero) > 10000):
    num = input("Entrada inválida! Informe o número criptografado de 4 digitos: ")


 # Descriptrografando
  def calc(x):
    if (x < 6):
      return x + 4
    else:
      return x - 6

  primeiro = calc (int(numero[0]))
  segundo = calc (int(numero[1]))
  terceiro = calc (int(numero[2]))
  quarto = calc (int(numero[3]))
  
  # Invertendo os números
  aux = primeiro
  primeiro = terceiro
  terceiro = aux
  aux = segundo
  segundo = quarto
  quarto = aux

  # imprimindo os numeros descriptografados
  print("A descriptografia do número informado é: ", int(primeiro), int(segundo), int(terceiro), int(quarto))

Descriptografia()