int sortie = 0; // Variable pour stocker l'état de sortie

void pas_a_pas(); // Déclaration de la fonction "pas_a_pas" pour le mode pas à pas
void sequence(); // Déclaration de la fonction "sequence" pour le mode séquence
void eteindre(); // Déclaration de la fonction "eteindre" pour éteindre les sorties
void continu(); // Déclaration de la fonction "continu" pour le mode continu
void tut(); // Déclaration de la fonction "tut" pour afficher un signal de test
void interrupt(); // Déclaration de la fonction "interrupt" pour la gestion des interruptions

main() {
     TRISA = 0b00000010; // Configuration du port A en sortie, sauf RA1
     PORTA = 0b11001000; // Mettre les sorties à zéro sauf RA6, RA7, RA3
     TRISB = 0b00000001; // Configuration du port B en sortie, sauf RB0
     PORTB = 0; // Mettre les sorties à zéro
     pcon.OSCF = 1; // Configuration du bit 3 du registre pcon pour une fréquence de 4 MHz (probablement une faute de frappe, devrait être "PCON.OSCF")
     CMCON = 0b00000111; // Désactiver les comparateurs sur RA0
     INTCON = 0b10010000; // Configuration des registres d'interruption externe (INTCON)
     OPTION_REG = 0b00000000; // Configuration des options d'interruption (OPTION_REG) pour le fonctionnement sur proteus

     while(1) {} // Boucle infinie pour maintenir le programme en cours d'exécution
}

void interrupt() {
    int mode = 0; // Variable pour stocker le mode

    if (RB0_bit == 0) { // Vérifie si la broche RB0 est à 0
        tut(); // Appelle la fonction tut()
        RA6_bit = 1; // Active la broche RA6
        RA7_bit = 1; // Active la broche RA7
        RA3_bit = 0; // Désactive la broche RA3
        mode = 1; // Affecte le mode 1 à la variable mode
        delay_ms(250); // Attend pendant 250 ms

        if (RB0_bit == 0) { // Vérifie à nouveau si la broche RB0 est à 0
            RA3_bit = 1; // Active la broche RA3
            RA7_bit = 1; // Active la broche RA7
            RA6_bit = 0; // Désactive la broche RA6
            mode = 2; // Affecte le mode 2 à la variable mode
            delay_ms(750); // Attend pendant 750 ms

            if (RB0_bit == 0) { // Vérifie à nouveau si la broche RB0 est à 0
                RA3_bit = 1; // Active la broche RA3
                RA6_bit = 1; // Active la broche RA6
                RA7_bit = 0; // Désactive la broche RA7
                mode = 3; // Affecte le mode 3 à la variable mode
                delay_ms(500); // Attend pendant 500 ms

                if (RB0_bit == 0) { // Vérifie à nouveau si la broche RB0 est à 0
                    RA7_bit = 1; // Active la broche RA7
                }
            }
        }
    }

    // Exécute différentes actions en fonction du mode

    if (mode == 1) {
        pas_a_pas(); // Appelle la fonction pas_a_pas()
    } else if (mode == 2) {
        sequence(); // Appelle la fonction sequence()
    } else if (mode == 3) {
        continu(); // Appelle la fonction continu()
    }
}

void pas_a_pas() {
    if (sortie == 0) {  // Si la variable sortie est égale à 0
        RA0_bit = 1;  // Active la broche RA0
        sortie = 1;  // Met à jour la variable sortie
    } else if (sortie == 256) {  // Si la variable sortie est égale à 256
        sortie = 0;  // Remet la variable sortie à 0
        PORTB = sortie;  // Met à jour la valeur du port B avec sortie
    } else {  // Sinon
        if (sortie == 1) {  // Si la variable sortie est égale à 1
            RA0_bit = 0;  // Désactive la broche RA0
            sortie *= 2;  // Double la valeur de sortie
        }
        PORTB = sortie;  // Met à jour la valeur du port B avec sortie
        sortie = sortie * 2;  // Double la valeur de sortie
    }
}

void sequence() {
    while (1) {  // Boucle infinie
        if (sortie == 1) {  // Si la variable sortie est égale à 1
            RA0_bit = 1;  // Active la broche RA0
            delay_ms(250);  // Attend pendant 250 ms
            RA0_bit = 0;  // Désactive la broche RA0
            sortie *= 2;  // Double la valeur de sortie
        } else if (sortie == 256) {  // Si la variable sortie est égale à 256
            sortie = 0;  // Remet la variable sortie à 0
            PORTB = sortie;  // Met à jour la valeur du port B avec sortie
            sortie = 1;  // Met à jour la variable sortie à 1
        } else {  // Sinon
            PORTB = sortie;  // Met à jour la valeur du port B avec sortie
            sortie *= 2;  // Double la valeur de sortie
            delay_ms(250);  // Attend pendant 250 ms
        }

        if (RB0_bit == 0) {  // Si la broche RB0 est à 0
            break;  // Sort de la boucle while
        }
    }
}
void continu() {
    while (1) {  // Boucle infinie
        if (sortie == 1) {  // Si la variable sortie est égale à 1
            RA0_bit = 1;  // Active la broche RA0
            delay_ms(1);  // Attend pendant 1 ms
            RA0_bit = 0;  // Désactive la broche RA0
            sortie *= 2;  // Double la valeur de sortie
        } else if (sortie == 256) {  // Si la variable sortie est égale à 256
            sortie = 0;  // Remet la variable sortie à 0
            PORTB = sortie;  // Met à jour la valeur du port B avec sortie
            sortie = 1;  // Met à jour la variable sortie à 1
        } else {  // Sinon
            PORTB = sortie;  // Met à jour la valeur du port B avec sortie
            sortie *= 2;  // Double la valeur de sortie
            delay_ms(1);  // Attend pendant 1 ms
        }

        if (RB0_bit == 0) {  // Si la broche RB0 est à 0
            break;  // Sort de la boucle while
        }
    }
}

void eteindre() {
    PORTB = 0;  // Éteint toutes les broches du port B
    RA0_bit = 0;  // Désactive la broche RA0
}

void tut() {
    RA2_bit = 1;  // Active la broche RA2
    delay_ms(500);  // Attend pendant 500 ms
    RA2_bit = 0;  // Désactive la broche RA2
}