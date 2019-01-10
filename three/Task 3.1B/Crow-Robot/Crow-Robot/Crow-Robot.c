/* 
* Team Id : 5377
* Author List : Yash Shah
* Filename: Crow-Robot.c
* Theme: TC -- Specific to eYRC
* Functions: magnet_pin_config(), motor_pin_config(), magnet_on(), magnet_off(),
		forward(), backward(), left(), right(), soft_left(), soft_right(), stop()
* Global Variables: F_CPU, PORTn variables.
*/

#define F_CPU 14745600
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>


// --------------------------------------------------------------------------------


/*
 * Function Name: magnet_pin_config
 * Input: None.
 * Output: Configures H port.
 * Logic:
 * 		1. Set all pins of H port to output pins by setting its Data Direction Register.
 * 		2. Set all pins of H port to low as default.
 * Example Call: magnet_pin_config();
 */
void magnet_pin_config()
{
	DDRH = 0xFF;
	PORTH =0x00;
}


/*
 * Function Name: magnet_on
 * Input: None.
 * Output: Energises the electromagnet.
 * Logic: Set H0 to high.
 * Example Call: magnet_on();
 */
void magnet_on()
{
	PORTH = 0x01;
}

/*
 * Function Name: magnet_off
 * Input: None.
 * Output: De-energises the electromagnet.
 * Logic: Set H0 to low.
 * Example Call: magnet_off();
 */
void magnet_off()
{
	PORTH = 0x00;
}


// --------------------------------------------------------------------------------


/*
 * Function Name: motor_pin_config
 * Input: None.
 * Output: Configures A port.
 * Logic:
 * 		1. Set all pins of A port to output pins by setting its Data Direction Register.
 * 		2. Set all pins of A port to low as default.
 * Example Call: motor_pin_config();
 */
void motor_pin_config()
{
	DDRA = 0xFF;
	PORTA = 0x00;
}


/*
 * Function Name: forward
 * Input: None.
 * Output: Both motors move in forward direction.
 * Logic: Set A3 and A1 to high.
 * Example Call: forward();
 */
void forward()
{
	PORTA = 0x0A;
}

/*
 * Function Name: backward
 * Input: None.
 * Output: Both motors move in backward direction.
 * Logic: Set A2 and A0 to high.
 * Example Call: backward();
 */
void backward()
{
	PORTA = 0x05;
}

/*
 * Function Name: left
 * Input: None.
 * Output: Left motor backward, Right motor forward.
 * Logic: Set A2 and A1 to high.
 * Example Call: left();
 */
void left()
{
	PORTA = 0x06;
}

/*
 * Function Name: right
 * Input: None.
 * Output: Right motor backward, left motor forward.
 * Logic: Set A3 and A0 to high.
 * Example Call: right();
 */
void right()
{
	PORTA = 0x09;	
}

/*
 * Function Name: soft_left
 * Input: None.
 * Output: Left motor stop, right motor forward.
 * Logic: Set A3 to high.
 * Example Call: soft_left();
 */
void soft_left()
{
	PORTA = 0x04;
}

/*
 * Function Name: soft_right
 * Input: None.
 * Output: Right motor stop, left motor forward.
 * Logic: Set A0 to high.
 * Example Call: soft_right();
 */
void soft_right()
{
	PORTA = 0x01;	
}

/*
 * Function Name: stop
 * Input: None.
 * Output: All motors stop.
 * Logic: Set A3, A2, A1, A0 to low.
 * Example Call: stop();
 */
void stop()
{
	PORTA = 0x00;
}


// --------------------------------------------------------------------------------


/*
 * Function Name: main
 * Input: None.
 * Output: Required robot motion.
 * Logic: Robot movement:
 * 		 Move forward for 3 sec
 * 		 Stop
 * 		 Energise Electromagnet  Wait 3 Sec
 * 		 Move backward for 3 sec  De-energise magnet
 * 		 Stop
 * 		 Wait 3 sec
 * Example Call: Called automatically by microcontroller.
 */
int main(void)
{
	motor_pin_config();
	magnet_pin_config();
    while (1) 
    {
		forward();
		_delay_ms(3000);
		stop();
		magnet_on();
		_delay_ms(3000);
		backward();
		_delay_ms(3000);
		magnet_off();
		stop();
		_delay_ms(3000);
    }
}
