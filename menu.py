import arcade
from arcade.gui import UIManager, UIFlatButton
from setup import settings
from texture import load_background_texture
from cycle import gameCycle
from overlay import fade


class MyView(arcade.View):
    def __init__(self):
        super().__init__()

        self.backgroundArray = load_background_texture()
        self.bgName = "Room701"

        self.btn_style = settings["style"]["btn"]
        self.manager = UIManager()
        self.gap = 200
        self.loading = False

        self.backgroundObj = arcade.Sprite()
        self.backgroundObj.texture = self.backgroundArray[self.bgName]
        self.backgroundObj.center_x = settings["window"]["width"] // 2
        self.backgroundObj.center_y = settings["window"]["height"] // 2
        self.backgroundObj.height = settings["window"]["height"]
        self.backgroundObj.width = settings["window"]["width"] - 150
        self.backgroundSpriteList = arcade.SpriteList()
        self.backgroundSpriteList.append(self.backgroundObj)

    def loadingComplete(self):
        def switch_view(delta_time):
            self.loading = False
            self.window.show_view(gameCycle())

        arcade.schedule_once(switch_view, 0)

    def on_show_view(self):
        self.manager.enable()

        startBtn = UIFlatButton(
            text="START GAME",
            width=400,
            height=50,
            style=self.btn_style,
            anchor_x="right",
        )
        startBtn.style.update(self.btn_style["normal"])
        startBtn.style.update(self.btn_style["hover"])

        startBtn.center_x = settings["window"]["width"] - self.gap
        startBtn.center_y = settings["window"]["height"] - 100
        self.manager.add(startBtn)

        exit = UIFlatButton(
            text="Exit", width=400, height=50, style=self.btn_style, anchor_x="right"
        )

        exit.center_x = settings["window"]["width"] - self.gap + 60
        exit.center_y = settings["window"]["height"] - 150
        self.manager.add(exit)

        @startBtn.event("on_click")
        def on_click(event):
            if self.loading:
                return

            self.loading = True

            fade.start(callback=self.loadingComplete, alpha=0, reverse=False)

        @exit.event("on_click")
        def on_exit(event):
            if self.loading:
                return
            arcade.close_window()

    def on_draw(self):
        self.clear()
        self.backgroundSpriteList.draw()
        self.manager.draw()
        if self.loading:
            fade.draw(self.window)

    def on_update(self, delta_time):
        if self.loading:
            fade.update(delta_time)


window = arcade.Window(
    settings["window"]["width"], settings["window"]["height"], settings["title"]
)
window.set_update_rate(1 / settings["window"]["fps"])

MyView = MyView()
window.show_view(MyView)

arcade.run()
