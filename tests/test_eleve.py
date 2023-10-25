from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve   
from metier.critere import Critere
from metier.satge import Stage

class TestEleve(TestCase):

    # Tester la méthode charger_user()
    def test_charger_user(self):
        # GIVEN
        email = 'test@example.com'
        mdp = '123456'      
        # WHEN
        eleve = Eleve.charger_user(email, mdp) 
        # THEN
        self.assertIsInstance(eleve, Eleve)

    #Tester la méthode possede_critere()
    def test_possede_critere(self):
        # GIVEN
        eleve = Eleve(email='test@example.com', mdp='123456')
        critere = Critere()  # Supposition
        # WHEN
        possede = eleve.possede_critere(critere)
        # THEN
        self.assertTrue(possede)  # Ou self.assertFalse(possede), selon ce que vous attendez

    #Tester la méthode ajouter_critereAuser()
    def test_ajouter_critereAuser(self):
        # GIVEN
        eleve = Eleve(email='test@example.com', mdp='123456')
        critere = Critere()  # Supposition
        # WHEN
        resultat = eleve.ajouter_critereAuser(critere)
        # THEN
        self.assertTrue(resultat)

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


    #Tester la méthode charger_all_critere
    def test_charger_all_critere(self):
        eleve = Eleve(email='test@example.com', mdp='123456')
        criteres = Eleve.charger_all_critere()
        self.assertIsInstance(criteres, list)

    #Tester la méthode charger_all_critere_mail()
    def test_charger_all_stageAuser(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        result = eleve.charger_all_stageAuser()
        self.assertIsInstance(result, list)
    for stage in result:
        self.assertIsInstance(stage, Stage)


    #Tester la méthode charger_all_stageAuser()
    def test_charger_all_stage_mail(self):
        result = Eleve.charger_all_stage_mail("email_exemple@gmail.com")
        self.assertIsInstance(result, list)
    for stage in result:
        self.assertIsInstance(stage, Stage)


    #Tester la méthode test_charger_all_stage_mail()
    def test_charger_all_stage_mail(self):
        result = Eleve.charger_all_stage_mail("email_exemple@gmail.com")
        self.assertIsInstance(result, list)
    for stage in result:
        self.assertIsInstance(stage, Stage)


    #Tester la méthode possede_stage()
    def test_possede_stage(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        stage = Stage()  # Initialisez comme nécessaire
        result = eleve.possede_stage(stage)
        self.assertIsInstance(result, bool)


    #Tester la méthode ajouter_stageAuser()
    def test_ajouter_stageAuser(self):
        # Assurez-vous que l'étudiant ne possède pas déjà ce stage
        self.assertFalse(self.eleve.possede_stage(self.stage))

        # Ajoutez le stage et vérifiez s'il a été ajouté
        self.eleve.ajouter_stageAuser(self.stage)
        self.assertTrue(self.eleve.possede_stage(self.stage))


    #Tester la méthode supprimer_stageAuser()
    def test_supprimer_stageAuser(self):
        eleve = Eleve()  
        stage = Stage() 

        # Assurons-nous que l'étudiant possède ce stage
        eleve.ajouter_stageAuser(stage)
        result_before = eleve.possede_stage(stage)
        self.assertIsInstance(result_before, bool)
        self.assertTrue(result_before)

        # Supprimer le stage et vérifiez s'il a été supprimé
        eleve.supprimer_stageAuser(stage)
        result_after = eleve.possede_stage(stage)
        self.assertIsInstance(result_after, bool)
        self.assertFalse(result_after)

    #Tester la méthode existe()
    def test_existe(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        result = eleve.existe()
        self.assertIsInstance(result, bool)
    
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

        # Ici, vous pouvez ajouter des assertions pour vérifier si les modifications ont été appliquées
        self.assertEqual(eleve_reloaded.email, new_email)
        self.assertEqual(eleve_reloaded.code_insee_residence, new_code)
        # Ajoutez d'autres assertions ici si nécessaire

    
    #Tester la méthode enregistrer()
    def test_enregistrer(self):
        eleve = Eleve()  # Initialisez comme nécessaire

        # Vérifiez que l'élément n'existe pas encore
        self.assertFalse(eleve.existe())

        eleve.enregistrer()  # Appel de la méthode enregistrer

        # Vérifiez que l'élément existe maintenant
        self.assertTrue(eleve.existe())


    #Tester la méthode supprimer_compte()
    def test_supprimer_compte(self):
        # Créez et enregistrez un nouvel élève pour s'assurer qu'il existe dans la base de données
        eleve = Eleve()  # Initialisez comme nécessaire
        eleve.enregistrer()

        # Assurez-vous que l'élève existe dans la base de données
        self.assertTrue(eleve.existe())

        # Supprimez le compte
        eleve.supprimer_compte()

        # Vérifiez que le compte a été supprimé
        self.assertFalse(eleve.existe())


    #Tester la méthode __str__() 
    def test_str_eleve_avec_critere_et_liste_stage(self):
        # GIVEN
        critere = Critere(specialite="Informatique", ville_cible="Paris", rayon_km=50)
        stage1 = Stage(url_stage="url1", titre="Stage en Informatique", specialite="Informatique", ville="Paris")
        stage2 = Stage(url_stage="url2", titre="Stage en Data Science", specialite="Data Science", ville="Paris")
        list_envie = [stage1, stage2]
        eleve = Eleve(email="test@example.com", mdp="password", critere=[critere], list_envie=list_envie, code_insee_residence="75000", souhaite_alertes=True)
        
        # WHEN
        result = eleve.__str__()

        # THEN
        expected_str = '''Les critères de l'utilisateur sont:
    Specialite: Informatique
    Ville cible: Paris
    Rayon: 50km
    Les caractéristiques de l'utilisateurs sont:
    email: test@example.com
    Liste de stages : Stage en Informatique à Paris
    Stage en Data Science à Paris
    Commune de résidence: 75000
    Souhaite alerte: True
    A trouvé un stage: False'''
        self.assertEqual(result, expected_str)


    #Tester la méthode set_souhaite_alertes()
    def test_set_souhaite_alertes(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        eleve.set_souhaite_alertes(True)  # Active les alertes
        self.assertTrue(eleve.souhaite_alertes)  # Vérifiez que les alertes sont actives


    #Tester la méthode set_stage_trouve()
    def test_set_stage_trouve(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        eleve.set_stage_trouve(True)  # Indique que l'élève a trouvé un stage
        self.assertTrue(eleve.stage_trouve)  # Vérifiez que stage_trouve est vrai


    from unittest.mock import patch
    #Tester la méthode rechercher_stage()
    def test_rechercher_stage(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        critere = Critere()  # Initialisez comme nécessaire

        # Mock du retour de la méthode `recherche_stage` de la classe `Critere`
        mock_return_value = [Stage(), Stage()]  # Assumez que Stage est une classe que vous avez définie
        with patch.object(Critere, 'recherche_stage', return_value=mock_return_value):
            # Assurez-vous que l'élève a des critères
            eleve.ajouter_critereAuser(critere)  

            # Test de la méthode
            result = eleve.rechercher_stage(critere)

        # Vérifiez que la méthode retourne une liste de stages
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(mock_return_value))

if __name__ == "__main__":
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )

