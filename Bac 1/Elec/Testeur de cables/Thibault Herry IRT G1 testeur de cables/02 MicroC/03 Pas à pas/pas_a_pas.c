// Prototypes
int sortie = 0;

void pas_a_pas();
//*********************************************

void main() {
TRISA = 0b00000010; // port A en sortie sauf RA1
PORTA = 0b11001000 ; // mettre les sorties ? z?ro sauf RA6, RA7,RA3
TRISB = 0b00000001; // Port B en sortie sauf RB_0
PORTB = 0 ; // mettre les sorties ? z?ro
pcon.OSCF = 1; // configure le bit 3 du registre pcon pour 4 mhz
CMCON = 0b00000111; // d?sactiver les comparateurs sur RA0

 while(1){
 if (RB0_bit==0) { // Si RB0 = 0 ex?cuter la ligne suivante
 pas_a_pas();
 delay_ms(250);
 } //fin du SI
 
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

//*********************************************
//sous-programme

 // Fin du sous-programme LED1 ;
 //void LED2(){ // d?but du Sous-programme LED1 ;
 //RA0_bit = 1 ;
 //delay_ms(250);
 //RA0_bit = 0 ;
 //RB1_bit = 1 ;
 //delay_ms(250);
 //RB1_bit = 0 ;
 //RB2_bit = 1 ;
 //delay_ms(250);
 //RB2_bit = 0 ;
 //RB3_bit = 1 ;
 //delay_ms(250);
 //RB3_bit = 0 ;
 //RB4_bit = 1 ;
 //delay_ms(250);
 //RB4_bit = 0 ;
 //RB5_bit = 1 ;
 //delay_ms(250);
 //RB5_bit = 0 ;
 //RB6_bit = 1 ;
 //delay_ms(250);
 //RB6_bit = 0 ;
 //RB7_bit = 1 ;
 //delay_ms(250);
 //RB7_bit = 0 ;