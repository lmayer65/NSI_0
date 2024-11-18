from entity import *




class Mob(Entity) :
    def __init__(self, file_name, scaling, img_width, img_height, coords) :
        # Attention, bien indiquer la taille de l'image qui sera affichée !
        super().__init__(file_name, scaling, img_width, img_height, coords)
        
        self.status = 0  
        
        # Position / Image de départ
        self.init_x_pos = 0
        self.init_y_pos = 0
        
        # Compteur pour le nombre de déplacement
        self.initcount_tick_move = randint(50,200)
        self.current_count_tick_move = 0
        
        
        
    def set_name(self, name) :
        pass
        ##### A COMPLETER #####
        
    def set_init_position(self, x_pos, y_pos):
        pass
        ##### A COMPLETER #####
        

           
    def setup(self) :
        # Chargement des textures
        super().setup()
        
        
        # Ouverture du fichier JSON file
        # Chargement des caractéristiques du monstre
        f = open(ORC_CAR_FILE)
        
        ##### A COMPLETER #####
 
        # Fermeture du fichier
        f.close()
        
        # Initialisation du statut et de la texture
        self.status = 0 
        self.texture = self.textures[0][0]
        
        
        
    def update(self) :
        # Ralentissement de la vitesse d'animation
        ##### A COMPLETER #####
        
        # Si l'indice courant de la texture dépasse le nombre d'images de l'animation
        # en cours, on revient à l'indice de la texture de départ.
        ##### A COMLETER #####
        
        
        # Déplacement du monstre (jusqu'au bout du compteur initialisé)    
        if self.current_count_tick_move < self.init_count_tick_move :
            if self.status == WALK_DOWN :
                self.change_y = -self.attributes['Speed']
            ##### A COMPLETER #####
            
            # Déplacement du monstre
            ##### A COMPLETER #####
            
            # Incrémentation du compteur de mouvement
            self.current_count_tick_move += 1 
        # Déplacement aléatoire et réinitialisation des attributs    
        else :
            # Remise à zéro du compteur et de l'indice de la texture à afficher
            self.current_count_tick_move = 0
            self.current_texture_indice = 0
            
            # Nouveau type de déplacement (self.status)
            ##### A COMPLETER #####
            
            # Initialisation aléatoire du nombre de déplacements 
            # (self.init_count_tick_move).
            ##### A COMPLETER #####
            
        # Réinitialisation du déplacement et nouvelle texture     
        self.change_x, self.change_y = 0,0                
        self.texture = self.textures[self.status][self.current_texture_indice]
            
        
        