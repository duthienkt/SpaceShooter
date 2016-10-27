import random
import math
from constant import *
from garfield import *


class Bullet(GUpdatable, GDrawable):
    def __init__(self, im, expl_im, pos, head):
        self.img = im
        self.head = head
        self.position = pos
        self.explosionIm = expl_im
        self.alive = True

    def update(self, delta_time):
        if not self.alive:
            self.explosionIm.update(delta_time)

    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        (x, y) = self.position
        x -= x0
        y -= y0

        if self.alive:
            (x0, y0) = self.head
            x -= x0
            y -= y0
            screen.blit(self.img, (x, y))
        else:
            x -= self.explosionIm.width / 2
            y -= self.explosionIm.height / 2
            self.explosionIm.draw(screen, (x, y))

    def explosive(self):
        self.alive = False

    def is_alive(self):
        return self.alive or self.explosionIm.is_continued()

    def get_damage(self, distance):
        return distance * 0


class UpBulletType1(Bullet):
    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y -= delta_time * 300 / 1000
            self.position = (x, y)

    def __init__(self, pos):
        super().__init__(
            garfield_load_image(PATH_BULLET[0]),
            Animation(PATH_BULLET_EXPLOSION[0], BULLET_EXPLOSION_LENGTH[0], 70, False),
            pos
            , BULLET_HEAD[0])

    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 1


class UpBulletType2(Bullet):
    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y -= delta_time * 400 / 1000
            self.position = (x, y)

    def __init__(self, pos):
        super().__init__(
            garfield_load_image(PATH_BULLET[1]),
            Animation(PATH_BULLET_EXPLOSION[1], BULLET_EXPLOSION_LENGTH[1], 70, False),
            pos
            , BULLET_HEAD[1])

    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 2


class UpBulletType3(Bullet):
    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y -= delta_time * 500 / 1000
            self.position = (x, y)

    def __init__(self, pos):
        super().__init__(
            garfield_load_image(PATH_BULLET[2]),
            Animation(PATH_BULLET_EXPLOSION[2], BULLET_EXPLOSION_LENGTH[2], 70, False),
            pos
            , BULLET_HEAD[2])

    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 4


class UpRocketType1(Bullet):
    def get_damage(self, distance):
        if distance > 140:
            return 0
        else:
            return 50 / (1 + (distance / 14) * (distance / 14))

    def __init__(self, pos):
        super().__init__(Animation(PATH_BULLET[6], 2, 100),
                         Animation(PATH_BULLET_EXPLOSION[6], BULLET_EXPLOSION_LENGTH[6], 70, False),
                         pos
                         , BULLET_HEAD[6])
        self.speed = 200

    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y -= delta_time * self.speed / 1000.0
            self.speed += delta_time * 250 / 1000.0
            self.position = (x, y)
            self.img.update(delta_time)

    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        (x, y) = self.position
        x -= x0
        y -= y0
        if self.alive:
            (x0, y0) = self.head
            x -= x0
            y -= y0
            self.img.draw(screen, (x, y))
        else:
            x -= self.explosionIm.width / 2
            y -= self.explosionIm.height / 2
            self.explosionIm.draw(screen, (x, y))


class UpRocketType2(Bullet):
    def get_damage(self, distance):
        if distance > 200:
            return 0
        else:
            return 100 / (1 + (distance / 14) * (distance / 14))

    def __init__(self, pos):
        super().__init__(Animation(PATH_BULLET[7], 2, 100),
                         Animation(PATH_BULLET_EXPLOSION[7], BULLET_EXPLOSION_LENGTH[7], 70, False),
                         pos
                         , BULLET_HEAD[7])
        (self.centerX, y) = self.position
        self.dr = random.randint(0, 1) * 2 - 1
        self.rad = 0
        self.speed = 250

    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            x = self.centerX + 70 * math.sin(self.rad)* self.dr
            self.rad += math.pi * delta_time / 1000.0
            if self.rad > math.pi * 2:
                self.rad -= math.pi * 2
            y -= delta_time * self.speed / 1000
            self.speed += delta_time * 270 / 1000.0
            self.position = (x, y)
            self.img.update(delta_time)

    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        (x, y) = self.position
        x -= x0
        y -= y0
        if self.alive:
            (x0, y0) = self.head
            x -= x0
            y -= y0
            self.img.draw(screen, (x, y))
        else:
            x -= self.explosionIm.width / 2
            y -= self.explosionIm.height / 2
            self.explosionIm.draw(screen, (x, y))


########################################################################################################################

class BulletPath:
    pass

class CircleBulletPath(BulletPath):
    def __init__(self, center, number_of_bullet, speed, image = "red"):
        super().__init__()
        self.bulletList = []
        self.number_of_bullet = number_of_bullet
        self.make_bullet(center,number_of_bullet,speed, image)

    def make_bullet(self, center, number_of_bullet,speed, image):
        angle_inc = math.pi*2 / number_of_bullet
        for i in range (0, number_of_bullet):
            rad = i*angle_inc
            dx = math.cos(rad)
            dy = math.sin(rad)
            direction = (dx,dy)
            self.bulletList.append(BulletInPath(image, center, speed, direction))

