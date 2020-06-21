"""
MatheX, le 20 juin 2020
Série d'introduction à Pygame
Prérequis:
    - les bases de Python
    - les listes et les fonctions
#1 premier épisode de la série:
    - fenêtre principale du jeu
    - horloge du jeu
    - le joueur (graphisme simplifié)
    - mouvement du joueur (mouvement simple)
    - collision avec un méchant (graphisme simplifié)
#2 deuxième épisode de la série:
    - réorganisation du code en fonction
    - image pour le joueur et l'ennemi
    - le joueur ne sort plus de l'écran
    - customisation de l'interface
    - ajout d'une image de fond et du sol
    - sprites fixés au sol
    - changement de direction de l'image du joueur



"""

# import des bibliothèques
import pygame
import random
import os

################### Initialisation ######################################

# constantes
BLUE = (0,0,255) # couleur (R,G,B)
RED = (255,0,0) # couleur (R,G,B)
GREEN = (0,255,0) # couleur (R,G,B)
BLACK = (0,0,0) # couleur (R,G,B)
WHITE = (255,255,255) # couleur (R,G,B)
pas = 20 # vitesse du joueur (nombre de pixels par mouvement)

# initialisation de pygame
pygame.init()

# fenêtre principale du jeu
window = pygame.display.set_mode((1400, 700))
pygame.display.set_icon(pygame.image.load(os.path.join('image', 'icon.png')).convert_alpha())
pygame.display.set_caption('Pygame Introduction')

# images de fond d'écran
bg = pygame.image.load(os.path.join('image', 'SKY.png')).convert_alpha()
bg = pygame.transform.scale(bg,window.get_size())
ground = pygame.image.load(os.path.join('image', 'ground.png')).convert_alpha()
ground = pygame.transform.scale(ground,(window.get_width(),ground.get_height()//2))
pos_y_ground = window.get_height() - ground.get_height()

# son
pygame.mixer.init()
mySound = pygame.mixer.Sound(os.path.join('music', 'ambiance.ogg'))
# pygame.mixer.Sound.play(mySound,loops=-1) # musique de fond
sound_collision = pygame.mixer.Sound(os.path.join('music', 'shoot.ogg'))


# joueur
player = pygame.image.load(os.path.join('image', 'robot.png')).convert_alpha()
player = pygame.transform.rotozoom(player,0,0.2)
playerRect = pygame.draw.rect( window, RED, (100,pos_y_ground-player.get_height()+16,player.get_width()-60,player.get_height()-16),1)
player_right = True # pour mémoriser la direction du joueur


# ennemi
enemy = pygame.image.load(os.path.join('image', 'zombie.png')).convert_alpha()
enemy = pygame.transform.rotozoom(enemy,0,0.2)
enemyRect = pygame.draw.rect( window, RED, (100,pos_y_ground-enemy.get_height()+12,enemy.get_width()-27,enemy.get_height()-12),1)
enemy_right = True # pour mémoriser la direction de l'ennemi

# horloge du jeu
clock = pygame.time.Clock()

# pour savoir si on doit toujours jouer
run = True  # mettre à False pour quitter le jeu

################### Gestion des évènements ######################################

# gère les évènements du jeu
def manageEvents():
    global run , player , player_right
    # pour quitter la fenêtre principale
    events = pygame.event.get()  # récupère tous les évènements
    for event in events:
        if event.type == pygame.QUIT:  # vérifie si on veut quitter
            run = False

    # mouvement du joueur
    keys = pygame.key.get_pressed()  # récupère toutes les touches pressées
    if keys[pygame.K_LEFT]:
        if playerRect.x > 0: # pour ne pas sortir de l'écran
            if player_right: # pour diriger le joueur dans la bonne direction
                player = pygame.transform.flip(player,True,False)
                player_right = False
            playerRect.move_ip(-pas, 0)
    elif keys[pygame.K_RIGHT]:
        if playerRect.x < window.get_width()-playerRect.width-10:  # pour ne pas sortir de l'écran
            if not player_right: # pour diriger le joueur dans la bonne direction
                player = pygame.transform.flip(player,True,False)
                player_right = True
            playerRect.move_ip(pas, 0)
    '''
    elif keys[pygame.K_DOWN]:
        if playerRect.y < window.get_height() - playerRect.height - 10:  # pour ne pas sortir de l'écran
            playerRect.move_ip(0, pas)  # l'axe y est dirigé vers le bas
    elif keys[pygame.K_UP]:
        if playerRect.y > 0:  # pour ne pas sortir de l'écran
            playerRect.move_ip(0, -pas)
    '''

################### Logique de jeu ######################################

# gère la logique de jeu
def gameLogic():
    global enemy , enemy_right
    # détection de collision entre le joueur et l'ennemi
    if playerRect.colliderect(enemyRect):
        enemyRect.x = random.randint(0, window.get_width() - enemyRect.width)
        # enemyRect.y = random.randint(0, window.get_height() - enemyRect.height)
        pygame.mixer.Sound.play(sound_collision)  # sound effect

    # pour diriger l'ennemi en direction du  joueur
    if enemyRect.x < playerRect.x and not enemy_right:
        enemy = pygame.transform.flip(enemy, True, False)
        enemy_right = True
    elif enemyRect.x > playerRect.x and enemy_right:
        enemy = pygame.transform.flip(enemy, True, False)
        enemy_right = False



################### Affichage du jeu ######################################

# redessine le jeu
def drawGame():
    # mis à jour de l'affichage du fond de la fenêtre principale
    #window.fill(BLACK)
    window.blit(bg,(0,0))
    window.blit(ground, (0, window.get_height()-ground.get_height()))

    # dessine le joueur (image) et le rectangle associé
    pygame.draw.rect(window, RED, playerRect,1)
    window.blit(player,(playerRect.x-25,playerRect.y-9))

    # desssine l'ennemi à sa position actuelle
    pygame.draw.rect(window, RED, enemyRect,1)
    window.blit(enemy, (enemyRect.x - 13, enemyRect.y - 13))

    # mis à jour de l'affichage global
    pygame.display.update()

################### Boucle du jeu ######################################

# boucle principale du jeu
while run:
    clock.tick(20)  #20 images/sec max

    manageEvents()
    gameLogic()
    drawGame()

#quitte pygame
pygame.quit()
