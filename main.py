import pygame

from Players import Player
from Paredinha import Paredinha



def colisao_das_paredinhas():
    if pygame.sprite.spritecollide(player.sprite, paredinhas, False):
        return True
    else:
        return False



pygame.init()
screen = pygame.display.set_mode((480,416))
pygame.display.set_caption('Bom party')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf', 50)
game_active = False


mapa = pygame.image.load('imagens/mapa.png').convert()
mapa = pygame.transform.scale2x(mapa)



#menu----------------------------------------------------------------------------------
menu = pygame.image.load('imagens/menu.png').convert()
menu = pygame.transform.scale2x(menu)

nome_do_jogo = test_font.render("BOM PARTY", False, "Black")
nome_do_jogo_rect = nome_do_jogo.get_rect(center = (240, 100))

maguinho = pygame.image.load('imagens/players/maguinho/maguinho_down_walk_1.png').convert_alpha()
maguinho = pygame.transform.scale(maguinho,(64,64))
maguinho_rect = maguinho.get_rect(center = (175,170))

trollazul = pygame.image.load('imagens/players/trollazul/trollazul_down_walk_1.png').convert_alpha()
trollazul = pygame.transform.scale(trollazul,(64,64))
trollazul_rect = trollazul.get_rect(center = (305,170))

trollverde = pygame.image.load('imagens/players/trollverde/trollverde_down_walk_1.png').convert_alpha()
trollverde = pygame.transform.scale(trollverde,(64,64))
trollverde_rect = trollverde.get_rect(center = (175,270))

hominho1 = pygame.image.load('imagens/players/hominho1/hominho1_down_walk_1.png').convert_alpha()
hominho1 = pygame.transform.scale(hominho1,(64,64))
hominho1_rect = hominho1.get_rect(center = (305,265))

player_selecionado = ""

#paredinhas no mapa--------------------------------------------------------------------
paredinhas = pygame.sprite.Group()
paredinhas.add(Paredinha())


#jogo----------------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #tudo isso pra ver qual player escolheu
        if game_active == False:
            if event.type == pygame.MOUSEBUTTONDOWN:        
                if maguinho_rect.collidepoint(event.pos):
                    player_selecionado = "maguinho"
                    player = pygame.sprite.GroupSingle()
                    player.add(Player(player_selecionado))
                    game_active = True
                elif trollazul_rect.collidepoint(event.pos):
                    player_selecionado = "trollazul"
                    player = pygame.sprite.GroupSingle()
                    player.add(Player(player_selecionado))
                    game_active = True
                elif trollverde_rect.collidepoint(event.pos):
                    player_selecionado = "trollverde"
                    player = pygame.sprite.GroupSingle()
                    player.add(Player(player_selecionado))
                    game_active = True
                elif hominho1_rect.collidepoint(event.pos):
                    player_selecionado = "hominho1"
                    player = pygame.sprite.GroupSingle()
                    player.add(Player(player_selecionado))
                    game_active = True

    if game_active == True:
        screen.blit(mapa, (0,0))

        paredinhas.draw(screen)
        
        player.draw(screen)
        player.update(colisao_das_paredinhas())
    else:
        screen.blit(menu, (0,0))
        screen.blit(nome_do_jogo, nome_do_jogo_rect)

        screen.blit(maguinho,maguinho_rect)
        screen.blit(trollazul,trollazul_rect)
        screen.blit(trollverde,trollverde_rect)
        screen.blit(hominho1,hominho1_rect)
    
    pygame.display.update()
    clock.tick(60)