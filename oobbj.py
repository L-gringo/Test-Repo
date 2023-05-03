class fiche:
    def __init__(self, nom, prenom, taille, age, sexe, adresse, travail, statut):
        self.nom = nom
        self.prenom = prenom
        self.taille = taille
        self.age = age
        self.sexe = sexe
        self.adresse = adresse
        self.travail = travail
        self.statut = statut

    def portrait(self):
        return "{} {} {} {}".format(self.nom, self.prenom, self.taille, self.age)


Perso_1 = fiche(
    "ALIOU", "Mahmoulh", 30, 177, "male", "lyon", "ingenieur", "celibataire"
)
# print(Perso_1.nom)
print(Perso_1.portrait())
