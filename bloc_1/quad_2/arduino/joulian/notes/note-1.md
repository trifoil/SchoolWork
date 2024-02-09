# Prise de note - arduino - N01

## Faire clignoter la LED intégrée

```cpp
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

## Faire clignoter une LED sur un pin

```cpp
int LED = 7;

void setup() {
    pinMode(LED, OUTPUT);
}

void loop() {
    digitalWrite(LED, HIGH);
    delay(1000);
    digitalWrite(LED, LOW);
    delay(1000);
}
```

## Allumer une LED RGB en violet

```cpp
int RED = 13;
int GREEN = 12;
int BLUE = 11;
 
void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {
  analogWrite(RED, 255);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 255);
}
```

## Théorie

### Base
- La déclaration des variables se fait avant le void setup !
- `void setup()`: la première fonction qui est exécutée au lancement du programme
- `void loop()`: une fonction qui est exécutée juste après `void setup()`, elle est exécutée à l'infini

- `pinMode(PIN, OUTPUT/INPUT)` Permet de dire si un PIN est une entrée ou une sortie
- `digitalWrite(PIN, HIGH/LOW)` Envoie ou non du courant sur le PIN
- `analogWrite(PIN, 0-255)` Envoie un signal entre 0 et 255
- `analogRead(PIN, 0-1023)` Retourne comme valeur un signal analogique compris entre 0 et 1023

### Structure de base

```cpp
// importe tes modules ici

// Declare tes variables ici

void setup() {
  // pinMode ici
}

void loop() {
  // digitalWrite, analogWrite, analogRead ici
}
```

## Notice

> Ces notes ne sont pas forcement correctes (voir syntheses).