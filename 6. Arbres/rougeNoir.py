"""
    Implémentation d'un arbre auto équilibré rouge-noir

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
    A la création d'un nouveau Noeud, ce Noeud est ROUGE
"""

class Noeud:
    def __init__(self, valeur):
        self.gauche = None
        self.droit = None
        self.valeur = valeur
        self.pere = None
        self.couleur = 'ROUGE'

"""
    Structure d'un arbre rouge-noir, un arbre pointe vers un noeud racine
"""

class RougeNoir:

    """
        Constructeur : Création d'un arbre sans aucun élément
        La structure FeuilleNulle permet de créer des feuilles noires au bout de chaque branche
        Cette structure permet de revenir vers le père le cas échéant
    """

    def __init__(self):
        self.FeuilleNulle = Noeud(0)
        self.FeuilleNulle.couleur = 'NOIR'
        self.FeuilleNulle.gauche = None
        self.FeuilleNulle.droit = None
        self.racine = self.FeuilleNulle

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

            print("(" + str(n.valeur) + " - " + n.couleur + ")")
            self.__afficher_helper(n.gauche, indent, Type_noeud.FILS_GAUCHE)
            self.__afficher_helper(n.droit, indent, Type_noeud.FILS_DROIT)

    """
        Recherche d'un élément dans l'arbre, la fonction renvoie :
        - Un Noeud si l'élément est trouvé
        - FeuilleNulle sinon
    """

    def recherche(self, v):
        cur = self.racine
        while cur != self.FeuilleNulle and cur.valeur != v: 
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
        while n.gauche != self.FeuilleNulle:
            n = n.gauche
        return n
        
    def maximum(self):
        return self.__maximum_helper(self.racine)

    def __maximum_helper(self, n):
        while n.droit != self.FeuilleNulle:
            n = n.droit
        return n
    
    """
        Fonctions qui permettent de trouver le successeur ou le predecesseur direct d'une valeur
        Ces fonctions sont utilisées dans la fonction de suppression
    """

    def successeur(self, n):
        if n.droit != self.FeuilleNulle:
            return self.__minimum_helper(n.droit)
        else:
            p = n.pere
            f = n
            while p != None and f == p.droit:
                f = p
                p = p.pere

            return p
            
    def predecesseur(self, n):
        if n.gauche != self.FeuilleNulle:
            return self.__maximum_helper(n.gauche)
        else:
            p = n.pere
            f = n
            while p != None and f == p.gauche:
                f = p
                p = p.pere

            return p
        
    """
        Lors de la remise en place des propriétés d'un arbre rouge-noir nous avons besoin de faire des rotations
        
        Rotation gauche : 

             n                          n        filsD              filsD
            / \                        / \        / \               /  \
           a   filsD         --->      a  b       b  c    -->      n    c
               /  \                                               / \
               b   c                                             a   b
    """

    def rotationGauche(self, n):

        # On raccroche le fils gauche du fils droit de n en tant que fils droit de n
        filsD = n.droit
        n.droit = filsD.gauche

        if filsD.gauche != self.FeuilleNulle:
            filsD.gauche.pere = n

        # On raccroche le filsD au père de n à la position qu'occupait n
        filsD.pere = n.pere
        if n.pere == None:
            self.racine = filsD
        elif n == n.pere.gauche:
            n.pere.gauche = filsD
        else:
            n.pere.droit = filsD

        # On raccorde n et filsD dans le nouvel ordre
        filsD.gauche = n
        n.pere = filsD

    """
        Lors de la remise en place des propriétés d'un arbre rouge-noir nous avons besoin de faire des rotations
        
        Rotation droite : 

             n                          n        filsG              filsG
            / \                        / \        / \               /  \
        filsG  c         --->         b  c       a   b    -->      a    n
        /  \                                                           / \
        a   b                                                         b   c
    """

    def rotationDroite(self, n):

        # On raccroche le fils droit du fils gauche de n en tant que fils gauche de n
        filsG = n.gauche
        n.gauche = filsG.droit

        if filsG.droit != self.FeuilleNulle:
            filsG.droit.pere = n

        # On raccroche le filsD au père de n à la position qu'occupait n
        filsG.pere = n.pere
        if n.pere == None:
            self.racine = filsG
        elif n == n.pere.gauche:
            n.pere.gauche = filsG
        else:
            n.pere.droit = filsG

        # On raccorde n et filsG dans le nouvel ordre
        filsG.droit = n
        n.pere = filsG
    
    """
        Insertion d'un élément dans un arbre binaire de recherche
    """
   
    def insererVal(self, v):
        n = Noeud(v)
        n.gauche = self.FeuilleNulle
        n.droit = self.FeuilleNulle
        if self.racine == self.FeuilleNulle:
            self.racine = n
        else:
            cur = self.racine
            insertionOK = False

            while not insertionOK:
                if v < cur.valeur:
                    if cur.gauche == self.FeuilleNulle:
                        cur.gauche = n
                        n.pere = cur
                        insertionOK = True
                    else:
                        cur = cur.gauche
                else:
                    if cur.droit == self.FeuilleNulle:
                        cur.droit = n
                        n.pere = cur
                        insertionOK = True
                    else:
                        cur = cur.droit
        self.reorganisation_insertion(n)  

    """
        Réorganisation des propriétés de l'arbre après l'ajout de l'élément n
    """

    def reorganisation_insertion(self, n):
        while n != self.racine and n.pere.couleur == 'ROUGE':
            # Si le père est le fils gauche du grand père
            if n.pere == n.pere.pere.gauche:
                # Récupération du fils droit du grand père (l'oncle de n)
                filsD = n.pere.pere.droit

                # Si le père est rouge et l'oncle est rouge, alors on passe les deux en noir et on répercute le rouge sur le grand père
                # On traite le grand père au tour d'après
                if filsD.couleur == 'ROUGE':
                    n.pere.couleur = 'NOIR'
                    filsD.couleur = 'NOIR'
                    n.pere.pere.couleur = 'ROUGE'
                    n = n.pere.pere

                # n a un père rouge et un oncle noir, il va falloir rééquilibre l'arbre
                else:
                    # Si n est le fils droit de son père on passe sur le père et on effectue une rotation à gauche (le fils droit de n devient le père de n)
                    if n == n.pere.droit:
                        n = n.pere
                        self.rotationGauche(n)

                    # On passe le père en couleur noir et le grand père en couleur rouge puis on effectue une rotation droite sur le grand père (le fils gauche du grand père devient le père du grand père)
                    n.pere.couleur = 'NOIR'
                    n.pere.pere.couleur = 'ROUGE'
                    self.rotationDroite(n.pere.pere)

            # Si le père est le fils droit du grand père
            else:
                # Récupération du fils gauche du grand père (l'oncle de n)
                filsG = n.pere.pere.gauche

                # Si le père est rouge et l'oncle est rouge, alors on passe les deux en noir et on répercute le rouge sur le grand père
                # On traite le grand père au tour d'après     
                if filsG.couleur == 'ROUGE':
                    n.pere.couleur = 'NOIR'
                    filsG.couleur = 'NOIR'
                    n.pere.pere.couleur = 'ROUGE'
                    n = n.pere.pere
                # n a un père rouge et un oncle noir, il va falloir rééquilibre l'arbre
                else:
                    # Si n est le fils gauche de son père on passe sur le père et on effectue une rotation à droite (le fils gauche de n devient le père de n)
                    if n == n.pere.gauche:
                        n = n.pere
                        self.rotationDroite(n)

                    # On passe le père en couleur noir et le grand père en couleur rouge puis on effectue une rotation gauche sur le grand père (le fils droit du grand père devient le père du grand père)
                    n.pere.couleur = 'NOIR'
                    n.pere.pere.couleur = 'ROUGE'
                    self.rotationGauche(n.pere.pere)

        # Pour avoir un arbre rouge-noir valide il faut une racone noire  
        self.racine.couleur = 'NOIR'

    """
        Suppression d'un élément dans l'arbre rouge-noir. Si l'élément n'existe pas, il ne se passe rien
    """

    def supprimerVal(self, v):
        n = self.recherche(v)
        if n != self.FeuilleNulle:
            self.supprimer(n)

    def supprimer(self, n):
        if n != self.FeuilleNulle:
            if n.gauche == self.FeuilleNulle or n.droit == self.FeuilleNulle:
                if n.gauche == self.FeuilleNulle:
                    t = n.droit
                else:
                    t = n.gauche

                p = n.pere
                if p.gauche == n:
                    p.gauche = t
                else:
                    p.droit = t

                t.pere = p

                if n.couleur == 'NOIR':
                    self.reorganisation_suppression(t)
            else:
                s = self.successeur(n)
                n.valeur = s.valeur
                self.supprimer(s)

    """
        Réorganisation des propriétés de l'arbre après la suppression de l'élément n
        La suppression de l'élément n a remplacé l'élément en question par une structure de type self.FeuilleNulle, du coup n est une feuille vide mais rataché à l'ancienne place de n dans l'arbre
    """

    def reorganisation_suppression(self, n):
        while n != self.racine and n.couleur == 'NOIR':
            
            # Si n est le fils gauche de son père 
            if n == n.pere.gauche:

                # filsD est le frère de n
                filsD = n.pere.droit

                # Si n est noir alors que son frère est rouge, on passe le père en rouge et les fils en noir, on rééquilibre avec une rotation gauche (le fils droit du père de n (filsD) devient le père du père de n)
                if filsD.couleur == 'ROUGE':
                    n.pere.couleur = 'ROUGE'
                    filsD.couleur = 'NOIR'
                    self.rotationGauche(n.pere)
                    # Après la rotation filsD reprend la valeur du frère de n
                    filsD = n.pere.droit

                # Si les deux fils du filsD sont noirs, alors filsD devient rouge. On remonte ensuite vers la racine en considérant le père de n
                if filsD.gauche.couleur == 'NOIR' and filsD.droit.couleur == 'NOIR':
                    filsD.couleur = 'ROUGE'
                    n = n.pere

                # Si les deux fils de filsD ne sont pas noirs
                else:
                    # Si le fils droit du frère de n est noir, alors on passe son fils gauche à noir et filsD devient rouge, on rééquilibre avec une rotation droite (le fils gauche de filsD devient le père de filsD)
                    if filsD.droit.couleur == 'NOIR':
                        filsD.gauche.couleur = 'NOIR'
                        filsD.couleur = 'ROUGE'
                        self.rotationDroite(filsD)
                        # Après la rotation filsD reprend la valeur du frère de n
                        filsD = n.pere.droit
                    filsD.couleur = n.pere.couleur
                    n.pere.couleur = 'NOIR'
                    filsD.droit.couleur = 'NOIR'
                    # On effectue une rotation gauche sur le père de n (le fils droit du père de n devient le père du père de n)
                    self.rotationGauche(n.pere)
                    # Apres cette rotation l'arbre est équilibré, on interrompt la boucle
                    n = self.racine
            
            # Si n est le fils droit de son père
            else:

                # filsG est le frère de n
                filsG = n.pere.gauche

                # Si n est noir alors que son frère est rouge, on passe le père en rouge et les fils en noir, on rééquilibre avec une rotation droite (le fils gauche du père de n (filsG) devient le père du père de n)
                if filsG.couleur == 'ROUGE':
                    n.pere.couleur = 'NOIR'
                    filsG.couleur = 'NOIR'
                    self.rotationDroite(n.pere)
                    # Après la rotation filsG reprend la valeur du frère de n
                    filsG = n.pere.gauche

                # Si les deux fils du filsG sont noirs, alors filsG devient rouge. On remonte ensuite vers la racine en considérant le père de n
                if filsG.droit.couleur == 'NOIR' and filsG.gauche.couleur == 'NOIR':
                    filsG.couleur = 'ROUGE'
                    n = n.pere
                else:

                     # Si le fils gauche du frère de n est noir, alors on passe son fils gauche à noir et filsG devient rouge, on rééquilibre avec une rotation gauche (le fils droit de filsG devient le père de filsG)
                    if filsG.gauche.couleur == 'NOIR':
                        filsG.droit.couleur = 'NOIR'
                        filsG.couleur = 'ROUGE'
                        self.rotationGauche(filsG)
                        # Après la rotation filsG reprend la valeur du frère de n
                        filsG = n.pere.gauche
                    filsG.couleur = n.pere.couleur
                    n.pere.couleur = 'NOIR'
                    filsG.gauche.couleur = 'NOIR'
                    # On effectue une rotation droite sur le père de n (le fils gauche du père de n devient le père du père de n)
                    self.rotationDroite(n.pere)
                    # Apres cette rotation l'arbre est équilibré, on interrompt la boucle
                    n = self.racine

        # En sortant de la boucle on se trouve soit sur la racine, soit sur un noeud noir
        n.couleur = 'NOIR'


a = RougeNoir()
a.insererVal(5)
a.insererVal(3)
a.insererVal(6)
a.insererVal(2)
a.insererVal(4)
a.insererVal(10)
a.insererVal(7)
a.insererVal(12)
a.insererVal(1)
a.afficher()



