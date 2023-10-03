#line 1 "C:/Users/thiba/OneDrive/Bureau/thibault_herry_G1/MicroC/Pas_a_pas/pas_a_pas.c"

int sortie = 0;

void pas_a_pas();


void main() {
TRISA = 0b00000010;
PORTA = 0b11001000 ;
TRISB = 0b00000001;
PORTB = 0 ;
pcon.OSCF = 1;
CMCON = 0b00000111;

 while(1){
 if (RB0_bit==0) {
 pas_a_pas();
 delay_ms(250);
 }

 }
}
void pas_a_pas(){
 if (sortie==0){
 RA0_bit = 1;
 sortie=1;
 RA3_bit=0;
}
else if (sortie==256){
sortie=0;
PORTB = sortie;
}
else {
if (sortie==1){
RA0_bit =0;
sortie*=2;
}
PORTB = sortie;
sortie=sortie*2;
}
}
