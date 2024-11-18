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
        # Permet d'accéder à tous les éléments du jeu
        self.game = game
        # Permet de générer une IHM dans la fenêtre du jeu
        self.game.manager = arcade.gui.UIManager()
        self.game.manager.enable()
        
        self.menu_bar = None   # Menu du jeu
        self.player_box = None # Affiche les caractéristiques principales du joueur
        self.clicked_mob_box = None # Affiche les caractéristiques principales du mob cliqué
        
        
    # Création du menu du jeu (réduit ici au bouton Quit)
    def create_game_menu(self) :
        # Création d'une box horizontale
        ########## A COMPLETER #########
        
        # Quitter le jeu
         ########## A COMPLETER #########
        
        # Associe ce bouton au jeu à quitter (game)
         ########## A COMPLETER #########
        
        # Ajut du bouton dans la box et placement en bas/ droite de l'écran
         ########## A COMPLETER #########

        pass
        
    
    # Caractéristiques principales du joueur
    def create_player_box(self) :
        # Création de la box principale (horizontale)
        self.player_box = arcade.gui.UIBoxLayout(vertical = False)
        
        # Création d'un bouton texturé pour acueillir l'image du joueur
        ##### A COMPLETER #####
        
        ##### A COMPLETER #####     # Ajout dans la box
        
        # Création d'une box verticale
        v_box_2 = arcade.gui.UIBoxLayout()
        
        # Création de deux labels pour le nom et le nombre d'HP du joueur
        ##### A COMPLETER #####
        ##### A COMPLETER #####
        
        # Ajout des labels dans v_box_2
        ##### A COMPLETER #####
        
        # Ajout de v_box_2 dans la box principale (joueur)
        self.player_box.add(v_box_2)
        
    
        
        
    # Caractéristiques du monstre cliqué
    def create_clicked_mob_box(self, clicked_mob) :
        # Création de la box principale (horizontale)
        self.clicked_mob_box = arcade.gui.UIBoxLayout(vertical = False)
        
        # Création d'un bouton texturé pour acueillir l'image du monstre clické
        ##### A COMPLETER #####
        
        ##### A COMPLETER #####                                 # Ajout dans la box
        
        # Création d'une box verticale
         ##### A COMPLETER #####
        
        # Création de deux labels pour le nom et le nombre d'HP du monstre clické
         ##### A COMPLETER #####
        
        # Ajout des labels dans v_box_2
         ##### A COMPLETER #####
        
        # Ajout de v_box_2 dans la box principale 
         ##### A COMPLETER #####
        
        
    # Mise en place de l'IHM  
    def setup(self) :
        # Création du contexte pour l'IHM
        ###### A COMPLETER ######
        
        # Ajout du menu du jeu
        ###### A COMPLETER ######

        pass
        
    
      
    def upate(self) :
        self.setup()
        

    def draw(self) :
        self.game.manager.draw()
        
        
        
