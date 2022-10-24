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

class File:
    def __init__(self):
        self.tete = None
    
    def parcoursFile(self):
        print('***********************************************************')
        if self.tete == None:
            print("La liste est vide")
        else:
            print(self.tete.valeur)
            p = self.tete.prochain
            while p != self.tete:
                print(p.valeur)
                p = p.prochain
    
    def enfiler(self, v):
        ele = Element(v)
        if self.tete is not None:
            ele.prochain = self.tete
            ele.precedent = self.tete.precedent
            self.tete.precedent.prochain = ele
            self.tete.precedent = ele
        else:
            ele.prochain = ele
            ele.precedent = ele
        self.tete = ele

    def defiler(self):
        if self.tete is not None:
            if self.tete == self.tete.prochain:
                v = self.tete.valeur 
                self.tete = None
                return v
            else:
                v = self.tete.valeur
                self.tete.precedent.prochain = self.tete.prochain
                self.tete.prochain.precedent = self.tete.precedent
                self.tete = self.tete.prochain
                return v


l = File()
l.enfiler(1)
l.enfiler(2)
l.enfiler(3)
l.parcoursFile()
l.enfiler(5)
l.enfiler(6)
l.enfiler(7)
l.parcoursFile()
print(l.defiler())
print(l.defiler())
print(l.defiler())
print(l.defiler())
print(l.defiler())
l.parcoursFile()

