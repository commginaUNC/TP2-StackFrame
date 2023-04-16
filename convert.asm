segment .data

segment .text
    global asm_calculadora

asm_calculadora:
    enter 0,0
    fld qword [ebp + 8] 
    fld qword [ebp + 16]
    fmul st1,st0
    fstp qword [ebp + 8] 
    leave
    ret