class DiamondBulletPath (BulletPath):
    def __init__(self, center , number_of_bullet, speed, image = "blue"):
        self.center = center
        self.bulletList = []
        self.number_of_bullet = number_of_bullet
        self.make_bullet(center, number_of_bullet, speed, image)

    def make_bullet(self, center, number_of_bullet, speed, image):
        offset = [0]*4
        (x0, y0) = center
        for i in range(0, number_of_bullet):

            if (i%4 == 0):
                direction = (1,1)
                offset[0] += 1
                (dx, dy) = direction
                newx = x0 - dx*offset[0]*20
                newy = y0 + dy*offset[0]*20
            elif (i%4 == 1):
                direction = (-1, -1)
                offset[1] += 1
                (dx, dy) = direction
                newx = x0 - dx * offset[1] * 20
                newy = y0 + dy * offset[1] * 20
            elif (i%4 == 2):
                direction = (-1, 1)
                offset[2] += 1
                (dx, dy) = direction
                newx = x0 + dx * offset[2] * 20
                newy = y0 - dy * offset[2] * 20
            else:
                direction = (1, -1)
                offset[3] += 1
                (dx, dy) = direction
                newx = x0 + dx * offset[3] * 20
                newy = y0 - dy * offset[3] * 20

            self.bulletList.append(BulletInPath(image, (newx,newy), speed, direction))


class BulletInPath(Bullet):
    def __init__(self, path, pos, speed, direction):
        bullet_img = 10
        if (path == "red"):
            bullet_img = 10
        elif (path == "blue"):
            bullet_img = 11
        elif (path == "green"):
            bullet_img = 12
        elif (path == "yellow"):
            bullet_img = 13
        super().__init__(
            garfield_load_image(PATH_BULLET[bullet_img]),
            Animation(PATH_BULLET_EXPLOSION[3], BULLET_EXPLOSION_LENGTH[3], 70, False),
            pos
            , BULLET_HEAD[3])
        self.path = path
        self.speed = speed
        self.direction = direction

    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
                (x, y) = self.position
                (dx,dy) = self.direction
                inc = delta_time * self.speed / 1000
                x += inc*dx
                y += inc*dy
                self.position = (x, y)


    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 1


class DownBulletType1(Bullet):
    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y += delta_time * 150 / 1000
            self.position = (x, y)

    def __init__(self, pos):
        super().__init__(
            garfield_load_image(PATH_BULLET[3]),
            Animation(PATH_BULLET_EXPLOSION[3], BULLET_EXPLOSION_LENGTH[3], 70, False),
            pos
            , BULLET_HEAD[3])

    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 1


class DownBulletType2(Bullet):
    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y += delta_time * 250 / 1000
            self.position = (x, y)

    def __init__(self, pos):
        super().__init__(
            garfield_load_image(PATH_BULLET[4]),
            Animation(PATH_BULLET_EXPLOSION[4], BULLET_EXPLOSION_LENGTH[1], 70, False),
            pos
            , BULLET_HEAD[4])

    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 2


class DownBulletType3(Bullet):
    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y += delta_time * 300 / 1000
            self.position = (x, y)

    def __init__(self, pos):
        super().__init__(
            garfield_load_image(PATH_BULLET[5]),
            Animation(PATH_BULLET_EXPLOSION[5], BULLET_EXPLOSION_LENGTH[5], 70, False),
            pos
            , BULLET_HEAD[5])

    def get_damage(self, distance):
        if distance > 0:
            return 0
        return 4


class DownRocketType1(Bullet):
    def get_damage(self, distance):
        if distance > 140:
            return 0
        else:
            return 50 / (1 + (distance / 14) * (distance / 14))

    def __init__(self, pos):
        super().__init__(Animation(PATH_BULLET[8], 2, 100),
                         Animation(PATH_BULLET_EXPLOSION[8], BULLET_EXPLOSION_LENGTH[8], 70, False),
                         pos
                         , BULLET_HEAD[8])

    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            y += delta_time * 170 / 1000
            self.position = (x, y)
            self.img.update(delta_time)

    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        (x, y) = self.position
        x -= x0
        y -= y0
        if self.alive:
            (x0, y0) = self.head
            x -= x0
            y -= y0
            self.img.draw(screen, (x, y))
        else:
            x -= self.explosionIm.width / 2
            y -= self.explosionIm.height / 2
            self.explosionIm.draw(screen, (x, y))


class DownRocketType2(Bullet):
    def get_damage(self, distance):
        if distance > 200:
            return 0
        else:
            return 100 / (1 + (distance / 14) * (distance / 14))

    def __init__(self, pos):
        super().__init__(Animation(PATH_BULLET[9], 2, 100),
                         Animation(PATH_BULLET_EXPLOSION[9], BULLET_EXPLOSION_LENGTH[9], 70, False),
                         pos
                         , BULLET_HEAD[9])
        (self.centerX, y) = self.position
        self.dr = random.randint(0, 1) * 2 - 1
        self.rad = 0

    def update(self, delta_time):
        super().update(delta_time)
        if self.alive:
            (x, y) = self.position
            x = self.centerX + 70 * math.sin(self.rad)
            self.rad += math.pi * delta_time / 1000.0 * self.dr
            if self.rad > math.pi * 2:
                self.rad -= math.pi * 2
            y += delta_time * 220 / 1000

            self.position = (x, y)
            self.img.update(delta_time)

    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        (x, y) = self.position
        x -= x0
        y -= y0
        if self.alive:
            (x0, y0) = self.head
            x -= x0
            y -= y0
            self.img.draw(screen, (x, y))
        else:
            x -= self.explosionIm.width / 2
            y -= self.explosionIm.height / 2
            self.explosionIm.draw(screen, (x, y))


