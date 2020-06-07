"""
MatheX, le 07 juin 2020
Série d'introduction à Pygame
Prérequis:
    - les bases de Python
    - les listes et les fonctions
#1 première épisode de la série:
    - fenêtre principale du jeu
    - horloge du jeu
    - le joueur (graphisme simplifié)
    - mouvement du joueur (mouvement simple)
    - collision avec un méchant (graphisme simplifié)
"""

# import des bibliothèques
import pygame
import random

# constantes
BLUE = (0,0,255) # couleur (R,G,B)
RED = (255,0,0) # couleur (R,G,B)
GREEN = (0,255,0) # couleur (R,G,B)
BLACK = (0,0,0) # couleur (R,G,B)
WHITE = (255,255,255) # couleur (R,G,B)
pas = 20 # vitesse du joueur (nombre de pixels par mouvement)

# initialisation de pygame
pygame.init()

# fenêtre principle du jeu
window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

# joueur
player = pygame.draw.rect(window,BLUE,(100,100,20,20))

# ennemi
enemy = pygame.draw.rect(window,RED,(300,300,20,20))

# horloge du jeu
clock = pygame.time.Clock()


run = True  # mettre à False pour quitter le jeu

# boucle principale du jeu
while run:
    clock.tick(10)  #20 images/sec max

    # pour quitter la fenêtre principale
    events = pygame.event.get() # récupère tous les évènements
    for event in events:
        if event.type == pygame.QUIT: # vérifie si on veut quitter
            run = False

    # mouvement du joueur
    keys = pygame.key.get_pressed() # récupère toutes les touches pressées
    if keys[pygame.K_LEFT]:
        player.move_ip(-pas,0)
    elif keys[pygame.K_RIGHT]:
        player.move_ip(pas,0)
    elif keys[pygame.K_DOWN]:
        player.move_ip(0,pas) # l'axe y est dirigé vers le bas
    elif keys[pygame.K_UP]:
        player.move_ip(0,-pas)

    # détection de collision entre le joueur et l'ennemi
    if player.colliderect(enemy):
        enemy.x = random.randint(0,window.get_width()-enemy.width)
        enemy.y = random.randint(0,window.get_height()-enemy.height)


    # mis à jour de l'affichage du fond de la fenêtre principale
    window.fill(BLACK)

    # desssine le joueur à sa position actuelle
    pygame.draw.rect(window, BLUE, player)

    # desssine l'ennemi à sa position actuelle
    pygame.draw.rect(window, RED, enemy)

    # mis à jour de l'affichage global
    pygame.display.update()

#quitte pygame
pygame.quit()
