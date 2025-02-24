import pygame as pg
from settings import *
from assets import *
from backgrounds import samurai_sheet, boss_sheet, npc_sheet, enemy_sheet

class Character:
    def __init__(self, flip, char_type, x, y, vx, data, sprite_sheet, animation_steps, world_length, health):
        self.vx = vx
        self.flip = flip
        self.char_type = char_type
        self.x = x
        self.y = y
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 # 0:Idle, 1:walk, 2:Run, 3:Jump, 4:death, 5:hit, 6:Attack, 7:Attack 2, 8:Attack 3    # Demon: 0:idle, 1:walk, 2: attack, 3:hit, 4:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pg.time.get_ticks() # tidspunktet for når bildet ble oppdatert
        self.vy = 0
        self.walking = False
        self.running = False
        self.jumping = False
        self.attacking = False
        self.following = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack3_cooldown = 0
        self.hit = False
        self.health = health
        self.alive = True
        self.scalex = 15*SAMURAI_SCALE if self.char_type == "samurai" else 70*BOSS_SCALE
        self.scaley = 25*SAMURAI_SCALE if self.char_type == "samurai" else 75*BOSS_SCALE
        self.rect = pg.Rect(x, y, self.scalex, self.scaley)
        self.world_length = world_length
        self.damage = 10

    def load_images(self, sprite_sheet, animation_steps):
        #henter ut bilder fra spritesheet
        animation_list = []
        sheet_width, sheet_height = sprite_sheet.get_size()
        for y, animation in enumerate(animation_steps): # for loop for y-aksen  enumerate er som en tracker som sier hvor mange ganger vi har gått gjennom loopen. samme som y=0 også y+=1
            temp_img_list = []
            for x in range(animation): # for loop for x-aksen
                rect = pg.Rect(x * self.size[0], y * self.size[1], self.size[0], self.size[1])
                if rect.right <= sheet_width and rect.bottom <= sheet_height:
                    temp_img = sprite_sheet.subsurface(rect)
                    temp_img_list.append(pg.transform.scale(temp_img, (self.size[0] * self.image_scale, self.size[1] * self.image_scale))) # en rad med bilder i liste
            animation_list.append(temp_img_list) # alle bilder i en liste, delt opp i flere lister
        return animation_list



    def movement(self, scroll, scrolling, target, boss, enemies, screen):
        if self.char_type != "npc":  # Kun spilleren og fiender blir påvirket
            self.vy += GRAVITY
            self.y += self.vy
        self.running = False
        self.walking = False
        keys_pressed = pg.key.get_pressed()
        
        if self.alive == True:
            if self.y > HEIGHT - (self.rect.height + 67):
                self.y = HEIGHT - (self.rect.height + 67)
                self.vy = 0
                self.jumping = False

            if self.char_type == "samurai":
                #Kan bare gjøre andre ting om jeg ikke agriper
                if self.attacking == False:
                    #movement
                    if keys_pressed[pg.K_a]:
                        self.x = int(self.x - (self.vx / 3))
                        self.walking = True
                        self.flip = True
                    if keys_pressed[pg.K_a] and keys_pressed[pg.K_LSHIFT]:
                        self.x -= self.vx
                        self.running = True
                        self.flip = True
                    if keys_pressed[pg.K_d]:
                        self.x = int(self.x + (self.vx / 3))
                        self.walking = True
                        self.flip = False
                    if keys_pressed[pg.K_d] and keys_pressed[pg.K_LSHIFT]:
                        self.x = int(self.x + self.vx)
                        self.running = True
                    #Hoppe
                    if keys_pressed[pg.K_w]:
                        if self.y == HEIGHT - (self.rect.height + 67):
                            self.vy = -22
                            self.jumping = True
                    #angrep
                    if keys_pressed[pg.K_l]:
                        self.attack_type = 1
                        self.damage = 10
                    elif keys_pressed[pg.K_k]:
                        self.attack_type = 2
                        self.damage = 10
                    elif keys_pressed[pg.K_p]:
                        self.attack_type = 3
                        self.damage = 30
                    if keys_pressed[pg.K_l] or keys_pressed[pg.K_k] or keys_pressed[pg.K_p]:
                        self.attack(screen, [boss] + (enemies if isinstance(enemies, list) else [enemies]))

            if self.char_type == "boss" or self.char_type == "enemy":

                """ if ((keys_pressed[pg.K_a] and keys_pressed[pg.K_LSHIFT]) or keys_pressed[pg.K_a]) and self.x >=self.world_length - self.rect.width:
                    self.x -= self.vx """
                distance_to_person = abs(self.x - target.x)
                #if not scrolling:
                if distance_to_person <= 300:
                    self.following = True
                if self.following:
                    if not scrolling:
                        if self.x < target.x:
                            self.x += self.vx
                            self.flip = True
                        if self.x > target.x:
                            self.x -= self.vx
                            self.flip = False
                        self.walking = True
                    else: 
                        self.x += 0
                        self.walking = True

            if (self.char_type == "boss" or self.char_type == "enemy") and self.alive and self.attack_cooldown == 0:
                distance_to_target = abs(self.x - target.x)
                if distance_to_target < 100:
                    if self.char_type == "enemy":
                        self.damage = 5
                    elif self.char_type == "boss":
                        self.damage = 10
                    self.attack(screen, target)

                # Ensure the enemy doesn't move beyond the world boundaries
                if self.x < 0:
                    self.x = 0
                if self.x > self.world_length - self.rect.width:
                    self.x = self.world_length - self.rect.width
                            
            if self.char_type == "npc":
                return

            # Oppdatere rektangelet basert på objektenes posisjon
            self.rect.topleft = (int(self.x), int(self.y))
            if self.flip:
                self.rect.left -= 20

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack3_cooldown > 0:
            self.attack3_cooldown -= 1


    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack3_cooldown > 0:
            self.attack3_cooldown -= 1
        # sjekker hva personen gjør eks: løper eller idle
        if self.char_type == "samurai":
            if self.health <= 0:
                self.health = 0
                self.alive = False
                self.update_action(4) # Dead
            elif self.hit == True:
                self.update_action(5) # Hit
            elif self.attacking == True:
                if self.attack_type == 1:
                    self.update_action(6) # Attack 1
                elif self.attack_type == 2: 
                    self.update_action(7) # Attack 2
                elif self.attack_type == 3:
                    self.update_action(8) #Attack 3
            elif self.jumping == True:
                self.update_action(3) #h Jumping
            elif self.running == True:
                self.update_action(2) # Running 
            elif self.walking == True:
                self.update_action(1) # Walking
            else:
                self.update_action(0) # Idle

        if self.char_type == "boss":
            if self.health <= 0:
                self.health = 0
                self.alive = False
                self.update_action(4) # Dead
            elif self.hit == True:
                self.update_action(3) # Hit
            elif self.attacking == True:
                self.update_action(2) # attack
            elif self.walking == True:
                self.update_action(1) # Walking
            else:
                self.update_action(0) # Idle
                
        if self.char_type == "enemy":
            if self.health <= 0:
                self.health = 0
                self.alive = False
                self.y = 287
                self.update_action(3) # Dead
            elif self.hit == True:
                self.update_action(2) # Hit
            elif self.attacking == True:
                self.update_action(1) # Attack
            elif self.walking == True:
                self.update_action(1) # Walking
            else:
                self.update_action(0) # Idle


        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        # sjekker om nok tid har gått siden siste oppdatering
        if pg.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1 
            self.update_time = pg.time.get_ticks()
        # sjekker om vi har nådd slutten av animasjonen
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
            # Sjekker om noen har angrepet
            if self.char_type == "samurai":
                if self.action == 6 or self.action == 7:
                    self.attacking = False
                    self.attack_cooldown = 20
                elif self.action == 8:
                    self.attacking = False
                    self.attack_cooldown = 100
                    self.attack3_cooldown = 150
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 20

            if self.char_type == "boss":
                if self.action == 2:
                    self.attacking = False
                    self.attack_cooldown = 150
                if self.action == 3:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 150
                    
            if self.char_type == "enemy":
                if self.action == 1:
                    self.attacking = False
                    self.attack_cooldown = 40
                if self.action == 2:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 40
            
            if self.char_type == "npc":
                self.rect.topleft = (self.x, self.y)

    def attack(self, screen, targets):
            if not isinstance(targets, list):
                targets = [targets]
            if self.attack_cooldown == 0:
                self.attacking = True
                attack_width = self.rect.width
                if self.char_type == "samurai":
                    # Samurai ser mot høyre fra start
                    attack_x = self.rect.right if not self.flip else self.rect.left - attack_width
                elif self.char_type == "boss" or self.char_type == "enemy":
                    # Boss ser mot venstre fra start
                    attack_x = self.rect.left - attack_width if not self.flip else self.rect.right

                attacking_rect = pg.Rect(attack_x, self.rect.y, attack_width, self.rect.height)

                for target in targets:
                    if attacking_rect.colliderect(target.rect):
                        target.health -= self.damage
                        target.hit = True

                self.attack_cooldown = 150 if self.char_type == "boss" else (40 if self.char_type == "enemy" else 20)


    def update_action(self, new_action):
        # sjekker om handlingen har endret seg
        if new_action != self.action:
            self.action = new_action
            # oppdaterer bildet
            self.frame_index = 0
            # oppdaterer tiden
            self.update_time = pg.time.get_ticks()

    def draw(self, screen):
        img = pg.transform.flip(self.image, self.flip, False)
        # justere posisjonen av bildet basert på flip
        if self.flip:
            img_x = self.rect.x - (img.get_width() - self.rect.width) // 2 - 23
        else:
            img_x = self.rect.x - (self.image_scale * self.offset[0])
        img_y = self.rect.y - (self.image_scale * self.offset[1])

        if self.char_type == "npc":
            screen.blit(img, (self.x, self.y+65))
        elif self.char_type == "enemy":
            screen.blit(img, (self.x, self.y+21))
        else:   
            screen.blit(img, (img_x, img_y))


def create_characters(world_length):
    person = Character(False, "samurai", 100, 100, 7, SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS, world_length, 100)
    boss = Character(False, "boss", 3000, 100, 3, BOSS_DATA, boss_sheet, BOSS_ANIMATION_STEPS, world_length, 100)
    npc = Character(False, "npc", 100, HEIGHT-100, 0, NPC_DATA, npc_sheet, NPC_ANIMATION_STEPS, world_length, 100)
    
    enemies = []
    for i in range(1, 3):
        enemy = Character(False, "enemy", 500 * i, HEIGHT-100, 2, ENEMY_DATA, enemy_sheet, ENEMY_ANIMATION_STEPS, world_length, 20)
        enemies.append(enemy)
        
    return person, boss, npc, enemies