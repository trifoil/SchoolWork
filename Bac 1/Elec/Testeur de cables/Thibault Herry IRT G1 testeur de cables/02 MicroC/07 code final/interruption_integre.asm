
_main:

;interruption_integre.c,10 :: 		main() {
;interruption_integre.c,11 :: 		TRISA = 0b00000010; // Configuration du port A en sortie, sauf RA1
	MOVLW      2
	MOVWF      TRISA+0
;interruption_integre.c,12 :: 		PORTA = 0b11001000; // Mettre les sorties à zéro sauf RA6, RA7, RA3
	MOVLW      200
	MOVWF      PORTA+0
;interruption_integre.c,13 :: 		TRISB = 0b00000001; // Configuration du port B en sortie, sauf RB0
	MOVLW      1
	MOVWF      TRISB+0
;interruption_integre.c,14 :: 		PORTB = 0; // Mettre les sorties à zéro
	CLRF       PORTB+0
;interruption_integre.c,15 :: 		pcon.OSCF = 1; // Configuration du bit 3 du registre pcon pour une fréquence de 4 MHz (probablement une faute de frappe, devrait être "PCON.OSCF")
	BSF        PCON+0, 3
;interruption_integre.c,16 :: 		CMCON = 0b00000111; // Désactiver les comparateurs sur RA0
	MOVLW      7
	MOVWF      CMCON+0
;interruption_integre.c,17 :: 		INTCON = 0b10010000; // Configuration des registres d'interruption externe (INTCON)
	MOVLW      144
	MOVWF      INTCON+0
;interruption_integre.c,18 :: 		OPTION_REG = 0b00000000; // Configuration des options d'interruption (OPTION_REG)
	CLRF       OPTION_REG+0
;interruption_integre.c,20 :: 		while(1) {} // Boucle infinie pour maintenir le programme en cours d'exécution
L_main0:
	GOTO       L_main0
;interruption_integre.c,21 :: 		}
L_end_main:
	GOTO       $+0
; end of _main

_interrupt:
	MOVWF      R15+0
	SWAPF      STATUS+0, 0
	CLRF       STATUS+0
	MOVWF      ___saveSTATUS+0
	MOVF       PCLATH+0, 0
	MOVWF      ___savePCLATH+0
	CLRF       PCLATH+0

