# Dossier pour les exercices sur les piles

Définition: Structure de données linéaire qui suit le principe LIFO (Last In, First Out), ce qui signifie que le dernier élément ajouté est le premier à être retiré.

Opérations principales:
-> push()          | Ajoute un élément au sommet de la pile
-> pop()           | Retire et retourne l'élément au sommet
-> peek() ou top() | Consulte l'élément au sommet sans le retirer
-> isEmpty()       | Vérifie si la pile est vide
-> size()          | Retourne le nombre d'élément

Avantages:
 Simple à implémenter
 Accès rapide (temps constant O(1)) pour push et pop
 Très utile pour gérer des opérations imbriquées (ex : appels de fonctions)

Inconvénients:
 Accès limité (seulement au sommet)
 Pas adaptée pour accéder à des éléments au milieu
 Peut provoquer des erreurs si on dépile une pile vide (stack underflow)

Exemples d'utilisation en sciences:
 Simulation de systèmes dynamiques
 Résolution de problèmes récursifs
 Modélisation d’événements empilés dans le temps