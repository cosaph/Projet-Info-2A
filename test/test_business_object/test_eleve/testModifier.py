import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode modifier()
    def test_modifier(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        eleve.enregistrer()  # Assurez-vous que l'élément est enregistré avant la modification

        # Sauvegardez les valeurs initiales pour comparaison ultérieure
        initial_values = {
            'email': eleve.email,
            'code_insee_residence': eleve.code_insee_residence,
    }
        # Effectuez quelques modifications sur l'objet `eleve` ici
        new_email = "new_email@example.com"
        new_code = "nouveau_code"
        eleve.email = new_email
        eleve.code_insee_residence = new_code
        # Modifiez d'autres attributs ici si nécessaire

        eleve.modifier()  # Appel de la méthode modifier
    
        # Rechargez l'objet depuis la base de données pour s'assurer que les modifications ont été appliquées
        eleve_reloaded = Eleve.charger_user(new_email, eleve.mdp)  # Utilisez la méthode charger_user

        self.assertEqual(eleve_reloaded.email, new_email)
        self.assertEqual(eleve_reloaded.code_insee_residence, new_code)
    

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )



