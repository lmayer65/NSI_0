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
        self.init_count_tick_move = randint(50,200)
        self.current_count_tick_move = 0
        
        
        
    def set_name(self, name) :
        self.attributes['Name'] = name
        
    def set_init_position(self, x_pos, y_pos):
        pass
        
        

           
    def setup(self) :
        # Chargement des textures
        super().setup()
        
        
        # Ouverture du fichier JSON file
        # Chargement des caractéristiques du joueur
        f = open('Mobs/mob.json')
        data = json.load(f)
        
        for key,value in data[self.attributes['Name']].items():
            self.attributes[key] = value
 
        # Fermeture du fichier
        f.close()
        
        #P Etat initial du joueur
        self.status = 0 
        self.texture = self.textures[0][0]
        
        
        
    def update(self) :
        # Diminue la vitesse d'animation
        
        
        # Animation du monstre
        
            
                
        # Si changement de type de déplacement
        
        
        # Réinitialisation de l'état du monstre (statut et texture)
        self.change_x, self.change_y = 0,0                
        self.texture = self.textures[self.status][self.current_texture_indice]
            
        
        