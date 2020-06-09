import time #Para generar pausa
#carne 201701026

carne = 26
serie = []

def coll(num):                          #funcion de Collatz 
    while (num != 1):                   # while hasta que no sea 1 el numero no sale del ciclo
        serie.append(num)           #vemos si es par o impar dependiendo aplicamos la formula
        if(num%2 > 0):
            num = 3*num +1
        else:
            num = num // 2
    serie.append(num)                   # guardamos en un vector y mandamos
    return serie    



archivo = open('collatz.txt' ,'w')                      #abrimos el archivo 
archivo.write('Secuencias de Collatz desde 2 a 026 \n')
print('Secuencias de Collatz desde 2 a 026')
for i in range(2,carne+1):
    print(str(coll(i)))
    ser = str(coll(i))
    archivo.write(ser + '\n')
    time.sleep(1)
    serie = []
archivo.close() #Siempre cerrar el archivo al finalizar la escritura
print('Escritura Finalizada')  