from constants import *
import json


class Entity(arcade.Sprite) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée et non
        # la taille totale !
        super().__init__(file_name, scaling, 0, 0, img_width, img_height)
        
        self.file_name = file_name
        self.scaling = scaling
        self.img_width = img_width
        self.img_height = img_height
        
        self.coords = coords
        self.textures= []
        self.current_texture_indice = 0
        
        self.center_x = 0
        self.center_y = 0
        self.attributes = {}
        
                
    def setup(self) :
        # Chargement des animations du joueur en fonction de son statut
        pass
                     
    
    def update(self) :
        pass


