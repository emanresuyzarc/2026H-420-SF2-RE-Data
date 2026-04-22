class Dictionnaire:
    def __init__(self):
        self.dico = {}
    
    def ajouter_element(self, cle, valeur): # Ajoute un élément au dictionnaire
        self.dico[cle] = valeur
        return self.dico
    
    def voir_valeur(self, cle): # retourne la valeur associée à la clé
        return self.dico[cle]
    
    def nombre_items(self): # retourne le nombre d'items du dictionnaire
        return len(self.dico)
