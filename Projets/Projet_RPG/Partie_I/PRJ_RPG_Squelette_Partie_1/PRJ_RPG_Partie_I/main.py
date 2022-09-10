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
        
        
        # Création de la map
        self.map = Map()
        self.map.setup()
        self.scene = arcade.Scene.from_tilemap(self.map.tile_map)
        
        # Liste des mobs à afficher
        
        
        
        # Création du joueur
        

        # Ajout du joueur dans la list de mobs à afficher
        # ATTENTION : avant l'appel au setup(), plantage sinon !!
        
        
        # Création de 15 orcs
           
        
        # Ajout des orcs dans la list de mobs à afficher
        # ATTENTION : avant l'appel au setup(), plantage sinon !!
        
       
        # Création du moteur physique (déplacement et collision du joueur)
        walls = [self.scene["ground_collide1"],self.scene["nature_collide2"],
                 self.scene["house_collide2"]]

        
        
        # Création de l'IHM
        
        
        

    
    def on_key_press(self, key, modifiers):
        # Mouvements du joueur
        pass
        
        
    def on_key_release(self, key, modifiers):
        # Fin de mouvement du joueur
        pass
             
    
    def on_mouse_press(self, x, y, button, modifiers) :
        # Attention à transformer les coordonnées relatives en coordonnées absolues
       
      
        # Récupère la liste d'entités cliquées
        
        
        # Si clic sur une entité (un seul à priori)
        
        # Sinon on affiche la GUI basique (menu + joueur)
        
        pass
      
  
      
    def on_update(self, delta_time):
        # Déplace le joueur, gère les collisions avec les objets de la map
        
        
         
        # Mise à jour du joueur
        
        
        # Mise à jour des mobs
        
       
        
        # Positionne la caméra sur le joueur
        
        pass
      
    
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
def main():
    window = My_Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()