;interruption_integre.c,23 :: 		void interrupt() {
;interruption_integre.c,24 :: 		int mode = 0; // Variable pour stocker le mode
	CLRF       interrupt_mode_L0+0
	CLRF       interrupt_mode_L0+1
;interruption_integre.c,26 :: 		if (RB0_bit == 0) { // Vérifie si la broche RB0 est à 0
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_interrupt2
;interruption_integre.c,27 :: 		tut(); // Appelle la fonction tut()
	CALL       _tut+0
;interruption_integre.c,28 :: 		RA6_bit = 1; // Active la broche RA6
	BSF        RA6_bit+0, BitPos(RA6_bit+0)
;interruption_integre.c,29 :: 		RA7_bit = 1; // Active la broche RA7
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;interruption_integre.c,30 :: 		RA3_bit = 0; // Désactive la broche RA3
	BCF        RA3_bit+0, BitPos(RA3_bit+0)
;interruption_integre.c,31 :: 		mode = 1; // Affecte le mode 1 à la variable mode
	MOVLW      1
	MOVWF      interrupt_mode_L0+0
	MOVLW      0
	MOVWF      interrupt_mode_L0+1
;interruption_integre.c,32 :: 		delay_ms(250); // Attend pendant 250 ms
	MOVLW      2
	MOVWF      R11+0
	MOVLW      69
	MOVWF      R12+0
	MOVLW      169
	MOVWF      R13+0
L_interrupt3:
	DECFSZ     R13+0, 1
	GOTO       L_interrupt3
	DECFSZ     R12+0, 1
	GOTO       L_interrupt3
	DECFSZ     R11+0, 1
	GOTO       L_interrupt3
	NOP
	NOP
;interruption_integre.c,34 :: 		if (RB0_bit == 0) { // Vérifie à nouveau si la broche RB0 est à 0
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_interrupt4
;interruption_integre.c,35 :: 		RA3_bit = 1; // Active la broche RA3
	BSF        RA3_bit+0, BitPos(RA3_bit+0)
;interruption_integre.c,36 :: 		RA7_bit = 1; // Active la broche RA7
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;interruption_integre.c,37 :: 		RA6_bit = 0; // Désactive la broche RA6
	BCF        RA6_bit+0, BitPos(RA6_bit+0)
;interruption_integre.c,38 :: 		mode = 2; // Affecte le mode 2 à la variable mode
	MOVLW      2
	MOVWF      interrupt_mode_L0+0
	MOVLW      0
	MOVWF      interrupt_mode_L0+1
;interruption_integre.c,39 :: 		delay_ms(750); // Attend pendant 750 ms
	MOVLW      4
	MOVWF      R11+0
	MOVLW      207
	MOVWF      R12+0
	MOVLW      1
	MOVWF      R13+0
L_interrupt5:
	DECFSZ     R13+0, 1
	GOTO       L_interrupt5
	DECFSZ     R12+0, 1
	GOTO       L_interrupt5
	DECFSZ     R11+0, 1
	GOTO       L_interrupt5
	NOP
	NOP
;interruption_integre.c,41 :: 		if (RB0_bit == 0) { // Vérifie à nouveau si la broche RB0 est à 0
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_interrupt6
;interruption_integre.c,42 :: 		RA3_bit = 1; // Active la broche RA3
	BSF        RA3_bit+0, BitPos(RA3_bit+0)
;interruption_integre.c,43 :: 		RA6_bit = 1; // Active la broche RA6
	BSF        RA6_bit+0, BitPos(RA6_bit+0)
;interruption_integre.c,44 :: 		RA7_bit = 0; // Désactive la broche RA7
	BCF        RA7_bit+0, BitPos(RA7_bit+0)
;interruption_integre.c,45 :: 		mode = 3; // Affecte le mode 3 à la variable mode
	MOVLW      3
	MOVWF      interrupt_mode_L0+0
	MOVLW      0
	MOVWF      interrupt_mode_L0+1
;interruption_integre.c,46 :: 		delay_ms(500); // Attend pendant 500 ms
	MOVLW      3
	MOVWF      R11+0
	MOVLW      138
	MOVWF      R12+0
	MOVLW      85
	MOVWF      R13+0
L_interrupt7:
	DECFSZ     R13+0, 1
	GOTO       L_interrupt7
	DECFSZ     R12+0, 1
	GOTO       L_interrupt7
	DECFSZ     R11+0, 1
	GOTO       L_interrupt7
	NOP
	NOP
;interruption_integre.c,48 :: 		if (RB0_bit == 0) { // Vérifie à nouveau si la broche RB0 est à 0
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_interrupt8
;interruption_integre.c,49 :: 		RA7_bit = 1; // Active la broche RA7
	BSF        RA7_bit+0, BitPos(RA7_bit+0)
;interruption_integre.c,50 :: 		}
L_interrupt8:
;interruption_integre.c,51 :: 		}
L_interrupt6:
;interruption_integre.c,52 :: 		}
L_interrupt4:
;interruption_integre.c,53 :: 		}
L_interrupt2:
;interruption_integre.c,57 :: 		if (mode == 1) {
	MOVLW      0
	XORWF      interrupt_mode_L0+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__interrupt41
	MOVLW      1
	XORWF      interrupt_mode_L0+0, 0
L__interrupt41:
	BTFSS      STATUS+0, 2
	GOTO       L_interrupt9
;interruption_integre.c,58 :: 		pas_a_pas(); // Appelle la fonction pas_a_pas()
	CALL       _pas_a_pas+0
;interruption_integre.c,59 :: 		} else if (mode == 2) {
	GOTO       L_interrupt10
L_interrupt9:
	MOVLW      0
	XORWF      interrupt_mode_L0+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__interrupt42
	MOVLW      2
	XORWF      interrupt_mode_L0+0, 0
L__interrupt42:
	BTFSS      STATUS+0, 2
	GOTO       L_interrupt11
;interruption_integre.c,60 :: 		sequence(); // Appelle la fonction sequence()
	CALL       _sequence+0
;interruption_integre.c,61 :: 		} else if (mode == 3) {
	GOTO       L_interrupt12
L_interrupt11:
	MOVLW      0
	XORWF      interrupt_mode_L0+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__interrupt43
	MOVLW      3
	XORWF      interrupt_mode_L0+0, 0
L__interrupt43:
	BTFSS      STATUS+0, 2
	GOTO       L_interrupt13
;interruption_integre.c,62 :: 		continu(); // Appelle la fonction continu()
	CALL       _continu+0
;interruption_integre.c,63 :: 		}
L_interrupt13:
L_interrupt12:
L_interrupt10:
;interruption_integre.c,64 :: 		}
L_end_interrupt:
L__interrupt40:
	MOVF       ___savePCLATH+0, 0
	MOVWF      PCLATH+0
	SWAPF      ___saveSTATUS+0, 0
	MOVWF      STATUS+0
	SWAPF      R15+0, 1
	SWAPF      R15+0, 0
	RETFIE
; end of _interrupt

_pas_a_pas:

