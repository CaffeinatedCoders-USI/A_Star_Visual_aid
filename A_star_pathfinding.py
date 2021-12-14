import pygame
import os
import A_star_pathfinding_helper


WIDTH = 800 #Grid Size
WIN = pygame.display.set_mode((WIDTH, WIDTH + 100))
pygame.display.set_caption("A* Path Finding Algorithm")




    
def main(win, width):
    pygame.init()
    ROWS = 50
    grid = A_star_pathfinding_helper.make_grid(ROWS, width)
    start = None
    end = None
    run = True
    win.fill(A_star_pathfinding_helper.WHITE)
    move_x = 50
    pygame.draw.rect(WIN,(50,50,50), pygame.Rect(0, 800, 800, 900))
    pygame.draw.rect(WIN, (0,150,100), pygame.Rect(30 + move_x, 830, 600 + move_x, 880))
    A_star_pathfinding_helper.writeLB(str("First Left Click (Start Node/Block)"),50 + move_x,845)
    A_star_pathfinding_helper.writeLB(str("Second Left Click (End Node/Block/Goal)"),50 + move_x,860)
    A_star_pathfinding_helper.writeLB(str("Third Left Click (Wall/Obstacle)"),50 + move_x,875)
    A_star_pathfinding_helper.writeLB(str("C Key (Clears the Grid)"),400 + move_x,845)
    A_star_pathfinding_helper.writeLB(str("Spacebar (Start the pathfinding)"),400 + move_x,860)
    A_star_pathfinding_helper.writeLB(str("Right Click (Resets Single Block)"),400 + move_x,875)
    while run:
        A_star_pathfinding_helper.draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = A_star_pathfinding_helper.get_clicked_pos(pos, ROWS, width)
                try:
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()

                    elif not end and spot != start:
                        end = spot
                        end.make_end()

                    elif spot != end and spot != start:
                        spot.make_barrier()
                except:
                    print("Out of bounds")

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    A_star_pathfinding_helper.algorithm(lambda: A_star_pathfinding_helper.draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)