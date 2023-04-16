libconvert.so: convert.o
	gcc -shared -W -m32 -o libconvert.so convert.o

calc: main.c asm_io.o convert.o cdecl.h
	gcc -o calc asm_io.o convert.o -m32 main.c

asm_io.o: asm_io.asm asm_io.inc
	nasm -f elf32 -d ELF_TYPE asm_io.asm

convert.o: convert.asm asm_io.inc
	nasm -f elf32 convert.asm

clean:
	rm asm_io.o convert.o calc libconvert.so