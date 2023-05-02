voto = 1
votoTotal = 0
votoc1 = 0
votoc2 = 0
votoc3 = 0
nulo = 0
porc_1: 0
porc_2: 0
porc_3: 0

c1=input("Digite o nome do candidato1: ")
c2=input("Digite o nome do candidato2: ")
c3=input("Digite o nome do candidato3: ")

while voto != 0: 
    print
    (f"""
    ==========================================
                    "Eleição"
    ==========================================
    ==========================================
        1:{c1}
        2:{c2}
        3:{c3}
    ========================================""")
    voto = int(input("Qual seu voto: "))
    
    match voto:
        case 0:
            break
        case 1:
            votoc1 += 1
            votoTotal += 1
        case 2:
            votoc2 += 1
            votoTotal += 1
        case 3:
            votoc3 += 1
            votoTotal += 1
        case _:
            nulo += 1
            votoTotal +=1
            print("Voto nulo")

porc_1 = (votoc1 * 100) / votoTotal
porc_2 = (votoc2 * 100) / votoTotal
porc_3 = (votoc3 * 100) / votoTotal
porc_nulo = (nulo * 100) / votoTotal

print(f"""
{c1}, {votoc1}, {porc_1:.2f}
{c2}, {votoc2}, {porc_2:.2f}
{c3}, {votoc3}, {porc_3:.2f}
Nulos, {nulo}, {porc_nulo:.2f}
""")



            


