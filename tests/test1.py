from scr.critere import Critere
from scr.eleveNonAuthentifie import EleveNonAuthentifie
from scr.eleveAuthentifie import EleveAuthentifie
from scr.prof import Prof
from scr.admin import Admin
from scr.contactEmployeur import ContactEmployeur

unCritere = Critere("idd", "47001", "dataS", 3, 6, "pme")

unEleve = EleveNonAuthentifie(unCritere)
deuxEleve = EleveAuthentifie(unCritere, "mail", "mdp", "47001", True)
unProf = Prof(unCritere, "mail", "mdp",  "47001", True)
unAdmin = Admin(unCritere, "mail", "mdp", "47001", True)
#print(unEleve)
#print(deuxEleve)
print(unAdmin)

unContact = ContactEmployeur("b", "d")
print(unContact)