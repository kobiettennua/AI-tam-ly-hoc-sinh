'''import itertools
import string
import time

start = time.time()
attempts = 0    

charset = string.ascii_lowercase
target = "vinh"

for attempt in itertools.product(charset, repeat = 4):
    guess = ''.join(attempt)
    attempts += 1
    if guess == target:
        print(f"passworld found: {guess} in {attempts} tries and {time.time() - start:.2f} seconds!")
        break'''

'''from turtle import *
import colorsys

bgcolor('black')
pensize(4)
tracer(10)
h=0

def test(a,n):
    circle(5+n,60), left(a), circle(5+n,60)

for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    color(c,'black'), begin_fill()
    test(90,i/2), end_fill()
    test(160,i*1.2), penup()
    test(0,0), test(90,i/2), pendown()
done()'''



import pygame
import sys
import time
import random

pygame.init()

WIDTH, HEIGHT = 1500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Karaoke Retro Rain")

font = pygame.font.SysFont("Courier New", 70, bold=True)
logo_font = pygame.font.SysFont("Courier New", 25)

lyrics = [
    "Noi anh ve troi do con mua",
    "Khong biet bay gio em da on chua",
    "Anh khong the yeu them mot nguoi",
    "Cam xuc cua anh chang con nhu xua",
    "Noi anh di noi do khong em dem toi bao vay anh thi xin thua",
    "Chac em khong muon nho anh roi",
    "Cam xuc bay gio dong lai dieu thuoc",
    "     ...  "
]

WHITE = (255, 255, 255)
RAIN_COLOR = (200,200, 255)
LOGO_COLOR = (180, 180, 180)

word_delay = 0.2
line_delay = 0.5


class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.uniform(2, 5)
        self.length = random.randint(8, 15)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)
            self.speed = random.uniform(2, 5)
            self.length = random.randint(8, 15)

    def draw(self, surface):
        pygame.draw.line(surface, RAIN_COLOR,
                         (self.x, self.y),
                         (self.x, self.y + self.length), 2)

raindrops = [Raindrop() for _ in range(100)]

def draw_scanlines(surface):
    for y in range(0, HEIGHT, 4):
        pygame.draw.line(surface, (50, 50, 50), (0, y), (WIDTH, y))


class NoiseSpot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(2, 6)
        gray = random.randint(80, 180)
        self.color = (gray, gray, gray)
        self.lifetime = random.uniform(0.1, 0.5)
        self.birth = time.time()

    def draw(self, surface):
        if time.time() - self.birth > self.lifetime:
            self.reset()
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.size, self.size))

noises = [NoiseSpot() for _ in range(60)]

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines, current = [], ""
    for w in words:
        test_line = current + w + " "
        if font.size(test_line)[0] <= max_width - 200:
            current = test_line
        else:
            lines.append(current.strip())
            current = w + " "
    if current:
        lines.append(current.strip())
    return lines

def render_frame(displayed):
    frame = pygame.Surface((WIDTH, HEIGHT))
    frame.fill((0, 0, 0))

    for drop in raindrops:
        drop.fall()
        drop.draw(frame)

    lines = wrap_text(displayed.strip(), font, WIDTH)
    y = HEIGHT // 2 - len(lines) * font.get_height() // 2
    for l in lines:
        text_surface = font.render(l, True, WHITE)
        rect = text_surface.get_rect(center=(WIDTH // 2, y))
        frame.blit(text_surface, rect)
        y += font.get_height() + 10

    draw_scanlines(frame)

    for n in noises:
        n.draw(frame)

    screen.blit(frame, (0, 0))
    pygame.display.flip()

for line in lyrics:
    words = line.split()
    displayed = ""

    for word in words:
        displayed += word + " "
        start_time = time.time()

        while time.time() - start_time < word_delay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            render_frame(displayed)

    delay_start = time.time()
    while time.time() - delay_start < line_delay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        render_frame(displayed)

pygame.quit()
sys.exit()

