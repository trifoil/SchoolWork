#line 1 "C:/Users/thiba/OneDrive/Bureau/Thibault Herry IRT G1 testeur de cables/MicroC/Interuptions/MyProject.c"
void main();
void interupt();
void InitExternal_INT();

void main() {
 TRISA = 0b00000010;
 PORTA = 0b11001000;
 TRISB = 0b00000001;
 PORTB = 0;
 pcon.OSCF = 1;
 CMCON = 0b00000111;
 InitExternal_INT();


 while(1) {
 RB4_bit = 1;
 delay_ms(1000);
 RB4_bit = 0;
 delay_ms(1000);
 }
}

void InitExternal_INT(void) {
 INTCON = 0b10010000;
 OPTION_REG = 0b01000000;
}

void interrupt() {
 INTCON = 0x90;
 RB4_bit = 0;
 RB3_bit = 1;
 delay_ms(1000);
 RB3_bit = 0;
}
