from constants import *



class Map :
    def __init__(self) :
        self.tile_map = None
        
        
    def setup(self) :
        # Traitement des calques à collisions.
        layers_options = {
            "ground_collide1" : {"use_spatial_hash": True },
            "nature_collide2" : {"use_spatial_hash": True },
            "house_collide2" : {"use_spatial_hash": True }
        }
        
        # Charge la map en format .json
        self.tile_map = arcade.load_tilemap(MAP_FILE, MAP_SCALING, layers_options)
        
        
