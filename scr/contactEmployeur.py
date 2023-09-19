class ContactEmployeur:
    def __init__(self, nom=None, prenom=None, email=None, tel=None):
        self.nom, self.prenom, self.email, self.tel = nom, prenom, email, tel

    def __str__(self):
        return "nom: {}\nPrénom: {}\nEmail: {}\nTel: {} ".format(self.nom, self.prenom, self.email, self.tel)