;interruption_integre.c,66 :: 		void pas_a_pas() {
;interruption_integre.c,67 :: 		if (sortie == 0) {  // Si la variable sortie est égale à 0
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas45
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas45:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas14
;interruption_integre.c,68 :: 		RA0_bit = 1;  // Active la broche RA0
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,69 :: 		sortie = 1;  // Met à jour la variable sortie
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;interruption_integre.c,70 :: 		} else if (sortie == 256) {  // Si la variable sortie est égale à 256
	GOTO       L_pas_a_pas15
L_pas_a_pas14:
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas46
	MOVLW      0
	XORWF      _sortie+0, 0
L__pas_a_pas46:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas16
;interruption_integre.c,71 :: 		sortie = 0;  // Remet la variable sortie à 0
	CLRF       _sortie+0
	CLRF       _sortie+1
;interruption_integre.c,72 :: 		PORTB = sortie;  // Met à jour la valeur du port B avec sortie
	CLRF       PORTB+0
;interruption_integre.c,73 :: 		} else {  // Sinon
	GOTO       L_pas_a_pas17
L_pas_a_pas16:
;interruption_integre.c,74 :: 		if (sortie == 1) {  // Si la variable sortie est égale à 1
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__pas_a_pas47
	MOVLW      1
	XORWF      _sortie+0, 0
L__pas_a_pas47:
	BTFSS      STATUS+0, 2
	GOTO       L_pas_a_pas18
;interruption_integre.c,75 :: 		RA0_bit = 0;  // Désactive la broche RA0
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,76 :: 		sortie *= 2;  // Double la valeur de sortie
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;interruption_integre.c,77 :: 		}
L_pas_a_pas18:
;interruption_integre.c,78 :: 		PORTB = sortie;  // Met à jour la valeur du port B avec sortie
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;interruption_integre.c,79 :: 		sortie = sortie * 2;  // Double la valeur de sortie
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;interruption_integre.c,80 :: 		}
L_pas_a_pas17:
L_pas_a_pas15:
;interruption_integre.c,81 :: 		}
L_end_pas_a_pas:
	RETURN
; end of _pas_a_pas

_sequence:

;interruption_integre.c,83 :: 		void sequence() {
;interruption_integre.c,84 :: 		while (1) {  // Boucle infinie
L_sequence19:
;interruption_integre.c,85 :: 		if (sortie == 1) {  // Si la variable sortie est égale à 1
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__sequence49
	MOVLW      1
	XORWF      _sortie+0, 0
L__sequence49:
	BTFSS      STATUS+0, 2
	GOTO       L_sequence21
;interruption_integre.c,86 :: 		RA0_bit = 1;  // Active la broche RA0
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,87 :: 		delay_ms(250);  // Attend pendant 250 ms
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
;interruption_integre.c,88 :: 		RA0_bit = 0;  // Désactive la broche RA0
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,89 :: 		sortie *= 2;  // Double la valeur de sortie
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;interruption_integre.c,90 :: 		} else if (sortie == 256) {  // Si la variable sortie est égale à 256
	GOTO       L_sequence23
L_sequence21:
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__sequence50
	MOVLW      0
	XORWF      _sortie+0, 0
L__sequence50:
	BTFSS      STATUS+0, 2
	GOTO       L_sequence24
;interruption_integre.c,91 :: 		sortie = 0;  // Remet la variable sortie à 0
	CLRF       _sortie+0
	CLRF       _sortie+1
;interruption_integre.c,92 :: 		PORTB = sortie;  // Met à jour la valeur du port B avec sortie
	CLRF       PORTB+0
;interruption_integre.c,93 :: 		sortie = 1;  // Met à jour la variable sortie à 1
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;interruption_integre.c,94 :: 		} else {  // Sinon
	GOTO       L_sequence25
L_sequence24:
;interruption_integre.c,95 :: 		PORTB = sortie;  // Met à jour la valeur du port B avec sortie
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;interruption_integre.c,96 :: 		sortie *= 2;  // Double la valeur de sortie
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;interruption_integre.c,97 :: 		delay_ms(250);  // Attend pendant 250 ms
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
;interruption_integre.c,98 :: 		}
L_sequence25:
L_sequence23:
;interruption_integre.c,100 :: 		if (RB0_bit == 0) {  // Si la broche RB0 est à 0
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_sequence27
;interruption_integre.c,101 :: 		break;  // Sort de la boucle while
	GOTO       L_sequence20
;interruption_integre.c,102 :: 		}
L_sequence27:
;interruption_integre.c,103 :: 		}
	GOTO       L_sequence19
L_sequence20:
;interruption_integre.c,104 :: 		}
L_end_sequence:
	RETURN
; end of _sequence

_continu:

