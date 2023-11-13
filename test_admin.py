# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_admin.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/13 14:47:19 by cosaph            #+#    #+#              #
#    Updated: 2023/11/13 15:36:13 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from unittest.mock import patch
from metier.admin import Admin
import unittest
from dao.userDao import UserDao
from metier.eleve import Eleve

class TestAdmin(unittest.TestCase):

    def setUp(self):
        
        self.admin = Admin(
            email="admin@example.com",
            mdp="password",
            code_insee_residence="12345",
            souhaite_alertes=True
        )
        
    def test_charger_user(self):
        
        # GIVEN
        email = "m"
        mdp = "m" #en clair 
        mdp_chiffre = UserDao().chiffrer_mdp(mdp, email)
        expected_admin = Admin(
            email=email,
            mdp=mdp_chiffre,
            code_insee_residence=None,
            souhaite_alertes=False
        )
        # WHEN
        admin = Admin.charger_user(email, mdp)

        # THEN
        self.assertEqual(admin.email, expected_admin.email)
        self.assertEqual(admin.mdp, expected_admin.mdp)
        self.assertEqual(admin.code_insee_residence, expected_admin.code_insee_residence)
        self.assertEqual(admin.souhaite_alertes, expected_admin.souhaite_alertes)

    def test_chargerTout(self):
        
        # GIVEN
        expected_result = ["m", "a", "b"]

        # WHEN
        result = self.admin.chargerTout()

        # THEN
        self.assertEqual(expected_result, result)

    def test_supprime_user(self):
        
        # GIVEN
        expected_result = None
        user_sup = Eleve("a", "a")
        

        # WHEN
        result = self.admin.supprime_user(user_sup)
        print(result)
        # THEN
        self.assertEqual(expected_result, result)

    def test_envoi_mail(self):
        
        # GIVEN
        expected_result = None
        mail = "coralie.cottet@hotmail.fr"

        # WHEN
        result = self.admin.envoi_mail(mail)

        # THEN
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()