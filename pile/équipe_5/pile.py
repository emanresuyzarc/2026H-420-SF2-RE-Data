class Pile:
    def __init__(self):
        self.elements = []

    def vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
       
        if self.est_vide():
            raise Exception()
        return self.elements.pop()

    def sommet(self):
       
        if self.est_vide():
            raise Exception()
        return self.elements[-1]

    def taille(self):
       
        return len(self.elements)