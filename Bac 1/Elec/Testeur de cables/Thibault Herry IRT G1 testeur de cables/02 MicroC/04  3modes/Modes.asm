
_main:

;Modes.c,10 :: 		void main() {
;Modes.c,11 :: 		TRISA = 0b00000010; // port A en sortie sauf RA1
	MOVLW      2
	MOVWF      TRISA+0
;Modes.c,12 :: 		PORTA = 0b11001000 ; // mettre les sorties ? z?ro sauf RA6, RA7,RA3
	MOVLW      200
	MOVWF      PORTA+0
;Modes.c,13 :: 		TRISB = 0b00000001; // Port B en sortie sauf RB_0
	MOVLW      1
	MOVWF      TRISB+0
;Modes.c,14 :: 		PORTB = 0 ; // mettre les sorties ? z?ro
	CLRF       PORTB+0
;Modes.c,15 :: 		pcon.OSCF = 1; // configure le bit 3 du registre pcon pour 4 mhz
	BSF        PCON+0, 3
;Modes.c,16 :: 		CMCON = 0b00000111; // d?sactiver les comparateurs sur RA0
	MOVLW      7
	MOVWF      CMCON+0
;Modes.c,18 :: 		while(1){
L_main0:
;Modes.c,19 :: 		int x=0;
	CLRF       main_x_L1+0
	CLRF       main_x_L1+1
;Modes.c,20 :: 		if (RB0_bit==0) {
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main2
;Modes.c,21 :: 		x=1;
	MOVLW      1
	MOVWF      main_x_L1+0
	MOVLW      0
	MOVWF      main_x_L1+1
;Modes.c,22 :: 		delay_ms(250);
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
;Modes.c,23 :: 		}
L_main2:
;Modes.c,24 :: 		if(RB0_bit ==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main4
;Modes.c,25 :: 		x=2;
	MOVLW      2
	MOVWF      main_x_L1+0
	MOVLW      0
	MOVWF      main_x_L1+1
;Modes.c,26 :: 		delay_ms(750);
	MOVLW      4
	MOVWF      R11+0
	MOVLW      207
	MOVWF      R12+0
	MOVLW      1
	MOVWF      R13+0
L_main5:
	DECFSZ     R13+0, 1
	GOTO       L_main5
	DECFSZ     R12+0, 1
	GOTO       L_main5
	DECFSZ     R11+0, 1
	GOTO       L_main5
	NOP
	NOP
;Modes.c,27 :: 		}
L_main4:
;Modes.c,28 :: 		if (RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main6
;Modes.c,29 :: 		x=3;
	MOVLW      3
	MOVWF      main_x_L1+0
	MOVLW      0
	MOVWF      main_x_L1+1
;Modes.c,30 :: 		}
L_main6:
;Modes.c,31 :: 		if (x==1){
	MOVLW      0
	XORWF      main_x_L1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main32
	MOVLW      1
	XORWF      main_x_L1+0, 0
L__main32:
	BTFSS      STATUS+0, 2
	GOTO       L_main7
;Modes.c,32 :: 		eteindre();
	CALL       _eteindre+0
;Modes.c,33 :: 		RA3_bit=0;
	BCF        RA3_bit+0, BitPos(RA3_bit+0)
;Modes.c,34 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_main8:
	DECFSZ     R13+0, 1
	GOTO       L_main8
	DECFSZ     R12+0, 1
	GOTO       L_main8
	DECFSZ     R11+0, 1
	GOTO       L_main8
	NOP
	NOP
;Modes.c,35 :: 		pas_a_pas();
	CALL       _pas_a_pas+0
;Modes.c,36 :: 		}
	GOTO       L_main9
L_main7:
;Modes.c,37 :: 		else if(x==2){
	MOVLW      0
	XORWF      main_x_L1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main33
	MOVLW      2
	XORWF      main_x_L1+0, 0
L__main33:
	BTFSS      STATUS+0, 2
	GOTO       L_main10
;Modes.c,38 :: 		eteindre();
	CALL       _eteindre+0
;Modes.c,39 :: 		RA6_bit=0;
	BCF        RA6_bit+0, BitPos(RA6_bit+0)
;Modes.c,40 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_main11:
	DECFSZ     R13+0, 1
	GOTO       L_main11
	DECFSZ     R12+0, 1
	GOTO       L_main11
	DECFSZ     R11+0, 1
	GOTO       L_main11
	NOP
	NOP
;Modes.c,41 :: 		sequence();
	CALL       _sequence+0
;Modes.c,42 :: 		}
	GOTO       L_main12
L_main10:
;Modes.c,43 :: 		else if(x==3){
	MOVLW      0
	XORWF      main_x_L1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main34
	MOVLW      3
	XORWF      main_x_L1+0, 0
L__main34:
	BTFSS      STATUS+0, 2
	GOTO       L_main13
;Modes.c,44 :: 		eteindre();
	CALL       _eteindre+0
;Modes.c,45 :: 		RA7_bit=0;
	BCF        RA7_bit+0, BitPos(RA7_bit+0)
;Modes.c,46 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_main14:
	DECFSZ     R13+0, 1
	GOTO       L_main14
	DECFSZ     R12+0, 1
	GOTO       L_main14
	DECFSZ     R11+0, 1
	GOTO       L_main14
	NOP
	NOP
;Modes.c,47 :: 		continu();
	CALL       _continu+0
;Modes.c,48 :: 		}
L_main13:
L_main12:
L_main9:
;Modes.c,49 :: 		}
	GOTO       L_main0
;Modes.c,50 :: 		}
L_end_main:
	GOTO       $+0
