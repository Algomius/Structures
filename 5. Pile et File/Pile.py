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

class Pile:
    def __init__(self):
        self.tete = None
    
    def parcoursPile(self):
        print('***********************************************************')
        if self.tete == None:
            print("La pile est vide")
        else:
            print(self.tete.valeur)
            p = self.tete.prochain
            while p != self.tete:
                print(p.valeur)
                p = p.prochain
    
    def push(self, v):
        ele = Element(v)
        if self.tete is None :
            ele.prochain = ele
            ele.precedent = ele
            self.tete = ele
        else:
            ele.prochain = self.tete
            ele.precedent = self.tete.precedent 
            self.tete.precedent.prochain = ele
            self.tete.precedent = ele 

    def pop(self):
        if self.tete is not None:
            if self.tete is self.tete.prochain:
                v = self.tete.valeur
                self.tete = None
                return v
            else:  
                v = self.tete.precedent.valeur
                self.tete.precedent.precedent.prochain = self.tete
                self.tete.precedent = self.tete.precedent.precedent
                return v


l = Pile()
l.push(1)
l.push(2)
l.push(3)
l.parcoursPile()
l.push(5)
l.push(6)
l.push(7)
l.parcoursPile()
print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop())
l.parcoursPile()

