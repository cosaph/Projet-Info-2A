from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch
from metier.admin import Admin
# Admin = __import__("Projet-Info-2A.metier.admin")
from metier.eleve import Eleve

class TestAdmin(TestCase):

    """faut il tester la méthode init??"""

    def test_charger_user(self):
        pass

    """Pour la méthode modifier_user, on différencie deux cas:
    - le cas où l'utilisateur entré en paramètre existe
    - le cas où l'utilisateur entré en paramètre n'existe pas"""
    def test_modifier_user_existe(self):
        """GIVEN"""
        existing_user = Eleve("user@mail.com","aime dé pé")
        un_admin = Admin("admin@mail.com","le mdp")

        """WHEN"""
        with patch.object(Eleve, "existe", return_value = True):
            with patch.object(existing_user, 'modifier') as mock_modifier:
                un_admin.modifier_user(existing_user)
            
        """THEN"""
        mock_modifier.assert_called_once()

if __name__ == "__main__":
    """Run the tests"""
    TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestAdmin)
    )