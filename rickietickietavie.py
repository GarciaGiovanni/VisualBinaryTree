import math
import pygame
import pygame.gfxdraw

class Node:
    def __init__(self, surface, color, x, y, radius):
        self._surface = surface
        self._color = color
        self._x = x
        self._y = y
        self._radius = radius

def calc_dist(p1, p2):
    return math.floor(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))

def main():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    
    
    # initialize pygame
    pygame.init()
    screen_size = (1000, 1000)
    
    # create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("pygame Test")

    nodeList = [ Node(screen, RED, 100, 100, 35), Node(screen, RED, 200, 200, 35), Node(screen, RED, 300, 200, 35), Node(screen, RED, 400, 200, 35) ]

    # clock is used to set a max fps
    clock = pygame.time.Clock()
    
    # create a demo surface, and draw a red line diagonally across it
    surface_size = (700, 500)
    test_surface = pygame.Surface(surface_size)
    test_surface.fill(WHITE)
    
    running = True
    while running:
        closest = nodeList[0]
        #Gross way of getting closest circle
        for i in range(len(nodeList)):
            if (calc_dist((nodeList[i]._x, nodeList[i]._y), pygame.mouse.get_pos()) < calc_dist((closest._x, closest._y), pygame.mouse.get_pos())):
                closest = nodeList[i]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #clear the screen
        screen.fill(BLACK)
        
        mouseREL = pygame.mouse.get_rel()
                
        #print(f"{closest._x} | {closest._y}")
        # draw to the screen
        # YOUR CODE HERE

        pygame.draw.line(screen, WHITE, (100, 300), (400, 300), 4)
        clipped_line = pygame.Rect((nodeList[0]._x, nodeList[0]._y), (100, 100)).clipline((100, 300), (400, 300))
        if (clipped_line):
            print('HITTTT')

        

        if pygame.mouse.get_pressed()[0]:
            if (calc_dist((closest._x, closest._y), pygame.mouse.get_pos()) <= closest._radius):
                closest._x = pygame.mouse.get_pos()[0]
                closest._y = pygame.mouse.get_pos()[1]

        for i in range(len(nodeList)):
            pygame.draw.circle(screen, closest._color, (nodeList[i]._x, nodeList[i]._y), nodeList[i]._radius)
            if (i+1 < len(nodeList)):
                pygame.draw.line(screen, closest._color, (nodeList[i]._x, nodeList[i]._y), (nodeList[i+1]._x, nodeList[i+1]._y))
        
        #pygame.draw.circle(screen, RED, (((300-100)**2)-(35**2)-(100**2), 300), 20)
                
                


        # flip() updates the screen to make our changes visible
        pygame.display.flip()
        
        # how many updates per second
        clock.tick(360)
    
    pygame.quit()
main()