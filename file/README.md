## Définition *(Partie II: Algorithmique et Programmation)*: 
Une file (en anglais queue) est une structure de données fondée sur le principe « premier arrivé, premier sorti » (ou FIFO pour First In, First Out), ce qui veut dire que les premiers éléments ajoutés à la file seront les premiers à être récupérés. Le fonctionnement ressemble à une file d'attente : les premières personnes à arriver sont les premières personnes à sortir de la file. 


## Opérations *(Partie II: Algorithmique et Programmation)*: 
Cette structure de donnée contient deux opérations principales:Enfiler et Défiler.Enfieler sert à ajouter un élément dans la file. Son terme anglais correspondant est « Enqueue ». Défiler, lui, renvoie le prochain élément de la file, et le retire de la file. Son terme anglais correspondant est « Dequeue ». 


## Avantages & inconvénients *(Wikipédia)*:
-Dans un logiciel informatique, l'avantage de cet ordonnancement réside dans sa relative simplicité ; cependant elle pénalise les processus à temps bref d'exécution : en effet, si on lance, à la suite d'un processus qui demande beaucoup de temps de calcul, une petite tâche (par exemple, dans un serveur qui ne gère qu'une imprimante, imprimer une page), la petite tâche devra attendre la fin de la tache qui demande beaucoup plus de temps (imprimer cent pages) avant de s'exécuter.

-À l'époque des machines à un seul processeur, c’était la technique la plus fiable pour être sûr d'effectuer les opérations dans un ordre logique.

-Cet algorithme est également utilisé comme politique de remplacement des lignes de cache en raison de sa simplicité d'implémentation et de son faible coût. Néanmoins, il présente dans cet usage une anomalie connue sous le nom d'anomalie de Belady : augmenter le nombre d'étages de la file peut avoir un effet négatif sur la performance.


## Exemples d'utilisation *(Wikipédia)*:
-En général, pour mémoriser temporairement des transactions qui doivent attendre pour être traitées.

-Les serveurs d'impression, qui traitent ainsi les requêtes dans l'ordre dans lequel elles arrivent, et les insèrent dans une file d'attente (dite aussi queue ou spool).

-Certains moteurs multitâches, dans un système d'exploitation, qui doivent accorder du temps-machine à chaque tâche, sans en privilégier aucune.

-Un algorithme de parcours en largeur utilise une file pour mémoriser les nœuds visités.

-Pour créer toutes sortes de mémoires tampons (en anglais « buffers »).

-En gestion des stocks les algorithmes doivent respecter la gestion physique des stocks pour assurer la cohérence physique/valorisation.