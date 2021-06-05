a=int(input("introdu primul numar:"))
b=int(input("introdu al doilea numar:"))
c=int(input("introdu al treilea numar:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
