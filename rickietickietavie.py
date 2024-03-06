import math
from BinaryTree import Node
import Calculate
import pygame
import pygame.gfxdraw

def main():
    #Variable assignment
    x = 100
    WHITE = (255, 255, 255)
    BLUE = (30, 144, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Binary Tree
    Tree = Node(100, 150, 150)
    
    # initialize pygame
    pygame.init()
    screen_size = (1000, 800)
    
    # create a window
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption("Binary Tree Visual")

    # Things to be removed and reimplemented
    nodeList = [

    ]

    lineList = [
        (100, 300, 400, 300),
    ]


    # clock is used to set a max fps
    clock = pygame.time.Clock()
    
    running = True
    placement = False
    while running:
        # Game loop variable assignments
        mousePos = pygame.mouse.get_pos()
        
        if (placement != True):
            color=BLUE

        # Find closest circle relative to mouse position
        if (len(nodeList) != 0):
            closest = nodeList[0]
            for node in nodeList:
                if Calculate.calc_dist((node._x, node._y), mousePos) < Calculate.calc_dist((closest._x, closest._y), mousePos):
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

        # detect intersection
        for node in nodeList:
            for line in lineList:
                intersections = Calculate.line_circle_intersection(node, line[0], line[1], line[2], line[3])
                if intersections:
                    if len(intersections) == 1:
                        pass
                    elif len(intersections) == 2:
                        pass
                    else:
                        pass

        # Creation Buttons
        button1 = pygame.Rect((935, 0), (65, 65))

        # Handle circle movement and clicks
        if pygame.mouse.get_pressed()[0]:
            if placement and button1.collidepoint(mousePos) != True:
                Tree.insert(20)
                print(Tree.left.data)
                placement = False
            elif len(nodeList)!=0 and Calculate.calc_dist((closest._x, closest._y), mousePos) <= closest._radius:
                closest._x, closest._y = mousePos
            elif button1.collidepoint(mousePos):
                placement = True
                color=WHITE
        if pygame.mouse.get_pressed()[2]:
            if len(nodeList)!=0 and Calculate.calc_dist((closest._x, closest._y), mousePos) <= closest._radius:
                nodeList.pop(nodeList.index(closest))
        pygame.draw.rect(screen, color, button1)

        # update display
        pygame.display.flip()
        
        # set fps
        clock.tick(360)
    pygame.quit()

main()