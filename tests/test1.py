from scr.critere import Critere
from scr.eleveNonAuthentifie import EleveNonAuthentifie
from scr.eleveAuthentifie import EleveAuthentifie
from scr.prof import Prof
from scr.admin import Admin
from scr.contactEmployeur import ContactEmployeur

unCritere = Critere("47001", "dataS", 3, 6, "blabla", "pme")
unEleve = EleveNonAuthentifie(unCritere)
deuxEleve = EleveAuthentifie(unCritere, "unid", "mdp", "mail", "47001", True)
unProf = Prof(unCritere, "unid", "mdp", "mail", "47001", True)
unAdmin = Admin(unCritere, "unid", "mdp", "mail", "47001", True)
#print(unEleve)
#print(deuxEleve)
print(unAdmin)

unContact = ContactEmployeur("b", "d")
print(unContact)