salariobruto = float(input("Informe o salario: "))

if salariobruto < 1257.12:
    print("Recebendo esse salario a áliquota vai ser de 0%" , 
          "\nO seu salario bruto vai ser R$ " , salariobruto, 
          "\nO salario Liquido vai ser R$  " , salariobruto, 
          "\nO valor total a pagar vai ser R$ 00.00")
elif salariobruto > 1257.12 and salariobruto < 2510.00:
    aliquota = 0.17
    salarioliquido= salariobruto - 0.17
    imp = salariobruto * aliquota
    print ("Recebendo esse salario a áliquota vai ser  ", aliquota, 
           "\no salario Bruto vai ser de R$ ", salariobruto, 
           "\nO salario liquido vai ser R$ ", salarioliquido, 
           "\nO valor total a pagar vai  R$ ", imp)
else:
    aliquota = 0.28
    salarioliquido= salariobruto - 0.28
    imp = salariobruto * aliquota
    print("Recebendo esse salario a áliquota vai ser  ", aliquota, 
           "\no salario Bruto vai ser de R$", salariobruto, 
           "\nO salario liquido vai ser R$ ", salarioliquido, 
           "\nO valor total a pagar vai ser R$ ", imp)