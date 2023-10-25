from metier.prof import Prof
from metier.stage import Stage
from dao.userDao import UserDao
from metier.listEnvie import ListEnvie
from dao.assoCritUserDAO import AssoCritUserDao
from dao.assoStageUserDao import AssoStageUserDao

class TestProf(TestCase):

    def test_charger_user_valide(self):
        # GIVEN
        UserDao.charger_user = lambda x, y: {"email": x, "mdp": y, "profil": "Prof", "code_insee_residence": None, "souhaite_alertes": False}  # Mock
        AssoCritUserDao.exist_email = lambda x: False  # Mock
        AssoStageUserDao.exist_email = lambda x: False  # Mock

        email = "email@example.com"
        mdp = "password"

        # WHEN
        prof = Prof.charger_user(email, mdp)

        # THEN
        self.assertIsInstance(prof, Prof)
        self.assertEqual(prof.email, email)
        self.assertEqual(prof.mdp, mdp)

    def test_charger_user_invalide(self):
        # GIVEN
        UserDao.charger_user = lambda x, y: None  # Mock

        email = "email@example.com"
        mdp = "password"

        # WHEN / THEN
        with self.assertRaises(Exception) as context:
            Prof.charger_user(email, mdp)

        self.assertEqual(str(context.exception), "email ou mdp incorrect")

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestProf)
    )
