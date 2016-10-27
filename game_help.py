import pygame
from garfield import Garfield, GActivity ,garfield_load_image
from constant import *
from component import FlyButton

class HelpGame(GActivity):

    def draw(self, screen, position=(0, 0)):
        screen.blit(self.background, position)
        self.backbt.draw(screen,position)

    def on_mouse_pressed(self, button, position):
        if self.backbt.on_mouse_pressed(button, position):
                return True
        return super().on_mouse_pressed(button, position)

    def on_mouse_released(self, button, position):
        if self.backbt.on_mouse_released(button, position):
                return True
        return super().on_mouse_released(button, position)

    def __init__(self, context):
        super().__init__(context)
        self.background = garfield_load_image(HELP_BACKGROUND)
        self.backbt = Back(context)

    def on_key_released(self, key):
        return super().on_key_released(key)

    def update(self, delta_time):
        self.backbt.update(delta_time)

    def on_key_pressed(self, key):
        return super().on_key_pressed(key)

    def on_mouse_move(self, position, rel, buttons):
        self.backbt.on_mouse_move(position, rel, buttons)
        super().on_mouse_move(position, rel, buttons)

class Back(FlyButton):
    def __init__(self, context):
        super().__init__(context, (20, 20), (20,20),
                         BACK_IMAGE[0],BACK_IMAGE[1])
    def on_click(self):
        self.context.start_activity("menu")
