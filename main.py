import pygame, random
from ant import Ant 
pygame.init()
pygame.display.set_caption("Langton's Ant")


WIDTH, HEIGHT = 700, 700  
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60


#helper functions
def change_dir(gc, d):
    if gc == 0:
        d += 1 
        if d == 4:
            d = 0
    else:
        d -= 1 
        if d == -1:
            d = 3
    return d

def other_pheromone_present(ants, counter, coord):
    for i in range(len(ants)):
        if i != counter and coord in ants[i].pheromone:
            return i 

    return -1


#main game loop
def main():
    running = True
    grid = []
    N = 100
    for i in range(N):
        t = []
        for j in range(N):
            t.append(0)
        grid.append(t)
    size = WIDTH//N

    ants = []
    ant_n = 50
    ant_color = (255, 0, 0)
    for i in range(ant_n):
        d = random.choice([0, 1, 2, 3])
        x = random.randrange(0, N)
        y = random.randrange(0, N)
        ant = Ant(x, y, size, ant_color, d)
        ants.append(ant)

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # background color
        SCREEN.fill((255,255,255))

        # drawing grid
        x, y = 0, 0
        for i in range(N):
            for j in range(N):
                color = (255, 255, 255)
                if grid[i][j] == 1:
                    color = (0,0,0)
                pygame.draw.rect(SCREEN, color, pygame.Rect(x, y, size, size))
                pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(x, y, size, size), 1)
                x += size
            y += size
            x = 0


        # drawing ants and movements
        counter = 0
        for ant in ants: 
            ant.display(SCREEN)
            grid[ant.y][ant.x] = not grid[ant.y][ant.x]

            # moving ahead
            idx = other_pheromone_present(ants, counter, [ant.y, ant.x])
            if [ant.y, ant.x] in ant.pheromone:
                p = random.randrange(1, 100)
                if p <= 20:
                    ant.dir = change_dir(grid[ant.y][ant.x], ant.dir)
            
            elif idx != -1:
                p = random.randrange(1, 100)
                if p <= 20:
                    ant.dir = change_dir(grid[ant.y][ant.x], ant.dir)

                ant.pheromone.append([ant.y, ant.x])
                ants[idx].pheromone.remove([ant.y, ant.x])

            else:
                ant.pheromone.append([ant.y, ant.x])
                ant.dir = change_dir(grid[ant.y][ant.x], ant.dir)


            ant.move(N)
            counter += 1



        CLOCK.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
