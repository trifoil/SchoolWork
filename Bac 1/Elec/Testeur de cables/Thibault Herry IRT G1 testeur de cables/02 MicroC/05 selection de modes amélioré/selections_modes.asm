
_main:

;selections_modes.c,7 :: 		main(){
;selections_modes.c,8 :: 		TRISA = 0b00000010; // port A en sortie sauf RA1
	MOVLW      2
	MOVWF      TRISA+0
;selections_modes.c,9 :: 		PORTA = 0b11001000 ; // mettre les sorties ? z?ro sauf RA6, RA7,RA3
	MOVLW      200
	MOVWF      PORTA+0
;selections_modes.c,10 :: 		TRISB = 0b00000001; // Port B en sortie sauf RB_0
	MOVLW      1
	MOVWF      TRISB+0
;selections_modes.c,11 :: 		PORTB = 0 ; // mettre les sorties ? zéro
	CLRF       PORTB+0
;selections_modes.c,12 :: 		pcon.OSCF = 1; // configure le bit 3 du registre pcon pour 4 mhz
	BSF        PCON+0, 3
;selections_modes.c,13 :: 		CMCON = 0b00000111; // désactiver les comparateurs sur RA0
	MOVLW      7
	MOVWF      CMCON+0
;selections_modes.c,14 :: 		while (1){
L_main0:
;selections_modes.c,15 :: 		int mode =0;
	CLRF       main_mode_L1+0
	CLRF       main_mode_L1+1
;selections_modes.c,16 :: 		if(RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main2
;selections_modes.c,17 :: 		tut();
	CALL       _tut+0
;selections_modes.c,18 :: 		RA6_bit=1;
	BSF        RA6_bit+0, BitPos(RA6_bit+0)
;selections_modes.c,19 :: 		RA7_bit=1;
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;selections_modes.c,20 :: 		RA3_bit=0;
	BCF        RA3_bit+0, BitPos(RA3_bit+0)
;selections_modes.c,21 :: 		mode =1;
	MOVLW      1
	MOVWF      main_mode_L1+0
	MOVLW      0
	MOVWF      main_mode_L1+1
;selections_modes.c,22 :: 		delay_ms(250);
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
;selections_modes.c,23 :: 		if(RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main4
;selections_modes.c,24 :: 		RA3_bit=1;
	BSF        RA3_bit+0, BitPos(RA3_bit+0)
;selections_modes.c,25 :: 		RA7_bit=1;
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;selections_modes.c,26 :: 		RA6_bit=0;
	BCF        RA6_bit+0, BitPos(RA6_bit+0)
;selections_modes.c,27 :: 		mode=2;
	MOVLW      2
	MOVWF      main_mode_L1+0
	MOVLW      0
	MOVWF      main_mode_L1+1
;selections_modes.c,28 :: 		delay_ms(750);
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
;selections_modes.c,29 :: 		if (RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main6
;selections_modes.c,30 :: 		RA3_bit=1;
	BSF        RA3_bit+0, BitPos(RA3_bit+0)
;selections_modes.c,31 :: 		RA6_bit=1;
	BSF        RA6_bit+0, BitPos(RA6_bit+0)
;selections_modes.c,32 :: 		RA7_bit=0;
	BCF        RA7_bit+0, BitPos(RA7_bit+0)
;selections_modes.c,33 :: 		mode=3;
	MOVLW      3
	MOVWF      main_mode_L1+0
	MOVLW      0
	MOVWF      main_mode_L1+1
;selections_modes.c,34 :: 		delay_ms(500);
	MOVLW      3
	MOVWF      R11+0
	MOVLW      138
	MOVWF      R12+0
	MOVLW      85
	MOVWF      R13+0
L_main7:
	DECFSZ     R13+0, 1
	GOTO       L_main7
	DECFSZ     R12+0, 1
	GOTO       L_main7
	DECFSZ     R11+0, 1
	GOTO       L_main7
	NOP
	NOP
;selections_modes.c,35 :: 		if (RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_main8
;selections_modes.c,36 :: 		RA7_bit=1;
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;selections_modes.c,37 :: 		}
L_main8:
;selections_modes.c,39 :: 		}
L_main6:
;selections_modes.c,41 :: 		}
L_main4:
;selections_modes.c,42 :: 		}
L_main2:
;selections_modes.c,43 :: 		if (mode==1){
	MOVLW      0
	XORWF      main_mode_L1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main39
	MOVLW      1
	XORWF      main_mode_L1+0, 0
L__main39:
	BTFSS      STATUS+0, 2
	GOTO       L_main9
;selections_modes.c,44 :: 		pas_a_pas();
	CALL       _pas_a_pas+0
;selections_modes.c,45 :: 		}
	GOTO       L_main10
L_main9:
;selections_modes.c,46 :: 		else if(mode==2){
	MOVLW      0
	XORWF      main_mode_L1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main40
	MOVLW      2
	XORWF      main_mode_L1+0, 0
L__main40:
	BTFSS      STATUS+0, 2
	GOTO       L_main11
;selections_modes.c,47 :: 		sequence();
	CALL       _sequence+0
;selections_modes.c,48 :: 		}
	GOTO       L_main12
L_main11:
;selections_modes.c,49 :: 		else if (mode==3){
	MOVLW      0
	XORWF      main_mode_L1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main41
	MOVLW      3
	XORWF      main_mode_L1+0, 0
L__main41:
	BTFSS      STATUS+0, 2
	GOTO       L_main13
;selections_modes.c,50 :: 		continu();
	CALL       _continu+0
;selections_modes.c,51 :: 		}
L_main13:
L_main12:
L_main10:
;selections_modes.c,52 :: 		}
	GOTO       L_main0
;selections_modes.c,53 :: 		}
L_end_main:
	GOTO       $+0
