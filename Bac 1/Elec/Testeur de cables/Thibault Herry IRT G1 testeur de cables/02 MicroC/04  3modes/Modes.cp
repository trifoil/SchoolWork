#line 1 "C:/Users/thiba/OneDrive/Bureau/Thibault Herry IRT G1 testeur de cables/MicroC/04  3modes/Modes.c"

int sortie = 0;

void pas_a_pas();
void sequence();
void eteindre();
void continu();


void main() {
 TRISA = 0b00000010;
 PORTA = 0b11001000 ;
 TRISB = 0b00000001;
 PORTB = 0 ;
 pcon.OSCF = 1;
 CMCON = 0b00000111;

 while(1){
 int x=0;
 if (RB0_bit==0) {
 x=1;
 delay_ms(250);
 }
 if(RB0_bit ==0){
 x=2;
 delay_ms(750);
 }
 if (RB0_bit==0){
 x=3;
 }
 if (x==1){
 eteindre();
 RA3_bit=0;
 delay_ms(250);
 pas_a_pas();
 }
 else if(x==2){
 eteindre();
 RA6_bit=0;
 delay_ms(250);
 sequence();
 }
 else if(x==3){
 eteindre();
 RA7_bit=0;
 delay_ms(250);
 continu();
 }
}
}
void pas_a_pas(){
 if (sortie==0){
 RA0_bit = 1;
 sortie=1;
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

void sequence(){
 RA0_bit = 1 ;
 delay_ms(250);
 RA0_bit = 0 ;
 RB1_bit = 1 ;
 delay_ms(250);
 RB1_bit = 0 ;
 RB2_bit = 1 ;
 delay_ms(250);
 RB2_bit = 0 ;
 RB3_bit = 1 ;
 delay_ms(250);
 RB3_bit = 0 ;
 RB4_bit = 1 ;
 delay_ms(250);
 RB4_bit = 0 ;
 RB5_bit = 1 ;
 delay_ms(250);
 RB5_bit = 0 ;
 RB6_bit = 1 ;
 delay_ms(250);
 RB6_bit = 0 ;
 RB7_bit = 1 ;
 delay_ms(250);
 RB7_bit = 0 ;
}
void continu(){
 while(1){
 RA0_bit = 1 ;
 RA0_bit = 0 ;
 RB1_bit = 1 ;
 RB1_bit = 0 ;
 RB2_bit = 1 ;
 RB2_bit = 0 ;
 RB3_bit = 1 ;
 RB3_bit = 0 ;
 RB4_bit = 1 ;
 RB4_bit = 0 ;
 RB5_bit = 1 ;
 RB5_bit = 0 ;
 RB6_bit = 1 ;
 RB6_bit = 0 ;
 RB7_bit = 1 ;
 RB7_bit = 0 ;
 if (RB0_bit==0){
 break;
 eteindre();
 }
 }
}
void eteindre(){
 PORTB=0;
 RA3_bit=1;
 RA6_bit=1;
 RA7_bit=1;
 RA0_bit=0;
 RA1_bit=0;

}
