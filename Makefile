calc: convert.o
	gcc -m32 -o calc main.c convert.o

convert.o: 
	nasm -f elf32 -o convert.o convert.asm

clean:
	rm convert.o calc 