#######################################################################################################################
class Player(GDrawable, GUpdatable, KeyboardInteractive):
    def __init__(self, space, pos, menu_tool):
        self.menuTool = menu_tool
        self.space = space
        self.position = pos
        self.bulletSpace = space.playerBullets
        self.rockets = [15, 5]

        self.dxc = 0
        self.dyc = 0
        self.level = 0
        self.gun = PLAYER_GUN[self.level]
        self.gunId = 0
        self.img = garfield_load_image(PATH_PLAYER[self.level])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.speed = PLAYER_SPEED[self.level]
        self.hp = PLAYER_HP[self.level]
        self.menuTool.set_hp(100)
        self.gunDelay = 0
        self.dImg = None
        self.power = 0
        self.coin = 0
        self.menuTool.set_rocket_type1(self.rockets[0])
        self.menuTool.set_rocket_type2(self.rockets[1])
        self.menuTool.set_coin(self.coin)
        self.menuTool.set_power(self.power)

    def inc_rocket(self, d, id):
        self.rockets[id] += d
        self.menuTool.set_rocket_type1(self.rockets[0])
        self.menuTool.set_rocket_type2(self.rockets[1])

    def inc_coin(self, c):
        self.coin += c
        self.menuTool.set_coin(self.coin)

    def inc_power(self, p):
        self.power += p
        self.menuTool.set_power(self.power)
        if self.power <= 2:
            self.change_level(0)
        elif self.power <= 6:
            self.change_level(1)
        elif self.power <= 15:
            self.change_level(2)
        else:
            self.change_level(3)

    def change_level(self, lev):
        if self.level == lev:
            return
        self.menuTool.set_level(lev)
        self.level = lev
        self.gun = PLAYER_GUN[self.level]
        self.img = garfield_load_image(PATH_PLAYER[self.level])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.speed = PLAYER_SPEED[self.level]
        self.hp = PLAYER_HP[self.level]
        self.menuTool.set_hp(100)
        self.menuTool.set_rocket_type1(self.rockets[0])
        self.menuTool.set_rocket_type2(self.rockets[1])

    def update(self, delta_time):
        (x, y) = self.position
        if abs(self.hp) <= 0.001:
            if self.hp > -0.5:
                if self.dImg is None:
                    self.dImg = Animation(PATH_EFF + "die.png", 5, 100, False)
                elif not self.dImg.is_continued():
                    self.hp = -1
                    self.dImg = None
        if self.dImg is not None:
            self.dImg.update(delta_time)
            return
        if self.hp < 0:
            return
        dl = math.sqrt(self.dxc * self.dxc + self.dyc * self.dyc)
        if dl > 0:
            # print((self.dxc, self.dyc))
            x += self.dxc * self.speed * delta_time / 1000.0 / dl
            y += self.dyc * self.speed * delta_time / 1000.0 / dl
            # print((dx, dy))
        y += self.space.screenSpeed * delta_time / 1000.0
        if y > self.space.screenY + 640:
            y = self.space.screenY + 640
        if y < self.space.screenY + 50:
            y = self.space.screenY + 50
        if x < 50:
            x = 50
        if x > 750:
            x = 750

        self.position = (x, y)
        self.gunDelay += delta_time

        if self.gunDelay > 60000 / self.speed / (self.speed / 100):
            self.gunDelay %= 60000 / self.speed / (self.speed / 100)
            self.fire(0)

    def draw(self, screen, position=(0, 0)):
        (x, y) = self.position
        (x0, y0) = position
        if self.dImg is not None:
            x -= x0 + self.dImg.width / 2
            y -= y0 + self.dImg.height / 2
            self.dImg.draw(screen, (x, y))
        else:
            if self.hp > 0:
                x -= x0 + self.width / 2
                y -= y0 + self.height / 2
                screen.blit(self.img, (x, y))

    def on_key_pressed(self, key):
        if key == 122:
            self.fire(1)
            return True
        if key == 120:
            self.fire(2)
            return True
        if key == 273:
            self.dyc = -1
            return True
        if key == 274:
            self.dyc = 1

        if key == 276:
            self.dxc = -1
            return True
        if key == 275:
            self.dxc = 1
            return True

    def on_key_released(self, key):
        if key == 273:
            if self.dyc < 0:
                self.dyc = 0
            return True
        if key == 274:
            if self.dyc > 0:
                self.dyc = 0
        if key == 276:
            if self.dxc < 0:
                self.dxc = 0
            return True
        if key == 275:
            if self.dxc > 0:
                self.dxc = 0
            return True

    def fire(self, bullet_id):
        if bullet_id == 0:
            self.gunId = (self.gunId + 1) % len(self.gun)
            b = None
            (x0, y0) = self.position
            (x, y) = self.gun[self.gunId]
            x0 += x - self.width / 2
            y0 += y - self.height / 2
            if self.level == 0:
                b = UpBulletType1((x0, y0))
            elif self.level == 1:
                b = UpBulletType2((x0, y0))
            elif self.level == 2:
                b = UpBulletType3((x0, y0))
            elif self.level == 3:
                k = random.randint(0, 5) % 3
                if k == 0:
                    b = UpBulletType3((x0, y0))
                elif k == 1:
                    b = UpBulletType1((x0, y0))
                elif k == 2:
                    b = UpBulletType2((x0, y0))
            self.bulletSpace.append(b)

        if bullet_id == 1:
            if self.rockets[0] > 0:
                (x0, y0) = self.position
                y0 -= self.height / 3
                self.bulletSpace.append(UpRocketType1((x0, y0)))
                self.rockets[0] -= 1
                self.menuTool.set_rocket_type1(self.rockets[0])
        if bullet_id == 2:
            if self.rockets[1] > 0:
                (x0, y0) = self.position
                y0 -= self.height / 3
                self.bulletSpace.append(UpRocketType2((x0, y0)))
                self.rockets[1] -= 1
                self.menuTool.set_rocket_type2(self.rockets[1])
        pass

    def check(self, pos):
        (x0, y0) = self.position
        (x, y) = pos
        x += -x0 + self.width / 2
        y += -y0 + self.height / 2
        c = garfield_pick_color(self.img, (x, y))
        if c is None:
            return False
        (r, g, b, a) = c
        return a > 20

    def is_alive(self):
        return self.hp > -0.5 or self.dImg is not None

    def damage(self, d):
        if self.hp < 0:
            return
        self.hp -= d
        if self.hp < 0:
            self.space.screenSpeed = -100
            self.hp = 0
            garfield_sound_play(PATH_EXPL_SOUND)
        if self.hp > PLAYER_HP[self.level]:
            self.hp = PLAYER_HP[self.level]
        self.menuTool.set_hp(self.hp / PLAYER_HP[self.level] * 100)


