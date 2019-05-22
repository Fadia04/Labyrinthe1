

class Employe: # définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire.
# Définir un constructeur permettant d’initialiser les attributs de la méthode par des valeurs saisies par l’utilisateur.
    def __init__(self): # la méthode constructeur
        # on décrit les attributs:
        self.matricule = 10941 # instanciation de l'attribut matricule. On crée une variable matricule et on lui donne pour valeur 10941.
        self.nom = "SALIM" # instanciation de l'attribut nom. On crée une variable nom et on lui donne pour valeur SALIM.
        self.prenom = "Omar"
        self.date_de_naissance = "04/08/1990"
        self.date_d_embauche = "05/11/2012"
        self.salaire = 10000

employe = Employe()


