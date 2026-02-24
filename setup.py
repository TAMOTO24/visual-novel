import arcade

arcade.load_font("Assets/Fonts/Fonstars-4Bo0p.ttf")


settings = {
    "title": "Beastars Visual Novel",
    "window": {
        "width": 1700,
        "height": 920,
        "fps": 60,
    },
    "style": {
        "btn": {
            "normal": {
                "font_name": "Fonstars",
                "font_size": 20,
                "font_color": arcade.color.BLACK,
                "bg": (0, 0, 0, 0),
            },
            "hover": {
                "font_name": "Fonstars",
                "font_size": 20,
                "font_color": arcade.color.RED,
                "bg": (0, 0, 0, 0),
            },
            "press": {
                "font_name": "Fonstars",
                "font_size": 20,
                "font_color": arcade.color.BLACK,
                "bg": (0, 0, 0, 0),
            },
        }
    },
}
