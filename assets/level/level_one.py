from settings import WIN_WIDTH, WIN_HEIGHT


map_one = {
    "floor": [(WIN_WIDTH, 75), (0, WIN_HEIGHT - 75), "blue"],
    "wall_left": [(50, WIN_HEIGHT), (0, 0), "blue"],
    "wall_right": [(50, WIN_HEIGHT), (WIN_WIDTH - 50, 0), "blue"],
    "platform_one": [(100, 50), (500, 500), "blue"],
}
