# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/20 19:19:17 by cosaph            #+#    #+#              #
#    Updated: 2023/09/21 12:15:01 by cosaph           ###   ########.fr        #
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

cursor.execute("""
  CREATE TABLE recherche_stages (
       id TEXT,
       titre TEXT,
       URL TEXT,
       location TEXT
   )
""") 
               
id = 1
titre = "Stage consultant(e) Data analyst - Secteur Luxe F/H"
url = "https://www.example.com/stage-data-analyst"
location = "Paris, France"

query = "INSERT INTO recherche_stages (id, titre, URL, location) VALUES (%s, %s, %s, %s)"
values = (id, titre, url, location)

cursor.execute(query, values)     
      


with open('/home/cosaph/ENSAI2A/projet_info/projet/jobs.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
       "INSERT INTO recherche_stages VALUES (%s, %s, %s)",
       row
    )
        
    
conn.commit()

cursor.execute("SELECT * FROM recherche_stages")
rows = cursor.fetchall()

for row in rows:
    print("titre:", row[0])
    print("URL:", row[1])
    print("location:", row[2])
    print("-------------------")
        

