# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    creation_bdd.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/20 19:19:17 by cosaph            #+#    #+#              #
#    Updated: 2023/09/25 16:04:45 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import psycopg2

# -------- On se connecte à la base de données -------- #
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="0106200",
    host="localhost",
    port="5432"
)

# -------- Le curseur -------- #

cursor = conn.cursor()

# -------- Creation de la table recherche_stages -------- #
cursor.execute("""
  CREATE TABLE recherche_stages (
       id TEXT,
       titre TEXT,
       URL TEXT,
       location TEXT
   )
""") 

