def recibirVertices():
    print("Ingrese los vértices de la siguiente forma: ")
    print("[x,y,z]")
    preVert=input(":")
    Vert=[]
    for i in range(0,len(preVert)):
        if i%2==0:
            Vert.append(preVert[i])
    print(Vert)
    return Vert
def recibirAristas():
    print("Ingrese las aristas de la siguiente forma: ")
    print("(x,y)")
    print("Presione ENTER después de cada arista")
    print("Cuando ya no hayan más aristas que ingresar ingrese 0")
    Aris=[]
    ingreso=""
    while ingreso!='0':
        ingreso=input("Ingrese arista: ")
        if ingreso=='0':
            break
        else:
            apoyo=(ingreso[1],ingreso[3])
            Aris.append(apoyo)
            apoyo="" 

    return Aris

def formarDiccionario():
    Vertices=recibirVertices()
    Aristas=recibirAristas()
   
    pre_ar=[]
    post_ar=[]
    for i in range(0,len(Aristas)):
        pre_ar.append(Aristas[i][0])
        post_ar.append(Aristas[i][1])
    
    j=0
    while 0<=j<len(pre_ar):
        if j>0:
            if pre_ar[j] == pre_ar[j-1]:
                if type(post_ar[j-1])== str:
                    post_ar[j-1]=[post_ar[j-1]]
                post_ar[j-1].append(post_ar[j])
                post_ar.pop(j)
                pre_ar.pop(j)
                j=0
                
        j+=1
    diccionario=dict(zip(pre_ar,post_ar))
    print(diccionario)
    return diccionario

grafo_V = formarDiccionario()

V_T = []#vertices de T
E_T=[] # aristas de T

ocupados=[]

def Busqu_profundidad(grafo, vertice,V_T):
     if vertice in grafo and vertice not in V_T:
        V_T.append(vertice) 
        for u in grafo[vertice]:
            if u not in ocupados: 
                ocupados.append(u)        
                E_T.append((vertice,u))
                Busqu_profundidad(grafo,u,V_T)
            

Busqu_profundidad(grafo_V, '1',V_T)


print(E_T)




