n = int(input("Digite um numero: "))
res = 0
for c in range(1, n):
    if n < 0:
        res -= 1/n
    else:
        res += 1/n
print(res)
