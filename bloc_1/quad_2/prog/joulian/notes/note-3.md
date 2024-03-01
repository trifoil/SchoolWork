# Prise de note - prog - N{xx}

## Classes

### Constructeur
- On initialise les attributs dedans le constructeur !
#### Types
    - par defaut (aucun arguments)
    - de recopie (un seul argument, une instance de meme classe)

### Relations entre classes
    - Association (une classe utilise une autre, mais pas de dependance)
    - Composition-Composition (une classe en compose une autre, le composant est dependant de la classe d'origine)
    - Composition-Aggregation (une classe en compose une autre, le composant n'est pas dependant de la classe d'origine)
    - Heritage (Classe mere/fille)

### Polymorphisme

- Des classes differentes qui on des methodes en commun mais qui font pas exactement la meme chose.

### surcharge-redefinition
    - Overloading (surcharge): reecrire dans une **classe** une methode qui a le meme nom mais **pas les meme parametres**

    - Overriding (redefinition): reecire dans une **classe herite** une methode avec **les meme parametres** (terme exact: Meme signature)

### Heritage d'implementation
    - Une classe fille herite des methodes/attributs d'une classe mere
    - extends

### Heritage d'Interface
    - Lien entre une classe mere et une classe fille
    - Une interface, definit ce qu'une classe doit avoir (methode/attribus)

## Classes en python

### Cree une abstract method

- on importe ABC et abstractmethod depuis abc
- on dit que notre classe depend de ABC
- on met @abstractmethod devant la methode abstraite

```py
from abc import ABC, abstractmethod

class nom_classe(ABC)

    @abstractmethod
    def abstract_method_name():
        ...code
```

## exos

### Super Hero

- Classe SuperHeros > Mutant,Humain,Metahumain,NonHumain

```typescript
class SuperHero {
    charisme: int,
    strenght: int,
    speed: int,
    surnom: string,
    alies: SuperHero[],
    void sauter(),
    void sauverLeMonde(),
    void FaireSemblantDeCeBattreCarCEstMieuxPourLaCameraQuandMemeWsh(),
    void addAlie(alie: SuperHero),
}

class Mutant implements SuperHero {
    pouvoir: string,
    void utiliserPouvoir()
}

class Humain implements SuperHero {
    argent: int,
    void utiliserArgent()
}

class MetaHumain implements SuperHero {
    tauxMutation: int,
    typeMutation: string,
    void seTransformer()
}

class NonHumain implements SuperHero {
    race: string,
    couleurPeau: string,
    void utiliserCapaciteNonHumai()
}
```

##2

## Notice

> Ces notes ne sont pas forcement correctes (voir syntheses).