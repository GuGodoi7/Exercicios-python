num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
num3 = float(input('Digite mais um numero: '))

if num1 > num2 > num3:
    print( num1,num2,num3)
elif num2 > num1 > num3:
    print(num1,num2,num3)
elif num3 > num1 > num2:
    print(num3,num1,num2)
elif num1 > num3 > num2:
    print(num1,num3,num2)
elif num2 > num3 > num1:
    print(num2,num3,num1)
else:
    print(num3,num2,num1)
    