########################################################################################################################
class EnemyType1(GDrawable, GUpdatable, KeyboardInteractive):
    def __init__(self, space, pos):
        self.space = space
        self.position = pos
        self.bulletSpace = space.enemyBullets
        self.dxc = 30 * (random.randint(0, 1) * 2 - 1)
        self.dyc = -12 * (random.randint(0, 1) * 2 - 1)
        self.gunId = 0
        self.img = garfield_load_image(PATH_ENEMY[0])
        self.dImg = None
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.hp = 24
        self.gunDelay = 0
        self.gunElapse = 500
        self.dr = random.randint(0, 1) * 2 - 1
        self.gun = [(36, 72), (67, 72)]
        self.lastGun = 0

    def update(self, delta_time):
        if abs(self.hp) <= 0.001:
            if self.hp > -0.5:
                if self.dImg is None:
                    self.dImg = Animation(PATH_EFF + "bum.png", 8, 100, False)
                elif not self.dImg.is_continued():
                    self.hp = -1
                    self.dImg = None
        if self.dImg is not None:
            self.dImg.update(delta_time)
            return
        if self.hp < 0:
            return
        self._active(delta_time)
        self._active_gun(delta_time)

    #Moving enemy
    def _active(self, delta_time):
        (x, y) = self.position
        if x < 5:
            self.dxc = 30
        if x > 795:
            self.dxc = -30
        x += self.dxc * delta_time / 1000.0
        y += self.dyc * delta_time / 1000.0 * self.dr

        self.position = (x, y)

    def _active_gun(self, delta_time):
        self.gunDelay += delta_time
        delta_delay = random.randint(0, 2 * self.gunDelay)
        if self.gunDelay > self.gunElapse + delta_delay:
            self.gunDelay = 0
            self.fire()

    def draw(self, screen, position=(0, 0)):
        (x, y) = self.position
        (x0, y0) = position
        if self.dImg is not None:
            x -= x0 + self.dImg.width / 2
            y -= y0 + self.dImg.height / 2
            self.dImg.draw(screen, (x, y))
        else:
            if self.hp > 0:
                x -= x0 + self.width / 2
                y -= y0 + self.height / 2
                screen.blit(self.img, (x, y))

    def select_gun(self):
        self.lastGun = (self.lastGun + 1) % len(self.gun)
        return self.lastGun

    def fire(self):
        (x0, y0) = self.position
        (x, y) = self.gun[self.select_gun()]
        y0 += y - self.height / 2
        x0 += x - self.width / 2

        b = DownBulletType1((x0, y0))
        self.bulletSpace.append(b)

        r = random.randint(1,15)
        if (r == 1):
            bullet_number = random.randint(10,20)
            for j in range(0,5):
                bulletPath = CircleBulletPath(self.position, bullet_number, 100 + 10*j)
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)

        if (r == 2):
            for j in range(0, 10):
                (x0,y0) = self.position
                (x,y) = self.space.player.position
                dx = x-x0
                dy = y-y0
                if dx > 0: direcx = 1
                else: direcx = -1
                if dy > 0: direcy = abs(dy/dx)
                else: direcy = -abs(dy/dx)
                direction = (direcx, direcy)
                print(direction)
                b = BulletInPath("yellow", self.position, 300 + 10*j, direction)
                self.bulletSpace.append(b)

    def check(self, pos):
        (x0, y0) = self.position
        (x, y) = pos
        x += -x0 + self.width / 2
        y += -y0 + self.height / 2
        c = garfield_pick_color(self.img, (x, y))
        if c is None:
            return False
        (r, g, b, a) = c
        return a > 20

    def is_alive(self):
        return self.hp > -0.5 or self.dImg is not None

    def damage(self, d):
        if self.hp <= 0:
            return
        if (self.hp<= d):
            self.exp_sound()
        self.hp -= d
        if self.hp <= 0:
            self.add_item(self.width / 2, self.height / 2)
            self.hp = 0

    def get_value_of_coin(self):
        return 14

    def get_value_of_rocket(self, id):
        if id == 0:
            return 5
        else:
            return 2

    def get_fred_per_100x5(self):
        return [10, 50, 20, 10, 10]

    def add_item(self, dix, diy):
        d = 0
        s = self.get_fred_per_100x5()
        x = random.randint(0, 100)
        for i in range(5):
            d += s[i]
            if d >= x:
                self.space.items.append(self.get_item(i, dix, diy))
                return

    def get_item(self, id_type, im_x, im_y):
        (x, y) = self.position
        x += -self.width / 2 + im_x
        y += -self.height / 2 + im_y
        if id_type == 0:
            return HpItem((x, y), self.space)
        elif id_type == 1:
            return CoinItem((x, y), self.space, self.get_value_of_coin())
        elif id_type == 2:
            return Rocket1Item((x, y), self.space, self.get_value_of_rocket(0))
        elif id_type == 3:
            return Rocket2Item((x, y), self.space, self.get_value_of_rocket(1))
        elif id_type == 4:
            return PowerItem((x, y), self.space)
    def exp_sound(self):
        garfield_sound_play(PATH_EXPL_SOUND)


