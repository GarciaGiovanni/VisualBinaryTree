import math

#Distance between two points
def calc_dist(p1, p2):
    return math.floor(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))

#Test intersection of a line and a circle
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