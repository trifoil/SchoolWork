int sortie = 0;
void pas_a_pas();
void sequence();
void eteindre();
void continu();
void tut();
main(){
     TRISA = 0b00000010; // port A en sortie sauf RA1
     PORTA = 0b11001000 ; // mettre les sorties ? z?ro sauf RA6, RA7,RA3
     TRISB = 0b00000001; // Port B en sortie sauf RB_0
     PORTB = 0 ; // mettre les sorties ? zéro
     pcon.OSCF = 1; // configure le bit 3 du registre pcon pour 4 mhz
     CMCON = 0b00000111; // désactiver les comparateurs sur RA0
     
     while (1){
              int mode =0;
              if(RB0_bit==0){
                 tut();
                 RA6_bit=1;
                 RA7_bit=1;
                 RA3_bit=0;
                 mode =1;
                 delay_ms(250);
                 if(RB0_bit==0){
                    RA3_bit=1;
                    RA7_bit=1;
                    RA6_bit=0;
                    mode=2;
                    delay_ms(750);
                    if (RB0_bit==0){
                       RA3_bit=1;
                       RA6_bit=1;
                       RA7_bit=0;
                       mode=3;
                       delay_ms(500);
                       if (RB0_bit==0){
                          RA7_bit=1;
                          }
                        
                       }

                    }
                 }
              if (mode==1){
                 pas_a_pas();
                 }
              else if(mode==2){
                   sequence();
              }
              else if (mode==3){
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
     while(1){
         if (sortie==1){
            RA0_bit=1;
            delay_ms(250);
            RA0_bit=0;
            sortie *= 2;
         }
         else if(sortie==256){
              sortie=0;
              PORTB=sortie;
              sortie=1;
         }
         else{
              PORTB = sortie;
              sortie *= 2;
              delay_ms(250);
         }
         if (RB0_bit==0){
               break;
            }
         }
}
void continu(){
     while(1){
         if (sortie==1){
            RA0_bit=1;
            delay_ms(1);
            RA0_bit=0;
            sortie *= 2;
         }
         else if(sortie==256){
              sortie=0;
              PORTB=sortie;
              sortie=1;
         }
         else{
              PORTB = sortie;
              sortie *= 2;
              delay_ms(1);
         }
         if (RB0_bit==0){
               break;
            }
         }
}
void eteindre(){
     PORTB=0;
     RA0_bit=0;

}
void tut(){
RA2_bit=1;
delay_ms(500);
RA2_bit=0;
}