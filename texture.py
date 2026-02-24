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
        "Black": arcade.load_texture("Assets/Other/BackGround/Black.png"),
        "DramaClubPeople": arcade.load_texture(
            "Assets/Other/BackGround/DramaClubPeople.png"
        ),
        "DramaClubStreet": arcade.load_texture(
            "Assets/Other/BackGround/DramaClubStreet.png"
        ),
        "Frame1": arcade.load_texture("Assets/Other/BackGround/Frame1.png"),
        "Frame2_1": arcade.load_texture("Assets/Other/BackGround/Frame2.1.png"),
        "Frame2_3": arcade.load_texture("Assets/Other/BackGround/Frame2.3.png"),
        "Frame4_1": arcade.load_texture("Assets/Other/BackGround/Frame4.1.png"),
        "Frame4_2": arcade.load_texture("Assets/Other/BackGround/Frame4.2.png"),
        "Frame4_3": arcade.load_texture("Assets/Other/BackGround/Frame4.3.png"),
        "Frame4_4": arcade.load_texture("Assets/Other/BackGround/Frame4.4.png"),
        "Frame4_5": arcade.load_texture("Assets/Other/BackGround/Frame4.5.png"),
        "Frame4_6": arcade.load_texture("Assets/Other/BackGround/Frame4.6.png"),
        "Frame5_1": arcade.load_texture("Assets/Other/BackGround/Frame5.1.png"),
        "HerbivoresHostel": arcade.load_texture(
            "Assets/Other/BackGround/HerbivoresHostel.png"
        ),
        "MaleDressingRoom": arcade.load_texture(
            "Assets/Other/BackGround/MaleDressingRoom.png"
        ),
        "Preview": arcade.load_texture("Assets/Other/BackGround/Preview.png"),
        "Preview1": arcade.load_texture("Assets/Other/BackGround/Preview1.png"),
        "Preview2": arcade.load_texture("Assets/Other/BackGround/Preview2.png"),
        "Room701": arcade.load_texture("Assets/Other/BackGround/Room701.png"),
        "Room701Grouph": arcade.load_texture(
            "Assets/Other/BackGround/Room701Grouph.png"
        ),
        "School": arcade.load_texture("Assets/Other/BackGround/School.png"),
        "School2": arcade.load_texture("Assets/Other/BackGround/School2.png"),
        "SchoolFrame": arcade.load_texture("Assets/Other/BackGround/SchoolFrame.png"),
        "Street1": arcade.load_texture("Assets/Other/BackGround/Street1.png"),
    }

    return textures


def load_dialogue_texture():
    textures = {
        "dialogue": arcade.load_texture("Assets/Dialogue/Dialogue.png"),
        "dialogue-icon": arcade.load_texture("Assets/Dialogue/Dialogue_Icon.png"),
    }
    return textures
