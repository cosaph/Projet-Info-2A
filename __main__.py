
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

database = input(" Le nom de votre base de donnée : ")
user = input(" Le nom de votre user : ")
host = input(" Le nom de votre host : ")
password = input(" Le mot de passe de votre base de donnée : ")

def create_tables():
    conn = psycopg2.connect(database= "postgres", user = "postgres", host = "localhost", password = "01062000")
    cursor = conn.cursor()

    with open("data/bdd_projet_info.sql", "r") as f:
        sql = f.read()
        cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()

create_tables()


# Création d'un admin et de deux utilisateurs pour les tests de l'application 
# L'admin est créé avec l'adresse mail et le mot de passe suivant : "m", "m"
# Les deux utilisateurs sont créés avec les adresses mails et les mots de passe suivants : "a", "a" et "b", "b"
UserDao().creer_un_admin()

UserDao().creer_deux_exemeple()


# This script launch the application

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    #logger.info("START")   
    
    # run the Start View
    current_view = StartView()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        #with open("graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            #print(asset.read())
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()

    with open(
        "graphical_assets/suprised_pikachu.txt", "r", encoding="utf-8"
    ) as asset:
        print(asset.read()) 






