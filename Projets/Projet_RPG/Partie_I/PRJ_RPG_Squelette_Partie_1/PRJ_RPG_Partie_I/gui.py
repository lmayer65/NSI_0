from PIL import Image
from application import *
from constants import *
import arcade
import arcade.gui
from main import *



# Transformation d'images
# Teintes grisées
def to_gray(img) :
    img_new = Image.new("RGB", img.size)
    
    for i in range(img.size[0]) :
        for j in range(img.size[1]) :
            red, green, blue = img.getpixel((i,j))
            
            gray = int(red*0.299 + green*0.587 + blue*0.144)
            
            img_new.putpixel((i,j),(gray,gray,gray))
            
    return img_new


# Transparence
def to_alpha(img) :
    img_new = Image.new("RGBA", img.size)
    alpha = 100
    
    for i in range(img.size[0]) :
        for j in range(img.size[1]) :
            red, green, blue = img.getpixel((i,j))
            
            img_new.putpixel((i,j),(red, green, blue, alpha))
            
    return img_new
            
    




# Permet de quitter le jeu
class QuitButton(arcade.gui.UIFlatButton):
    def set_window(self, game) :
        self.game = game
    
    # Pour quitter le jeu
    def on_click(self, event: arcade.gui.UIOnClickEvent) :
        self.game.close()
        


# Gestion des icônes interactifs
class IconButton(arcade.gui.UITextureButton) :
    def __init__(self, name, tex, wid, hei) :
        super().__init__(texture = tex, width = wid, height = hei)
        self.name = name  # Nom de l'action
        
        # Création des deux textures correspondant aux deux états suivant :
        self.normal = None
        self.clicked = None
        
    def set_gui(self, gui) :
        self.gui = gui
    
    
    # En cas de clic, le bouton passe à l'état "cliqué"
    def on_click(self, event: arcade.gui.UIOnClickEvent) :
        # On désactive les éventuels états cliqué des boutons
        self.gui.act_1.texture = self.gui.act_1.normal
        self.gui.act_2.texture = self.gui.act_2.normal
        self.gui.act_3.texture = self.gui.act_3.normal
        
        # Le bouton cliqué passe en mode cliqué.
        self.texture = self.clicked
        


    
        
        
      
        
class Gui() :
    def __init__(self,game) :
        # Pointeur sur l'instance de la classe `My_Game`
        self.game = game
        # Permet de générer un GUI dans la fenêtre de jeu
        self.game.manager = arcade.gui.UIManager()
        self.game.manager.enable()
        
        # Menu du jeu
        self.menu_bar = None 
        # Affiche les caractéristiques principales du joueur
        self.player_box = None 
        # Affiche les actions du joueurs
        self.player_action_box = None
        # Affiche les caractéristiques principales du mob cliqué
        self.clicked_mob_box = None
        
        #▀ Boutons d'actions (dans player_action_box)
        # A prévoir dans une liste ?
        self.act_1 = None
        self.act_2 = None
        self.act_3 = None
        
        
    # Création du menu du jeu
    def create_game_menu(self) :
        pass
        
    
    # Caractéristiques principales du joueur
    def create_player_box(self) :
        pass
              
        
    # Regroupement des attaques du joueurs
    def create_player_action_box(self) :
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
        
        
        