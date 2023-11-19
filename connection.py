# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/01 20:00:47 by cosaph            #+#    #+#              #
#    Updated: 2023/11/19 20:11:40 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import psycopg2
from dao.userDao import UserDao


def create_tables():
    conn = psycopg2.connect(database="postgres", user="postgres", host="localhost", password = "01062000")
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