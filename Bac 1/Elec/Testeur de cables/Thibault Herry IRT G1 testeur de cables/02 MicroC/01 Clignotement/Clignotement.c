
void main() {
TRISA = 0b00000010; //RA7 RA6 RA5 RA4 RA3 RA2 RA1 RA0 - sorties RA1 - entr?e
PORTA = 0;
TRISB = 0b00000001; //RB7 RB6 RB5 RB4 RB3 RB2 RB1 RB0 - sorties : RB0 - entr?e
PORTB = 0;
pcon.OSCF = 1; // Configure l?oscillateur interne a 4MHz

while (1) {
RB4_bit = 1; // allumer
Delay_ms(1000);  /* One second pause */
RB4_bit = 0; // ?teindre
Delay_ms(1000);  /* One second pause */

}
}