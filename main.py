import random
import string

nomes = [
    "Lucas", "Marcos", "ana", "beatriz", "carlos", 
    "fernanda", "rafael", "juliana", "pedro", "camila"
]

sobrenomes = [
    "silva", "santos", "oliveirs", "pereira", 
    "costa", "rodrigues", "alves", "lima"
]

def gerar_nome_completo():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    return f"{nome} {sobrenome}"

def gerar_username(nome_completo):
    nome, sobrenome = nome_completo.lower().split()
    numero = random.randint(10, 99)
    return f"{nome}.{sobrenome}{numero}"

def gerar_email(username):
    dominios = ["gmail.com", "outlook.com", "proton.me"]
    dominio = random.choice(dominios)
    return f"{username}@{dominio}"

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits = "!@#$%¨&*"
    senha = ""

    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha

def gerar_identidade():
    nome = gerar_nome_completo
    username = gerar_username(nome)
    email = gerar_email(username)
    senha = gerar_senha()

    print("\n Identidade Fictícia Gerada:")
    print("-------------------------------")
    print(f"Nome: {nome}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Senha: {senha}")
    print("-------------------------------\n")
    print("Identidade gerada com sucesso!")

if __name__ == "__main__":
    gerar_identidade()