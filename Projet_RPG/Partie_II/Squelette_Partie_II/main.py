from mapy import *
from player import *
from mob import *
from gui import *



# Classe de base du jeu
class My_Game(arcade.Window):  
    def __init__(self):
        # Création de la fenêtre 
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
          
        self.map = None
       
        self.scene = None
        self.physics_engine = None
        self.camera = None
        
        self.player = None
        self.mobs = []
        self.sprites_list = None
        
        self.gui = None
        


    def setup(self):
        # Couleur de fond de la map.
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        # Création de la caméra
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Création de la map
        self.map = Map(self)
        self.map.setup()
        self.scene = arcade.Scene.from_tilemap(self.map.tile_map)
        self.map.set_collisions()
        
        # Liste des mobs à afficher
        self.sprites_list = arcade.SpriteList()
        
        
        # Création du joueur
        ##### A COMPLETER #####

        # Ajout du joueur dans la list de mobs à afficher
        # ATTENTION : avant l'appel au setup(), plantage sinon !!
        #### A COMPLETER #####
        
                   
        # Création de X orcs placés aléatoirement, X au choix :) 
        # A placer dans la liste 'self.mobs'
        ##### A COMPLETER #####
        

        # ATTENTION : avant l'appel au setup(), plantage sinon !!
        for mob in self.mobs :
            self.sprites_list.append(mob)
            mob.setup()
       
        # Gestion des collisions du joueur avec la carte (si joueur)
        if self.player :
            self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.map.walls)
        
        
        # Création de l'IHM (GUI)
        ##### A COMPLETER #####
        
        

    
    def on_key_press(self, key, modifiers):
        # Si pas encore de joueur
        if not self.player :
            return 

        # Mouvements du joueur
        if key == arcade.key.LEFT : # Vers la gauche
            self.player.change_x = -self.player.attributes['Speed']
        ##### A COMPLETER #####
        elif key == arcade.key.LEFT : # Déciblage d'un monstre
            self.gui.update()
        
      
    def on_key_release(self, key, modifiers):
        # Si pas encore de joueur
        if not self.player :
            return
        
        # Fin de mouvement du joueur
        if key == arcade.key.LEFT :
            self.player.change_x = 0
        ##### A COMPLETER ######
                                   
    
        
        
    def on_mouse_press(self, x, y, button, modifiers) :
        # Si pas encore de joueur
        if not self.player :
            return
        
        # Attention à transformer les coordonnées relatives en coordonnées absolues
        new_x = 0       ##### A MODIFIER #####
        new_y = 0       ##### A MODIFIER #####
        
        # Récupère ce qui a été cliqué sous forme de liste
        clicked_mob = arcade.get_sprites_at_point((new_x, new_y), self.sprites_list)
        
        # Si un monstre a bien été choisi et qui n'est pas le joueur (un seul en même temps)
        if len(clicked_mob) > 0 :
            self.player.clicked_mob = clicked_mob[0] # clicked_mob[0] est ciblé par le joueur
     
        # Mise à jour de l'IHM
        self.gui.update()
      
        
      
    def on_update(self, delta_time):
        # Si pas encore de joueur
        if not self.player :
            return
        
        # Déplace le joueur, gère les collisions avec les objets de la map
        self.physics_engine.update() 
             
        # Mise à jour du joueur
        ##### A COMPLETER #####
        
        # Mise à jour des mobs
        ##### A COMPLETER #####
              
        # Positionne la caméra sur le joueur
        self.center_camera_to_player()
      
    
    # Permet de centrer la caméra sur le joueur
    def center_camera_to_player(self):
        # Si pas encore de joueur
        if not self.player :
            return
        
        screen_center_x = self.player.center_x - self.camera.viewport_width//2
        screen_center_y = self.player.center_y - self.camera.viewport_height//2
  
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)         
      
        
      
    def on_draw(self):
        # Efface l'écran
        ##### A COMPLETER #####
        
        # Activation de la caméra
        self.camera.use()

        # Affichage de la scène (map)
        self.scene.draw()
        
        # Affichage des mobs
        ##### A COMPLETER #####
        
        # Affichage de l'IHM (GUI)
        ##### A COMPLETER ####
        

        



# Fonction principale
def main():
    window = My_Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()