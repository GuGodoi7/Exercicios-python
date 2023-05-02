h = int(input("Informe a hr: "))
m = int(input("Informe os minutos: "))
s = int(input("Infor os semundos: "))

h = 0

while h < 24:
    m=0
    while m < 60:
        s = 0 
        while s < 60:
            print(f"{h:2} : {m:2} : {s:2} ")
            if f" ":
                print("Acordaaaaaaaa")
                break
            s +=1 
        if f"{h:2} : {m:2}":
            break
        m+=1
    if f"{h:2}":
        break
    h += 1
                  

