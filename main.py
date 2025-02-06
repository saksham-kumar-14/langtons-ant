import pygame, random
from ant import Ant 
pygame.init()
pygame.font.init()
pygame.display.set_caption("Langton's Ant")


WIDTH, HEIGHT = 700, 700 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 25
FONT = pygame.font.SysFont("freesansbold.ttf", 36)

#main game loop
def main():
    running = True
    grid = []
    N = 100
    for i in range(N):
        t = []
        for j in range(N):
            t.append(1)
        grid.append(t)
    size = WIDTH//N

    ants = []
    ant_n = 10
    ant_color = (255, 0, 0)
    for i in range(ant_n):
        d = random.choice([0, 1, 2, 3])
        x = random.randrange(0, N)
        y = random.randrange(0, N)
        ant = Ant(x, y, size, ant_color, d)
        ants.append(ant)

    steps = 0

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
                color = (0, 0, 0)
                if grid[i][j] == 1:
                    color = (255, 255, 255)
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

            # pheromones
            pheromone_in_ant = ant.find_pheromone([ant.y, ant.x])
            pheromone_in_others = -1
            other_ant_with_pheromone = -1
            for j in range(len(ants)):
                pheromone_in_others = ants[j].find_pheromone([ant.y, ant.x])
                if j != counter and  pheromone_in_others != -1:
                    other_ant_with_pheromone = j
                    break

            if pheromone_in_ant != -1:
                p = random.randrange(1, ant.max_prob + 1)
                if p <= ant.pheromone[pheromone_in_ant][1]:
                    ant.change_dir(grid[ant.y][ant.x])
                ant.pheromone.pop(pheromone_in_ant)

            elif pheromone_in_others != -1:
                p = random.randrange(1, ant.max_prob + 1)
                if p > ants[other_ant_with_pheromone].pheromone[pheromone_in_others][1]:
                    ant.change_dir(grid[ant.y][ant.x])
                ants[other_ant_with_pheromone].pheromone.pop(pheromone_in_others)

            else:
                ant.dir = ant.change_dir(grid[ant.y][ant.x])

            ant.move(N)
            ant.pheromone.append([ [ant.y, ant,x], ant.forward_prob ])
            counter += 1 
            for j in range(len(ant.pheromone)):
                if ant.pheromone[j][1] > 0:
                    ant.pheromone[j][1] -= ant.decay_rate


        # displaying font
        frames = FONT.render(f"Steps: {steps}", True, (255, 0 ,0))
        SCREEN.blit(frames, (0 ,0))
        steps += 1


        CLOCK.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
