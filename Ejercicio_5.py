#Diseñe un programa que lea una cadena y muestre en una lista con todas sus palabras en 
#mayúscula, la lista devuelta no debe tener palabras repetidas
#a=[]

#texto=input('Digite la oracion o frase: ')
#texto=texto.upper()
#for c in texto:
#    a.append(set(texto))
#    if(c !=" "):
#        a.append(c)
#texto.split(" ")
#a.append(set(texto))
#print(a)
texto=input("Digite el una palabra: ")          
texto=texto.upper()
r=texto.split(" ")
resultado=[set(r)]

print(resultado)