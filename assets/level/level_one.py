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
            "enemy_one": [(200, 500), 150],
            "enemy_two": [(WIN_WIDTH - 700, 85), 100],
            "enemy_three": [(WIN_WIDTH - 350, 500), 100],
        },
    ],
    3: [
        {
            "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
            "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
            "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
            "player": [(WIN_WIDTH // 2, WIN_HEIGHT // 2)],
        }
    ],
}
