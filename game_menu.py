from  component import FlyButton
from constant import *
from garfield import GActivity, garfield_load_image


class MenuGame(GActivity):
    def draw(self, screen, position=(0, 0)):
        screen.blit(self.background, position)
        for b in self.menuButton:
            b.draw(screen, position)

    def on_mouse_pressed(self, button, position):
        for b in self.menuButton:
            if b.on_mouse_pressed(button, position):
                return True
        return super().on_mouse_pressed(button, position)

    def on_mouse_released(self, button, position):
        for b in self.menuButton:
            if b.on_mouse_released(button, position):
                return True
        return super().on_mouse_released(button, position)

    def __init__(self, context):
        super().__init__(context)
        self.background = garfield_load_image(PATH_BACKGROUND)
        self.menuButton = [PlayNewgame(context), PlayHelp(context), PlayExit(context)]

    def on_key_released(self, key):
        return super().on_key_released(key)

    def update(self, delta_time):
        for b in self.menuButton:
            b.update(delta_time)

    def on_key_pressed(self, key):
        return super().on_key_pressed(key)

    def on_mouse_move(self, position, rel, buttons):
        for b in self.menuButton:
            b.on_mouse_move(position, rel, buttons)

        super().on_mouse_move(position, rel, buttons)


class PlayNewgame(FlyButton):
    def __init__(self, context):
        super().__init__(context, (context.width + 20, 265), (context.width / 2 + 100, 265),
                         PATH_BUTTONS[0][0], PATH_BUTTONS[0][1])

    def on_click(self):
        self.context.start_activity("play")


class PlayHelp(FlyButton):
    def __init__(self, context):
        super().__init__(context, (context.width + 20, 360), (context.width / 2 + 100, 360),
                         PATH_BUTTONS[1][0], PATH_BUTTONS[1][1])

    def on_click(self):
        self.context.start_activity("help")


class PlayExit(FlyButton):
    def __init__(self, context):
        super().__init__(context, (context.width + 20, 455), (context.width / 2 + 100, 455),
                         PATH_BUTTONS[2][0], PATH_BUTTONS[2][1])

    def on_click(self):
        self.context.start_activity("exit")
