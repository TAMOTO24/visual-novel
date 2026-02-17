import arcade
import json
from characters import characterArray
from setup import settings


def readDialogue():
    try:
        with open("dialogue.json", "r") as f:
            data = json.load(f)
            return data["dialogue"]
    except FileNotFoundError:
        print(f"Error reading dialogue file: File not found")
        return []


def characterScrypt(array, name):
    if name == "Legoshi":
        return array

    if name not in characterArray:
        return array

    return array + [characterArray[name]]


def position_characters(characters):
    center = settings["window"]["width"] // 2

    if len(characters) == 1:
        characters[0].sprite.center_x = center

    elif len(characters) == 2:
        characters[0].sprite.center_x = center - 300
        characters[1].sprite.center_x = center + 300


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.dialogue_c = 0  # dialogue counter
        self.dialogue_txt = readDialogue()
        self.main_character = characterArray["Legoshi"]
        self.main_character.sprite.center_x = (
            settings["window"]["width"] - self.main_character.Width // 2
        )  # position the main character on the right side of the screen
        self.main_character.sprite.center_y = (
            settings["window"]["height"] - self.main_character.Height
        )  # position the main character at the bottom of the screen
        self.character_list = arcade.SpriteList()

        self.characters = characterScrypt([], self.dialogue_txt[0]["name"])
        self.text_obj = arcade.Text(
            self.dialogue_txt[0]["message"],
            100,
            200,
            arcade.color.WHITE,
            20,
            multiline=True,
            width=300,
        )

    def on_draw(self):
        self.clear()

        for ch in self.characters:
            self.character_list.append(ch.sprite)

        self.character_list.draw()
        self.text_obj.draw()
        self.character_list.clear()

        if self.dialogue_txt[self.dialogue_c]["name"] == "Legoshi":
            main_ch = arcade.SpriteList()
            main_ch.append(self.main_character.sprite)
            main_ch.draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.dialogue_c += 1
            self.text_obj.text = self.dialogue_txt[self.dialogue_c]["message"]

            chName = self.dialogue_txt[self.dialogue_c]["name"]
            if self.dialogue_txt[self.dialogue_c].get("both") or chName == "Legoshi":
                # if we get BOTH command then we need to add another character inside
                self.characters = characterScrypt(self.characters, chName)
            else:
                self.characters = characterScrypt([], chName)
            position_characters(self.characters)

    # def on_update(self, delta_time):
    #     if not self.dialogue_txt[self.dialogue_c].get("both"):
    #         self.characters = []


def main():
    window = arcade.Window(
        settings["window"]["width"], settings["window"]["height"], settings["title"]
    )
    window.set_update_rate(1 / settings["window"]["fps"])

    game = GameView()
    window.show_view(game)

    arcade.run()


if __name__ == "__main__":
    main()
