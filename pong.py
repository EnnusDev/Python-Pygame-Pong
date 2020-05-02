import pygame
import os

path = r"C:\User\Path"

class Ball(object):
    
    def __init__(self, x, y, dirx, diry, side):
        self.x = x
        self.y = y
        self.dirx = dirx
        self.diry = diry
        self.side = side

    def move(self):
        global height, width, player1, player2
        
        if self.y <= 50 and self.diry == -5:
            self.diry = 5
        elif self.y + self.side >= height and self.diry == 5:
            self.diry = -5
        elif self.x == player1.x + player1.width and self.dirx == -5:
            if self.y < player1.y + player1.height and self.y + self.side > player1.y:
                self.dirx = 5
        elif self.x + self.side == player2.x and self.dirx == 5:
            if self.y < player2.y + player2.height and self.y  + self.side > player2.y:
                self.dirx = -5
        
        self.x += self.dirx
        self.y += self.diry

    def draw(self, window):
        pygame.draw.rect(window, white, (self.x, self.y, self.side, self.side))

    def score(self):
        global ball, score1, score2
        if self.x == width - self.side:
            score1 += 1
            ball = Ball(width//2 -5, height//2 -5, -5, -5, 20)
        if self.x == 0:
            score2 += 1
            ball = Ball(width//2 -5, height//2 -5, 5, -5, 20)        


class Paddle(object):
    
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.y > 50:
            self.y -= self.vel
        elif key[pygame.K_DOWN] and self.y + self.height < height:
            self.y += self.vel

    def computer (self):
        global ball, width, height

        if ball.x > width//4 and ball.dirx > 0:
            if self.y < ball.y and self.y + self.height < height:
                self.y += self.vel
            elif self.y > ball.y and self.y > 50:
                self.y -= self.vel

    def draw(self, window):
        pygame.draw.rect(window, white, (self.x, self.y, self.width, self.height))


def menu(window):

    font = pygame.font.SysFont("comicsans", 30, True)

    label_player1 = font.render("You ", 1, white)
    window.blit(label_player1, (150,20))

    label_player2 = font.render("Computer ", 1, white)
    window.blit(label_player2, (width - 200,20))

    label_score = font.render(str(score1) + " - " + str(score2), 1, white)
    window.blit(label_score, (width//2 - 20,20))

    pygame.draw.line(window, white, (0, 50), (width, 50))

def sprint():
    global FPS
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        FPS = 60
    else:
        FPS = 30

def redraw(window):
    
    window.fill(black)
    window.blit(pygame.image.load(os.path.join(path, "bg.png")), (0,50))
    menu(window)
    ball.draw(window)
    player1.draw(window)
    player2.draw(window)

    pygame.display.update()


def main():

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    run = True
    while run: 
        
        clock.tick(FPS) 
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        
        player1.move()
        player2.computer()
        ball.move()
        ball.score()
        sprint()
        redraw(window)
    pygame.quit()


if __name__ == "__main__":
    FPS = 30
    width = 700
    height = 500
    score1 = 0
    score2 = 0
    white = (255,255,255)
    black = (0,0,0)
    ball = Ball(width//2 -5, height//2 -5, -5, -5, 20)
    player1 = Paddle(20, height//2, 10, 50, 5)
    player2 = Paddle(width - 30, height//2, 10, 50, 5)
    main()
