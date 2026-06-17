/*
 * Interrupt timer eg.c
 *
 * Created: 11/05/2026 12:41:58 pm
 * Author : Ramish
 */ 

#define F_CPU 1000000UL

#include <avr/io.h>
#include <avr/interrupt.h>

volatile unsigned char overflow_count = 0;

ISR(TIMER0_OVF_vect)
{
	overflow_count++;

	if(overflow_count >= 31)
	{
		PORTB ^= (1<<PB0);   // Toggle LED

		overflow_count = 0;
	}
}

int main(void)
{
	// PB0 as output
	DDRB |= (1<<PB0);

	// Timer0 Normal Mode
	TCCR0 = 0x00;

	// Prescaler = 1024
	TCCR0 |= (1<<CS02) | (1<<CS00);

	// Enable Timer0 Overflow Interrupt
	TIMSK |= (1<<TOIE0);

	// Enable Global Interrupts
	sei();

	while(1)
	{
		// Main loop does nothing
		// ISR handles timing
	}
}

