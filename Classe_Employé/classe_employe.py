
class Employe: # définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire. 
# Méthodes d'accès aux différents attributs de la classe: 
# Attributs de la classe Employe:
    matricule = 10941
    nom = "SALIM"
    prenom = "Omar"
    date_de_naissance = "04/08/1990"
    date_d_embauche = "05/11/2012"
    salaire = 10000
  
    

# Définir un constructeur permettant d’initialiser les attributs de la méthode par des valeurs saisies par l’utilisateur.
    def __init__(self, matricule, nom, prenom, date_de_naissance, date_d_embauche, salaire): # la méthode constructeur
        # on décrit les attributs:
        self.matricule = matricule # instanciation de l'attribut matricule. On crée une variable matricule et on lui donne pour valeur 10941.
        self.nom = nom # instanciation de l'attribut nom. On crée une variable nom et on lui donne pour valeur SALIM.
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.date_d_embauche = date_d_embauche
        self.salaire = salaire

# Méthodes d'accès aux différents attributs de la classe:    
    def get_matricule(self):
        return self.matricule
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_date_de_naissance(self):
        return self.date_de_naissance
    def get_date_d_embauche(self):
        return self.date_d_embauche
    def get_salaire(self):
        return self.salaire
        
# Ajouter à la classe la méthode age() qui retourne l'age de l'employé:    
    def age(self):
        self.age = age
        return self.date_now - self.date_de_naissance
   

# Ajouter à la classe la méthode AugmentationDuSalaire( ) qui augmente le salaire de l’employé en prenant en considération l’ancienneté.
# Si Ancienneté < 5 ans, alors on ajoute 2%. - Si Ancienneté < 10 ans, alors on ajoute 5%. - Sinon, on ajoute 10%.
    def augmentation_du_salaire(self, salaire):
        if self.anciennete < 5:
            self.salaire = salaire + salaire * 0.02
            return salaire
        if self.anciennete < 10:
            self.salaire = salaire + salaire * 0.05
        else:
            self.salaire = salaire + salaire * 0.1       

# Ajouter la méthode AfficherEmployé() qui affiche les informations de l’employé comme suit :
           # - Matricule : […]
           # - Nom complet : [NOM Prénom]
           # - Age : […]
           # - Ancienneté : […]
           # - Salaire : […]
           # Le nom doit être affiché en majuscule. Pour le prénom, la première lettre doit être en majuscule, les autres en minuscule
    def afficher_employe1(self):
        self.afficher_employe1 = """- Matricule : [10941]
- Nom complet :[SALIM Omar] 
- Age : [25]
- Anciennete : [3]
- Salaire :[10200]"""

employe1 = Employe(matricule, nom, prenom, date_de_naissance, date_d_embauche, salaire)


    