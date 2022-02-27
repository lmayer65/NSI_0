from constants import *
import json


class Entity(arcade.Sprite) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée et non
        # la taille totale !
        super().__init__(file_name, scaling, 0, 0, img_width, img_height)
        
        self.file_name = file_name  # Nom du fichier des animations
        self.scaling = scaling      # Réduction / agrandissement
        self.img_width = img_width    # Largeur de la PARTIE de l'image à afficher
        self.img_height = img_height  # Hauteur de la PARTIE de l'image à afficher 
        
        self.coords = coords    # Coordonnées des parties de l'image (texture) à afficher
        self.textures= []       # Ensemble des textures à charger en fonction des postures
        self.current_texture_indice = 0   # Numéro de la texture à afficher
        
        self.center_x = 0       # Abscisse ABSOLUE du centre de l'entité
        self.center_y = 0       # Ordonnée ABSOLUE du centre de l'entité
        self.attributes = {}    # Caractéristiques de l'entité (Points de vie etc .)
        
                
    def setup(self) :
        # Chargement des animations du mob
        pass
                     
    
    def update(self) :
        pass


