import pygame


# dir 0 -> up, 1 -> right, 2 -> down, 3 -> left
class Ant:
    def __init__(self, x, y, size, color, d):
        self.x, self.y = x, y
        self.dir = d
        self.size = size
        self.color = color

        self.pheromone = [] # element of the form [ [x, y], forward_probability]
        self.forward_prob = 20
        self.max_prob = 100

        self.decay_rate = self.forward_prob*0.2

    def change_dir(self, white):
        if white:
            self.dir += 1 
            if self.dir == 4:
                self.dir = 0 
        else:
            self.dir -= 1 
            if self.dir == -1:
                self.dir = 3

        return self.dir

    def move(self, N):

        if self.dir == 0 and self.y > 0:
            self.y -= 1
        elif self.dir == 1 and self.x <  N - 1:
            self.x += 1
        elif self.dir == 2 and self.y <  N - 1:
            self.y += 1
        elif self.dir == 3 and self.x >  0:
            self.x -= 1

    def display(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size), 1)


    def find_pheromone(self, coord):
        for i in range(len(self.pheromone)):
            if self.pheromone[i][0] == coord :
                return i 
        return -1
