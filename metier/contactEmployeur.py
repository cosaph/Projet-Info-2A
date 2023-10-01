from dao.contactEmployeurDAO import ContactEmployeurDAO


class ContactEmployeur:
    def __init__(self, email, nom=None, prenom=None,  tel=None):
        self.email, self.nom, self.prenom, self.tel = email, nom, prenom, tel

    def __str__(self):
        return "nom: {}\nPrénom: {}\nEmail: {}\nTel: {} ".format(self.nom, self.prenom, self.email, self.tel)
  
    def supprimer_contact(self):
        if self.existe():
            ContactEmployeurDAO().delete(self)

    def modifier_contact(self):
        if self.existe():
            ContactEmployeurDAO().update(self)
    
    def existe(self):
        return ContactEmployeurDAO().exist_id(self)
    
    def enregistrer_contact(self):
        """ Enregistrement dans la base ou modification si existe déjà"""
        if not self.existe():
            ContactEmployeurDAO().add(self)
        else:
            ContactEmployeurDAO().update(self)