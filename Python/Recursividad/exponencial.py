import time
import sys

count_mod=0
count_recursive=0
count_iterative=0

def expo_rec_mod(x ,b):
    global count_mod
    if b == 0:
        return 0
    elif b == 1:
        return x
    else:
         if (b % 2) == 0:
            count_mod+=1
            return expo_rec_mod(x,b/2)* expo_rec_mod(x,b/2) 
         else:
            count_mod+=2
            return x*expo_rec_mod(x ,(b-1)/2) * expo_rec_mod(x ,(b-1)/2)


def expo_rec(x ,b):
    global count_recursive
    if b == 0:
        return 1
    else:
        count_recursive+=1
        return x*expo_rec(x ,b-1)


def expo_ite(x ,b):
    global count_iterative
    result=x
    for i in range(b-1):
        count_iterative+=1
        result=result*x
    return result



x = int(sys.argv[1])  
b = int(sys.argv[2])
start_time = time.time()
resul=expo_rec(x ,b)
print("Exponencial recursivo: Resultado= %d usando, %d multiplicaciones en %s segundos" %(resul,count_recursive, time.time() - start_time))




start_time = time.time()
resul=expo_ite(x ,b)
print("Exponencial iterativo: Resultado= %d usando, %d multiplicaciones en %s segundos" %(resul,count_iterative, time.time() - start_time))


start_time = time.time()
resul=expo_rec_mod(x ,b)
print("Exponencial recursivo modificado: Resultado= %d usando, %d multiplicaciones en %s segundos" %(resul,count_mod, time.time() - start_time))


