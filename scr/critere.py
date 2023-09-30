""" from dao.critereDAO import CritereDAO  """

# ---- Library ---- #

import requests
from bs4 import BeautifulSoup
import csv



class Critere:
    """
    Une Critere est caractérisé par une commune cible, une spécialité, 
    une duree min et max de stage et des tailles d'entreprises dans lesquelles l'utilisateur
    est disposé à faire un stage.
    """
    def __init__(self, 
<<<<<<< HEAD
                code_insee_cible: str,
                rayon_km : float,
                specialite: str,
=======
                code_insee_cible: str, 
                rayon_km : float, 
                specialite: str, 
>>>>>>> e53d40698734f993256eb13ec40f8a73c172c602
                duree_min: int, 
                duree_max: int):
        ''' Constructeur d'un objet Critere'''
        self.code_insee_cible = code_insee_cible
        # convertion en majuscule
        self.specialite = specialite.upper()
        self.duree_min = duree_min
        self.duree_max = duree_max
        self.rayon_km = rayon_km
        self.id = CritereDAO().calcul_id(self)
    
    def __str__(self):
        res = "id: {} \nCommune cible: {} \nSpecialite du stage: {} \nDurée minimum du stage: {} \nDurée maximum du stage: {}".format(self.id, self.code_insee_cible, self.specialite, self.duree_min, self.duree_max)
        return res
        
    def recherche_stage(self):

        specialite_input = input("Entrez le type de stage que vous recherchez : ")
        location_input = input("Dans quelle localité ? ")
        radius_input = input("Dans un rayon de combien de kilomètres ? ")

        params = {'q': specialite_input, 'l': location_input, 'stage': specialite_input, 'location': location_input, 'radius': radius_input}
        url = requests.Request('GET', 'https://www.stage.fr/jobs/', params=params).prepare().url
        """ url = requests.Request('GET', 'https://emploi.lefigaro.fr/', params=params).prepare().url """

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        div_elements = soup.find_all('div', class_='media-heading listing-item__title')
        span_elements = soup.find_all('span', class_='listing-item__info--item listing-item__info--item-location')

        tableau = []

        for i in range(len(div_elements)):
            link_elements = div_elements[i].find_all('a')
            location_element = span_elements[i].text

        for link_element in link_elements:
            title = link_element.text
            url = link_element['href']
            tableau.append([title, url, location_element])

        with open('jobs.csv', 'w', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(['Titre', 'URL', 'Location'])
            writer.writerows(tableau)

        print("Exportation vers le fichier CSV terminée.")

    def enregistrer_critere(self):
        pass
    
    def supprimer_critere(self):
        pass

    def recherche_stage(self, url_site):
        pass