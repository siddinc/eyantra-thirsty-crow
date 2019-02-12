CC = avr-gcc
OBJ = main.c
BOARD = atmega2560

main: $(OBJ)
	$(CC) -g -Os -mmcu=$(BOARD) -c $^
	$(CC) -g -mmcu=$(BOARD) -o $@.elf $@.o
	avr-objcopy -j .text -j .data -O ihex $@.elf $@.hex

.PHONY: clean
clean:
	rm -f *.o *.elf *.hex
