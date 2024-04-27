email = input("Digite seu email: ")

username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Seu nome de usuario é {username} e o dominio é {domain}")
