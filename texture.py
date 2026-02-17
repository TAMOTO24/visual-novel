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