;interruption_integre.c,105 :: 		void continu() {
;interruption_integre.c,106 :: 		while (1) {  // Boucle infinie
L_continu28:
;interruption_integre.c,107 :: 		if (sortie == 1) {  // Si la variable sortie est égale à 1
	MOVLW      0
	XORWF      _sortie+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__continu52
	MOVLW      1
	XORWF      _sortie+0, 0
L__continu52:
	BTFSS      STATUS+0, 2
	GOTO       L_continu30
;interruption_integre.c,108 :: 		RA0_bit = 1;  // Active la broche RA0
	BSF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,109 :: 		delay_ms(1);  // Attend pendant 1 ms
	MOVLW      2
	MOVWF      R12+0
	MOVLW      75
	MOVWF      R13+0
L_continu31:
	DECFSZ     R13+0, 1
	GOTO       L_continu31
	DECFSZ     R12+0, 1
	GOTO       L_continu31
;interruption_integre.c,110 :: 		RA0_bit = 0;  // Désactive la broche RA0
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,111 :: 		sortie *= 2;  // Double la valeur de sortie
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;interruption_integre.c,112 :: 		} else if (sortie == 256) {  // Si la variable sortie est égale à 256
	GOTO       L_continu32
L_continu30:
	MOVF       _sortie+1, 0
	XORLW      1
	BTFSS      STATUS+0, 2
	GOTO       L__continu53
	MOVLW      0
	XORWF      _sortie+0, 0
L__continu53:
	BTFSS      STATUS+0, 2
	GOTO       L_continu33
;interruption_integre.c,113 :: 		sortie = 0;  // Remet la variable sortie à 0
	CLRF       _sortie+0
	CLRF       _sortie+1
;interruption_integre.c,114 :: 		PORTB = sortie;  // Met à jour la valeur du port B avec sortie
	CLRF       PORTB+0
;interruption_integre.c,115 :: 		sortie = 1;  // Met à jour la variable sortie à 1
	MOVLW      1
	MOVWF      _sortie+0
	MOVLW      0
	MOVWF      _sortie+1
;interruption_integre.c,116 :: 		} else {  // Sinon
	GOTO       L_continu34
L_continu33:
;interruption_integre.c,117 :: 		PORTB = sortie;  // Met à jour la valeur du port B avec sortie
	MOVF       _sortie+0, 0
	MOVWF      PORTB+0
;interruption_integre.c,118 :: 		sortie *= 2;  // Double la valeur de sortie
	RLF        _sortie+0, 1
	RLF        _sortie+1, 1
	BCF        _sortie+0, 0
;interruption_integre.c,119 :: 		delay_ms(1);  // Attend pendant 1 ms
	MOVLW      2
	MOVWF      R12+0
	MOVLW      75
	MOVWF      R13+0
L_continu35:
	DECFSZ     R13+0, 1
	GOTO       L_continu35
	DECFSZ     R12+0, 1
	GOTO       L_continu35
;interruption_integre.c,120 :: 		}
L_continu34:
L_continu32:
;interruption_integre.c,122 :: 		if (RB0_bit == 0) {  // Si la broche RB0 est à 0
	BTFSC      RB0_bit+0, BitPos(RB0_bit+0)
	GOTO       L_continu36
;interruption_integre.c,123 :: 		break;  // Sort de la boucle while
	GOTO       L_continu29
;interruption_integre.c,124 :: 		}
L_continu36:
;interruption_integre.c,125 :: 		}
	GOTO       L_continu28
L_continu29:
;interruption_integre.c,126 :: 		}
L_end_continu:
	RETURN
; end of _continu

_eteindre:

;interruption_integre.c,128 :: 		void eteindre() {
;interruption_integre.c,129 :: 		PORTB = 0;  // Éteint toutes les broches du port B
	CLRF       PORTB+0
;interruption_integre.c,130 :: 		RA0_bit = 0;  // Désactive la broche RA0
	BCF        RA0_bit+0, BitPos(RA0_bit+0)
;interruption_integre.c,131 :: 		}
L_end_eteindre:
	RETURN
; end of _eteindre

_tut:

;interruption_integre.c,133 :: 		void tut() {
;interruption_integre.c,134 :: 		RA2_bit = 1;  // Active la broche RA2
	BSF        RA2_bit+0, BitPos(RA2_bit+0)
;interruption_integre.c,135 :: 		delay_ms(500);  // Attend pendant 500 ms
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
;interruption_integre.c,136 :: 		RA2_bit = 0;  // Désactive la broche RA2
	BCF        RA2_bit+0, BitPos(RA2_bit+0)
;interruption_integre.c,137 :: 		}
L_end_tut:
	RETURN
; end of _tut
