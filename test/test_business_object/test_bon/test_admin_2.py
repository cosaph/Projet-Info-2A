# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_admin_2.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/26 15:53:25 by cosaph            #+#    #+#              #
#    Updated: 2023/10/26 15:55:05 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.insert(0,"/home/cosaph/ENSAI2A/projet")
from metier.eleve import Eleve
from metier.admin import Admin


from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch

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