
# ---- Library ---- #

import requests
from bs4 import BeautifulSoup
import csv
from dao.critereDAO import CritereDAO


class Critere:
    """
    Une Critere est caractérisé par une commune cible, une spécialité, 
    une duree min et max de stage et des tailles d'entreprises dans lesquelles l'utilisateur
    est disposé à faire un stage.
    """
    def __init__(
        self,
        ville_cible: str,
        rayon_km: float,
        specialite: str,
        duree_min: int,
        duree_max: int
            ):
        ''' Constructeur d'un objet Critere'''
        self.ville_cible = ville_cible
        # convertion en majuscule
        self.specialite = specialite.upper()
        self.duree_min = duree_min
        self.duree_max = duree_max
        self.rayon_km = rayon_km
        self.id_crit = CritereDAO().calcul_id(self)
    
    def __str__(self):
        res = "id_crit: {} \nCommune cible: {} \nSpecialite du stage: {} \nDurée minimum du stage: {} \nDurée maximum du stage: {}".format(self.id_crit, self.ville_cible, self.specialite, self.duree_min, self.duree_max)
        return res
    
    def __eq__(self, other):
        return self.id_crit == other.id_crit
        
    def recherche_stage(self):

        # specialite_input = input("Entrez le type de stage que vous recherchez : ")
        # location_input = input("Dans quelle localité ? ")
        # radius_input = input("Dans un rayon de combien de kilomètres ? ")

        specialite_input = self.specialite
        location_input = self.ville_cible
        radius_input = self.rayon_km

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

    def existe(self):
        return CritereDAO().exist_id(self)

    def enregistrer_critere(self):
        if not self.existe():
            CritereDAO().add(self)

    def supprimer_critere(self):
        if self.existe():
            CritereDAO().delete(self)
    
    @classmethod
    def charger_critere(self, id_crit):
        res = CritereDAO().charger_critere(id_crit)
        if not res:
            raise "L'identifiant n'existe pas"
        return Critere(res["ville_cible"], res["rayon_km"], res["specialite"], res["duree_min"], res["duree_max"])

