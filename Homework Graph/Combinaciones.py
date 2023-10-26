def Combinacion(n,r):
    l_n=[]
    combs=[]
    for i in range(1,n+1):
        l_n.append(i)
    

    for j in range(0,len(l_n)):
        for k in range(0,len(l_n)):
            if k>j:
                aux=(l_n[j],l_n[k])
                combs.append(aux)
    print(combs)
Combinacion(6,2)