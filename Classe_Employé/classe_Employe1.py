

class Employe:# définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire. 
# Méthodes d'accès aux différents attributs de la classe:
    
    def num_matricule(self, matricule):
        return "le matricule est le " + matricule
        
    def le_nom(self, nom):
        return "le nom est " + nom

    def le_prenom(self, prenom):
        return "le prénom est " + prenom 
    
    def la_date_de_naissance(self, date_de_naissance):
        return "la date de naissance est le " + date_de_naissance
    
    def la_date_d_embauche(self, date_d_embauche):
        return "la date d'embauche est le " + date_d_embauche 

    def le_salaire(self, salaire):
        return "le salaire est " + salaire   
employe = Employe()
print(employe.num_matricule("10941"))
print(employe.le_nom("SALIM"))
print(employe.le_prenom("Omar"))
print(employe.la_date_de_naissance("04/08/1990"))
print(employe.la_date_d_embauche("05/11/2012"))
print(employe.le_salaire("10000"))