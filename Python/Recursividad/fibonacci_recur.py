import time
import sys
count_recursive=0
count_iterative=0

def fib_rec(n):
    global count_recursive

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        count_recursive+=1
        return fib_rec(n-1) + fib_rec(n-2)


def fib_ite(n):
    global count_iterative
    if(n==0):
        return 0
    result = 0
    pred1 = 0;
    pred2 = 1;
    for  i in range(n-1):
        count_iterative+=1
        result = pred1 + pred2;
        pred1 = pred2;
        pred2 = result;
    return pred2

n = int(sys.argv[1]) 

start_time = time.time()
resul=fib_rec(n)
print("Fibonacci recursivo modificado: Resultado= %d usando, %d sumas en %s segundos" %(resul,count_recursive, time.time() - start_time))


start_time = time.time()
resul=fib_ite(n)
print("Fibonacci iterativo: Resultado= %d usando, %d sumas en %s segundos" %(resul,count_iterative, time.time() - start_time))
