class voiture:
    def __init__(self, marque, type, annee, prix):
        self.marque = marque
        self.type = type
        self.annee = annee
        self.prix = prix

    def info(self):
        return "{} {} {}".format(self.type, self.marque, self.annee)


voit_1 = voiture("Toyota", "RAV4", 2008, 10000)

# print(voiture.info(voit_1))
print(voit_1.info())
