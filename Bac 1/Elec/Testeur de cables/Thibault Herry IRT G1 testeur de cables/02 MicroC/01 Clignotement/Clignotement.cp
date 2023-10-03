#line 1 "C:/Users/thiba/OneDrive/Bureau/thibault_herry_G1/MicroC/Clignotement/Clignotement.c"

void main() {
TRISA = 0b00000010;
PORTA = 0;
TRISB = 0b00000001;
PORTB = 0;
pcon.OSCF = 1;

while (1) {
RB4_bit = 1;
Delay_ms(1000);
RB4_bit = 0;
Delay_ms(1000);

}
}
