from pygame import *
from random import randint
mixer.pre_init(44100, -16, 1, 512)
init()
font.init()

x1 = 350
y1 = 400
#создай окно игры
width_win = 700
height_win = 500
window = display.set_mode((width_win, height_win))
display.set_caption("Пинг-Понг")
#задай фон сцены
background = transform.scale(image.load('zadniy_phone.png'), (700, 500))
FPS = 60

score = 0
game = True

class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
