
# ---- Library ---- #

import requests
from bs4 import BeautifulSoup
import csv
from dao.critereDAO import CritereDAO
# from metier.stage import Stage


class Critere:
    """
    Une Critere est caractérisé par une commune cible, une spécialité, 
    une duree min et max de stage et des tailles d'entreprises dans lesquelles l'utilisateur
    est disposé à faire un stage.
    """
    def __init__(
        self,
        localisation: str,
        rayon: float,
        critere: str
        # duree_min : float
        # duree_max : float
            ):
        ''' Constructeur d'un objet Critere'''
        self.localisation = localisation
        # convertion en majuscule
        self.critere = critere.upper()
        self.rayon = rayon
        self.id_crit = CritereDAO().calcul_id(self)
        # self.duree_min = duree_min
        # self.duree_max = duree_max

    # def __str__(self):
    #     res = "id_crit: {} \nCommune cible: {} \nSpecialite du stage: {} \nDurée minimum du stage: {} \nDurée maximum du stage: {}".format(self.id_crit, self.ville_cible, self.specialite, self.duree_min, self.duree_max)
    #     return res

    def __eq__(self, other):
        return self.id_crit == other.id_crit
        
    def recherche_stage(critere, localisation, rayon):
        params = {'q': critere, 'l': localisation, 'stage': critere, 'location': localisation, 'radius': rayon}
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
                tableau.append({
                    'url': link_element['href'],
                    'title': link_element.text,
                    'location': location_element
                })

        return tableau
            
    def exportation_csv(critere, localisation, rayon):
        # Perform the job search and retrieve the data
        tableau = Critere.recherche_stage(critere, localisation, rayon)
    
        # Define the CSV file path
        csv_file = 'job_offers.csv'
    
        # Prepare the CSV file headers
        fieldnames = ['URL', 'Title', 'Location']
    
        # Write the data to the CSV file
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
        
            # Write the headers to the CSV file
            writer.writeheader()
        
            #  Write each job offer data to the CSV file
            for item in tableau:
                writer.writerow({'URL': item['url'], 'Title': item['title'], 'Location': item['location']})

        print(f"Job offers exported to '{csv_file}' successfully.")

    def existe(self):
        return CritereDAO().exist_id(self)

    def enregistrer_critere(self):
        if not self.existe():
            CritereDAO().add(self)

    def supprimer_critere(self):
        if self.existe():
            CritereDAO().delete(self)
    
    @classmethod
    def charger_critere(self, id_crit, verbose=False):
        # rrrr A mon avis ca ne marche plus
        res = CritereDAO().charger_critere(id_crit)
        if not res:
            raise "L'identifiant n'existe pas"
        res = Critere(
            localisation=res["ville_cible"],
            rayon=res["rayon_km"],
            critere=res["specialite"],
            duree_min=res["duree_min"],
            duree_max=res["duree_max"]
            )
        if verbose:
            print(res)
        return res

