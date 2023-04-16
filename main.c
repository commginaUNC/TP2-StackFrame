
#include <stdio.h>
#include <stdlib.h>
#include "cdecl.h"

extern double asm_calculadora(double,double);

int main(int argc, char const *argv[]){

    double tasa_cambio = atof(argv[1]);
    double cotizacion = atof(argv[2]);
    double conversion;


    conversion = asm_calculadora(tasa_cambio,cotizacion);
    printf("%f", conversion);
    return 0;
}