import arcade


def load_textures():
    textures = {
        "Jack": {
            "usual": arcade.load_texture("Assets/Characters/Jack/Jack_Usual.png"),
        },
        "Bill": {
            "usual": arcade.load_texture("Assets/Characters/Bill/Bill.png"),
            "uniform": arcade.load_texture("Assets/Characters/Bill/Bill_Uniform.png"),
        },
        "Legoshi": {
            "usual": arcade.load_texture("Assets/Legoshi_Icon/Legoshi.png"),
            "calm": arcade.load_texture("Assets/Legoshi_Icon/Legoshi_Calm.png"),
        },
    }
    return textures


def load_background_texture():
    textures = {
        "Street1": arcade.load_texture("Assets/Other/BackGround/Street1.png"),
        "School": arcade.load_texture("Assets/Other/BackGround/School.png"),
        "Room701": arcade.load_texture("Assets/Other/BackGround/Room701Grouph.png"),
        }
    return textures

def load_dialogue_texture():
    textures = {
        "dialogue": arcade.load_texture("Assets/Dialogue/Dialogue.png"),
        "dialogue-icon": arcade.load_texture("Assets/Dialogue/Dialogue_Icon.png"),
    }
    return textures
