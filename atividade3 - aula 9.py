string = input("Digite uma string: ")

string = string.upper()

contagem = {}
for caracter in string:
    if caracter in contagem:
        contagem[caracter] += 1
    else:
        contagem[caracter] = 1

for caracter, quantidade in contagem.items():
    print(f"O caracter  '{caracter}' aparece {quantidade} vezes na string")