; end of _main

_pas_a_pas:

;Modes.c,51 :: 		void pas_a_pas(){
;Modes.c,52 :: 		if (sortie==0){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas36
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas36:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas15
;Modes.c,53 :: 		RA0_bit = 1;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,54 :: 		sortie=1;
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;Modes.c,55 :: 		}
	GOTO       L_pas_a_pas16
L_pas_a_pas15:
;Modes.c,56 :: 		else if (sortie==256){
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas37
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas37:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas17
;Modes.c,57 :: 		sortie=0;
	CLRF       _sortie+0
	CLRF       _sortie+1
;Modes.c,58 :: 		PORTB = sortie;
	CLRF       PORTB+0
;Modes.c,59 :: 		}
	GOTO       L_pas_a_pas18
L_pas_a_pas17:
;Modes.c,61 :: 		if (sortie==1){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas38
	MOVLW      1
	XORWF      _sortie+0, 0
L__pas_a_pas38:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas19
;Modes.c,62 :: 		RA0_bit =0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,63 :: 		sortie*=2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;Modes.c,64 :: 		}
L_pas_a_pas19:
;Modes.c,65 :: 		PORTB = sortie;
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;Modes.c,66 :: 		sortie=sortie*2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;Modes.c,67 :: 		}
L_pas_a_pas18:
L_pas_a_pas16:
;Modes.c,68 :: 		}
L_end_pas_a_pas:
	RETURN
; end of _pas_a_pas

_sequence:

;Modes.c,70 :: 		void sequence(){
;Modes.c,71 :: 		RA0_bit = 1 ;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,72 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence20:
	DECFSZ     R13+0, 1
	GOTO       L_sequence20
	DECFSZ     R12+0, 1
	GOTO       L_sequence20
	DECFSZ     R11+0, 1
	GOTO       L_sequence20
	NOP
	NOP
;Modes.c,73 :: 		RA0_bit = 0 ;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,74 :: 		RB1_bit = 1 ;
	BSF        RB1_bit+0, BitPos(RB1_bit+0)
;Modes.c,75 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence21:
	DECFSZ     R13+0, 1
	GOTO       L_sequence21
	DECFSZ     R12+0, 1
	GOTO       L_sequence21
	DECFSZ     R11+0, 1
	GOTO       L_sequence21
	NOP
	NOP
;Modes.c,76 :: 		RB1_bit = 0 ;
	BCF        RB1_bit+0, BitPos(RB1_bit+0)
;Modes.c,77 :: 		RB2_bit = 1 ;
	BSF        RB2_bit+0, BitPos(RB2_bit+0)
;Modes.c,78 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence22:
	DECFSZ     R13+0, 1
	GOTO       L_sequence22
	DECFSZ     R12+0, 1
	GOTO       L_sequence22
	DECFSZ     R11+0, 1
	GOTO       L_sequence22
	NOP
	NOP
;Modes.c,79 :: 		RB2_bit = 0 ;
	BCF        RB2_bit+0, BitPos(RB2_bit+0)
;Modes.c,80 :: 		RB3_bit = 1 ;
	BSF        RB3_bit+0, BitPos(RB3_bit+0)
;Modes.c,81 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence23:
	DECFSZ     R13+0, 1
	GOTO       L_sequence23
	DECFSZ     R12+0, 1
	GOTO       L_sequence23
	DECFSZ     R11+0, 1
	GOTO       L_sequence23
	NOP
	NOP
;Modes.c,82 :: 		RB3_bit = 0 ;
	BCF        RB3_bit+0, BitPos(RB3_bit+0)
;Modes.c,83 :: 		RB4_bit = 1 ;
	BSF        RB4_bit+0, BitPos(RB4_bit+0)
;Modes.c,84 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence24:
	DECFSZ     R13+0, 1
	GOTO       L_sequence24
	DECFSZ     R12+0, 1
	GOTO       L_sequence24
	DECFSZ     R11+0, 1
	GOTO       L_sequence24
	NOP
	NOP
;Modes.c,85 :: 		RB4_bit = 0 ;
	BCF        RB4_bit+0, BitPos(RB4_bit+0)
;Modes.c,86 :: 		RB5_bit = 1 ;
	BSF        RB5_bit+0, BitPos(RB5_bit+0)
;Modes.c,87 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence25:
	DECFSZ     R13+0, 1
	GOTO       L_sequence25
	DECFSZ     R12+0, 1
	GOTO       L_sequence25
	DECFSZ     R11+0, 1
	GOTO       L_sequence25
	NOP
	NOP
;Modes.c,88 :: 		RB5_bit = 0 ;
	BCF        RB5_bit+0, BitPos(RB5_bit+0)
;Modes.c,89 :: 		RB6_bit = 1 ;
	BSF        RB6_bit+0, BitPos(RB6_bit+0)
;Modes.c,90 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence26:
	DECFSZ     R13+0, 1
	GOTO       L_sequence26
	DECFSZ     R12+0, 1
	GOTO       L_sequence26
	DECFSZ     R11+0, 1
	GOTO       L_sequence26
	NOP
	NOP
;Modes.c,91 :: 		RB6_bit = 0 ;
	BCF        RB6_bit+0, BitPos(RB6_bit+0)
;Modes.c,92 :: 		RB7_bit = 1 ;
	BSF        RB7_bit+0, BitPos(RB7_bit+0)
;Modes.c,93 :: 		delay_ms(250);
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_sequence27:
	DECFSZ     R13+0, 1
	GOTO       L_sequence27
	DECFSZ     R12+0, 1
	GOTO       L_sequence27
	DECFSZ     R11+0, 1
	GOTO       L_sequence27
	NOP
	NOP
;Modes.c,94 :: 		RB7_bit = 0 ;
	BCF        RB7_bit+0, BitPos(RB7_bit+0)
;Modes.c,95 :: 		}
L_end_sequence:
	RETURN
