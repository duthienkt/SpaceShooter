from pygame import *

from component import FlyButton
from physical import *


class MenuTool(GActivity):
    def draw(self, screen, position=(0, 0)):
        screen.blit(self.bgTool, (800, 0))
        screen.blit(self.shipImage[self.level], (820, 265))
        screen.blit(self.power, (841, 370))
        screen.blit(self.coin, (841, 416))
        screen.blit(self.rocket1, (835, 460))
        screen.blit(self.rocket2, (835, 520))
        screen.blit(self.level_text, (910, 160))
        screen.blit(self.rocket_type1_num_text, (900, 460))
        screen.blit(self.rocket_type2_num_text, (900, 520))
        screen.blit(self.power_num_text, (900, 365))
        screen.blit(self.coin_num_text, (900, 410))
        screen.blit(self.hpBar2, (20, 20))
        pygame.draw.rect(screen, COLOR_GREEN, (38, 26, 240 * self.hp_view / 100, 32), 0)
        screen.blit(self.hpBar, (20, 20))
        if self.visit_boos:
            screen.blit(self.hpBar2_boss, (400, 20))
            pygame.draw.rect(screen, COLOR_RED,
                             (730 - 240 * self.hp_boss_view / 100, 26, 240 * self.hp_boss_view / 100, 32), 0)
            screen.blit(self.hpBar_boss, (400, 20))

        for b in self.menuTool:
            b.draw(screen, position)

    def on_mouse_pressed(self, button, position):
        for b in self.menuTool:
            if b.on_mouse_pressed(button, position):
                return True
        return super().on_mouse_pressed(button, position)

    def on_mouse_released(self, button, position):
        for b in self.menuTool:
            if b.on_mouse_released(button, position):
                return True
        return super().on_mouse_released(button, position)

    def __init__(self, context):
        super().__init__(context)
        self.bgTool = garfield_load_image(PATH_BGTOOL)
        self.power = garfield_load_image(PATH_STATUS[0])
        self.coin = garfield_load_image(PATH_STATUS[1])
        self.rocket1 = garfield_load_image(PATH_STATUS[2])
        self.rocket2 = garfield_load_image(PATH_STATUS[3])

        self.menuTool = [Exit(context)]
        self.shipImage = [garfield_load_image(PATH_SHIP_LV[0]),
                          garfield_load_image(PATH_SHIP_LV[1]),
                          garfield_load_image(PATH_SHIP_LV[2]),
                          garfield_load_image(PATH_SHIP_LV[3])]

        self.ship = self.shipImage[0]
        self.hpBar = garfield_load_image(PATH_HPBAR[0])
        self.hpBar2 = garfield_load_image(PATH_HPBAR[1])
        self.level = 0
        self.hp = PLAYER_HP[self.level]
        self.hp_view = 0
        self.rocket_type1_num = 0
        self.rocket_type2_num = 0
        self.coin_num = 0
        self.power_num = 0

        self.font44 = garfield_font(PATH_FONT, 44)
        self.font35 = garfield_font(PATH_FONT, 35)
        self.level_text = self.font44.render(str(self.level + 1), True, COLOR_RED)
        self.coin_num_text = self.font35.render(str(self.coin_num), True, COLOR_BLUE)
        self.power_num_text = self.font35.render(str(self.power_num), True, COLOR_BLUE)
        self.rocket_type1_num_text = self.font35.render(str(self.rocket_type1_num), True, COLOR_BLUE)
        self.rocket_type2_num_text = self.font35.render(str(self.rocket_type2_num), True, COLOR_BLUE)

        self.hpBar_boss = garfield_load_image(PATH_HPBAR[2])
        self.hpBar2_boss = garfield_load_image(PATH_HPBAR[3])
        self.hp_boss = 0
        self.hp_boss_view = 0
        self.visit_boos = False

    def on_key_released(self, key):
        return super().on_key_released(key)

    def update(self, delta_time):
        if abs(self.hp - self.hp_view) < delta_time / 20:
            self.hp_view = self.hp
        elif self.hp_view > self.hp:
            self.hp_view -= delta_time / 20
        elif self.hp_view < self.hp:
            self.hp_view += delta_time / 20

        if abs(self.hp_boss - self.hp_boss_view) < delta_time / 20:
            self.hp_boss_view = self.hp_boss
        elif self.hp_boss_view > self.hp_boss:
            self.hp_boss_view -= delta_time / 20
        elif self.hp_boss_view < self.hp_boss:
            self.hp_boss_view += delta_time / 20

        for b in self.menuTool:
            b.update(delta_time)

    def on_key_pressed(self, key):
        return super().on_key_pressed(key)

    def on_mouse_move(self, position, rel, buttons):
        for b in self.menuTool:
            b.on_mouse_move(position, rel, buttons)

        super().on_mouse_move(position, rel, buttons)

    def set_level(self, lv):
        if (self.level != lv):
            self.level = lv
            self.level_text = self.font44.render(str(self.level + 1), True, COLOR_RED)

    def set_hp(self, hpp):
        if hpp > 100:
            self.hp = 100
        elif hpp < 0:
            self.hp = 0
        else:
            self.hp = hpp

    def set_boss_visit(self, vi=True):
        self.visit_boos = vi
        if not vi:
            self.hp_boss_view = 0

    def set_hp_boss(self, hpp):
        if hpp > 100:
            self.hp_boss = 100
        elif hpp < 0:
            self.hp_boss = 0
        else:
            self.hp_boss = hpp

    def set_rocket_type1(self, rocket_type1):
        if (self.rocket_type1_num != rocket_type1):
            self.rocket_type1_num = rocket_type1
            self.rocket_type1_num_text = self.font35.render(str(self.rocket_type1_num), True, COLOR_BLUE)

    def set_rocket_type2(self, rocket_type2):
        if (self.rocket_type2_num != rocket_type2):
            self.rocket_type2_num = rocket_type2
            self.rocket_type2_num_text = self.font35.render(str(self.rocket_type2_num), True, COLOR_BLUE)

    def set_power(self, power):
        if (self.power_num != power):
            self.power_num = power
            self.power_num_text = self.font35.render(str(self.power_num), True, COLOR_BLUE)

    def set_coin(self, coin):
        if (self.coin_num != coin):
            self.coin_num = coin
            self.coin_num_text = self.font35.render(str(self.coin_num), True, COLOR_BLUE)


class Exit(FlyButton):
    def __init__(self, context):
        super().__init__(context, (900, 590), (900, 590),
                         PATH_TOOL_BUTTON[0][0], PATH_TOOL_BUTTON[0][1])

    def on_click(self):
        self.context.start_activity("exit")
