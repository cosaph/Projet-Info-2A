class ContactEmployeur:
    def __init__(self, email=None, nom=None, prenom=None,  tel=None):
        self.email, self.nom, self.prenom, self.tel = email, nom, prenom, tel

    def __str__(self):
        return "nom: {}\nPrénom: {}\nEmail: {}\nTel: {} ".format(self.nom, self.prenom, self.email, self.tel)
    
    def enregistrer_contact(self):
        pass

    def supprimer_contact(self):
        pass

    def modifier_contact(self):
        pass
    
    def existe(self):
        pass