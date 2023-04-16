segment .data

segment .text
    global asm_calculadora

asm_calculadora:
    push ebp
    mov ebp, esp
    fld qword [ebp + 8] 
    fld qword [ebp + 12]
    fmul st1,st0
    fstp qword [ebp + 8] 
    pop ebp
    ret

