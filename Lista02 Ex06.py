idade = -1
maior = 0
idadeFinal = 0

while idade != 0:
    if idade > maior:
        maior = idade 
        nomeFinal = nome
        sexoFinal = sexo
    nome = (input("Informe seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = (input("Informe se gênero: "))

print("nome " , nomeFinal, "idade" , maior , "gênero" , sexoFinal)

