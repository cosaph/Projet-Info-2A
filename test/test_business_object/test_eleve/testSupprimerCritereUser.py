import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode supprimer_critereAuser()
    def test_supprimer_critereAuser(self):
        # GIVEN
        eleve = Eleve(email='test@example.com', mdp='123456')
        id_crit = 1
        # Assurez-vous que le critère existe pour cet élève (pour simuler cela dans un environnement de test)
        AssoCritUserDao().add(eleve, id_crit)  # Vous pouvez adapter cette partie selon vos besoins
        # Exécution de la méthode
        eleve.supprimer_critereAuser(id_crit)
        # Assertions
        self.assertFalse(AssoCritUserDao().exist_id(eleve.email, id_crit))  # Le critère ne doit plus être associé à cet élève
        self.assertFalse(CritereDAO().exist_id_crit(id_crit))  # Le critère ne doit plus exister dans la base de données (si c'était le seul élève à l'avoir)
 

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )

 


    
