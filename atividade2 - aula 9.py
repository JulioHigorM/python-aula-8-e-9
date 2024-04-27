numero = int(input("Digite um número inteiro de três algarismos: "))

inverso = int(str(numero)[::-1])

soma = numero + inverso
print(f"A soma de {numero} com seu inverso {inverso} é: {soma}")
