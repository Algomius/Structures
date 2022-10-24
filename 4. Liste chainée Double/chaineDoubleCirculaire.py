"""
    Element d'une liste chainée
"""

class Element:
    def __init__(self, data):
        self.valeur = data
        self.prochain = None
        self.precedent = None


"""
    Definition de la liste chainée
"""

class ListeChaineeDoubleCirculaire:
    def __init__(self):
        self.tete = None
    
    def parcoursListe(self):
        print('***********************************************************')
        if self.tete == None:
            print("La liste est vide")
        else:
            print(self.tete.valeur)
            p = self.tete.prochain
            while p != self.tete:
                print(p.valeur)
                p = p.prochain
    
    def insererTete(self, v):
        ele = Element(v)
        if self.tete is None:
            ele.prochain = ele
            ele.precedent = ele
        else:
            ele.precedent = self.tete.precedent
            ele.prochain = self.tete
            self.tete.precedent.prochain = ele
            self.tete.precedent = ele
        self.tete = ele

    def insererQueue(self, v):
        ele = Element(v)
        if self.tete is None:
            ele.prochain = ele
            ele.precedent = ele
            self.tete = ele
        else:
            ele.precedent = self.tete.precedent
            ele.prochain = self.tete
            self.tete.precedent.prochain = ele
            self.tete.precedent = ele

    def supprimerElement(self, v):
        tst = True
        p = self.tete
        while tst or p != self.tete:
            tst = False
            if p.valeur == v:
                if p == p.precedent:
                    self.tete = None
                else:
                    p.precedent.prochain = p.prochain
                    p.prochain.precedent = p.precedent
                    if self.tete == p:
                        self.tete = p.prochain
                return
            p = p.prochain

    def supprimerPremier(self):
        if self.tete is not None:
            if self.tete is self.tete.prochain:
                self.tete = None
            else:
                self.tete.precedent.prochain = self.tete.prochain
                self.tete.prochain.precedent = self.tete.precedent
                self.tete = self.tete.prochain

    def supprimerDernier(self):
        if self.tete is not None:
            if self.tete is self.tete.prochain:
                self.tete = None
            else:  
                self.tete.precedent.precedent.prochain = self.tete
                self.tete.precedent = self.tete.precedent.precedent


l = ListeChaineeDoubleCirculaire()
l.insererTete(1)
l.insererTete(2)
l.insererTete(3)
l.parcoursListe()
l.supprimerElement(1)
l.parcoursListe()
l.insererQueue(5)
l.insererQueue(6)
l.insererQueue(7)
l.parcoursListe()
l.supprimerDernier()
l.supprimerDernier()
l.supprimerDernier()
l.supprimerDernier()
l.supprimerDernier()
l.supprimerDernier()
l.supprimerDernier()
l.parcoursListe()

