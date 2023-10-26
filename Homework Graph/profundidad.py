grafo = {

    'A' : ['B','C','F'],
    'B' : ['D','E'],
    'C' : [],
    'D' : [],
    'E' : [],
    'F' : [],

}

ARISTAS =['AB', 'AC', 'BD', 'BE', 'CF', 'E,F']
tomados = set()

recorrido ="A"
def B_profundidad(tomados, grafo, vertice):
    if vertice in grafo:
        print(vertice)
        tomados.add(vertice)
        

        
        for x in grafo[vertice]:
            print(vertice)
            print(x)
            B_profundidad(tomados,grafo,x)


B_profundidad(tomados,grafo, 'A')
print(recorrido)