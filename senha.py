

lista_de_login = ["oi","ab"]
lista_de_senha = ["123","345"]
nlogin = 999999999999999
nsenha = 888888888888888

def verifica(chave, lista):
    return lista.index(chave)
            
while True:
    login = input("Digite seu login: ")
    if login in lista_de_login:
        break
nlogin = verifica(login, lista_de_login)
senha = input("Digite sua senha: ")
if senha in lista_de_senha:
    nsenha = verifica(senha, lista_de_senha)
else:
    print("Senha incorreta!")
print(nlogin)
print(nsenha)
if nlogin == nsenha:
    print("Senha correta!")
else:
    print("Senha incorreta!")