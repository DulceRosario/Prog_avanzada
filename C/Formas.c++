#include <stdio.h>
#include <iostream>
#include <sys/time.h>
#include <stddef.h>  
using namespace std;

double get_walltime()
 {
     double wcTime;
    struct timeval tp;
    gettimeofday(&tp, NULL);

    wcTime = (double)(tp.tv_sec + tp.tv_usec/1000000.0);
    return wcTime;
}

int main(void){
    int n;
    double sT,eT;

    cout << "Ingrese tamaño de arreglos N: ";
    cin >> n;

    int a[n];
    int i, suma;
    int *p;
    
    for (i = 0; i<n; i++){
        a[i] = 2;     // inicializa vect
    }
    p = &a[0];


    // Forma 1
    sT=get_walltime();
    for (suma = 0, i=0; i<n; i++){
        suma += a[i];
    }
    eT=get_walltime();
    printf("Valor 1 de suma es:  %d , con un tiempo de ejecución de %f segundos \n", suma, eT-sT);
    // Forma 2
    sT=get_walltime();
    for (suma=0, i=0; i<n; i++){
        suma += *(a + i);
    }
    eT=get_walltime();
    printf("Valor 2 de suma es:  %d , con un tiempo de ejecución de %f segundos \n", suma , eT-sT);

  
    // Forma 3
    sT=get_walltime();
    for (p=a, i=0, suma=0; i<n; ++i){
        suma += p[i];
    }
    eT=get_walltime();
     printf("Valor 3 de suma es:  %d , con un tiempo de ejecución de %f segundos \n", suma , eT-sT);

    // Forma 4
    sT=get_walltime();
    for (p=a, suma=0; p<&a[n]; ++p){
        suma += *p;
    }
    eT=get_walltime();
     printf("Valor 4 de suma es:  %d , con un tiempo de ejecución de %f segundos \n", suma , eT-sT);
     

    return(0);
}



