from constant import *
from game_tool import MenuTool
from garfield import GActivity, garfield_distance
from physical import Player, ScreenItem


class MainGame(GActivity):
    def __init__(self, context):
        super().__init__(context)
        self.playerBullets = []
        self.enemyBullets = []
        self.screenY = 0
        self.screenSpeed = -60
        self.screenItem = [ScreenItem(0), ScreenItem(1)]
        self.menuTool = MenuTool(context)
        self.player = Player(self, (300, 600), self.menuTool)
        self.enemy = []
        self.items = []
        self.screenItem[0].get_enemy(self, self.enemy)
        self.screenItem[1].get_enemy(self, self.enemy)

    def update(self, delta_time):
        self.__update_screen(delta_time)
        e = self.player
        for b in self.enemyBullets:
            if e.hp > 0:
                if b.alive:
                    if e.check(b.position):
                        b.explosive()
                        e.damage(b.get_damage(0))

        self.__update_player(delta_time)
        self.__update_enemy(delta_time)
        self.__update_player_bullet(delta_time)
        self.__update_enemy_bullet(delta_time)
        self.__update_items(delta_time)
        self.menuTool.update(delta_time)


    def __update_player(self, delta_time):

        for b in self.enemy:
            if b.hp > 0:
                if b.check(self.player.position) or self.player.check(b.position):
                    self.player.damage(b.hp)
                    b.damage(self.player.hp)
                    print(self.player.hp)
        self.player.update(delta_time)
        pass

    def __update_items(self, delta_time):
        l = len(self.items)
        for k in range(l):
            i = l - 1 - k
            (x, y) = self.items[i].position
            if y > self.screenY + 750 or not self.items[i].is_alive():
                self.items.remove(self.items[i])
        l = len(self.items)

        for k in range(l):
            item = self.items[k]
            item.update(delta_time)
            if self.player.hp > 0:
                if item.check(self.player.position) or self.player.check(item.position):
                    item.action(self.player)

    def __draw_items(self, screen, position=(0, 0)):
        l = len(self.items)
        for k in range(l):
            self.items[k].draw(screen, position)

    def __update_screen(self, delta_time):
        self.screenY += self.screenSpeed * delta_time / 1000.0

        if self.screenItem[0].screenY >= self.screenY + 690:
            if self.screenItem[1].isLast():
                self.screenSpeed = 0
                return
            print("Load New Item")
            print(self.screenItem[0].item_id + 1)
            self.screenItem[0] = self.screenItem[1]
            self.screenSpeed = self.screenItem[0].getSpeed()
            self.screenItem[1] = ScreenItem(self.screenItem[0].item_id + 1)
            self.screenItem[1].get_enemy(self, self.enemy)
            if self.screenItem[1].isLast() or self.screenItem[0].isBoss():
                self.screenSpeed = 0
        pass

    def __draw_screen(self, screen, position=(0, 0)):
        self.screenItem[0].draw(screen, position)
        self.screenItem[1].draw(screen, position)

    def __update_player_bullet(self, delta_time):
        l = len(self.playerBullets)
        for k in range(l):
            i = l - 1 - k
            (x, y) = self.playerBullets[i].position
            if y < self.screenY - 100 or not self.playerBullets[i].is_alive():
                self.playerBullets.remove(self.playerBullets[i])
        l = len(self.playerBullets)
        for k in range(l):
            self.playerBullets[k].update(delta_time)

    def __draw_player_bullet(self, screen, position=(0, 0)):
        l = len(self.playerBullets)
        for k in range(l):
            self.playerBullets[k].draw(screen, position)

    def __update_enemy_bullet(self, delta_time):
        l = len(self.enemyBullets)
        for k in range(l):
            i = l - 1 - k
            (x, y) = self.enemyBullets[i].position
            if y > self.screenY + 750 or not self.enemyBullets[i].is_alive():
                self.enemyBullets.remove(self.enemyBullets[i])
        l = len(self.enemyBullets)

        for k in range(l):
            self.enemyBullets[k].update(delta_time)

    def __draw_enemy_bullet(self, screen, position=(0, 0)):
        l = len(self.enemyBullets)
        for k in range(l):
            self.enemyBullets[k].draw(screen, position)

    def __update_enemy(self, delta_time):
        l = len(self.enemy)
        for k in range(l):
            i = l - 1 - k
            (x, y) = self.enemy[i].position
            if y > self.screenY + 690 + self.enemy[i].height or not self.enemy[i].is_alive():
                self.enemy.remove(self.enemy[i])
            elif y > self.screenY - self.enemy[i].height / 2:
                e = self.enemy[i]
                e.update(delta_time)
                for b in self.playerBullets:
                    if e.hp > 0:
                        if e.check(b.position):
                            if b.alive:
                                b.explosive()
                                e.damage(b.get_damage(0))
                                if b.get_damage(1) > 0:
                                    for eo in self.enemy:
                                        if eo != e:
                                            eo.damage(b.get_damage(garfield_distance(eo.position, b.position)))

    def __draw_enemy(self, screen, position=(0, 0)):
        l = len(self.enemy)
        for k in range(l):
            self.enemy[k].draw(screen, position)

    def draw(self, screen, position=(0, 0)):
        screen.fill(COLOR_BACKGROUND)
        (x, y) = position
        camera = (x, self.screenY)
        self.__draw_screen(screen, camera)
        self.__draw_items(screen, camera)
        self.player.draw(screen, camera)
        self.__draw_enemy(screen, camera)
        self.__draw_player_bullet(screen, camera)
        self.__draw_enemy_bullet(screen, camera)
        self.menuTool.draw(screen)

    def on_mouse_released(self, button, position):
        if self.menuTool.on_mouse_released(button, position):
            return True
        return super().on_mouse_released(button, position)

    def on_mouse_pressed(self, button, position):
        # self.player.f = DownRocketType2(position)
        if self.menuTool.on_mouse_pressed(button, position):
            return True
        pass

    def on_mouse_move(self, position, rel, buttons):
        self.menuTool.on_mouse_move(position, rel, buttons)
        super().on_mouse_move(position, rel, buttons)

    def on_key_pressed(self, key):
        print(key)
        if key == 27:
            self.context.start_activity("menu")
        # Hack this game
        if key >= 282 and key <= 285:
            self.player.change_level(key - 282)
        if self.player.on_key_pressed(key):
            return True

        return super().on_key_pressed(key)

    def on_key_released(self, key):
        # print(key)
        if self.player.on_key_released(key):
            return True
        return super().on_key_released(key)
