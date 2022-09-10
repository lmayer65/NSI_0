from entity import *


class Player(Entity) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée !
        super().__init__(file_name, scaling, img_width, img_height, coords)
        
        self.status = 0  
        
        # Position / PV de départ
        self.init_x_pos = 0 
        self.init_y_pos = 0
        self.init_hp = 0
        
        
        
       
    def setup(self) :
        # Chargement des textures
        super().setup()
        
        
        # Ouverture du fichier JSON file
        # Chargement des caractéristiques du joueur
        f = open("Mobs/player.json")
        data = json.load(f)
        
        for key,value in data["Player"].items():
            self.attributes[key] = value
 
        # Fermeture du fichier
        f.close()
        
        
        # Position / Etat / Image de départ
        
        
        
            
    def update(self) :
        # Le joueur doit rester sur la map
        # Les abscisses, ne pas dépasser la largeur de la map
        
            
        # Puis les ordonnées, ne pas dépasser la hauteur de la map
        
            
            
        # Animation
        # Si le joueur ne bouge pas, pas d'animation
        
    
            
        # Si changement de type de déplacement
        
            
        # Image suivante sauf si l'on est à la fin de l'animation (retour au début)
        pass
       
        
               
        
        
            
        
            