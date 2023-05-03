class Employee:
    nbre_emp = 0
    pourcentage = 1.05

    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.email = nom + prenom + "@yahoo.fr"

        Employee.nbre_emp = +1

    def prime(self):
        self.salaire = self.salaire * self.pourcentage

    @classmethod
    def defprime(cls, montant):
        cls.pourcentage = montant


emp_1 = Employee("MAHMOULH", "ALIOU", 42000)
emp_2 = Employee("John", "DOE", 60000)
print(Employee.nbre_emp)
emp_1.defprime(1.06)
# print(emp_1.email)
print(Employee.pourcentage)
print(emp_1.pourcentage)
# emp_1.pourcentage = 1.08
# emp_1.prime()
# emp_2.prime()
# print(emp_1.pourcentage)
# print(emp_2.pourcentage)
# print(emp_1.__dict__)
# print(emp_2.__dict__)
