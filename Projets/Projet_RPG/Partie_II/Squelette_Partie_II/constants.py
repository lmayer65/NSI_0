import arcade
from random import randint

# L'écran en général
SCREEN_WIDTH = 800    # Largeur de la fenêtre
SCREEN_HEIGHT = 600   # Hauteur de la fenêtre
SCREEN_TITLE = "NSI_RPG"   # Titre de l'écran (jeu)


# Map
MAP_FILE = "Maps/map.json"  # Nom du fichier de la carte
MAP_SCALING = 0.5   # Mise à l'échelle souhaitée d'un tile
MAP_WIDTH = 1280  # Largeur de la map créée
MAP_HEIGHT = 1280 # Hauteur de la map créée


# Caractéristiques du joueur
PLAYER_WIDTH, PLAYER_HEIGHT = 16, 32
PLAYER_SCALING = 0.5
PLAYER_FILE = "Mobs/player.png"

# Indices des animatioons du joueur
#### NE PAS CHANGER ####
PLAYER_WALK_DOWN, PLAYER_WALK_LEFT, PLAYER_WALK_RIGHT, PLAYER_WALK_UP = 0,1,2,3
PLAYER_ATTACK_DOWN, PLAYER_ATTACK_LEFT, PLAYER_ATTACK_RIGHT, PLAYER_ATTACK_UP = 4,5,6,7

# Coordonnées des images de chaque animation du joueur
### A COMPLETER / MODIFIER en fonction de l'image ###
PLAYER_WD_COORDS = [(0,0), (16,0), (32,0), (48,0)]      # Marche vers le bas
PLAYER_WR_COORDS = []                                   # Marche vers la droite
PLAYER_WU_COORDS = []                                   # Marche vers le haut
PLAYER_WL_COORDS = []                                   # Marche vers la gauche

PLAYER_AD_COORDS = []                                   # Attaque vers le bas
PLAYER_AR_COORDS = []                                   # Attaque vers la droite
PLAYER_AU_COORDS = []                                   # Attaque vers le haut
PLAYER_AL_COORDS = []                                   # Attaque vers la gauche


# Regroupement des données précédentes (joueur) dans une liste
#### NE PAS CHANGER ####
PLAYER_SPRITE_COORDS = [PLAYER_WD_COORDS, PLAYER_WL_COORDS, PLAYER_WR_COORDS, PLAYER_WU_COORDS, \
                       PLAYER_AD_COORDS, PLAYER_AL_COORDS, PLAYER_AR_COORDS, PLAYER_AU_COORDS ]


# Caractéristiques d'un orc (mob)


