"""
    Implémentation d'un arbre binaire de recherche

    Auteur : Philippe Schlegel
"""

from enum import Enum


"""
    Enumération qui témoigne du type de noeud, utilisé pour l'affichage de l'arbre
"""

class Type_noeud(Enum):
    RACINE = 1
    FILS_GAUCHE = 2
    FILS_DROIT = 3

"""
    Structure d'un noeud de l'arbre, lors de la création, un noeud n'a ni fils et ni père
"""

class Noeud:
    def __init__(self, valeur):
        self.gauche = None
        self.droit = None
        self.valeur = valeur
        self.pere = None

"""
    Structure d'un arbre binaire de recherche, un arbre pointe vers un noeud racine
"""

class Arbre:

    """
        Constructeur : Création d'un arbre sans aucun élément
    """

    def __init__(self):
        self.racine = None

    """
        Fonctions qui permettent l'affichage de l'arbre, très utile pour débugguer
    """

    def afficher(self):
        self.__afficher_helper(self.racine, "", Type_noeud.RACINE)

    def __afficher_helper(self, n, indent, typeNoeud):
        if n != None:
            print(indent,end='')
            if typeNoeud == Type_noeud.FILS_DROIT:
                print("D----",end='')
                indent += "     "
            elif typeNoeud == Type_noeud.RACINE:
                print("R----",end='')
                indent += "|    "
            else:
                print("G----",end='')
                indent += "|    "

            print('(' + str(n.valeur) + ')')
            self.__afficher_helper(n.gauche, indent, Type_noeud.FILS_GAUCHE)
            self.__afficher_helper(n.droit, indent, Type_noeud.FILS_DROIT)


    """
        Recherche d'un élément dans l'arbre, la fonction renvoie :
        - Un Noeud si l'élément est trouvé
        - None sinon
    """

    def recherche(self, v):
        cur = self.racine
        while cur != None and cur.valeur != v: 
            if v < cur.valeur:
                cur = cur.gauche
            elif v > cur.valeur:
                cur = cur.droit
        return cur
   
    """
        Fonctions de recherche de minimum et de maximum de l'arbre
        Les deux fonctions renvoient directement un Noeud
    """

    def minimum(self):
        return self.__minimum_helper(self.racine)

    def __minimum_helper(self, n):
        while n.gauche != None:
            n = n.gauche
        return n
        
    def maximum(self):
        return self.__maximum_helper(self.racine)

    def __maximum_helper(self, n):
        while n.droit != None:
            n = n.droit
        return n

    """
        Fonctions qui permettent de trouver le successeur ou le predecesseur direct d'une valeur
        Ces fonctions sont utilisées dans la fonction de suppression
    """

    def successeur(self, n):
        if n.droit != None:
            return self.__minimum_helper(n.droit)
        else:
            p = n.pere
            f = n
            while p != None and f == p.droit:
                f = p
                p = p.pere

            return p
            
    def predecesseur(self, n):
        if n.gauche != None:
            return self.__maximum_helper(n.gauche)
        else:
            p = n.pere
            f = n
            while p != None and f == p.gauche:
                f = p
                p = p.pere

            return p

    """
        Insertion d'un élément dans un arbre binaire de recherche
    """

    def insererVal(self, v):
        n = Noeud(v)

        # Si l'arbre est vide
        if self.racine == None:
            self.racine = n
        else:
            cur = self.racine
            insertionOK = False

            # Tant que l'insertion n'est pas faite on cherche l'emplacement idéal
            while not insertionOK:
                if v < cur.valeur:
                    if cur.gauche == None:
                        cur.gauche = n
                        n.pere = cur
                        insertionOK = True
                    else:
                        cur = cur.gauche
                else:
                    if cur.droit == None:
                        cur.droit = n
                        n.pere = cur
                        insertionOK = True
                    else:
                        cur = cur.droit
    """
        Suppression d'un élément dans l'arbre binaire de recherche. Si l'élément n'existe pas, il ne se passe rien
    """

    def supprimerVal(self, v):
        n = self.recherche(v)
        if n != None:
            self.supprimer(n)

    def supprimer(self, n):
        if n != None:
            if n.gauche == None or n.droit == None:
                if n.gauche == None:
                    t = n.droit
                else:
                    t = n.gauche

                p = n.pere
                if p.gauche == n:
                    p.gauche = t
                else:
                    p.droit = t
                
                if t != None:
                    t.pere = p
            else:
                s = self.successeur(n)
                n.valeur = s.valeur
                self.supprimer(s)




a = Arbre()
for x in range(1, 21):
    a.insererVal(x)
a.afficher()
print(a.minimum().valeur)
print(a.maximum().valeur)


#racine.afficher()

#print(racine.recherche(10))
#print(racine.recherche(6))
#print(racine.recherche(22))

#print(racine.minimum())
#print(racine.maximum())

#print(racine.successeur())
#print(racine.gauche.droit.successeur())
#print(racine.predecesseur())
#print(racine.droit.droit.gauche.predecesseur())