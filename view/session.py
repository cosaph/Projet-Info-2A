# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    session.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:59:36 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 17:45:40 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.singleton import Singleton


class Session(metaclass=Singleton):
    
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.user_name: str = ":)"