# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection_bdd.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/25 15:59:34 by cosaph            #+#    #+#              #
#    Updated: 2023/09/29 18:25:23 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import psycopg2
import csv


conn = psycopg2.connect(
    dbname="id7335",
    user="id7335",
    password="id7335",
    host="sgbd-eleves.domensai.ecole",
    port="5432"
)

cursor = conn.cursor()

"""
# -------- remplissage de la table -------- #    

  
# -------- Supprimer le contenu d'une table --------#

table_name = "recherche_stages"
query = f"DELETE FROM {table_name}"
cursor.execute(query)

# -------- Re-remplir la table avec les nouvelles données  -------- #

with open('/home/cosaph/ENSAI2A/projet_info/projet/jobs.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cursor.execute(
       "INSERT INTO recherche_stages VALUES (%s, %s, %s)",
       row
    )
        

"""        
# -------- Valider les modifications et fermer la connexion -------- #



# -------- Affichage de la table -------- #

cursor.execute("SELECT * FROM projetInfo.critere")
rows = cursor.fetchall()

for row in rows:
    print("titre:", row[0])
    print("URL:", row[1])
    print("location:", row[2])
    print("-------------------") 
        

conn.commit()
cursor.close()
conn.close()