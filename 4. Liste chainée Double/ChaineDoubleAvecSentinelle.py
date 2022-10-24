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

class ListeChaineeDouble:
    def __init__(self):
        self.tete = None
        self.queue = None
    
    def parcoursListe(self):
        print('***********************************************************')
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
        if self.tete is not None:
            self.tete.precedent = ele
        else:
            self.queue = ele
        self.tete = ele

    def insererQueue(self, v):
        ele = Element(v)
        p = self.tete
        if p is None:
            self.tete = ele
            self.queue = ele
        else:
            self.queue.prochain = ele
            ele.precedent = self.queue
            self.queue = ele

    def supprimerEle(self, v):
        p = self.tete
        while p is not None:
            if p.valeur == v:
                if p.precedent is None and p.prochain is None:
                    self.tete = None
                    self.queue = None
                elif p.precedent == None:
                    self.tete = p.prochain  
                    self.tete.precedent = None
                elif p.prochain == None:
                    self.queue = p.precedent
                    self.queue.prochain = None
                else:
                    p.precedent.prochain = p.prochain
                    p.prochain.precedent = p.precedent
                return
            p = p.prochain


l = ListeChaineeDouble()
l.insererTete(1)
l.insererTete(2)
l.insererTete(3)
l.parcoursListe()
l.supprimerEle(3)
l.parcoursListe()
l.insererQueue(5)
l.insererQueue(6)
l.insererQueue(7)
l.parcoursListe()
