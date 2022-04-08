#Diseñe un programa que lea una lista de 20 elementos, pero validando que los datos leídos
#sean todos positivos, cuando el numero sea negativo, alertaremos a través de un mensaje 
#y le daremos la oportunidad al usuario que repita el numero hasta que este sea positivo
n=0
b=[]
while n <20:
    a=int(input('Digite valor numerico: '))
    while a <0:
        print('Digite solo numeros positivos')
        a=int(input('Digite valor numerico: '))
    b.append(a)
    n+=1
print(b)