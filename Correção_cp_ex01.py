nome = input("Informe seu nome: ")
salario = float(input("Informe o Valor do seu salario R$:"))
venda = int(input("Informe o tatal de vendas efetuada no mês: "))

comissao = venda * 0.15
vtotal = salario + comissao

print("O valor que esse vendedor ira receber no final do vai ser  de R$", vtotal )