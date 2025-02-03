import pygame


# dir 0 -> up, 1 -> right, 2 -> down, 3 -> left
class Ant:
    def __init__(self, x, y, size, color, d):
        self.x, self.y = x, y
        self.dir = d
        self.size = size
        self.color = color

        self.pheromone = []
        self.effect = []
        self.forward_prob = 20
        self.max_prob = 100

    def move(self, N):
        if self.dir == 0 and self.y != 0:
            self.y -= 1
        elif self.dir == 1 and self.x != N - 1:
            self.x += 1
        elif self.dir == 2 and self.y != N - 1:
            self.y += 1
        elif self.dir == 3 and self.x != 0:
            self.x -= 1

    def display(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size), 1)
