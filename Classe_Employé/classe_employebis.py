
class Employe:
    matricule = 10941
    nom = "SALIM"
    prenom = "Omar"
    date_de_naissance = "04/08/1990"
    date_d_embauche = "05/11/2012"
    salaire = 10000   
 
    def __init__(self, matricule, nom, prenom, date_de_naissance, date_d_embauche, salaire):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.date_d_embauche = date_d_embauche
        self.salaire = salaire
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

    def age(self, age):
        self.age = age
        return self.age
    def anciennete(self, anciennete):
        self.anciennete = anciennete
        return self.anciennete   

    def augmentation_du_salaire(self, salaire):
        if self.anciennete < 5:
            self.salaire = salaire + salaire * 0.02
            return salaire
        if self.anciennete < 10:
            self.salaire = salaire + salaire * 0.05
        else:
            self.salaire = salaire + salaire * 0.1       
    
    def afficher_employe1(self, matricule, nom_complet, age, anciennete, salaire):
        self.afficher_employe1 = "- matricule : " + str([matricule]), " nom complet : " + str([nom_complet]), "age : " +str([age]), "anciennete : " + str([anciennete]), "salaire : " + str([salaire])
        
         
employe1 = Employe(10941, "SALIM", "Omar", "4/8/1990", "5/11/2012", 10000)
print(employe1.get_date_de_naissance())
print(employe1.get_date_d_embauche())
employe1.age(2015-1990)
print(employe1.age)
employe1.anciennete(2015-2012)
print(employe1.anciennete)
employe1.augmentation_du_salaire(10000)
print(employe1.salaire)
employe1.afficher_employe1(10941, "SALIM_Omar", 25, 3, 10000) 
print(employe1.afficher_employe1)

def main():   


    if __name__ == '__main__':
        main()