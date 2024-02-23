from settings import WIN_WIDTH, WIN_HEIGHT


level_one = {
    1: [
        {
            "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
            "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
            "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
            "platform_one": [(400, 25), (50, 450), "blue"],
            "platform_two": [(400, 25), (WIN_WIDTH - 450, 450), "blue"],
            "platform_three": [(300, 25), (50, 300), "blue"],
            "platform_four": [(300, 25), (WIN_WIDTH - 350, 300), "blue"],
            "platform_five": [(300, 25), (WIN_WIDTH - 250, 150), "blue"],
            "portal": [(80, 120), (WIN_WIDTH - 150, 30), "white"],
            "player": [(100, 500)],
        },
        {
            "enemy_one": [(200, 300), 50],
            "enemy_two": [(WIN_WIDTH - 350, 300), 50],
            "enemy_three": [(WIN_WIDTH - 200, 150), 50],
            "enemy_four": [(150, 150), 50],
        },
    ],
    2: [
        {
            "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
            "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
            "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
            "platform_one": [(WIN_WIDTH, 25), (200, 150), "blue"],
            "platform_two": [(WIN_WIDTH - 200, 25), (0, 350), "blue"],
            "player": [(WIN_WIDTH - 200, 50)],
            "portal": [(80, 120), (80, WIN_HEIGHT - 195), "white"],
        },
        {
            "enemy_one": [(200, 400), 150],
            "enemy_two": [(WIN_WIDTH - 700, 85), 100],
            "enemy_three": [(WIN_WIDTH - 350, 500), 100],
        },
    ],
    3: [
        {
            "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
            "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
            "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
            "platform_one": [(50, 25), (100, WIN_HEIGHT - 150), "blue"],
            "platform_two": [(50, 25), (443, 401), "blue"],
            "platform_three": [(50, 25), (685, 331), "blue"],
            "platform_four": [(50, 25), (985, 331), "blue"],
            "platform_five": [(50, 25), (785, 131), "blue", True, 100],
            "platform_blabla": [(150, 25), (20, 185), "blue"],
            "player": [(WIN_WIDTH - 200, WIN_HEIGHT - 150)],
            "portal": [(80, 120), (70, 65), "white"],
        },
        {
            "enemy_one": [(200, 200), 100],
            "enemy_two": [(985, 281), 100],
            "enemy_three": [(600, 500), 20],
        },
    ],
    4: [
        {
            "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
            "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
            "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
            "player": [(100, WIN_HEIGHT - 150)],
            "portal": [(80, 120), (WIN_WIDTH - 130, WIN_HEIGHT - 196), "purple"],
        },
    ],
}
