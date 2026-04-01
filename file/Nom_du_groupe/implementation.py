#Les affaires avec les fichier vont chercher une liste qui serait dans l'autre document

import json

class File:
    def __init__(self,filename="file/Nom_du_groupe/file.json"): 
        self.base_de_donnee = []
        self.index_tete = 0
        self.filename = filename
        self.load_file()
        
    def load_file(self):
        with open(self.filename, "r") as f:
            file = json.load(f)
        for i in file:
            self.base_de_donnee.append(i)

    def est_vide(self):
        if len(self.base_de_donnee) == 0:
            return True
        return False
    
    def enqueue(self, valeur):
        self.base_de_donnee.append(valeur)

    def dequeue(self):
        if self.est_vide():
            return "Erreur: La file est vide"
        else:
            tete = self.base_de_donnee[self.index_tete]
            self.base_de_donnee[self.index_tete] = None
            self.index_tete += 1
            return tete
    
    def size(self):
        return len(self.base_de_donnee)

    def front(self):
        if self.est_vide():
            return "Erreur: La file est vide"
        else:
            return self.base_de_donnee[0]