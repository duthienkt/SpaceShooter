import pygame

from  component import FlyButton
from component import NormalCursor
from garfield import Garfield, garfield_music_is_busy, garfield_add_music, GActivity, Animation


class MenuGame(GActivity):
    def draw(self, screen, position=(0, 0)):
        self.logo.draw(screen, position)
        self.eff.draw(screen, (200, 200))

    def on_mouse_pressed(self, button, position):
        return super().on_mouse_pressed(button, position)

    def on_mouse_released(self, button, position):
        return super().on_mouse_released(button, position)

    def __init__(self, context):
        super().__init__(context)
        self.logo = FlyButton(context, (20, 130), (20, 400), "assets/defeat1.png", "assets/defeat2.png")
        # self.eff = Animation("assets/eff/xeo.png", 28, 100)
        self.eff = Animation("assets/eff/coin.png", 3, 100)

    def on_key_released(self, key):
        return super().on_key_released(key)

    def update(self, delta_time):
        self.logo.update(delta_time)
        self.eff.update(delta_time)

    def on_key_pressed(self, key):
        return super().on_key_pressed(key)

    def on_mouse_move(self, position, rel, buttons):
        super().on_mouse_move(position, rel, buttons)
        self.logo.on_mouse_move(position, rel, buttons)


class Main(Garfield):
    def __init__(self):
        super().__init__()
        self.cursor = NormalCursor("assets/cursor/cursor.png", 5)

        self.powerOff = None
        self.activity = None

    def setup(self):
        self.frame_rate(45)
        self.activity = MenuGame(self)
        self.trigger_music()
        pygame.mouse.set_visible(False)
        pass

    def on_mouse_move(self, position, rel, buttons):
        self.cursor.on_mouse_move(position, rel, buttons)
        self.activity.on_mouse_move(position, rel, buttons)
        pass

    def on_mouse_pressed(self, button, position):
        self.trigger_music()
        self.cursor.on_mouse_pressed(button, position)
        self.activity.on_mouse_pressed(button, position)
        pass

    def on_key_pressed(self, key):
        self.trigger_music()
        self.activity.on_key_pressed(key)

    def on_key_released(self, key):
        self.activity.on_key_released(key)

    def setting(self):
        self.size((1000, 690))
        pass

    def update(self, delta_time):
        self.activity.update(delta_time)

    def on_mouse_released(self, button, position):
        self.activity.on_mouse_released(button, position)
        self.cursor.on_mouse_released(button, position)
        # print("mouse_release()")

    def draw(self, screen=None, position=(0, 0)):
        screen.fill((40, 90, 180))
        self.activity.draw(screen, position)
        self.cursor.draw(self.screen)
        # print("draw()")
        pass

    def set_cursor(self, cursor):
        self.cursor = cursor

    def start_activity(self, activity_command):
        if activity_command == "exit":
            self.exit()

    def trigger_music(self):
        if not garfield_music_is_busy():
            garfield_add_music("assets/soundtrack/track2.ogg")


Main().__main__()
