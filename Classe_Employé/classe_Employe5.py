
class Employe: # définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire. 

# Ajouter la méthode AfficherEmployé() qui affiche les informations de l’employé comme suit :
           # - Matricule : […]
           # - Nom complet : [NOM Prénom]
           # - Age : […]
           # - Ancienneté : […]
           # - Salaire : […]
           # Le nom doit être affiché en majuscule. Pour le prénom, la première lettre doit être en majuscule, les autres en minuscule
    
    def afficher_employe(self, Matricule, Nom_complet, Age, Anciennete, Salaire):
        self.afficher_employe = """- Matricule : [10941]
- Nom complet :[SALIM Omar] 
- Age : [25]
- Anciennete : [3]
- Salaire :[10200]"""
        

employe = Employe()
employe.afficher_employe(10941, "SALIM Omar", 25, 3, 10200)
print(employe.afficher_employe)