; end of _main

_pas_a_pas:

;selections_modes.c,54 :: 		void pas_a_pas(){
;selections_modes.c,55 :: 		if (sortie==0){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas43
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas43:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas14
;selections_modes.c,56 :: 		RA0_bit = 1;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,57 :: 		sortie=1;
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;selections_modes.c,58 :: 		}
	GOTO       L_pas_a_pas15
L_pas_a_pas14:
;selections_modes.c,59 :: 		else if (sortie==256){
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas44
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas44:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas16
;selections_modes.c,60 :: 		sortie=0;
	CLRF       _sortie+0
	CLRF       _sortie+1
;selections_modes.c,61 :: 		PORTB = sortie;
	CLRF       PORTB+0
;selections_modes.c,62 :: 		}
	GOTO       L_pas_a_pas17
L_pas_a_pas16:
;selections_modes.c,64 :: 		if (sortie==1){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas45
	MOVLW      1
	XORWF      _sortie+0, 0
L__pas_a_pas45:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas18
;selections_modes.c,65 :: 		RA0_bit =0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,66 :: 		sortie*=2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;selections_modes.c,67 :: 		}
L_pas_a_pas18:
;selections_modes.c,68 :: 		PORTB = sortie;
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;selections_modes.c,69 :: 		sortie=sortie*2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;selections_modes.c,70 :: 		}
L_pas_a_pas17:
L_pas_a_pas15:
;selections_modes.c,71 :: 		}
L_end_pas_a_pas:
	RETURN
; end of _pas_a_pas

_sequence:

;selections_modes.c,73 :: 		void sequence(){
;selections_modes.c,74 :: 		while(1){
L_sequence19:
;selections_modes.c,75 :: 		if (sortie==1){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__sequence47
	MOVLW      1
	XORWF      _sortie+0, 0
L__sequence47:
	BTFSS      STATUS+0, 2
	GOTO       L_sequence21
;selections_modes.c,76 :: 		RA0_bit=1;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,77 :: 		delay_ms(250);
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
;selections_modes.c,78 :: 		RA0_bit=0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,79 :: 		sortie *= 2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;selections_modes.c,80 :: 		}
	GOTO       L_sequence23
L_sequence21:
;selections_modes.c,81 :: 		else if(sortie==256){
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__sequence48
	MOVLW      0
	XORWF      _sortie+0, 0
L__sequence48:
	BTFSS      STATUS+0, 2
	GOTO       L_sequence24
;selections_modes.c,82 :: 		sortie=0;
	CLRF       _sortie+0
	CLRF       _sortie+1
;selections_modes.c,83 :: 		PORTB=sortie;
	CLRF       PORTB+0
;selections_modes.c,84 :: 		sortie=1;
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;selections_modes.c,85 :: 		}
	GOTO       L_sequence25
L_sequence24:
;selections_modes.c,87 :: 		PORTB = sortie;
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;selections_modes.c,88 :: 		sortie *= 2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;selections_modes.c,89 :: 		delay_ms(250);
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
;selections_modes.c,90 :: 		}
L_sequence25:
L_sequence23:
;selections_modes.c,91 :: 		if (RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_sequence27
;selections_modes.c,92 :: 		break;
	GOTO       L_sequence20
;selections_modes.c,93 :: 		}
L_sequence27:
;selections_modes.c,94 :: 		}
	GOTO       L_sequence19
