from settings import WIN_WIDTH, WIN_HEIGHT


map_one = {
    "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
    "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
    "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
    "platform_one": [(400, 25), (50, 450), "blue"],
    "platform_two": [(400, 25), (WIN_WIDTH - 450, 450), "blue"],
    "platform_three": [(300, 25), (50, 300), "blue"],
    "platform_four": [(300, 25), (WIN_WIDTH - 350, 300), "blue"],
    "platform_five": [(300, 25), (WIN_WIDTH - 250, 150), "blue"],
}
