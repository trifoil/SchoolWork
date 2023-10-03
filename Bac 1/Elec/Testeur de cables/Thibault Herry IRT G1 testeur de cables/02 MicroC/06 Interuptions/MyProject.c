void main();
void interupt(); // Déclaration de la fonction "interupt" (probablement une faute de frappe, devrait être "interrupt")
void InitExternal_INT(); // Déclaration de la fonction "InitExternal_INT" pour initialiser l'interruption externe

void main() {
     TRISA = 0b00000010; // Configure les broches du port A en sortie, sauf RA1
     PORTA = 0b11001000; // Met les sorties à zéro sauf pour RA6, RA7, RA3
     TRISB = 0b00000001; // Configure les broches du port B en sortie, sauf RB0
     PORTB = 0; // Met les sorties à zéro
     pcon.OSCF = 1; // Configure le bit 3 du registre pcon pour une fréquence de 4 MHz (probablement une faute de frappe, devrait être "PCON.OSCF")
     CMCON = 0b00000111; // Désactive les comparateurs sur RA0
     InitExternal_INT(); // Appel de la fonction pour initialiser l'interruption externe
     

     while(1) { // Boucle infinie
         RB4_bit = 1; // Met la broche RB4 à l'état logique haut
         delay_ms(1000); // Attend 1 seconde
         RB4_bit = 0; // Met la broche RB4 à l'état logique bas
         delay_ms(1000); // Attend 1 seconde
     }
}

void InitExternal_INT(void) {
    INTCON = 0b10010000; // Configure les registres d'interruption externe (INTCON)
    OPTION_REG = 0b01000000; // Configure les options d'interruption (OPTION_REG)
}

void interrupt() { // Gestionnaire d'interruption
    INTCON = 0x90; // Réactive les interruptions externes
    RB4_bit = 0; // Met la broche RB4 à l'état logique bas
    RB3_bit = 1; // Met la broche RB3 à l'état logique haut
    delay_ms(1000); // Attend 1 seconde
    RB3_bit = 0; // Met la broche RB3 à l'état logique bas
}