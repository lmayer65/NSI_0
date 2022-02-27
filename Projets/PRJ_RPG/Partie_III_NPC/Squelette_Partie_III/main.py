from map import *
from player import *
from mob import *
from application import *
from gui import *



# Classe de base du jeu
class My_Game(Window):  # Hérite de la classe `Window`
    def __init__(self):
        # Création de la fenêtre 
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
          
        self.map = None         # Carte du jeu
       
        self.scene = None       # Permet d'afficher la carte (Arcade)
        self.physics_engine = None  # Moteur physique d'Arcade
        self.camera = None      # Vue sur la carte (Arcade)
        
        self.player = None      # Gestion du joueur
        self.mobs = []          # Gestion des monstres (d'où la liste)
        self.sprites_list = None  # Affichage des mobs (Arcade)
        
        self.gui = None         # Gestion de l'IHM



    def setup(self):
        # Couleur de fond de la map.
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        # Création de la caméra
        
        
        # Création de la map
        self.map = Map()
        self.map.setup()
        self.scene = arcade.Scene.from_tilemap(self.map.tile_map)
        
        
        # Liste des mobs à afficher
        
                
        # Création du joueur
       

        # Ajout du joueur dans la list de mobs à afficher
        # ATTENTION : avant l'appel au setup(), plantage sinon !!
        
        
                   
        # Création de X orcs placés aléatoirement, X au choix :)
        
            
        # ATTENTION : avant l'appel au setup(), plantage sinon !!
        
       
        # Création du moteur physique (déplacement et collision du joueur)
       
                
        # Création de l'IHM
      
        
        

    
    def on_key_press(self, key, modifiers):
        pass
        # Mouvements du joueur
        
        
        
    def on_key_release(self, key, modifiers):
        pass
        # Fin de mouvement du joueur
        
             
    
    def on_mouse_press(self, x, y, button, modifiers) :
        pass
        # Attention à transformer les coordonnées relatives en coordonnées absolues
        
      
        
      
    def on_update(self, delta_time):
        pass
        # Déplace le joueur, gère les collisions avec les objets de la map
       
         
        # Mise à jour du joueur
       
        
       
        # Mise à jour des mobs
        
       
        
        # Positionne la caméra sur le joueur
      
      
    
        # Permet de centrer la caméra sur le joueur
        
        
        
    def center_camera_to_player(self):
        pass
            
      
        
      
    def on_draw(self):
        # Efface l'écran
        self.clear()
        
        # Activation de la caméra
        

        # Affichage de la scène (map)
        self.scene.draw()
        
        # Affichage des mobs
        
        
        # Affichage de l'IHM
  
        

        



# Fonction principale
# NE PAS CHANGER
def main():
    # Instance de My_Game()
    window = My_Game()
    window.setup()
    
    # Lancement du jeu
    arcade.run()


if __name__ == "__main__":
    main()