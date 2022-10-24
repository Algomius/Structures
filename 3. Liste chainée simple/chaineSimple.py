"""
    Element d'une liste chainée
"""

class Element:
    def __init__(self, data):
        self.valeur = data
        self.prochain = None


"""
    Definition de la liste chainée
"""

class ListeChainee:
    def __init__(self):
        self.tete = None
    
    def parcoursListe(self):
        if self.tete == None:
            print("La liste est vide")
        else:
            p = self.tete
            while p is not None:
                print(p.valeur)
                p = p.prochain
    
    def insererTete(self, v):
        ele = Element(v)
        ele.prochain = self.tete
        self.tete = ele

    def insererQueue(self, v):
        ele = Element(v)
        p = self.tete
        if p is None:
            self.tete = ele
        else:
            while p.prochain is not None:
                p = p.prochain
            p.prochain = ele

    def supprimerEle(self, v):
        old = None
        p = self.tete
        while p is not None:
            if p.valeur == v:
                if old == None:
                    self.tete = p.prochain
                else:
                    old.prochain = p.prochain
                return
            old = p
            p = p.prochain


l = ListeChainee()
l.insererTete(1)
l.insererTete(2)
l.insererTete(3)
l.insererQueue(4)
l.parcoursListe()
