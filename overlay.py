import arcade


class FadeManager:
    def __init__(self):
        self.alpha = 0
        self.speed = 200
        self.active = False
        self.reverse = False
        self.callback = None      

    def start(self, callback, alpha=155, reverse=False):
        self.alpha = alpha
        self.active = True
        self.reverse = reverse
        self.callback = callback

    def update(self, delta_time):
        if not self.active:
            print("Fade is not active, skipping update")
            return
        if self.reverse:
            self.alpha -= self.speed * delta_time
        else:
            self.alpha += self.speed * delta_time
        if self.reverse and self.alpha <= 0:
            self.alpha = 0
            print("Fade completed (reverse)")
            self.active = False
        else:
            if self.alpha >= 255:
                self.alpha = 255
                self.active = False
                print("Fade completed")
                self.callback()
                print("Callback executed")

    def draw(self, window):
        # if not self.active:
        #     return
        arcade.draw_lbwh_rectangle_filled(
            0, 0, window.width, window.height, (0, 0, 0, int(self.alpha))
        )

fade = FadeManager()
