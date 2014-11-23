__author__ = 'Basti'

import random
from pygame import *
from pygame.sprite import *


def main():
    pygame.init()

    size = width, height = 640, 480
    run = True
    hitted_the_mole = False
    score = 0
    black = (0, 0, 0)
    white = (255, 255, 255)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    cursor_picture = pygame.image.load('./images/schaufel.png').convert_alpha()
    collideSound = pygame.mixer.Sound('./sounds/collide.wav')
    mole = Mole()
    sprites = RenderPlain(mole)
    lastMovementOfTheMole = 0
    font = pygame.font.SysFont(None, 25)

    # Display
    screen.fill(white)
    pygame.display.set_caption('Hit the mole!')

    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

    # Loop
    while run:
        # Timing
        clock.tick(30)
        actualTimeInSeconds = int(round(pygame.time.get_ticks()/1000))

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mole.rect.collidepoint(mouse.get_pos()) and not hitted_the_mole:
                    hitted_the_mole = True
                    collideSound.play()
                    score += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                pygame.image.save(screen, "screenshot.jpg")

        screen.fill(white)

        sprites.draw(screen)
        screen.blit(cursor_picture, pygame.mouse.get_pos())

        text = font.render("Score: " + str(score), True, black)
        screen.blit(text, (0, 0))

        # change mole position after every second
        if lastMovementOfTheMole != actualTimeInSeconds:
            lastMovementOfTheMole = actualTimeInSeconds

            hitted_the_mole = False
            mole.move(random.randint(0, width - mole.rect.width), random.randint(0, height - mole.rect.height))

        pygame.display.update()


class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        MoleImage = image.load("./images/mole.png")

        self.image = MoleImage.convert_alpha()
        self.width = self.image.get_width
        self.height = self.image.get_height
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = mouse.get_pos()

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

if __name__ == '__main__':
    main()