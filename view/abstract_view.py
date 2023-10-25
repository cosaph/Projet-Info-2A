# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    abstract_view.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:59:09 by cosaph            #+#    #+#              #
#    Updated: 2023/10/25 14:19:11 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod

from view.session import Session


class AbstractView(ABC):

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def make_choice(self):
        pass
