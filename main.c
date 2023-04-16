#include "cdecl.h"

int PRE_CDECL asm_calculadora(int,int) POST_CDECL;

int main(){

    int tasa_cambio, cotizacion;
    int conversion;

    conversion = asm_calculadora(tasa_cambio,cotizacion);
    //printf("La conversion es: %d\n", conversion);
    return 0;
}