produto = float(input('Digite o valor do produto: '))
quantidade = float(input('Informe a quantidade: '))

valor = produto * quantidade

desconto10 = valor * 0.1
desconto20 = valor * 0.2
desconto30 = valor * 0.3
desconto40 = valor * 0.4

if valor < 100:
    print('O total a ser pago é ' , (valor))
elif valor > 100 and valor < 199:
    print('O valor a ser pago é ' ,(valor - desconto10))
elif valor >200 and valor < 299:
    print('O valor a ser pago é ' , (valor - desconto20))
elif valor > 300 and valor < 400:
    print('O valor a ser pago é ' , (valor - desconto30))
else:
    print('O valor a ser pago é ' , (valor - desconto40))