# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/01 20:00:47 by cosaph            #+#    #+#              #
#    Updated: 2023/11/07 17:01:59 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import psycopg2


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