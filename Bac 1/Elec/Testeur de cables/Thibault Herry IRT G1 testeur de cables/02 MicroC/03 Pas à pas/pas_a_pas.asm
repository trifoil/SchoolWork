
_main:

;pas_a_pas.c,7 :: 		void main() {
;pas_a_pas.c,8 :: 		TRISA = 0b00000010; // port A en sortie sauf RA1
	MOVLW      2
	MOVWF      TRISA+0
;pas_a_pas.c,9 :: 		PORTA = 0b11001000 ; // mettre les sorties ? z?ro sauf RA6, RA7,RA3
	MOVLW      200
	MOVWF      PORTA+0
;pas_a_pas.c,10 :: 		TRISB = 0b00000001; // Port B en sortie sauf RB_0
	MOVLW      1
	MOVWF      TRISB+0
;pas_a_pas.c,11 :: 		PORTB = 0 ; // mettre les sorties ? z?ro
	CLRF       PORTB+0
;pas_a_pas.c,12 :: 		pcon.OSCF = 1; // configure le bit 3 du registre pcon pour 4 mhz
	BSF        PCON+0, 3
;pas_a_pas.c,13 :: 		CMCON = 0b00000111; // d?sactiver les comparateurs sur RA0
	MOVLW      7
	MOVWF      CMCON+0
;pas_a_pas.c,15 :: 		while(1){
L_main0:
;pas_a_pas.c,16 :: 		if (RB0_bit==0) { // Si RB0 = 0 ex?cuter la ligne suivante
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main2
;pas_a_pas.c,17 :: 		pas_a_pas();
	CALL       _pas_a_pas+0
;pas_a_pas.c,18 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
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
;pas_a_pas.c,19 :: 		} //fin du SI
L_main2:
;pas_a_pas.c,21 :: 		}
	GOTO       L_main0
;pas_a_pas.c,22 :: 		}
L_end_main:
	GOTO       $+0
; end of _main

_pas_a_pas:

;pas_a_pas.c,23 :: 		void pas_a_pas(){
;pas_a_pas.c,24 :: 		if (sortie==0){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas11
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas11:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas4
;pas_a_pas.c,25 :: 		RA0_bit = 1;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;pas_a_pas.c,26 :: 		sortie=1;
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;pas_a_pas.c,27 :: 		RA3_bit=0;
	BCF        RA3_bit+0, BitPos(RA3_bit+0)
;pas_a_pas.c,28 :: 		}
	GOTO       L_pas_a_pas5
L_pas_a_pas4:
;pas_a_pas.c,29 :: 		else if (sortie==256){
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas12
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas12:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas6
;pas_a_pas.c,30 :: 		sortie=0;
	CLRF       _sortie+0
	CLRF       _sortie+1
;pas_a_pas.c,31 :: 		PORTB = sortie;
	CLRF       PORTB+0
;pas_a_pas.c,32 :: 		}
	GOTO       L_pas_a_pas7
L_pas_a_pas6:
;pas_a_pas.c,34 :: 		if (sortie==1){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas13
	MOVLW      1
	XORWF      _sortie+0, 0
L__pas_a_pas13:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas8
;pas_a_pas.c,35 :: 		RA0_bit =0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;pas_a_pas.c,36 :: 		sortie*=2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;pas_a_pas.c,37 :: 		}
L_pas_a_pas8:
;pas_a_pas.c,38 :: 		PORTB = sortie;
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;pas_a_pas.c,39 :: 		sortie=sortie*2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;pas_a_pas.c,40 :: 		}
L_pas_a_pas7:
L_pas_a_pas5:
;pas_a_pas.c,41 :: 		}
L_end_pas_a_pas:
	RETURN
; end of _pas_a_pas
