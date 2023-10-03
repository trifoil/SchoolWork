
_main:

;Clignotement.c,2 :: 		void main() {
;Clignotement.c,3 :: 		TRISA = 0b00000010; //RA7 RA6 RA5 RA4 RA3 RA2 RA1 RA0 - sorties RA1 - entr?e
	MOVLW      2
	MOVWF      TRISA+0
;Clignotement.c,4 :: 		PORTA = 0;
	CLRF       PORTA+0
;Clignotement.c,5 :: 		TRISB = 0b00000001; //RB7 RB6 RB5 RB4 RB3 RB2 RB1 RB0 - sorties : RB0 - entr?e
	MOVLW      1
	MOVWF      TRISB+0
;Clignotement.c,6 :: 		PORTB = 0;
	CLRF       PORTB+0
;Clignotement.c,7 :: 		pcon.OSCF = 1; // Configure l?oscillateur interne a 4MHz
	BSF        PCON+0, 3
;Clignotement.c,9 :: 		while (1) {
L_main0:
;Clignotement.c,10 :: 		RB4_bit = 1; // allumer
	BSF        RB4_bit+0, BitPos(RB4_bit+0)
;Clignotement.c,11 :: 		Delay_ms(1000);  /* One second pause */
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
;Clignotement.c,12 :: 		RB4_bit = 0; // ?teindre
	BCF        RB4_bit+0, BitPos(RB4_bit+0)
;Clignotement.c,13 :: 		Delay_ms(1000);  /* One second pause */
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
;Clignotement.c,15 :: 		}
	GOTO       L_main0
;Clignotement.c,16 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
