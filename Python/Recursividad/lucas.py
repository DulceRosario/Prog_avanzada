import time
import sys

count_recursive=0
count_iterative=0

def lucas_rec(n):
    global count_recursive

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        count_recursive+=1
        return lucas_rec(n-1)+lucas_rec(n-2)
        


def lucas_ite(n):
    global count_iterative
    if (n==0):
        return 2
    if  (n==1):
        return 1
    acumulado=1
    anterior=2
    for i in range(n-1):
        count_iterative+=1
        aux=acumulado
        acumulado+=anterior
        anterior=aux        
    return acumulado

n = int(sys.argv[1]) 
start_time = time.time()
resul=lucas_rec(n)
print("Lucas recursivo modificado: Resultado= %d usando, %d sumas en %s segundos" %(resul,count_recursive, time.time() - start_time))


start_time = time.time()
resul=lucas_ite(n)
print("Lucas iterativo: Resultado= %d usando, %d sumas en %s segundos" %(resul,count_iterative, time.time() - start_time))