class EnemyType2(EnemyType1):
    def __init__(self, space, pos):
        super().__init__(space, pos)
        self.hp = 45
        self.img = garfield_load_image(PATH_ENEMY[1])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.gun = [(22, 45), (60, 45)]
        self.hp = 24
        self.gunDelay = 0
        self.gunElapse = 700
        self.eg = 0
        self.hv = (random.randint(0,1000)%2)*2-1

    def _active(self, delta_time):
        (x, y) = self.position
        if x < 0:
            self.dxc = 30
        if x > 800:
            self.dxc = -30
        if y < self.space.screenY + 400:
            if x < 400:
                self.dyc = -30*self.hv - random.randint(0, 5)
            else:
                self.dyc = 30*self.hv + random.randint(0, 5)

        x += self.dxc * delta_time / 1000.0
        y += self.dyc * delta_time / 1000.0

        if y+ 200> self.space.screenY+690:
            dyc = -120 - random.randint(0, 5)

        self.position = (x, y)

    def fire(self):
        (x0, y0) = self.position
        (x, y) = self.gun[self.select_gun()]
        y0 += y - self.height / 2
        x0 += x - self.width / 2
        b = DownBulletType2((x0, y0))
        self.bulletSpace.append(b)
        r = random.randint(1,5)
        if (r == 1):
            for j in range (0,5):
                bulletPath = DiamondBulletPath(self.position, 20, 100 + 10*j)
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)

        if (r == 2):
            for j in range(0, 10):
                (x0,y0) = self.position
                (x,y) = self.space.player.position
                dx = x-x0
                dy = y-y0
                if dx > 0: direcx = 1
                else: direcx = -1
                if dy > 0: direcy = abs(dy/dx)
                else: direcy = -abs(dy/dx)
                direction = (direcx, direcy)
                print(direction)
                b = BulletInPath("yellow", self.position, 300 + 10*j, direction)
                self.bulletSpace.append(b)

    def get_fred_per_100x5(self):
        return [20, 10, 10, 20, 40]


class EnemyType3(EnemyType1):
    def __init__(self, space, pos):
        super().__init__(space, pos)
        self.hp = 90
        self.img = garfield_load_image(PATH_ENEMY[2])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.gun = [(15, 60), (104, 60), (32, 42), (78, 42)]
        self.hp = 34
        self.gunDelay = 0
        self.gunElapse = 600
        self.eg = 0

    def _active(self, delta_time):
        (x, y) = self.position
        if x < 0:
            self.dxc = 50
        if x > 800:
            self.dxc = -50
        if x < 320:
            self.dyc = random.randint(-40, 40)
        else:
            self.dyc = random.randint(-30, 40)

        x += self.dxc * delta_time / 1000.0
        y += self.dyc * delta_time / 1000.0
        self.position = (x, y)

    def fire(self):
        (x0, y0) = self.position
        (x, y) = self.gun[self.select_gun()]
        y0 += y - self.height / 2
        x0 += x - self.width/2
        b = DownBulletType3((x0, y0))
        self.bulletSpace.append(b)

        r = random.randint(1,5)
        if (r == 1):
            for j in range(0,5):
                bulletPath = CircleBulletPath(self.position, random.randint(10,40), 100 + 10*j, "green")
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)

    def get_fred_per_100x5(self):
        return [30, 20, 30, 10, 20]



