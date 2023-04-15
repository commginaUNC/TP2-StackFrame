segment .data
    cotizacion_peso dw : 

segment .text
    global asm_main

asm_main:
    enter 0,0
    push ebp
    mov ebp, esp
    sub esp, 8
    mov eax, [ebp - 8] 
    mov ebx, [cotizacion_peso]
    imul eax, ebx
    mov [ebp - 4], eax
    mov eax, [ebp - 4]
    mov esp, ebp
    pop ebp
    ret

