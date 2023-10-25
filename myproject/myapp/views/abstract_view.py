from abc import ABC, abstractmethod

class AbstractView(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display_info(self):
        pass
    
    @abstractmethod
    def make_choice(self, request):
        pass

#
    #display_info() : qui va juste déterminer l'affichage en console
    #make_choice() : qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
