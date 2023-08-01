print("Olá, estou aqui para te ajudar a fazer um câmbio do seu dinheiro, para dolar, vamos começar?!")
nome = str(input("Qual é o seu nome: "))
carteira = float(input("Insira o valor desejado para o câmbio: R$"))
câmbio = carteira / 4.78
print("Então {} fez um câmbio de R${}, esse valor convertido em dolar da um total de US${}".format(nome, carteira, câmbio))