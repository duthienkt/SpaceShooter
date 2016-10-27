import random

import pygame

from component import NormalCursor
from  constant import *
from game_help import HelpGame
from game_menu import MenuGame
from garfield import Garfield, garfield_music_is_busy, garfield_add_music, garfield_load_image
from main_game import MainGame


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

    def __lazy_load_init(self):
        for i in range(15):
            garfield_load_image(PATH_SPACE + str(i) + ".png")

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
        self.cursor.update(delta_time)
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
        if activity_command == "play":
            self.activity = MainGame(self)
        if activity_command == "menu":
            self.activity = MenuGame(self)
        if activity_command == "help":
            self.activity = HelpGame(self)
        if activity_command == "exit":
            self.exit()

    def trigger_music(self):
        if not garfield_music_is_busy():
            garfield_add_music(PATH_MUSICS[random.randint(0, len(PATH_MUSICS)-1)])


Main().__main__()
