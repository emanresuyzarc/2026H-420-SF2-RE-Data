class File:
    def __init__(self):
        self.valeurs = []

    def ajouter_valeur(self, valeur):
        self.valeurs.append(valeur)

    def retirer_valeur(self):
        if self.valeurs:
            return self.valeurs.pop(0)
        else:
            raise IndexError("La file est vide")

    def obtenir_valeurs(self):
        return self.valeurs
