import math

from garfield import *


class NormalCursor(Animation, MouseInteractive):
    def __init__(self, image_path, frame_count, interval_time=300):
        super().__init__(image_path, frame_count, interval_time)
        self.position = (0, 0)

    def on_mouse_move(self, position, rel, buttons):
        self.position = position

    def draw(self, screen, position=(0, 0)):
        super().draw(screen, self.position)

    def on_mouse_released(self, button, position):
        return False

    def on_mouse_pressed(self, button, position):
        return False


class Button(GActivity):
    def __init__(self, context, position, path1, path2):
        super().__init__(context)
        self.mouseOutsideImage = garfield_load_image(path1)
        self.mouseInsideImage = garfield_load_image(path2)
        self.currentImage = self.mouseOutsideImage
        self.position = position

    def draw(self, screen, position=(0, 0)):
        (x0, y0) = position
        (x, y) = self.position
        screen.blit(self.currentImage, (x0+x, y0+y))

    def on_mouse_pressed(self, button, position):
        (x, y) = position
        (x0, y0) = self.position
        c = garfield_pick_color(self.currentImage, (x - x0, y - y0))
        if c is not None:
            (r, g, b, a) = c
            if a > 50:
                self.currentImage = self.mouseInsideImage
                return True
        return False

    def on_mouse_released(self, button, position):
        if not self.currentImage == self.mouseInsideImage:
            return
        self.currentImage = self.mouseOutsideImage
        (x, y) = position
        (x0, y0) = self.position
        c = garfield_pick_color(self.currentImage, (x - x0, y - y0))
        if c is not None:
            (r, g, b, a) = c
            if a > 50:
                return True
        return False

    def on_mouse_move(self, position, rel, buttons):
        (x, y) = position
        (x0, y0) = self.position
        c = garfield_pick_color(self.currentImage, (x - x0, y - y0))
        if c is not None:
            (r, g, b, a) = c
            if a > 50:
                self.currentImage = self.mouseInsideImage
                return
        self.currentImage = self.mouseOutsideImage

    def on_key_released(self, key):
        return super().on_key_released(key)

    def update(self, delta_time):
        super().update(delta_time)

    def on_key_pressed(self, key):
        return super().on_key_pressed(key)


class ClickAbleButton(Button):
    def __init__(self, context, position, path1, path2):
        super().__init__(context, position, path1, path2)
        self.pressed = False

    def on_mouse_pressed(self, button, position):
        if super().on_mouse_pressed(button, position):
            self.pressed = True
            return True
        return False

    def on_mouse_released(self, button, position):
        if super().on_mouse_released(button, position):
            if self.pressed:
                self.on_click()
            return True
        return False

    def on_click(self):
        pass


class FlyButton(ClickAbleButton):
    def __init__(self, context, position0, position1, path1, path2):
        super().__init__(context, position0, path1, path2)
        self.position0 = position0
        self.position1 = position1
        self.clicked = False

    def update(self, delta_time):
        (vx0, vy0) = self.position
        (vx1, vy1) = self.position1
        dx = vx1 - vx0
        dy = vy1 - vy0
        l = math.sqrt(dx * dx + dy * dy)

        if self.clicked and l < 1:
            self.clicked = False
            self.on_click()
        elif l >= 1:

            dx /= l
            dy /= l
            l = delta_time / 20.0 * math.log(1 + l / 5.0)
            dx *= l
            dy *= l
            self.position = (vx0 + dx, vy0 + dy)
