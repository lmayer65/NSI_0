from entity import *



class Player(Entity) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée !
        super().__init__(file_name, scaling, img_width, img_height, coords)
        
        self.status = 0  
        
        # Position / image de départ
        self.init_x_pos = 0 
        self.init_y_pos = 0
        
        # Monstre cliqué (s'il y a)
        self.clicked_mob = None
        
        
        
       
    def setup(self) :
        # Chargement des textures
        super().setup()
        
        
        # Ouverture du fichier JSON file
        # Chargement des caractéristiques du joueur
        f = open(PLAYER_CAR_FILE)
        ##### A COMPLETER #####
 
        # Fermeture du fichier
        f.close()
        
        
        # Position / Etat de départ
        self.center_x = self.attributes['Init_x'] * MAP_SCALING
        self.init_x_pos = self.center_x
        ##### A COMPLETER #####
        
        # Statut et texture de départ : à la base, le joueur est vers le bas
        self.status = WALK_DOWN 
        self.texture = self.textures[self.status][0]
        
        
            
    def update(self) :
        ######################## DEPLACEMENT #########################

        # Le joueur doit rester sur la map
        # Les abscisses, ne pas dépasser la largeur de la map
        # ATTENTION à l'échelle de la carte (MAP_SCALING)
        ###### A COMPLETER ###### 
            
        # Puis les ordonnées, ne pas dépasser la hauteur de la map
        ###### A COMPLETER ###### 
            
            
            
        ######################## ANIMATION ###########################

        # Si le joueur ne bouge pas, pas d'animation
        if not self.change_x and not self.change_y :
            return
        

        # Passage à la texture suivante (animation)
        self.current_texture_indice += 1
        
        # Image suivante sauf si l'on est à la fin de l'animation (retour au début)
        if self.current_texture_indice >= len(self.textures[self.status]) :
            self.current_texture_indice = 0
    
            
        # Si changement de type de déplacement
        if self.change_x < 0 :
            self.status = WALK_LEFT 
            self.current_texture_indice = 0
        ##### A COMPLETER #####
        
        # Nouvelle texture à afficher
        self.texture = self.textures[self.status][self.current_texture_indice]
       
        
               
        
        
            
        
            