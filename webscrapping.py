# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    webscrapping.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/08/30 15:10:14 by cosaph            #+#    #+#              #
#    Updated: 2023/09/01 22:39:21 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# --- Library --- #

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.stage.fr/jobs/?q=data&l='
response = requests.get(url)
""" 
soup = BeautifulSoup(response.text, 'html.parser')
[print((str(li) + '\n')) for li in liste]
 """

soup = BeautifulSoup(response.text, 'html.parser')
div_elements = soup.find_all('div', class_='media-heading listing-item__title')
span_elements = soup.find_all('span', class_ = 'listing-item__info--item listing-item__info--item-location')

tableau = []


for i in range(len(div_elements)):
    link_elements = div_elements[i].find_all('a')
    location_element = span_elements[i].text

    for link_element in link_elements:
        title = link_element.text
        url = link_element['href']
        tableau.append([title, url, location_element])



# Exporter le tableau dans un fichier CSV
with open('resultats.csv', 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['Titre', 'URL', 'Location'])  # Écrire les en-têtes des colonnes
    writer.writerows(tableau)

print("Exportation vers le fichier CSV terminée.")