"""
Série d'introduction à Pygame
Prérequis:
    - les bases de Python
    - les listes et les fonctions
#1 première partie de la série:
    - fenêtre principale du jeu
    - le joueur (graphisme simplifié)
    - mouvement du joueur (mouvement simple)
    - collision avec un méchant (graphisme simplifié)
"""

# import des librairies
import pygame
import time
import random

# déclaration des constantes
bleu = (0,0,255) # (R,G,B) entre 0 et 255
rouge = (255, 0, 0) # (R,G,B) entre 0 et 255
noir = (0,0,0) # (R,G,B) entre 0 et 255
blanc = (255,255,255) # (R,G,B) entre 0 et 255
pas = 10

# initialise Pygame
pygame.init()


# création de la fenêtre principale du jeu
window = pygame.display.set_mode( (500,500))

# création du joueur
player = pygame.draw.rect(window , bleu , (100,100,20,20))
# création du méchant
enemy = pygame.draw.rect(window, rouge, (300, 300, 20, 20))

# mis à jour de l'affichage
pygame.display.update()

run = True

# boucle principale du jeu
while run:
    # récupère tous les évènements
    events = pygame.event.get()

    # pour sortir de la boucle si on veut quitter le jeu
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    # mouvement du joueur
    K_Pressed = pygame.key.get_pressed()
    if K_Pressed[pygame.K_LEFT]:
        player.move_ip(-pas,0)
    elif K_Pressed[pygame.K_RIGHT]:
        player.move_ip(pas,0)
    elif K_Pressed[pygame.K_UP]:
        player.move_ip(0,-pas)
    elif K_Pressed[pygame.K_DOWN]:
        player.move_ip(0,pas)


    # mis à jour de la couleur de la fenêtre principale
    window.fill(noir)
    # mis à jour de l'affichage du joueur
    pygame.draw.rect(window, bleu, player)
    # mis à jour de l'affichage du méchant
    if player.colliderect(enemy):
        enemy.x = random.randint(0, window.get_width() - enemy.width)
        enemy.y = random.randint(0, window.get_width() - enemy.height)

    pygame.draw.rect(window, rouge, enemy)

    # mis à jour de l'affichage
    pygame.display.update()



# quitte Pygame
pygame.quit()
