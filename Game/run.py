__author__ = 'Basti'

from pygame import *
from pygame.sprite import *


def main():
    pygame.init()

    # Display
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Paint Brush')

    # Entities
    # bg = pygame.image.load('./images/world.jpg') # Background images
    # screen.blit(bg, (0, 0))

    black_brush = pygame.image.load('./images/blackBrush.gif')
    yellow_brush = pygame.image.load('./images/yellowBrush.gif')
    red_brush = pygame.image.load('./images/redBrush.gif')

    black_brush = pygame.transform.scale(black_brush, (32, 32))
    yellow_brush = pygame.transform.scale(yellow_brush, (32, 32))
    red_brush = pygame.transform.scale(red_brush, (32, 32))

    brush = black_brush
    # brush = pygame.transform.scale(brush, (64, 64))
    xPos = yPos = 16
    # brushRect = brush.get_rect()
    pygame.display.update()

    # Loop == ALTER
    # Assign Values to key variables
    keepGoing = True
    paint = False
    clock = pygame.time.Clock()

    ball = Ball()

    sprites = RenderPlain(ball)

    sprites.draw(screen)

    # Loop
    while keepGoing:
        # Timing
        clock.tick(30)

        # Events
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ball.rect.collidepoint(mouse.get_pos()):
                    print('collide')
                paint = True
            elif event.type == pygame.MOUSEBUTTONUP:
                paint = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                pygame.image.save(screen, "screenshot.jpg")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                brush = black_brush
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                brush = red_brush
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_y or event.key == pygame.K_z):
                brush = yellow_brush
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                brush = pygame.transform.scale(brush, (32, 32))
                xPos = yPos = 16
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                brush = pygame.transform.scale(brush, (16, 16))
                xPos = yPos = 8

        # Refresh Display
        if paint:
            # screen.blit(bg, (0, 0))
            screen.blit(brush, (x-xPos, y-yPos))
            pygame.display.update()


class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("./images/yellowBrush.gif").convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = mouse.get_pos()

if __name__ == '__main__':
    main()