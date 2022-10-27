import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player_escolhido):
        super().__init__()


        #up
        player_walk_up_1 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_up_1.png').convert_alpha()
        player_walk_up_1 = pygame.transform.scale2x(player_walk_up_1)
        
        player_walk_up_2 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_up_2.png').convert_alpha()
        player_walk_up_2 = pygame.transform.scale2x(player_walk_up_2)
        
        player_walk_up_3 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_up_3.png').convert_alpha()
        player_walk_up_3 = pygame.transform.scale2x(player_walk_up_3)
        
        #down
        player_down_walk_1 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_down_walk_1.png').convert_alpha()
        player_down_walk_1 = pygame.transform.scale2x(player_down_walk_1)

        player_down_walk_2 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_down_walk_2.png').convert_alpha()
        player_down_walk_2 = pygame.transform.scale2x(player_down_walk_2)

        player_down_walk_3 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_down_walk_3.png').convert_alpha()
        player_down_walk_3 = pygame.transform.scale2x(player_down_walk_3)
        
        #right
        player_right_walk_1 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_right_walk_1.png').convert_alpha()
        player_right_walk_1 = pygame.transform.scale2x(player_right_walk_1)

        player_right_walk_2 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_right_walk_2.png').convert_alpha()
        player_right_walk_2 = pygame.transform.scale2x(player_right_walk_2)

        player_right_walk_3 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_right_walk_3.png').convert_alpha()
        player_right_walk_3 = pygame.transform.scale2x(player_right_walk_3)

        player_right_walk_4 = pygame.image.load(f'imagens/players/{player_escolhido}/{player_escolhido}_right_walk_4.png').convert_alpha()
        player_right_walk_4 = pygame.transform.scale2x(player_right_walk_4)
        

        self.player_walk_up = [player_walk_up_1, player_walk_up_2,player_walk_up_3]
        self.player_walk_down = [player_down_walk_1,player_down_walk_2,player_down_walk_3]
        self.player_walk_right = [player_right_walk_1,player_right_walk_2,player_right_walk_3,player_right_walk_4]

        self.player_index = 0        
        self.image = self.player_walk_up[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))

    def player_input(self, colisao):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:    
                if self.rect.y >= 32:
                        self.rect.y -= 2
                self.animation_state('up')
        
        if keys[pygame.K_s]:
            if self.rect.y <= 350:
                self.rect.y += 2
            self.animation_state('down')

        if keys[pygame.K_d]:
            if self.rect.x <= 416:
                self.rect.x += 2
            self.animation_state('right')

        if keys[pygame.K_a]:
            if self.rect.x >= 32:
                self.rect.x -= 2
                self.animation_state('left')

    def animation_state(self, i):
            self.player_index += 0.1
            
            if i == "up":
                if self.player_index >= len(self.player_walk_up):
                    self.player_index = 0
                self.image = self.player_walk_up[int(self.player_index)]
            
            if i == "down":
                if self.player_index >= len(self.player_walk_down):
                    self.player_index = 0
                self.image = self.player_walk_down[int(self.player_index)]                

            if i == "right":
                if self.player_index >= len(self.player_walk_right):
                    self.player_index = 0
                self.image = self.player_walk_right[int(self.player_index)]
            
            if i == "left":
                if self.player_index >= len(self.player_walk_right):
                    self.player_index = 0
                self.muda = pygame.transform.flip(self.player_walk_right[int(self.player_index)], True, False)
                self.image = self.muda

    def update(self, colisao):
        self.player_input(colisao)
        #self.animation_state()