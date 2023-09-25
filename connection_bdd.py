# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection_bdd.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/25 15:59:34 by cosaph            #+#    #+#              #
#    Updated: 2023/09/25 16:07:34 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import psycopg2
import csv


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="0106200",
    host="localhost",
    port="5432"
)


cursor = conn.cursor()

# -------- remplissage de la table -------- #                


with open('/home/cosaph/ENSAI2A/projet_info/projet/jobs.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cursor.execute(
       "INSERT INTO recherche_stages VALUES (%s, %s, %s)",
       row
    )
        
    
conn.commit()

# -------- Affichage de la table -------- #
cursor.execute("SELECT * FROM recherche_stages")
rows = cursor.fetchall()

for row in rows:
    print("titre:", row[0])
    print("URL:", row[1])
    print("location:", row[2])
    print("-------------------")
        

