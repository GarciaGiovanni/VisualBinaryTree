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

def bezier_curve_intersection(x0, y0, x1, y1, x2, y2, t, h, k, r):
    return (x0-2*(x1)+x2)*t**2+2*(x1-x0)*t+(x0-h)**2+2*(x1-x0)*(x0-h)*t+(x0-h)**2+(y0-2*(y1)+y2)*t**2+2*(y1-y0)*t+(y0-k)**2+2*(y1-y0)*(y0-k)*t+(y0-k)**2-r**2

def line_circle_intersection(node, x1, y1, x2, y2):
    # Calculate the coefficients of the quadratic equation
    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = 2 * ((x2 - x1) * (x1 - node._x) + (y2 - y1) * (y1 - node._y))
    c = (node._x ** 2 + node._y ** 2 + x1 ** 2 + y1 ** 2 - 2 * (node._x * x1 + node._y * y1) - node._radius ** 2)
    
    # Calculate discriminant
    discriminant = b ** 2 - 4 * a * c
    
    # Check for real roots (intersections)
    if discriminant < 0:
        return None
    elif discriminant == 0:
        # Tangent intersection
        t = -b / (2 * a)
        intersection = (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        if 0 <= t <= 1:
            return [intersection]
        else:
            return None
    else:
        # Calculate the two possible solutions for t
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        # Calculate the intersection points
        intersection1 = (x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1))
        intersection2 = (x1 + t2 * (x2 - x1), y1 + t2 * (y2 - y1))
        
        # Check if the intersections lie on the line segment
        intersections = []
        if 0 <= t1 <= 1:
            intersections.append(intersection1)
        if 0 <= t2 <= 1:
            intersections.append(intersection2)
        
        if intersections:
            return intersections
        else:
            return None

def main():
    xTest = 350
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    
    # initialize pygame
    pygame.init()
    screen_size = (800, 600)
    
    # create a window
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption("pygame Test")

    nodeList = [Node(screen, RED, 100, 100, 35)]
                #Node(screen, RED, 200, 200, 35),
                #Node(screen, RED, 300, 200, 35),
                #Node(screen, RED, 400, 200, 35)]

    lineList = [
                (100, 300, 400, 300)]


    # clock is used to set a max fps
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # find closest circle
        closest = nodeList[0]
        for node in nodeList:
            if calc_dist((node._x, node._y), pygame.mouse.get_pos()) < calc_dist((closest._x, closest._y), pygame.mouse.get_pos()):
                closest = node
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # clear the screen
        screen.fill(BLACK)
        
        # draw lines and circles
        for i in range(len(nodeList)):
            pygame.draw.circle(screen, nodeList[i]._color, (nodeList[i]._x, nodeList[i]._y), nodeList[i]._radius)
            if i + 1 < len(nodeList):
                pygame.draw.line(screen, nodeList[i]._color, (nodeList[i]._x, nodeList[i]._y), (nodeList[i+1]._x, nodeList[i+1]._y))

        # draw a line from (100, 300) to (400, 300)
        pygame.draw.line(screen, WHITE, (100, 300), (400, 300), 1)
        
        #xTest += .1
        # detect intersection
        for node in nodeList:
            for line in lineList:
                intersections = line_circle_intersection(node, line[0], line[1], line[2], line[3])
                if intersections:
                    if len(intersections) == 1:
                        pygame.gfxdraw.bezier(screen, [(100, 300), (200, 300), (400, 300)], 90, WHITE)
                        xTest = 400
                    else:
                        pass
                        #print("Two intersections detected at:", intersections)
        nodeList[0]._y += 1
        # handle circle movement
        if pygame.mouse.get_pressed()[0]:
            if calc_dist((closest._x, closest._y), pygame.mouse.get_pos()) <= closest._radius:
                closest._x, closest._y = pygame.mouse.get_pos()

        print(bezier_curve_intersection(100, 300, 200, 300, 400, 300, 90, 100, 100, 35))

        # update display
        pygame.display.flip()
        
        # set fps
        clock.tick(360)
    pygame.quit()

main()