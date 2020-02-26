from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 255 ]
matrix = new_matrix()

for i in range(361):
    add_point(matrix, int(250 + (250 * math.cos(i))), int(250 + (250 * math.sin(i))))

draw_lines(matrix, screen, color)
display(screen)
