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
        for p_sprite in self.coords :
            s_textures = []
            for i in range(len(p_sprite)) :
                s_texture = arcade.load_texture(self.file_name, p_sprite[i][0], \
                    p_sprite[i][1], self.img_width, self.img_height)
                s_textures.append(s_texture)
            self.textures.append(s_textures)
                     
    
    def update(self) :
        pass


