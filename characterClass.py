import arcade
from setup import settings


class CharacterSprite:
    def __init__(self, texture: str, spriteW=460, spriteH=700, name="", emotions={}):
        self.sprite = arcade.Sprite(scale=0.9)
        self.sprite.texture = texture
        self.sprite.center_x = settings["window"]["width"] // 2
        self.sprite.center_y = spriteH // 2 + 100

        self.onScreen = False
        self.name = name
        self.emotions = emotions
        self.Width = spriteW
        self.Height = spriteH
        
    def change_emotion(self, emotion):
        if emotion in self.emotions:
            self.sprite.texture = self.emotions[emotion]

# class sceneBackground():
#     def __init__(self, ImgAdress:str, SpriteW, SpriteH, CharactersOnScreen:str):
#         self.objBackground = pygame.image.load(ImgAdress)
#         self.objBackground = pygame.transform.scale(self.objBackground,(SpriteW, SpriteH))
#         self.TwoCharacters = False
#         self.CharactersOnScreen = CharactersOnScreen
