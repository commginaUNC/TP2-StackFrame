segment .data

segment .text
    global asm_calculadora

asm_calculadora:
    push ebp
    mov ebp, esp
    mov eax, [ebp + 8] 
    mov edx, [ebp + 12]
    imul eax, edx
    pop ebp
    ret

