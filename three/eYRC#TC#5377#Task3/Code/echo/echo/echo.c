/* 
* Team Id : 5377
* Author List : Vikrant Gajria
* Filename: echo.c
* Theme: TC -- Specific to eYRC
* Functions: uart0_init(), uart_tx(data), uart_rx(), uart_tx_line(char *), main()
* Global Variables: F_CPU, RX, TX, TE, RE, data
*/

#define F_CPU 14745600
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#define RX  (1<<4)
#define TX  (1<<3)
#define TE  (1<<5)
#define RE  (1<<7)

// data: Given with problem statement.
volatile unsigned char data;


/*
 * Function Name: uart0_init
 * Input: None.
 * Output: Sets baud rate and character settings.
 * Logic: Initialise the settings required for USART communication.
 * Example Call: uart0_init();
 */
void uart0_init()
{
	UCSR0B = 0x00;							//disable while setting baud rate
	UCSR0A = 0x00;
	UCSR0C = 0x06;
	UBRR0L = 0x5F; 							//9600BPS at 14745600Hz
	UBRR0H = 0x00;
	UCSR0B = 0x98;
	UCSR0C = 3<<1;							//setting 8-bit character and 1 stop bit
	UCSR0B = RX | TX;
}


/*
 * Function Name: uart_tx
 * Input: character to transmit.
 * Output: Transmits one byte to UART.
 * Logic: Sets UDR0 to the provided byte character when transmit line is enabled.
 * Example Call: uart_tx('I');
 */
void uart_tx(char data)
{
	while(!(UCSR0A & TE));						//waiting to transmit
	UDR0 = data;
}


ISR(USART0_RX_vect)
{
	data = UDR0;
}


/*
 * Function Name: uart_rx
 * Input: None.
 * Output: Character byte received from UART.
 * Logic: Returns the byte.
 * Example Call: uart_tx('I');
 */
char uart_rx()
{
	while(!(UCSR0A & RE));						//waiting to receive
	return UDR0;
}


/*
 * Function Name: uart_tx_line
 * Input: None.
 * Output: Sends the whole string thorugh UART.
 * Logic: Loops through every element in consecutive memory locations and 
 * 		sends the bytes through every transmitting cycle.
 * 		Blocks the main function till the entire string is not sent.
 * Example Call: char line[] = "Hello World"; uart_tx(line);
 */
void uart_tx_line(char *c) {
	// Loop till we don't encounter string terminating character.
	while (*c != '\0') {
		uart_tx(*c);
		c++;	
	}
	uart_tx('\r');
	uart_tx('\n');
}


/*
 * Function Name: main
 * Input: None.
 * Output: "I received : {byte sent through UART}"
 * Logic: Continuously listens for a byte on the receiving line.
 * 		When a byte is received, format the result string
 * 		with the received byte and send the result string
 * 		through UART.
 * Example Call: Called automatically by microcontroller.
 */
int main(void)
{
    uart0_init();
	while (1) 
    { 
		char req = uart_rx();
		char res[] = "I received : %c";
		sprintf(res, res, req);
		uart_tx_line(res);
    }
}

