class Employe: # définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire. 
# Ajouter à la classe la méthode age() qui retourne l'age de l'employé:
# Ajouter à la classe la méthode Anciennete( ) qui retourne le nombre d’années d’ancienneté de l’employé.
   
   
    
    def age(self, age):
        self.age = age
        return age
    def anciennete(self, anciennete):
        self.anciennete = anciennete
        return anciennete
  
employe = Employe()
employe.age(2012 - 1990)
employe.anciennete(2015 - 2012)
print(employe.age)
print(employe.anciennete)
