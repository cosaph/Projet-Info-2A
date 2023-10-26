# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/26 10:06:06 by cosaph            #+#    #+#              #
#    Updated: 2023/10/26 10:08:01 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from test_eleve import TestEleve
from unittest import TextTestRunner, TestLoader

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCaassertIsInstancse(TestEleve)
    )

