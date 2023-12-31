
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:56:13 by cosaph            #+#    #+#              #
#    Updated: 2023/10/26 12:01:34 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import dotenv
import psycopg2

from view.start_view import StartView
from dao.userDao import UserDao
#from loguru import logger

#This script is the entry point of the application



# This script launch the application

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    #logger.info("START")   
    
    # run the Start View
    current_view = StartView()


    # while current_view is not none, the application is still running
    while current_view:
        # clear the terminal
        

        # a border between view
        #with open("graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            #print(asset.read())
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()
        #import os
        #os.system("clear")

    with open(
        "graphical_assets/suprised_pikachu.txt", "r", encoding="utf-8"
    ) as asset:
        print(asset.read()) 





