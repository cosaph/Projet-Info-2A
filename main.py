
from scr.critere import Critere
from scr.eleveNonAuthentifie import EleveNonAuthentifie


unCritere = Critere("47001", "dataS", 3, 6, "blabla", "pme")
unEleve = EleveNonAuthentifie(unCritere)
print(unEleve)
