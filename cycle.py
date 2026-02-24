import arcade
import json
from characters import characterArray
from setup import settings
from texture import load_background_texture, load_dialogue_texture


def readDialogue():
    try:
        with open("dialogue.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error reading dialogue file: File not found")
        return []


def characterScrypt(array, name, exp="", mainCharacter=""):
    if name == mainCharacter:
        return array

    characterArray[name].change_emotion(exp or "usual")
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
        self.dialogueContent = readDialogue()

        self.MCName = "Legoshi"
        self.chapter_id = self.dialogueContent["_id"]

        self.dialogue_txt = self.dialogueContent["nodes"][self.dialogueContent["start"]]
        self.backgroundArray = load_background_texture()
        self.bgName = self.dialogueContent["background"]

        self.DEFAULTDIALOGUEWIDTH = 130

        self.main_character = characterArray[self.MCName]
        self.main_character.sprite.center_x = (
            settings["window"]["width"] - self.main_character.Width // 2
        )  # position the main character on the right side of the screen
        self.main_character.sprite.center_y = (
            settings["window"]["height"] - self.main_character.Height
        )  # position the main character at the bottom of the screen
        self.character_list = arcade.SpriteList()

        self.characters = characterScrypt([], self.dialogue_txt["name"])
        self.text_obj = arcade.Text(
            self.dialogue_txt["message"],
            100,
            200,
            arcade.color.WHITE,
            30,
            multiline=True,
            width=settings["window"]["width"]
            - self.main_character.Width
            - self.DEFAULTDIALOGUEWIDTH,
        )
        # background setting
        self.backgroundObj = arcade.Sprite()
        self.backgroundObj.texture = self.backgroundArray[self.bgName]
        self.backgroundObj.center_x = settings["window"]["width"] // 2
        self.backgroundObj.center_y = settings["window"]["height"] // 2
        self.backgroundObj.height = settings["window"]["height"]
        self.backgroundObj.width = settings["window"]["width"]
        self.backgroundSpriteList = arcade.SpriteList()
        self.backgroundSpriteList.append(self.backgroundObj)

        # Dialogue box setting
        self.dialogueBox = arcade.Sprite()
        self.dialogueBox.texture = load_dialogue_texture()["dialogue"]
        self.dialogueBox.center_x = settings["window"]["width"] // 2
        self.dialogueBox.center_y = 160
        self.dialogueBox.width = settings["window"]["width"]
        self.dialogueBox.height = 300
        self.dialogueBoxList = arcade.SpriteList()
        self.dialogueBoxList.append(self.dialogueBox)

    def on_draw(self):
        self.clear()
        self.backgroundSpriteList.draw()

        self.character_list.draw()
        self.character_list.clear()
        self.dialogueBoxList.draw()

        if self.dialogue_txt["name"] == self.MCName:
            main_ch = arcade.SpriteList()
            main_ch.append(self.main_character.sprite)
            self.text_obj.width = (
                settings["window"]["width"] - 330
            )  # 330 is main characters width
            main_ch.draw()
        self.text_obj.draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            newDialgue = self.dialogueContent["nodes"][self.dialogue_txt["next"]]
            self.dialogue_txt = newDialgue
            msg = self.dialogue_txt["message"]
            self.text_obj.text = msg
            
            if self.dialogue_txt.get("background_change"):
                self.bgName = self.dialogue_txt["background_change"]
                self.backgroundObj.texture = self.backgroundArray[self.bgName]

            chName = self.dialogue_txt["name"]
            exp = self.dialogue_txt["expression"]
            if self.dialogue_txt.get("both") or chName == self.MCName:
                # if we get BOTH command then we need to add another character inside
                self.characters = characterScrypt(
                    self.characters, chName, exp, self.MCName
                )
            else:
                self.characters = characterScrypt([], chName, mainCharacter=self.MCName)

            position_characters(self.characters)

    def on_update(self, delta_time):
        # this cycle need to prepare sprites to draw on the screen
        for ch in self.characters:
            if not ch.sprite in self.character_list:
                self.character_list.append(ch.sprite)
        self.text_obj.width = settings["window"]["width"] - 130


def gameCycle(window):
    game = GameView()
    window.show_view(game)

    arcade.run()