L_sequence20:
;selections_modes.c,95 :: 		}
L_end_sequence:
	RETURN
; end of _sequence

_continu:

;selections_modes.c,96 :: 		void continu(){
;selections_modes.c,97 :: 		while(1){
L_continu28:
;selections_modes.c,98 :: 		if (sortie==1){
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__continu50
	MOVLW      1
	XORWF      _sortie+0, 0
L__continu50:
	BTFSS      STATUS+0, 2
	GOTO       L_continu30
;selections_modes.c,99 :: 		RA0_bit=1;
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,100 :: 		delay_ms(1);
	MOVLW      2
	MOVWF      R12+0
	MOVLW      75
	MOVWF      R13+0
L_continu31:
	DECFSZ     R13+0, 1
	GOTO       L_continu31
	DECFSZ     R12+0, 1
	GOTO       L_continu31
;selections_modes.c,101 :: 		RA0_bit=0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,102 :: 		sortie *= 2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;selections_modes.c,103 :: 		}
	GOTO       L_continu32
L_continu30:
;selections_modes.c,104 :: 		else if(sortie==256){
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__continu51
	MOVLW      0
	XORWF      _sortie+0, 0
L__continu51:
	BTFSS      STATUS+0, 2
	GOTO       L_continu33
;selections_modes.c,105 :: 		sortie=0;
	CLRF       _sortie+0
	CLRF       _sortie+1
;selections_modes.c,106 :: 		PORTB=sortie;
	CLRF       PORTB+0
;selections_modes.c,107 :: 		sortie=1;
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;selections_modes.c,108 :: 		}
	GOTO       L_continu34
L_continu33:
;selections_modes.c,110 :: 		PORTB = sortie;
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;selections_modes.c,111 :: 		sortie *= 2;
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;selections_modes.c,112 :: 		delay_ms(1);
	MOVLW      2
	MOVWF      R12+0
	MOVLW      75
	MOVWF      R13+0
L_continu35:
	DECFSZ     R13+0, 1
	GOTO       L_continu35
	DECFSZ     R12+0, 1
	GOTO       L_continu35
;selections_modes.c,113 :: 		}
L_continu34:
L_continu32:
;selections_modes.c,114 :: 		if (RB0_bit==0){
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_continu36
;selections_modes.c,115 :: 		break;
	GOTO       L_continu29
;selections_modes.c,116 :: 		}
L_continu36:
;selections_modes.c,117 :: 		}
	GOTO       L_continu28
L_continu29:
;selections_modes.c,118 :: 		}
L_end_continu:
	RETURN
; end of _continu

_eteindre:

;selections_modes.c,119 :: 		void eteindre(){
;selections_modes.c,120 :: 		PORTB=0;
	CLRF       PORTB+0
;selections_modes.c,121 :: 		RA0_bit=0;
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;selections_modes.c,123 :: 		}
L_end_eteindre:
	RETURN
; end of _eteindre

_tut:

;selections_modes.c,124 :: 		void tut(){
;selections_modes.c,125 :: 		RA2_bit=1;
	BSF        RA2_bit+0, BitPos(RA2_bit+0)
;selections_modes.c,126 :: 		delay_ms(500);
	MOVLW      3
	MOVWF      R11+0
	MOVLW      138
	MOVWF      R12+0
	MOVLW      85
	MOVWF      R13+0
L_tut37:
	DECFSZ     R13+0, 1
	GOTO       L_tut37
	DECFSZ     R12+0, 1
	GOTO       L_tut37
	DECFSZ     R11+0, 1
	GOTO       L_tut37
	NOP
	NOP
;selections_modes.c,127 :: 		RA2_bit=0;
	BCF        RA2_bit+0, BitPos(RA2_bit+0)
;selections_modes.c,128 :: 		}
L_end_tut:
	RETURN
; end of _tut
