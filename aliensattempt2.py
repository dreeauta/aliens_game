import pygame
import random
import time


KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276




def main():
    width = 500
    height = 700
    blue_color = (97, 159, 182)




    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/scene1.png').convert_alpha()
    wormhole_sound = pygame.mixer.Sound('sounds/music.wav')
    # self.font = pygame.font.SysFont('Arial', 25)
    # pygame.display.set_caption('Box Test')
    lose_effect = pygame.mixer.Sound('sounds/lose.wav')
    win_effect = pygame.mixer.Sound('sounds/win.wav')
    start_ticks=pygame.time.get_ticks() #starter tick
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()


    # Game initialization

    class Scene(object):
        def __init__(self):
            self.height = 700
            self.width = 500
            self.scene1 = pygame.image.load('images/scene1.png').convert_alpha()
            self.scene2 = pygame.image.load('images/scene2.png').convert_alpha()
            self.scene3 = pygame.image.load('images/scene3.png').convert_alpha()

        def display1(self, screen):
            screen.blit(self.scene1, (0,0))

        def display2(self, screen):
            screen.blit(self.scene2, (0,0))

        def display3(self, screen):
            screen.blit(self.scene3, (0,0))



    #
    #
    # class Scene_1(allScenes):
    #     def __init__(self):
    #         self.height = 700
    #         self.width = 500
    #         self.background = pygame.image.load('images/scene1.png').convert_alpha()
    #
    #
    #     def display(self, screen):
    #         screen.blit(self.background, (0,0))
    #
    #
    #
    # class Scene_2(allScenes):
    #     def __init__(self):
    #         self.height = 500
    #         self.width = 700
    #         self.background = pygame.image.load('images/scene2.png').convert_alpha()
    #
    #     def display(self,screen):
    #         screen.blit(self.background, (0,0))
    #
    #     def multiply(self):
    #         pygame.draw.alien()


    #
    # class Scene_3(allScenes):
    #     def __init__(self):
    #         self.height = 700
    #         self.width = 500
    #         self.background =
    #
    #     def display(self, screen):
    #         screen.blit(self.background, (0,0))
    #


    class Character(object):
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.x_dir = 0
            self.y_dir = 0
            self.image = image
            self.Sound = True



        def display(self,screen):
            if self.alive == True:
                screen.blit(self.image, (self.x,self.y))

        def update(self):
            self.x += self.x_dir
            self.y += self.y_dir


    class Player1(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/spaceship.png').convert_alpha()
            self.name = 'Player 1'
            self.x = x
            self.y = y
            self.x_dir = 0
            self.y_dir = 0
            self.alive = True


        def off_screen(self):
            if self.y < 15:      #top
                self.y = 15

            if self.x > 420:    #right
                self.x = 420

            if self.y > 650:     #down
                self.y =  650

            if self.x < 20:       #left
                self.x =  20



    class Aliens(Character):
        def __init__(self, x, y):
            self.name = 'aliens'
            self.x = x
            self.y = y
            self.x_dir = 0
            self.y_dir = 0
            self.image = pygame.image.load('images/alien.png').convert_alpha()
            self.alive = True
            self.Sound = True


        def display(self,screen):
            if self.alive == True:
                screen.blit(self.image, (self.x,self.y))


        def change_direction(self):

            rand_direction = random.randint(0,7)


            if rand_direction == 0:   # top or north
                self.x_dir = 0
                self.y_dir = -1

            elif rand_direction == 1:  #right or east
                self.x_dir = 1
                self.y_dir = 0

            elif rand_direction == 2:  #down or south
                self.x_dir =0
                self.y_dir = 1

            elif rand_direction == 3:  #left or west
                self.x_dir =-1
                self.y_dir = 0

            elif rand_direction == 4:   # Northeast - topright
                self.x_dir = 1
                self.y_dir = -1

            elif rand_direction == 5:  # Northwest - top left
                self.x_dir = -1
                self.y_dir = -1

            elif rand_direction == 6:  # Southwest - bottom left
                self.x_dir = -1
                self.y_dir = 1

            elif rand_direction == 7:  # South east - bottom right
                self.x_dir = 1
                self.y_dir = 1


        def off_screen(self):
            if self.y < 0:      #top
                self.y =  480
            else:
                self.y -= 5

            if self.x > 512:    #right
                self.x = 0
            else:
                self.x += 5

            if self.y > 480:     #down
                self.y =  0
            else:
                self.y += 5

            if self.x < 0:       #left
                self.x =  512
            else:
                self.x -= 5


    class Wormhole(Character):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.alive = 1
            self.wormhole1 = pygame.image.load('images/wormhole.png').convert_alpha()
            self.wormhole2 = pygame.image.load('images/wormhole2.png').convert_alpha()
            self.spaceship = pygame.image.load('images/spaceship.png').convert_alpha()

        def display1(self,screen):
            screen.blit(self.wormhole1, (self.x,self.y))

        def display2(self,screen):
            screen.blit(self.wormhole2, (self.x,self.y))

        def display3(self,screen):
            screen.blit(self.spaceship, (self.x,self.y))





    # class Wormhole_2(Character):
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #         self.alive = True
    #         self.image = pygame.image.load('images/wormhole2.png').convert_alpha()
    #
    #     def display(self,screen):
    #         if self.alive == True:
    #             screen.blit(self.image, (self.x,self.y))


    # class Home(Character):
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #         self.alive = True
    #         self.image = pygame.image.load('images/homebase.png').convert_alpha()
    #
    #
    #     def display(self,screen):
    #         if self.alive == True:
    #             screen.blit(self.image, (self.x,self.y))

    player1 = Player1(400,550)

    alien = Aliens(300, 70)
    alien2 = Aliens(400, 100)
    alien3 = Aliens(500,400)

    wormhole = Wormhole(30,40)
    wormhole2 = Wormhole(30,490)
    spaceship = Wormhole(300,40)


    scene = Scene()



    stop_game = False

    change_dir_counter = 0       # original change_dir_count


    while not stop_game:
        for event in pygame.event.get():


# this is for controlling the player1 with the keyboard, declared keys at
#the top of the page, and set controls in the pygame.event.get()

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    player1.y += 30
                elif event.key == KEY_UP:
                    player1.y -= 30
                elif event.key == KEY_LEFT:
                    player1.x -= 30
                elif event.key == KEY_RIGHT:
                    player1.x += 30

            if event.type == pygame.QUIT:
                stop_game = True

        # for alien in alien_list:        #moves alien
        #     print alien.update()
        # for alien in alien_list:        #call aliens from list
        #     print alien.off_screen()


        # seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        # if seconds>25: # if more than 10 seconds close the game
        #     break
        # print (seconds)
        # # Game logic



# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1

        if change_dir_counter == 120:
            alien.change_direction()   # changes alien direction
            alien2.change_direction()
            alien3.change_direction()
            change_dir_counter = 0


        alien.update()                  #moves alien around
        alien2.update()
        alien3.update()


        alien.off_screen()             #keeps alien on screen
        alien2.off_screen()
        alien3.off_screen()

        player1.off_screen()

                                    #keeps player1 inside screen

        #Colission Detection
        if player1.x + 40 < alien.x:
            pass
            # print "No Collision"
        elif alien.x + 40 < player1.x:
            pass
            # print "No Collision"
        elif player1.y + 40 < alien.y:
            pass
            # print "No Collision"
        elif alien.y + 40 < player1.y:
            pass
            # print "No Collision"
        else:
            player1.alive = False
            lose_effect.play()
            stop_game = True


        if player1.x + 40 < alien2.x:
            pass
            # print "No Collision"
        elif alien2.x + 40 < player1.x:
            pass
            # print "No Collision"
        elif player1.y + 40 < alien2.y:
            pass
            # print "No Collision"
        elif alien2.y + 40 < player1.y:
            pass
            # print "No Collision"
        else:
            player1.alive = False
            lose_effect.play()
            stop_game = True


        if player1.x + 40 < alien3.x:
            pass
            # print "No Collision"
        elif alien3.x + 40 < player1.x:
            pass
            # print "No Collision"
        elif player1.y + 40 < alien3.y:
            pass
            # print "No Collision"
        elif alien3.y + 40 < player1.y:
            pass
            # print "No Collision"
        else:
            player1.alive = False
            lose_effect.play()
            stop_game = True




        if wormhole.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif wormhole.x + 32 > player1.x:
            pass
            # print "No Collision"
        elif wormhole.y + 32 < player1.y:
            pass
            # print "No Collision"
        elif wormhole.y + 32 > player1.y:
            pass
            # print "No Collision"
        else:
            wormhole2.alive = 3



        if wormhole2.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif wormhole2.x + 32 > player1.x:
            pass
            # print "No Collision"
        elif wormhole2.y + 32 < player1.y:
            pass
            # print "No Collision"
        elif wormhole2.y + 32 > player1.y:
            pass
            # print "No Collision"
        else:
            spaceship.alive = 3


        if spaceship.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif spaceship.x + 32 > player1.x:
            pass
            # print "No Collision"
        elif spaceship.y + 32 < player1.y:
            pass
            # print "No Collision"
        elif spaceship.y + 32 > player1.y:
            pass
            # print "No Collision"
        else:
            spaceship.alive = 4
    #

        if wormhole.alive == 1:
            scene.display1(screen)
            alien.display(screen)
            wormhole.display1(screen)
            player1.display(screen)

        elif wormhole2.alive == 2:
            scene.display2(screen)
            alien2.display(screen)
            alien2.update()
            wormhole2.display2(screen)
            alien2.off_screen()
            player1.display(screen)


        elif spaceship.alive == 3:
            scene.display3(screen)
            alien3.display(screen)
            alien3.update()
            spaceship.display3(screen)
            player1.display(screen)
        #
        # elif spaceship.alive == False:
        #     break
        #
        # text you found the mothership, you win!


        # scenes = [scene.display1(screen), scene.display2(screen), scene.display3(screen)]



        # for scene in range(len(scenes)):
        #     background = scenes[scene]
        #     wormhole.alive += 1
        #     if wormhole.alive == 2:
        #         scenes
        # #
        #
        # for scene in range(len(scenes)):
        #     new_scene = scenes[scene]
        #     if wormhole.alive == False:
        #         new_scene.displayScene(screen)
        #         print new_scene
        # #

        # scene1.display(screen)

        # for alien in alien_list:        #call aliens from list



        # scene.display1(screen)
        #
        # #
        # alien.display(screen)
        #
        # wormhole.display1(screen)
        #
        # player1.display(screen)

        # scene1.displayScene(screen)



            #  # print "what scene is playing %s" % scenes
                # m = scenes[i].displayScene(screen)



        pygame.display.update()


main()
