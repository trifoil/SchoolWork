
_main:

;MyProject.c,5 :: 		void main() {
;MyProject.c,6 :: 		TRISA = 0b00000010; // Configure les broches du port A en sortie, sauf RA1
	MOVLW      2
	MOVWF      TRISA+0
;MyProject.c,7 :: 		PORTA = 0b11001000; // Met les sorties à zéro sauf pour RA6, RA7, RA3
	MOVLW      200
	MOVWF      PORTA+0
;MyProject.c,8 :: 		TRISB = 0b00000001; // Configure les broches du port B en sortie, sauf RB0
	MOVLW      1
	MOVWF      TRISB+0
;MyProject.c,9 :: 		PORTB = 0; // Met les sorties à zéro
	CLRF       PORTB+0
;MyProject.c,10 :: 		pcon.OSCF = 1; // Configure le bit 3 du registre pcon pour une fréquence de 4 MHz (probablement une faute de frappe, devrait être "PCON.OSCF")
	BSF        PCON+0, 3
;MyProject.c,11 :: 		CMCON = 0b00000111; // Désactive les comparateurs sur RA0
	MOVLW      7
	MOVWF      CMCON+0
;MyProject.c,12 :: 		InitExternal_INT(); // Appel de la fonction pour initialiser l'interruption externe
	CALL       _InitExternal_INT+0
;MyProject.c,15 :: 		while(1) { // Boucle infinie
L_main0:
;MyProject.c,16 :: 		RB4_bit = 1; // Met la broche RB4 à l'état logique haut
	BSF        RB4_bit+0, BitPos(RB4_bit+0)
;MyProject.c,17 :: 		delay_ms(1000); // Attend 1 seconde
	MOVLW      6
	MOVWF      R11+0
	MOVLW      19
	MOVWF      R12+0
	MOVLW      173
	MOVWF      R13+0
L_main2:
	DECFSZ     R13+0, 1
	GOTO       L_main2
	DECFSZ     R12+0, 1
	GOTO       L_main2
	DECFSZ     R11+0, 1
	GOTO       L_main2
	NOP
	NOP
;MyProject.c,18 :: 		RB4_bit = 0; // Met la broche RB4 à l'état logique bas
	BCF        RB4_bit+0, BitPos(RB4_bit+0)
;MyProject.c,19 :: 		delay_ms(1000); // Attend 1 seconde
	MOVLW      6
	MOVWF      R11+0
	MOVLW      19
	MOVWF      R12+0
	MOVLW      173
	MOVWF      R13+0
L_main3:
	DECFSZ     R13+0, 1
	GOTO       L_main3
	DECFSZ     R12+0, 1
	GOTO       L_main3
	DECFSZ     R11+0, 1
	GOTO       L_main3
	NOP
	NOP
;MyProject.c,20 :: 		}
	GOTO       L_main0
;MyProject.c,21 :: 		}
L_end_main:
	GOTO       $+0
; end of _main

_InitExternal_INT:

;MyProject.c,23 :: 		void InitExternal_INT(void) {
;MyProject.c,24 :: 		INTCON = 0b10010000; // Configure les registres d'interruption externe (INTCON)
	MOVLW      144
	MOVWF      INTCON+0
;MyProject.c,25 :: 		OPTION_REG = 0b01000000; // Configure les options d'interruption (OPTION_REG)
	MOVLW      64
	MOVWF      OPTION_REG+0
;MyProject.c,26 :: 		}
L_end_InitExternal_INT:
	RETURN
; end of _InitExternal_INT

_interrupt:
	MOVWF      R15+0
	SWAPF      STATUS+0, 0
	CLRF       STATUS+0
	MOVWF      ___saveSTATUS+0
	MOVF       PCLATH+0, 0
	MOVWF      ___savePCLATH+0
	CLRF       PCLATH+0

;MyProject.c,28 :: 		void interrupt() { // Gestionnaire d'interruption
;MyProject.c,29 :: 		INTCON = 0x90; // Réactive les interruptions externes
	MOVLW      144
	MOVWF      INTCON+0
;MyProject.c,30 :: 		RB4_bit = 0; // Met la broche RB4 à l'état logique bas
	BCF        RB4_bit+0, BitPos(RB4_bit+0)
;MyProject.c,31 :: 		RB3_bit = 1; // Met la broche RB3 à l'état logique haut
	BSF        RB3_bit+0, BitPos(RB3_bit+0)
;MyProject.c,32 :: 		delay_ms(1000); // Attend 1 seconde
	MOVLW      6
	MOVWF      R11+0
	MOVLW      19
	MOVWF      R12+0
	MOVLW      173
	MOVWF      R13+0
L_interrupt4:
	DECFSZ     R13+0, 1
	GOTO       L_interrupt4
	DECFSZ     R12+0, 1
	GOTO       L_interrupt4
	DECFSZ     R11+0, 1
	GOTO       L_interrupt4
	NOP
	NOP
;MyProject.c,33 :: 		RB3_bit = 0; // Met la broche RB3 à l'état logique bas
	BCF        RB3_bit+0, BitPos(RB3_bit+0)
;MyProject.c,34 :: 		}
L_end_interrupt:
L__interrupt8:
	MOVF       ___savePCLATH+0, 0
	MOVWF      PCLATH+0
	SWAPF      ___saveSTATUS+0, 0
	MOVWF      STATUS+0
	SWAPF      R15+0, 1
	SWAPF      R15+0, 0
	RETFIE
; end of _interrupt
