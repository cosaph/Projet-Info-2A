# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    unuser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 23:08:30 by cosaph            #+#    #+#              #
#    Updated: 2023/11/02 23:10:51 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from dao.assoStageUserDao import AssoStageUserDao
from dao.assoCritUserDAO import AssoCritUserDao
from dao.userDao import UserDao
from dao.critereDAO import CritereDAO
from dao.stageDAO import StageDao
from metier.listEnvie import ListEnvie
from metier.userNonAuthentifie import UserNonAuthentifie
from metier.stage import Stage
from metier.critere import Critere


class unUser(UserNonAuthentifie) :

    def ajouter_stageAuser(self, unStage):
        if self.possede_stage(unStage):
            raise "L' utilisateur a déjà ce stage dans la liste envie"
        if not unStage.existe():
            unStage.enregistrer_stage()
        self.list_envie.ajouter_stage(unStage)
        return AssoStageUserDao().add(unStage, self)