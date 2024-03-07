def valida_valor_produto():
    while True:
        try:
            preco_original = float(input('Digite o valor do produto: '))
            if preco_original <= 0:
                print('Valor do produto é invalido!\nValor deve ser maior que zero.')
            else:
                return preco_original
        except ValueError:
            print('Digite um numero.')
def valida_valor_desconto():
    while True:
        try:
            desconto = float(input('Digite o percentual de desconto que deseja aplicar: '))
            if 0 >= desconto >= 10:
                print('Valor do desconto é inválido!\nValor deve ser entre 1% e 10%')
            else:
                return desconto
        except ValueError:
            print('Digite um valor de desconto válido!')

def calcula_preco_com_desconto(preco_original, desconto):
    desconto_percentual = desconto / 100
    preco_final = preco_original - (preco_original * desconto_percentual)
    return preco_final

print('Bem vindo ao meu programa que aplica descontos')

preco_original = valida_valor_produto()

desconto = valida_valor_desconto()

preco_prod_final = calcula_preco_com_desconto(preco_original, desconto)

print(f'O preço do produto após a aplicação do desconto é R$:{preco_prod_final:.2f}')