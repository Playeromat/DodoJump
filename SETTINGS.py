class SETTINGS:
    # WINDOW
    GAME_WIDTH = 800
    GAME_HEIGHT = 600

    # Game
    GROUND = GAME_HEIGHT / 1.1

    # COLOURS
    BG_COLOUR = (255, 255, 255)
    PLAYER_COLOUR = (0, 0, 0)

    # TICKS
    FPS = 60
    PLAYER_TICK = 30
    OBSTACLE_TICK = 30

    # PLAYER
    PLAYER_HEIGHT = GAME_HEIGHT / 5
    PLAYER_WIDTH = GAME_WIDTH / 25
    PLAYER_POS = [GAME_WIDTH / 8, GROUND - PLAYER_HEIGHT]

    # PLAYER MOVEMENT
    GRAVITY = GAME_HEIGHT / 80
    JUMP_VEL = GAME_HEIGHT / 10

    # OBSTACLE
    OBSTACLE_LOW = GAME_HEIGHT / 8
    OBSTACLE_HIGH = GAME_HEIGHT / 5
    OBSTACLE_THIN = GAME_WIDTH / 25
    OBSTACLE_WIDE = GAME_WIDTH / 15

    # OBSTACLE MOVEMENT
    OBSTACLE_VEL = GAME_WIDTH / 100
