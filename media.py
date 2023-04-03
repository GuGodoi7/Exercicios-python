nota1 = float(input('Informe a nota da primeira prova: '))
nota2 = float(input('Informe a nota da segunda prova: '))
nota3 = float(input('Informe a nota da terceira prova: '))
nota = str

media = (nota1 + nota2 + nota3) / 3 

if media >= 9:
    nota = 'A'
elif media >= 8: 
    nota = 'B'
elif media >= 7:
    nota = 'C'
elif media >= 6:
    nota = 'D'
else:
    nota = 'F'

match nota:
    case 'A':
        print('Sua media foi ', media , 'Seu conceito é A ' )
    case 'B':
        print('Sua media foi ', media , 'Seu conceito é B ' )
    case 'C':
        print('Sua media foi ', media , 'Seu conceito é C ' )
    case 'E':
        print('Sua media foi ', media , 'Seu conceito é D ' )
    case 'D':
        print('Sua media foi ', media , 'Seu conceito é E ' )
    case 'F':
        print('Sua media foi ', media , 'Seu conceito é F ' )
