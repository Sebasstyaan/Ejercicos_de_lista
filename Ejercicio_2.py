# Construya un programa que almacene en a una lista obtenida con list(range(1,n)), donde n 
#es un entero que se pide por teclado, y modificar dicha lista para que cada componente de 
#la lista sea igual al cubo del componente original. El programa mostrará la lista obtenida por pantalla
n=int(input('Digite un numero: '))
a=[0,2,3,4,5,6,7,8,9]
c=[]
print(a)
a.insert(5,n)
for i in a:
    c.append(i**2)
print(c [1:6])