import arcade
from arcade.gui import UIManager, UIFlatButton
from setup import settings
from texture import load_background_texture
from cycle import gameCycle


class MyView(arcade.View):
    def __init__(self):
        super().__init__()

        self.backgroundArray = load_background_texture()
        self.bgName = "Room701"

        self.btn_style = settings["style"]["btn"]
        self.manager = UIManager()
        self.gap = 200

        self.backgroundObj = arcade.Sprite()
        self.backgroundObj.texture = self.backgroundArray[self.bgName]
        self.backgroundObj.center_x = settings["window"]["width"] // 2
        self.backgroundObj.center_y = settings["window"]["height"] // 2
        self.backgroundObj.height = settings["window"]["height"]
        self.backgroundObj.width = settings["window"]["width"] - 150
        self.backgroundSpriteList = arcade.SpriteList()
        self.backgroundSpriteList.append(self.backgroundObj)

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
            gameCycle(self.window)

        @exit.event("on_click")
        def on_exit(event):
            arcade.close_window()

    def on_draw(self):
        self.clear()
        self.backgroundSpriteList.draw()
        self.manager.draw()


window = arcade.Window(
    settings["window"]["width"], settings["window"]["height"], settings["title"]
)
window.set_update_rate(1 / settings["window"]["fps"])

MyView = MyView()
window.show_view(MyView)

arcade.run()