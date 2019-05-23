
class Employe: # définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire. 
# Ajouter à la classe la méthode AugmentationDuSalaire( ) qui augmente le salaire de l’employé en prenant en considération l’ancienneté.
# Si Ancienneté < 5 ans, alors on ajoute 2%. - Si Ancienneté < 10 ans, alors on ajoute 5%. - Sinon, on ajoute 10%.
  
    anciennete = 3
   
    def augmentation_du_salaire(self, salaire):
        if self.anciennete < 5:
            self.augmentation_du_salaire = salaire + salaire * 0.02
            return salaire
        if self.anciennete < 10:
            self.augmentation_du_salaire = salaire + salaire * 0.05
        else:
            self.augmentation_du_salaire = salaire + salaire * 0.1   

employe = Employe()
employe.augmentation_du_salaire(10000)
print(employe.augmentation_du_salaire)