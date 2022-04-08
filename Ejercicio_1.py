#Diseñe un alagoritmo que almacene una variable a a la lista obtenida mediante 
#list(range(1,5),y a continuación la modifique para que cada componente de la lista sea igual 
#al cuadrado del componente original. El programa deberá imprimir la lista obtenida en pantalla
a=[1,2,3,4,5,6,7,8,9]
b=[]
print(a)
for i in a:
    b.append(i**2)
print(b[1:5])