class EnemyBossChild(EnemyType1):
    def __init__(self, space, pos):
        super().__init__(space, pos)
        self.hp = 1500
        self.img = garfield_load_image(PATH_BOSS_CHILD)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.gun = [(68, 130), (328, 130),
                    (171, 163), (225, 163),
                    (198, 160)]
        self.gunDelay = 0
        self.gunElapse = 100
        self.rocketElapse = 2000
        self.eg = 0
        self.dxc = 20
        self.dyc = 0

    def _active(self, delta_time):
        self.space.menuTool.set_boss_visit(True)
        self.space.menuTool.set_hp_boss(self.hp / 15)
        (x, y) = self.position
        if x < self.width / 4:
            self.dxc = 10
        if x > 690 - self.width / 9:
            self.dxc = -10
        x += self.dxc * delta_time / 1000.0
        y += self.dyc * delta_time / 1000.0
        self.position = (x, y)

    def _active_gun(self, delta_time):
        self.gunDelay += delta_time
        delta_delay = random.randint(0, 2 * self.gunDelay)
        if self.gunDelay > self.gunElapse + delta_delay:
            self.gunDelay = 0
            self.fire()

    def draw(self, screen, position=(0, 0)):
        (x, y) = self.position
        (x0, y0) = position
        if self.dImg is not None:
            x -= x0 + self.dImg.width / 2
            y -= y0 + self.dImg.height / 2
            self.dImg.draw(screen, (x, y - 15))
            self.dImg.draw(screen, (x + 50, y))
            self.dImg.draw(screen, (x - 50, y))
            self.dImg.draw(screen, (x, y + 15))
        else:
            if self.hp > 0:
                x -= x0 + self.width / 2
                y -= y0 + self.height / 2
                screen.blit(self.img, (x, y))

    def get_fred_per_100x5(self):
        return [20, 15, 20, 20, 25]

    def damage(self, d):
        if self.hp > 0:
            if d >= self.hp:
                for e in self.space.enemy:
                    if e != self:
                        e.damage(10000)
                    self.add_item(10, 10)
                    self.add_item(30, 20)
                    self.add_item(70, 15)
                    self.add_item(199, 30)
                    self.add_item(210, 20)
        if self.hp // 200 != (self.hp - d) // 200:
            self.add_item(random.randint(0, self.width), random.randint(0, self.height))
        super().damage(d)
        if self.hp <= 0.01:
            self.space.screenSpeed = -60
            self.space.menuTool.set_boss_visit(False)

    def check(self, pos):
        (x0, y0) = self.position
        (x, y) = pos
        x += -x0 + self.width / 2
        y += -y0 + self.height / 2
        c = garfield_pick_color(self.img,(x, y))
        if c is None:
            return False
        (r, g, b, a) = c
        return a > 20

    def fire(self):
        if self.hp > 1200:
                self.gunElapse = 50
        elif self.hp > 1000:
                self.gunElapse = 100
        elif self.hp > 800:
                self.gunElapse = 75
        elif self.hp > 500:
            self.gunElapse = 50
        else:
            self.gunElapse = 100

        (x0, y0) = self.position
        gid = self.select_gun()
        (x, y) = self.gun[gid]
        (px, py) = self.space.player.position

        y0 += y - self.height / 2
        x0 += x - self.width / 2
        b = None
        limit = 20 + (50 - self.hp / 60)
        if gid ==4:
            limit += 30
        if (abs(x0 - px) < limit or gid == 4) and random.randint(0, 100)<30:
            if self.hp > 750:
                b = DownRocketType1((x0, y0))
            else:
                b = DownRocketType2((x0, y0))
        else:
            if self.hp > 1000:
                b = DownBulletType2((x0, y0))
            if self.hp > 500:
                if gid < 2:
                    b = DownBulletType2((x0, y0))
                else:
                    b = DownBulletType3((x0, y0))
            elif self.hp > 250:
                if gid < 2:
                    b = DownBulletType3((x0, y0))
                else:
                    b = DownBulletType3((x0, y0))
            else:
                if gid < 4:
                    b = DownBulletType3((x0, y0))
                else:
                    b = DownBulletType3((x0, y0))

        self.bulletSpace.append(b)

        r = random.randint(1, 10)
        if (r == 1):
            for j in range(0, 5):
                bulletPath = CircleBulletPath(self.position, 20, 100 + 10*j)
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)
        if (r == 5):
            for j in range(0, 5):
                bulletPath = DiamondBulletPath(self.position, 24, 100 + 10 * j)
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)

        if (r == 10):
            for j in range(0, 10):
                (x0,y0) = self.position
                (x,y) = self.space.player.position
                dx = x-x0
                dy = y-y0
                if dx > 0: direcx = 1
                else: direcx = -1
                if dy > 0: direcy = abs(dy/dx)
                else: direcy = -abs(dy/dx)
                direction = (direcx, direcy)
                print(direction)
                b = BulletInPath("yellow", self.position, 300 + 10*j, direction)
                self.bulletSpace.append(b)



class EnemyBoss(EnemyType1):
    def __init__(self, space, pos):
        super().__init__(space, pos)
        self.hp = 3000
        self.img = Animation(PATH_BOSS, 4, 100)
        self.width = self.img.width
        self.height = self.img.height
        self.gun = [(44, 227), (481, 227),
                    (70, 244), (457, 244),
                    (98, 256), (432, 256),
                    (119, 269), (409, 269),
                    (199, 315), (328, 315),
                    (0, 185), (527, 185),
                    (264, 350)]
        self.gunDelay = 0
        self.gunElapse = 100
        self.rocketElapse = 2000
        self.eg = 0
        self.dxc = 20
        self.dyc = 0

    def _active(self, delta_time):
        self.space.menuTool.set_boss_visit(True)
        self.space.menuTool.set_hp_boss(self.hp / 30)
        self.img.update(delta_time)
        (x, y) = self.position
        if x < self.width / 4:
            self.dxc = 10
        if x > 690 - self.width / 9:
            self.dxc = -10
        x += self.dxc * delta_time / 1000.0
        y += self.dyc * delta_time / 1000.0
        self.position = (x, y)

    def _active_gun(self, delta_time):
        self.gunDelay += delta_time
        delta_delay = random.randint(0, 2 * self.gunDelay)
        if self.gunDelay > self.gunElapse + delta_delay:
            self.gunDelay = 0
            self.fire()

    def draw(self, screen, position=(0, 0)):
        (x, y) = self.position
        (x0, y0) = position
        if self.dImg is not None:
            x -= x0 + self.dImg.width / 2
            y -= y0 + self.dImg.height / 2
            self.dImg.draw(screen, (x, y - 30))
            self.dImg.draw(screen, (x + 100, y))
            self.dImg.draw(screen, (x - 100, y))
            self.dImg.draw(screen, (x, y + 30))
        else:
            if self.hp > 0:
                x -= x0 + self.width / 2
                y -= y0 + self.height / 2
                self.img.draw(screen, (x, y))

    def get_fred_per_100x5(self):
        return [20, 20, 20, 20, 20]

    def damage(self, d):
        if self.hp > 0:
            if d >= self.hp:
                for e in self.space.enemy:
                    if e != self:
                        e.damage(10000)
                    self.add_item(10, 10)
                    self.add_item(30, 20)
                    self.add_item(70, 15)
                    self.add_item(199, 30)
                    self.add_item(210, 20)
        if self.hp // 200 != (self.hp - d) // 200:
            self.add_item(random.randint(0, self.width), random.randint(0, self.height))
        super().damage(d)
        if self.hp <= 0.01:
            self.space.screenSpeed = -60
            self.space.menuTool.set_boss_visit(False)

    def check(self, pos):
        (x0, y0) = self.position
        (x, y) = pos
        x += -x0 + self.width / 2
        y += -y0 + self.height / 2
        c = self.img.pick_color((x, y))
        if c is None:
            return False
        (r, g, b, a) = c
        return a > 20

    def fire(self):
        if self.hp < 2800:
            if self.hp > 2700:
                self.gunElapse = 10
            elif self.hp > 2300:
                self.gunElapse = 100
            elif self.hp > 2200:
                self.gunElapse =20
            elif self.hp > 2000:
                self.gunElapse = 15
            elif self.hp > 1900:
                self.gunElapse = 10
            elif self.hp > 1700:
                self.gunElapse = 100
            elif self.hp > 1500:
                self.gunElapse =20
            elif self.hp > 1400:
                self.gunElapse = 15
            elif self.hp > 1200:
                self.gunElapse = 10
            elif self.hp > 1000:
                self.gunElapse = 100
            elif self.hp > 800:
                self.gunElapse =20
            elif self.hp > 500:
                self.gunElapse = 15
            else:
                self.gunElapse = 50

        (x0, y0) = self.position
        gid = self.select_gun()
        (x, y) = self.gun[gid]
        (px, py) = self.space.player.position

        y0 += y - self.height / 2
        x0 += x - self.width / 2
        b = None
        limit = 20 + (50 - self.hp / 60)
        if gid > 10:
            limit += 30
        if abs(x0 - px) < limit:
            if self.hp > 1500:
                b = DownRocketType1((x0, y0))
            else:
                b = DownRocketType2((x0, y0))
        else:
            if self.hp > 2500:
                b = DownBulletType1((x0, y0))
            if self.hp > 2000:
                b = DownBulletType2((x0, y0))
            if self.hp > 1000:
                if gid < 2:
                    b = DownBulletType2((x0, y0))
                else:
                    b = DownBulletType1((x0, y0))
            elif self.hp > 500:
                if gid < 4:
                    b = DownBulletType2((x0, y0))
                else:
                    b = DownBulletType3((x0, y0))
            else:
                if gid < 2:
                    b = DownBulletType2((x0, y0))
                else:
                    b = DownBulletType3((x0, y0))

        self.bulletSpace.append(b)

        r = random.randint(1, 20)
        if (r == 1):
            for j in range(0, 10):
                bulletPath = CircleBulletPath(self.position, 40, 100+10*j)
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)
        if (r == 5):
            for j in range(0, 5):
                bulletPath = DiamondBulletPath(self.position, 40, 100+10*j)
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)
        if (r == 10):
            for j in range(0, 20):
                (x0,y0) = self.position
                (x,y) = self.space.player.position
                dx = x-x0
                dy = y-y0
                if dx > 0: direcx = 1
                else: direcx = -1
                if dy > 0: direcy = abs(dy/dx)
                else: direcy = -abs(dy/dx)
                direction = (direcx, direcy)
                print(direction)
                b = BulletInPath("yellow", self.position, 300 + 10*j, direction)
                self.bulletSpace.append(b)

        if (r == 15):
            for j in range(0,5):
                bulletPath = CircleBulletPath(self.position, random.randint(10,40), 100 + 10*j, "green")
                for i in range(0, bulletPath.number_of_bullet):
                    b = bulletPath.bulletList[i]
                    self.bulletSpace.append(b)

