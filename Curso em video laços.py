n= int(input("Digite um numero: "))
for x in range(1,n+1 ):
    print(x)
print("fim")

print('_________________________________________________________________________________________________')

i = int(input("Digite o inicio: "))
f = int(input("Digite o fim: "))
p = int(input("Digite o passo: "))

for x in range(i,f+1, p):
    print(x)
print("fim")

print("__________________________________________________________________________________________________")
s=0
for x in range(0,5):
    n = int(input("Informe um número: "))
    s += n
print('A soma desses dois valores é ' , s)