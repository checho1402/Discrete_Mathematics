V=['a','b','c','d','e','f','g','h'] #En orden.
E=[('a','b'),('a','g'),('a','g'),('a','c'),('b','d'),('b','g'),
('c','d'),('c','e'),('d','f'),('e''f'),('e','g'),('f','h')]
S=[]
V_=[]
E_=[]
#############
S.append(V[0])
V_.append(V[0])

#############
key=True
while key:
    for x in S:
        for y in V:
            if (x,y) in E :
                if x in S and y in S:
                    pass
                else:
                    E_.append((x,y))
                    S.append(y)
                    V_.append(y)
                    
                
    break
print(E_,V_)
##############

