from entity import *




class Mob(Entity) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée !
        super().__init__(file_name, scaling, img_width, img_height, coords)
        
        self.status = 0  
        
        # Position / Image de départ
        self.init_x_pos = 0
        self.init_y_pos = 0
        
        # Compteur pour le nombre maximal de déplacements (aléatoire)
        self.init_count_tick_move = 0
        # Compteur courant
        self.current_count_tick_move = 0
        
        
    # Position initiale éventuellement aléatoire     
    def set_init_position(self, x_pos, y_pos):
        pass
        # Placement du mob 
        # Attention : Tenir compte de MAP_SCALING
       
        # Initialisation des attributs `init_x_pox` et `init_y_pos`
        
        

           
    def setup(self) :
        # Chargement des textures (appel au parent)
        super().setup()
        
        
        # Ouverture du fichier JSON file
        # Chargement des caractéristiques du mob
        
 
        # Fermeture du fichier
        
        
        # Texture initiale à afficher
        self.texture = self.textures[0][0]
        
        
        
    def update(self) :
        # Mise à jour de l'animation
        
            
                
        # Si changement de type de déplacement
        
        
        # Mise à zéro du déplacement
        self.change_x, self.change_y = 0,0    

        # Nouvelle texture à afficher
        self.texture = self.textures[self.status][self.current_texture_indice]
            
        
        