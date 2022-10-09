Projet 7 DA-Python OC/Gavin Humphrey

Livrable du Projet 7 du parcours D-A Python d'OpenClassrooms : calcul de la meilleure combinaison d'actions en fonction de leurs bénéfices selon deux approches ;

    Bruteforce

    Approche Optimisé (Algorithme Glouton)

Testé sous Windows 10 - Python version 3.9.5
Initialisation du projet
Windows :

git clone https://github.com/Gavin-Humphrey/P7-AlgoInvest-and-Trade.git
cd P7-AlgoInvest-and-Trade 
python -m venv env 
env\scripts\activate

pip install -r requirements.txt

MacOS et Linux :

git clone https://github.com/Gavin-Humphrey/P7-AlgoInvest-and-Trade.git

cd P7-AlgoInvest-and-Trade
python3 -m venv env 
source env/bin/activate

pip install -r requirements.txt

Note : Lors du traitement des données, le programme affiche une barre de progression (tqdm).
Exécution du programme
Bruteforce

python bruteforce.py

Le montant d'investissement par défaut est fixé à 500€. Il est toutefois possible d'entrer un montant personnalisé.

Note : Le bruteforce ne traîte que les données du fichier "actions.csv", contenant 20 actions. Les datasets 1 et 2 résulteraient à un temps d'exécution extrêmement long.


Approche Optimisé(Approche Glouton)

Comme pour le bruteforce, il est possible d'entrer un montant personnalisé.


Enfin, il est également possible de traiter le fichier de actions.csv (20 actions), avec ou sans montant personnalisé 
