import pygame as pg
import random

# Initialize Pygame
pg.init()

# Set the screen size
screen = pg.display.set_mode((1000, 800))

# Set the caption of the window
pg.display.set_caption(r'PP2/\LAB7/\3.py')

# Create a clock object to control the frame rate
clock = pg.time.Clock()

# Create a surface for the menu
menue = pg.Surface((200, 800))
menue.fill((255, 100, 100))

# Initialize variables for drawing
p_f = 1
f = 1
c = 'black'
p_c = 'black'
d = 2
running = True

# Define the Button class
class Button(pg.sprite.Sprite):
    def __init__(self, flag, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.flag = flag
        # Create surface for different types of buttons
        if flag == 0:
            self.img = pg.Surface((70, 70))
            self.c = img
            self.img.fill(self.c)
        elif self.flag == 2:  # RECT
            self.img = pg.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pg.draw.rect(self.img, (0, 0, 0), (10, 20, 50, 35), 2)
        elif self.flag == 3:  # CIRCLE
            self.img = pg.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pg.draw.circle(self.img, (0, 0, 0), (35, 35), 20, 2)
        # Add other button types here
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.img, self.rect)

    def check(self, p):
        if self.rect.left < p[0] < self.rect.right and self.rect.top < p[1] < self.rect.bottom:
            return True
        else:
            return False

    def change(self):
        if self.flag == 0:
            self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.img.fill(self.c)

# Create buttons
pencil = Button(1, "pencil.png", 20, 50)
eraser = Button(1, "eraser2.png", 110, 50)
randomizer = Button(4, 'rand.png', 20, 160)
rec = Button(2, None, 20, 280)
cir = Button(3, None, 110, 280)
sqr = Button(5, None, 20, 390)
rtr = Button(6, None, 110, 390)
etr = Button(7, None, 20, 500)
rho = Button(8, None, 110, 500)

buttons = pg.sprite.Group()

# Add buttons to the sprite group
for i in range(0, 8, 2):
    buttons.add(Button(0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 20, 610 + i / 2 * 110))
    buttons.add(Button(0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 110, 610 + i / 2 * 110))

buttons.add(cir)
buttons.add(rec)
buttons.add(pencil)
buttons.add(eraser)
buttons.add(randomizer)
buttons.add(sqr)
buttons.add(rtr)
buttons.add(etr)
buttons.add(rho)

# Initialize variables for drawing
prev, cur = None, None
screen.fill('white')

# Main loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            prev = pg.mouse.get_pos()
            if -1 < prev[0] < 201:
                for o in buttons:
                    if o.check(prev):
                        f = o.flag
                        if f == 0:
                            f = p_f
                            c = o.c
                        elif f == 1:
                            p_f = 1
                            d = 2
                            if p_c:
                                c = p_c
                                p_c = None
                            if o == eraser:
                                d = 5
                                p_c = c
                                c = 'white'
                        elif f in [2, 3, 5, 6, 7, 8]:
                            p_f = f
                        elif f == 4:
                            for i in buttons:
                                i.change()
                        break

        if f == 1:
            if event.type == pg.MOUSEMOTION:
                cur = pg.mouse.get_pos()
                if prev:
                    pg.draw.line(screen, c, prev, cur, d)
                    prev = cur
            if event.type == pg.MOUSEBUTTONUP:
                prev = None
        # Add event handling for other button types here

    screen.blit(menue, (0, 0))
    for o in buttons:
        o.draw()
    pg.display.flip()

    clock.tick(300)

pg.quit()
