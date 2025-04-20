Fron pygane tvport

class Gamesprito(sprite.Sprite):

Аконструктор класса

dat init (seit, player image, player x, player y, sise x, size y, player speed): (Sprite):sprits. Sprite. init (self)
self.innge transform.scale(image.load(playerinage), (sicex, simy))
self.speed player speed

всикдый спрайт должен хранить свойство тест прахоугольник, который он висин

salf.rect self.image.get_rect()

self.rect.x player x

self.rect.y player y

Инстед, стоксовивающий героя на оке

def reset(self):

window.blit(self.image, (self.rect.x, self.rect.y))

класс главного игрока

class Player(GmSprite):в четод для упрекления спорей стрелками клавиатури
def update(self):
kayabay.got pressed()
1 koys[LEFT] and self.rect.x S
self.rect.x self.spood
it keys [KR] and seat.rect.x win width
self.rect.x salt.speed

class Player2(GameSprite):
  def update_r(self):
    keys pressed = key.get_pressed()
  if keys_pressed[K_UP] and self.rect.y >= 15:
    self.rect.y = self.speed
  if keys_pressed[X_DOWN] and self.rect.y <= 485:
    self.rect.y

a =arandint(1, 2)

window display.set_mode((700, 508))
display.set_caption("qeqoqeq')
background = transfora.scale(image.load('map.png"), (700, 500))

player Player('square.png", 15, 218, 15, 15, 65)

player2 = Player2('square.png', 620, 217, 15, 15, 65)
ball GameSprite('ball.png', 318, 218, 20, 40, 30)
