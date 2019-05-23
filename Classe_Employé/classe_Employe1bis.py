
class Employe:# définition de la classe employé.
# classe définissant un employé caractérisé par:
# son matricule, son nom, son prénom, sa date de naissance, sa date d'embauche
# et son salaire. 
# Méthodes d'accès aux différents attributs de la classe:

    def __init__(self, employe_attributes): # dico passé en paramètre.
        # on crée une boucle pour automatiser l'accès aux différents attributs.
        for attribute_name, attribute_value in employe_attributes.items():
# On crée une méthode setattr qui prend pour paramètre l'instance self et le nom et la valeur de l'attribut.
            setattr(self, attribute_name, attribute_value)
employe_attributes = {"Matricule" : 10941, "Nom": "SALIM", "Prenom": "Omar", "Date_de_naissance" : " 04/08/1990", "Date d'embauche" : "05/11/2012", "Salaire" : 1000} # dictionnaire contenant les attributs et leurs valeurs


employe = Employe(employe_attributes)
print(employe.Matricule) # On peut remplacer Matricule par chacun des autres attributs.