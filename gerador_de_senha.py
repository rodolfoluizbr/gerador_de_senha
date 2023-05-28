import random

# Definição dos conjuntos de caracteres possíveis para compor a senha
n = "1234567890"  # Números de 0 a 9
mi = "abcdefghijklmnopqrstuvwxyz"  # Letras minúsculas
ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letras maiúsculas
e = "%$#-_&"  # Caracteres especiais
all = n * 8 + mi * 8 + ma * 8 + e * 8  # Concatenação de todos os conjuntos em um único conjunto, multiplicados por 8 para gerar senhas maiores.

# Solicita ao usuário as propriedades desejadas para a senha
seleciona = input("Selecione as propriedades (n, ma, mi, e, all): ").split()

prefixo = input("Dê um prefixo: ")  # Solicita ao usuário um prefixo opcional para a senha
sufixo = input("Dê um sufixo: ")  # Solicita ao usuário um sufixo opcional para a senha
tamanho = int(input("Escolha o tamanho da senha: "))  # Solicita ao usuário o tamanho desejado para a senha

selecionadas = []
for opcao in seleciona:
    if opcao == "all":
        selecionadas.append(all)
    elif opcao == "ma":
        selecionadas.append(ma)
    elif opcao == "mi":
        selecionadas.append(mi)
    elif opcao == "n":
        selecionadas.append(n)
    elif opcao == "e":
        selecionadas.append(e)
    else:
        print(f"Opção inválida: {opcao}. Opção ignorada.")

seleciona = "".join(selecionadas)

# Geração da senha aleatória
senha = prefixo + "".join(random.sample(seleciona, tamanho)) + sufixo

print(senha)
