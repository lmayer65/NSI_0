from application import *
from constants import *
import arcade
import arcade.gui
from main import *



class QuitButton(arcade.gui.UIFlatButton):
    def set_window(self,game) :
        self.game = game
        
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        self.game.close()
        
        
        
class Gui() :
    def __init__(self,game) :
        self.game = game
        self.game.manager = arcade.gui.UIManager()
        self.game.manager.enable()
        
        self.menu_bar = None   # Menu du jeu
        self.player_box = None # Affiche les caractéristiques principales du joueur
        self.clicked_mob_box = None # Affiche les caractéristiques principales du mob cliqué
        
        
    # Création du menu du jeu
    def create_game_menu(self) :
        pass
        
    
    # Caractéristiques principales du joueur
    def create_player_box(self) :
        pass
        
        
        
    # Caractéristiques du monstre cliqué
    def create_clicked_mob_box(self, clicked_mob) :
        pass
        
        
    # IHM de base    
    def setup(self) :
        pass
        
              
        
        
        
        
    
    # IHM de base avec un monstre de cliqué
    def add_clicked_mob(self, clicked_mob) :
        pass
        
        
        
        
        
    def draw(self) :
        pass
        
        
        