class Win(EnemyType1):
    def __init__(self, space, pos):
        super().__init__(space, pos)
        self.hp = 100
        self.img = garfield_load_image(PATH_WIN)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.flag = True

    def _active(self, delta_time):

        pass

    def _active_gun(self, delta_time):
        pass

    def draw(self, screen, position=(0, 0)):
        if self.space.player.hp==0 and self.flag:
            self.img = garfield_load_image(PATH_LOST)
            self.width = self.img.get_width()
            self.height = self.img.get_height()
        (x, y) = self.position
        (x0, y0) = position
        if self.dImg is not None:
            x -= x0 + self.dImg.width / 2
            y -= y0 + self.dImg.height / 2
            self.dImg.draw(screen, (x, y - 30))
            self.dImg.draw(screen, (x + 100, y))
            self.dImg.draw(screen, (x - 100, y))
            self.dImg.draw(screen, (x, y + 30))
        else:
            if self.hp > 0:
                x -= x0 + self.width / 2
                y -= y0 + self.height / 2
                screen.blit(self.img, (x, y))

    def damage(self, d):
        if self.hp >= 0 and self.hp - 1 <= 0:
            self.space.context.start_activity("menu")
        self.hp -= 1

    def check(self, pos):
        (x0, y0) = self.position
        (x, y) = pos
        x += -x0 + self.width / 2
        y += -y0 + self.height / 2
        c = garfield_pick_color(self.img, (x, y))
        if c is None:
            return False
        (r, g, b, a) = c
        return a > 20


class Lost(Win):
    def __init__(self, space, pos):
        super().__init__(space, pos)
        self.img = garfield_load_image(PATH_LOST)
        self.delta = 0
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def update(self, delta_time):
        super().update(delta_time)
        self.delta += delta_time
        (x, y) = self.position
        if y > self.space.screenY + 690 or self.delta > 28000:
            self.space.context.start_activity("menu")




########################################################################################################################
class Item(GDrawable, GUpdatable):
    def __init__(self, pos, animation):
        self.animation = animation
        self.position = pos
        self.activated = False
        pass

    def is_alive(self):
        return not self.activated

    def draw(self, screen, position=(0, 0)):
        (x, y) = self.position
        (x0, y0) = position
        x -= x0 + self.animation.width / 2
        y -= y0 + self.animation.height / 2
        self.animation.draw(screen, (x, y))

    def update(self, delta_time):
        self.animation.update(delta_time)

    def check(self, pos):
        return garfield_distance(pos, self.position) < 40

    def __action__(self, player):
        pass

    def action(self, player):
        if self.is_alive():
            self.__action__(player)
            self.activated = True


