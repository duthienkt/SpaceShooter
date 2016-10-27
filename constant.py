KEY_ESC = 27
PATH_ASSETS = "assets/"
PATH_EFF = PATH_ASSETS + "eff/"
PATH_NORMAL_CURSOR = PATH_ASSETS + "cursor.png"

PATH_BACKGROUND = PATH_ASSETS + "background.png"
HELP_BACKGROUND = PATH_ASSETS + "help_bg.png"
BACK_IMAGE = [PATH_ASSETS + "back.png", PATH_ASSETS + "back2.png"]
PATH_LOGO = PATH_ASSETS + "logo.png"
KEY_ESC = 27

PATH_BUTTONS = [[PATH_ASSETS + "newgame.png", PATH_ASSETS + "newgame2.png"],
                [PATH_ASSETS + "help.png", PATH_ASSETS + "help2.png"],
                [PATH_ASSETS + "exit.png", PATH_ASSETS + "exit2.png"]]

COLOR_BACKGROUND = (40, 40, 200)

PATH_BULLET = [
    PATH_EFF + "bullet_1.png",
    PATH_EFF + "bullet_2.png",
    PATH_EFF + "bullet_3.png",

    PATH_EFF + "bullet_1_rv.png",
    PATH_EFF + "bullet_2_rv.png",
    PATH_EFF + "bullet_3_rv.png",

    PATH_EFF + "rocket_type_1.png",
    PATH_EFF + "rocket_type_2.png",

    PATH_EFF + "rocket_type_1_rv.png",
    PATH_EFF + "rocket_type_2_rv.png",

    PATH_EFF + "bullet_red.png",
    PATH_EFF + "bullet_blue.png",
    PATH_EFF + "bullet_green.png",
    PATH_EFF + "bullet_yellow.png"
]
BULLET_HEAD = [(5, 4),
               (7, 6),
               (10, 9),
               (6, 20),
               (7, 22),
               (8, 21),
               (25, 0),
               (25, 0),
               (24, 57),
               (24, 57),

               ]
PATH_BULLET_EXPLOSION = [
    PATH_EFF + "expl_small.png",
    PATH_EFF + "expl_plasma.png",
    PATH_EFF + "expl_big_red.png",

    PATH_EFF + "expl_small.png",
    PATH_EFF + "expl_plasma.png",
    PATH_EFF + "expl_big_red.png",

    PATH_EFF + "expl_rocket_1.png",
    PATH_EFF + "expl_rocket_2.png",

    PATH_EFF + "expl_rocket_1.png",
    PATH_EFF + "expl_rocket_2.png",

]

PATH_EXPL_SOUND = PATH_ASSETS+ "expls.ogg"
PATH_SOUNDTRACK = PATH_ASSETS +"soundtrack/"
PATH_MUSICS = [
    PATH_SOUNDTRACK+"battle.ogg",
    PATH_SOUNDTRACK+"background.ogg"

              ]
PATH_ITEM = [
PATH_EFF + "fixer.png",
    PATH_EFF + "coin.png",
    PATH_EFF + "item_rocket1.png",
    PATH_EFF + "item_rocket2.png",
    PATH_EFF + "power.png"

]

BULLET_EXPLOSION_LENGTH = [17, 13, 12, 17, 13, 12, 5, 5, 5, 5]

PATH_SHIP = PATH_ASSETS + "ship/"
PATH_SPACE = PATH_ASSETS + "space/"

PATH_ENEMY = [
    PATH_SHIP + "en1.png",
    PATH_SHIP + "en2.png",
    PATH_SHIP + "en7.png",
    PATH_SHIP + "en4.png",
    PATH_SHIP + "en5.png",
    PATH_SHIP + "en6.png",
    PATH_SHIP + "en3.png",
    PATH_SHIP + "en8.png"
]

PATH_PLAYER = [
    PATH_SHIP + "lv1.png",
    PATH_SHIP + "lv2.png",
    PATH_SHIP + "lv3.png",
    PATH_SHIP + "lv4.png",
]

PLAYER_GUN = [
    [(9, 46), (57, 46)],
    [(19, 38), (53, 38)],
    [(12, 40), (56, 49)],
    [(13, 50), (21, 45), (63, 45), (71, 50)]

]

PATH_BOSS = PATH_SHIP+"boss5/boss1.png"
PATH_BOSS_CHILD = PATH_SHIP+"boss3.png"
PATH_WIN = PATH_ASSETS+"win.png"
PATH_LOST = PATH_ASSETS+"defeat1.png"

PLAYER_SPEED = [400, 450, 500, 550]
PLAYER_HP = [150, 210, 300, 450]


##################################################################################################
PATH_TOOL = PATH_ASSETS + "tool/"

PATH_STATUS = [
    PATH_TOOL + "power.png",
    PATH_TOOL + "coin.png",
    PATH_TOOL + "rocket1.png",
    PATH_TOOL + "rocket2.png",
]

PATH_TOOL_BUTTON = [[PATH_TOOL + "exit.png",PATH_TOOL + "exit2.png"]]

PATH_BGTOOL = PATH_TOOL + "bgtool.jpg"

PATH_SHIP_LV = [
    PATH_TOOL +"ship_lv1.png",
    PATH_TOOL +"ship_lv2.png",
    PATH_TOOL +"ship_lv3.png",
    PATH_TOOL +"ship_lv4.png" ]

PATH_HPBAR = [
    PATH_TOOL + "hpbar.png",
              PATH_TOOL + "hpbar2.png",
    PATH_TOOL + "hpbar_boss.png",
              PATH_TOOL + "hpbar2_boss.png"
              ]


COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
PATH_FONT = PATH_ASSETS + "castellar.ttf"
