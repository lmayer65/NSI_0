from entity import *



class Player(Entity) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée !
        super().__init__(file_name, scaling, img_width, img_height, coords)
        
        self.status = 0  # Etat du joueur (animation) : walk_left par exemple
        
        # Position de départ
        self.init_x_pos = 0  # En abscisse
        self.init_y_pos = 0  # En ordonnée
        
        
        
       
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
        # ATTENTION à l'échelle de la carte.
        
        
        
        # Texture de départ : à la base, joueur se déplaçant vers le bas
        self.texture = self.textures[0][0]
        
        
            
    def update(self) :
        # Le joueur doit rester sur la map
        # Les abscisses, ne pas dépasser la largeur de la map
        # ATTENTION à l'échelle de la carte.
        
            
        # Puis les ordonnées, ne pas dépasser la hauteur de la map
        # ATTENTION à l'échelle de la carte.
            
            
        # Animation
        # Si le joueur ne bouge pas, pas d'animation
        if not self.change_x and not self.change_y :
            return
    
            
    
        # Si changement de type de déplacement
        
            
        
        # Image suivante sauf si l'on est à la fin de l'animation (retour au début)
        
        
        
        # Nouvelle texture à charger
        self.texture = self.textures[self.status][self.current_texture_indice]
       
        
               
        
        
            
        
            