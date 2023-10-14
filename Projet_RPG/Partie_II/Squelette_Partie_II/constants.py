import PIL.Image
import arcade
from random import randint


# L'écran en général
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NSI_RPG"


# Map
MAP_FILE = "Maps/map.json"
MAP_SCALING = 2   # Mise à l'échelle souhaitée d'un tile
MAP_WIDTH = 1280  # Largeur de la carte
MAP_HEIGHT = 1280 # Hauteur de la carte


################################### ENTITIES ###############################

WALK_DOWN, WALK_LEFT, WALK_RIGHT, WALK_UP = 0, 1, 2, 3

SLOW_ANIMATION = 5   # Permet de ralentir les animations (monstres)


################################### PLAYER ###############################

# Caractéristiques du joueur
PLAYER_WIDTH,PLAYER_HEIGHT = 32, 32
PLAYER_SCALING = 2
PLAYER_FILE = "Mobs/Player/player.png"          # Fichier des animations
PLAYER_CAR_FILE = "Mobs/Player/player.json"     # Fichier des caractéristiques


# Coordonnées des images de chaque animation du joueur
##### A COMPLETER / MODIFIER si autre image #####
PLAYER_WD_COORDS = [(0,0), (32,0), (64,0), (96,0)]  # Marche vers le bas
PLAYER_WU_COORDS = []                               # Marche vers la droite                             
PLAYER_WR_COORDS = []                               # Marche vers le haut
PLAYER_WL_COORDS = []                               # Marche vers la gauche


##### NE PAS CHANGER #####
PLAYER_SPRITE_COORDS = [ PLAYER_WD_COORDS, PLAYER_WL_COORDS, PLAYER_WR_COORDS, PLAYER_WU_COORDS ]
   
    
    
################################### ZOMBIE ORC ###############################

# Caractéristiques d'un zombie orc
##### A MODIFIER si autre image !! #####
ORC_WIDTH,ORC_HEIGHT = 32, 32
ORC_SCALING = 2

ORC_FILE = "Mobs/Orc/orc.png"      # Fichier des animations
ORC_CAR_FILE = "Mobs/Orc/mob.json" # Fichier des caractéristiques


# Coordonnées des images de chaque animation de l'orc
##### A COMPLETER / MODIFIER si autre image #####
ORC_WD_COORDS = [(0,0), (32,0), (64,0), (96,0), (128,0), (160,0), (192,0),  
                 (224,0), (256,0), (288, 0)]
ORC_WL_COORDS = []
ORC_WD_COORDS = []
ORC_WR_COORDS = []
ORC_WU_COORDS = []


# Regroupement des coordonnées précédentes dans une liste
##### NE PAS CHANGER #####
ORC_SPRITE_COORDS = [ ORC_WD_COORDS, ORC_WL_COORDS, ORC_WR_COORDS, ORC_WU_COORDS ]

