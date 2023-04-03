idade = int(input("Informe a idade do nadador: "))

if idade >=5 and idade <=7:
    print("Pessoas com essa idade é considerado da categoria Infantial A")
elif idade >= 8 and idade<=10:
    print("Pessoas com essa idade é considerado da categoria Infantial B  ")
elif idade >=11 and idade <=13:
    print("Pessoas com essa idade é considerado da categoria Juvenil A")
elif idade >=14 and idade<=17:
    print("Pessoas com essa idade é considerado da categoria Juveniu B")
elif idade >= 18:
    print("Pessoas com essa idade é considerado da categoria Sênior")
else:
    print("Pessoas com essa idade é considerado da categoria Sênior")
