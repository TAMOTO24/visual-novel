from characterClass import CharacterSprite
from texture import load_textures


def getCharacters():
    textures = load_textures()
    characters = {
        "Jack": CharacterSprite(
            textures["Jack"]["usual"],
            name="Jack",
            emotions=textures["Jack"],
        ),
        "Legoshi": CharacterSprite(
            textures["Legoshi"]["usual"],
            name="Legoshi",
            emotions=textures["Legoshi"],
        ),
        "Bill": CharacterSprite(
            textures["Bill"]["usual"],
            name="Bill",
            emotions=textures["Bill"],
        ),
    }
    return characters


characterArray = getCharacters()