; end of _sequence

_continu:

;Modes.c,96 :: 		void continu(){
;Modes.c,97 :: 		while(1){
L_continu28:
;Modes.c,98 :: 		RA0_bit = 1 ;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,99 :: 		RA0_bit = 0 ;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,100 :: 		RB1_bit = 1 ;
	BSF        RB1_bit+0, BitPos(RB1_bit+0)
;Modes.c,101 :: 		RB1_bit = 0 ;
	BCF        RB1_bit+0, BitPos(RB1_bit+0)
;Modes.c,102 :: 		RB2_bit = 1 ;
	BSF        RB2_bit+0, BitPos(RB2_bit+0)
;Modes.c,103 :: 		RB2_bit = 0 ;
	BCF        RB2_bit+0, BitPos(RB2_bit+0)
;Modes.c,104 :: 		RB3_bit = 1 ;
	BSF        RB3_bit+0, BitPos(RB3_bit+0)
;Modes.c,105 :: 		RB3_bit = 0 ;
	BCF        RB3_bit+0, BitPos(RB3_bit+0)
;Modes.c,106 :: 		RB4_bit = 1 ;
	BSF        RB4_bit+0, BitPos(RB4_bit+0)
;Modes.c,107 :: 		RB4_bit = 0 ;
	BCF        RB4_bit+0, BitPos(RB4_bit+0)
;Modes.c,108 :: 		RB5_bit = 1 ;
	BSF        RB5_bit+0, BitPos(RB5_bit+0)
;Modes.c,109 :: 		RB5_bit = 0 ;
	BCF        RB5_bit+0, BitPos(RB5_bit+0)
;Modes.c,110 :: 		RB6_bit = 1 ;
	BSF        RB6_bit+0, BitPos(RB6_bit+0)
;Modes.c,111 :: 		RB6_bit = 0 ;
	BCF        RB6_bit+0, BitPos(RB6_bit+0)
;Modes.c,112 :: 		RB7_bit = 1 ;
	BSF        RB7_bit+0, BitPos(RB7_bit+0)
;Modes.c,113 :: 		RB7_bit = 0 ;
	BCF        RB7_bit+0, BitPos(RB7_bit+0)
;Modes.c,114 :: 		if (RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_continu30
;Modes.c,115 :: 		break;
	GOTO       L_continu29
;Modes.c,117 :: 		}
L_continu30:
;Modes.c,118 :: 		}
	GOTO       L_continu28
L_continu29:
;Modes.c,119 :: 		}
L_end_continu:
	RETURN
; end of _continu

_eteindre:

;Modes.c,120 :: 		void eteindre(){
;Modes.c,121 :: 		PORTB=0;
	CLRF       PORTB+0
;Modes.c,122 :: 		RA3_bit=1;
	BSF        RA3_bit+0, BitPos(RA3_bit+0)
;Modes.c,123 :: 		RA6_bit=1;
	BSF        RA6_bit+0, BitPos(RA6_bit+0)
;Modes.c,124 :: 		RA7_bit=1;
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;Modes.c,125 :: 		RA0_bit=0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;Modes.c,126 :: 		RA1_bit=0;
	BCF        RA1_bit+0, BitPos(RA1_bit+0)
;Modes.c,128 :: 		}
L_end_eteindre:
	RETURN
; end of _eteindre
