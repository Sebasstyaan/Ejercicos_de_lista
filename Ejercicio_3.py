#Construya una lista que sustituya cualquier elemento negativo por cero.
a=[1,2,3,-4,-5,-6]
b=[]
print(a)
for i in a:
    if i<=0:
        i=0
    b.append(i)
print(b)