class HpItem(Item):
    def action(self, player):
        super().action(player)

    def __init__(self, pos, space):
        super().__init__(pos, Animation(PATH_ITEM[0], 3, 100))
        self.space = space
        self.dx = (random.randint(0, 999) % 2) * 1.5 - 1.5 / 2

    def __action__(self, player):
        player.damage(-50)

    def update(self, delta_time):
        super().update(delta_time)
        (x, y) = self.position
        if x < 30:
            self.dx = 1.5
        if x > 770:
            self.dx = -1.5
        x += self.dx
        dy = 8 - self.space.screenSpeed / 2
        y += dy * delta_time / 1000.0
        self.position = (x, y)


class Rocket1Item(Item):
    def action(self, player):
        super().action(player)

    def __init__(self, pos, space, stock):
        super().__init__(pos, Animation(PATH_ITEM[2], 5, 100))
        self.space = space
        self.dx = (random.randint(0, 999) % 2) * 1.5 - 1.5 / 2
        self.stock = stock

    def __action__(self, player):
        player.inc_rocket(self.stock, 0)

    def update(self, delta_time):
        super().update(delta_time)

        (x, y) = self.position
        if x < 30:
            self.dx = 1.5
        if x > 770:
            self.dx = -1.5
        x += self.dx
        dy = 11 - self.space.screenSpeed / 3
        y += dy * delta_time / 1000.0
        self.position = (x, y)


class Rocket2Item(Item):
    def action(self, player):
        super().action(player)

    def __init__(self, pos, space, stock):
        super().__init__(pos, Animation(PATH_ITEM[3], 5, 100))
        self.space = space
        self.dx = (random.randint(0, 999) % 2) * 1.5 - 1.5 / 2
        self.stock = stock

    def __action__(self, player):
        player.inc_rocket(self.stock, 1)

    def update(self, delta_time):
        super().update(delta_time)

        (x, y) = self.position
        if x < 30:
            self.dx = 1.5
        if x > 770:
            self.dx = -1.5
        x += self.dx
        dy = 11 - self.space.screenSpeed / 3
        y += dy * delta_time / 1000.0
        self.position = (x, y)


class PowerItem(Item):
    def action(self, player):
        super().action(player)

    def __init__(self, pos, space):
        super().__init__(pos, Animation(PATH_ITEM[4], 3, 100))
        self.space = space
        self.dx = (random.randint(0, 999) % 2) * 1.5 - 1.5 / 2

    def __action__(self, player):
        player.inc_power(1)

    def update(self, delta_time):
        super().update(delta_time)
        (x, y) = self.position
        if x < 30:
            self.dx = 1.5
        if x > 770:
            self.dx = -1.5
        x += self.dx
        dy = 11 - self.space.screenSpeed / 3
        y += dy * delta_time / 1000.0
        self.position = (x, y)


class CoinItem(Item):
    def action(self, player):
        super().action(player)

    def __init__(self, pos, space, coin):
        super().__init__(pos, Animation(PATH_ITEM[1], 3, 100))
        self.space = space
        self.dx = (random.randint(0, 999) % 2) * 1.5 - 1.5 / 2
        self.coin = coin

    def __action__(self, player):
        player.inc_coin(self.coin)

    def update(self, delta_time):
        super().update(delta_time)
        (x, y) = self.position
        if x < 30:
            self.dx = 1.5
        if x > 770:
            self.dx = -1.5
        x += self.dx
        dy = 11 - self.space.screenSpeed / 3
        y += dy * delta_time / 1000.0
        self.position = (x, y)


########################################################################################################################

class ScreenItem(GDrawable, GUpdatable):
    def __init__(self, item_id):
        self.item_id = item_id
        self.screenY = -item_id * 690
        self.background = garfield_load_image(PATH_SPACE + str(item_id) + ".png")

    def get_enemy(self, space, res):
        if space.player.hp <= 0:
            res.append(Lost(space, (400, self.screenY + 200)))
            space.speedY = -26
            return
        if self.isLast():
            if space.player.hp>0:
                res.append(Win(space, (400, self.screenY + 200)))
            else:
                res.append(Lost(space, (400, self.screenY + 200)))
            return
        res.append(EnemyType1(space, (400, self.screenY + 200)))
        if self.item_id > 0:
            res.append(EnemyType2(space, (random.randint(60, 630), self.screenY + 600)))
        res.append(EnemyType1(space, (590, self.screenY + 160)))
        if self.item_id > 4:
            if random.randint(0, 3) == 1:
                res.append(EnemyType2(space, (500, self.screenY + 600)))
            else:
                res.append(EnemyType2(space, (190, self.screenY + 600)))
        if self.item_id > 5:
            res.append(EnemyType3(space, (random.randint(30, 600), self.screenY + 600)))
        if self.item_id > 8:
            if random.randint(0, 3) == 1:
                res.append(EnemyType2(space, (random.randint(0, 500), self.screenY + random.randint(0, 600))))
            else:
                res.append(EnemyType2(space, (random.randint(0, 190), self.screenY + random.randint(0, 600))))
        if self.item_id > 10:
            res.append(EnemyType3(space, (random.randint(30, 600), self.screenY + random.randint(0, 600))))
        if self.isBoss():
            if self.item_id == 13:
                res.append(EnemyBoss(space, (300, self.screenY + 170)))
            else:
                res.append(EnemyBossChild(space, (300, self.screenY + 170)))


    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        y = self.screenY - y0
        screen.blit(self.background, (x0, y))

    def update(self, delta_time):
        pass

    def isLast(self):
        return self.item_id == 14

    def isBoss(self):
        return self.item_id == 13 or self.item_id == 6

    def getSpeed(self):
        if self.item_id == 13:
            return 0
        return -60

