num1 = int(input("informe 1 numero: "))
num2 = int(input("informe 1 numero: "))
soma = num1 + num2
multi = num1 * num2
maior = 0
menu = int(input('''Oque deseja fazer com essses números
Digite (1) para somar
digite (2) para multiplicar
digite (3) para saber o maior 
digite (4) para digitar novos números
digite (5) para finalizar'''))

while menu != 5:
    match menu:
        case 1:
            print("O valor da soma desses numeros é: " , soma)
            break
        case 2: 
            print('O resultado da multiplicação desses dois valores é:' , multi)
            break
        case 3:
            if num1 and num2 > maior:
                maior = num2 or num1
                break
        case 4:
            num1 = int(input("informe 1 numero"))
            num2 = int(input("informe 1 numero"))
            menu = int(input('''Oque deseja fazer com essses números
Digite (1) para somar
digite (2) para multiplicar
digite (3) para saber o maior 
digite (4) para digitar novos números
digite (5) para finalizar'''))  
                      
print('Programa finalizado')

print("TERMINAR")
