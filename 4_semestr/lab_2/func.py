Numeric = int | float

class Point:
    def __init__(self, x: Numeric, y: Numeric):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

class Line:
    def __init__(self, a: Numeric, b: Numeric, c: Numeric):
        self.a = a
        self.b = b
        self.c = c

class Cut_line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def is_point_on_line(self, point: Point) -> bool:
        return ((point.x - self.start.x) * (self.end.y - self.start.y) \
            == (point.y - self.start.y) * (self.end.x - self.start.x)) \
            and (self.start.x <= point.x or self.end.x >= point.x\
            or self.start.y <= point.y or self.end.y >= point.y)

class Circle:
    def __init__(self, center: Point, radius: Numeric):
        self.center = center
        self.radius = radius
    
    def is_on_circle(self, point: Point) -> bool:
        return (point.x - self.center.x)**2 + (point.y - self.center.y)**2 == self.radius**2

def crossing_points_two_lines(line1: Line, line2: Line) -> tuple[str, Point | None]:
    if (line1.a * line2.b - line1.b * line2.a) != 0:
        x = (line1.b * line2.c - line1.c * line2.b) / (line1.a * line2.b - line1.b * line2.a)
        y = (line1.c * line2.a - line1.a * line2.c) / (line1.a * line2.b - line1.b * line2.a)

        return ("cross", Point(x,y))
    
    if (line1.b * line2.c == line1.c * line2.b):
        return ("equal", None)
    
    return ("paralel", None)

def crossing_points_line_cut_line(line: Line, cut_line: Cut_line) -> Point | Cut_line | None:
    a = cut_line.end.y - cut_line.start.y
    b = cut_line.start.x - cut_line.end.x
    c = cut_line.start.x * (cut_line.start.y - cut_line.end.y) + cut_line.start.y * (cut_line.end.x - cut_line.start.x)

    line2 = Line(a, b, c)

    points = crossing_points_two_lines(line, line2)

    if points[0] == "equal":
        return cut_line
    
    if points[0] == "paralel":
        return None
    
    if cut_line.start.x > points[1].x or cut_line.end.x < points[1].x\
          or cut_line.start.y > points[1].y or cut_line.end.y < points[1].y:
        return None
    
    return points[1]

def crossing_points_two_cut_lines(cut1: Cut_line, cut2: Cut_line) -> Cut_line | Point | None:
    a1 = cut1.end.y - cut1.start.y
    b1 = cut1.start.x - cut1.end.x
    c1 = cut1.start.x * (cut1.start.y - cut1.end.y) + cut1.start.y * (cut1.end.x - cut1.start.x)

    line1 = Line(a1, b1, c1)

    a2 = cut2.end.y - cut2.start.y
    b2 = cut2.start.x - cut2.end.x
    c2 = cut2.start.x * (cut2.start.y - cut2.end.y) + cut2.start.y * (cut2.end.x - cut2.start.x)

    line2 = Line(a2, b2, c2)

    cross_point = crossing_points_two_lines(line1, line2)

    if cross_point[0] == "paralel":
        return None
    
    if cross_point[0] == "equal":
        if cut1.is_point_on_line(cut2.start):
            return Cut_line(cut2.start, cut1.end)
        elif cut2.is_point_on_line(cut1.start):
            return Cut_line(cut1.start, cut2.end)
        
        return None
    
    if cut1.is_point_on_line(cross_point[1]):
        return cross_point[1]
    
    return None

def crossing_points_line_circle(line: Line, circle: Circle) -> list[Point] | None:
    if line.b != 0:
        a_quad = 1 + (line.a**2) / (line.b**2)
        b_quad = -2 * circle.center.x + 2 * line.a * line.c / (line.b**2) + 2 * line.a * circle.center.y / line.b
        c_quad = circle.center.x ** 2 + line.c **2 / line.b**2 + 2 * line.c * circle.center.y / line.b + circle.center.y **2\
                - circle.radius **2

        D = b_quad**2 - 4 * a_quad *c_quad

        if D > 0:
            x1 = (-b_quad + D**(1/2)) / (2 * a_quad)
            x2 = (-b_quad - D**(1/2)) / (2 * a_quad)
            
            y1 = (-line.c - line.a * x1) / line.b
            y2 = (-line.c - line.a * x2) / line.b

            return [Point(x1, y1), Point(x2, y2)]
        
        elif D == 0:
            x = (-b_quad) / (2 * a_quad)
            y = (-line.c - line.a * x) / line.b

            return [Point(x, y)]
        
        return None
    
    a_quad = 1
    b_quad = -2 * circle.center.x
    c_quad = circle.center.x **2 + line.c**2/line.b**2 + 2 * line.c * circle.center.y / line.b + circle.center.y ** 2 \
            - circle.radius ** 2
    
    D = b_quad**2 - 4 * a_quad *c_quad

    if D > 0:
            x1 = (-b_quad + D**(1/2)) / (2 * a_quad)
            x2 = (-b_quad - D**(1/2)) / (2 * a_quad)
            
            y1 = (-line.c - line.a * x1) / line.b
            y2 = (-line.c - line.a * x2) / line.b

            return [Point(x1, y1), Point(x2, y2)]
        
    elif D == 0:
        x = (-b_quad) / (2 * a_quad)
        y = (-line.c - line.a * x) / line.b

        return [Point(x, y)]
    
    return None

def crossing_points_cut_line_circle(cut_line: Cut_line, circle: Circle) -> list[Point] | None:
    a = cut_line.end.y - cut_line.start.y
    b = cut_line.start.x - cut_line.end.x
    c = cut_line.start.x * (cut_line.start.y - cut_line.end.y) + cut_line.start.y * (cut_line.end.x - cut_line.start.x)

    line = Line(a, b, c)

    cross_points = crossing_points_line_circle(line, circle)

    if cross_points == None:
        return None
    
    for point in cross_points:
        if not cut_line.is_point_on_line(point):
            cross_points.remove(point)
    
    if len(cross_points) == 0:
        return None
    
    return cross_points

def crossing_points_circles(circle1: Circle, circle2: Circle) -> list[Point] | None:
    s = circle1.center.x ** 2 - circle2.center.x ** 2 + circle2.radius ** 2 - circle1.radius ** 2 + circle1.center.y **2\
        + circle2.center.y **2 + 2 * circle1.center.y * circle2.center.y
    
    a = (2 * circle2.center.x - 2 * circle1.center.x) ** 2 + 4 * (circle1.center.y + circle2.center.y) ** 2
    b = 2 * (2 * circle2.center.x - 2 * circle1.center.x) * s - 8 * circle2.center.x * (circle1.center.y + circle2.center.y) ** 2
    c = s**2 - 4 * (circle2.radius ** 2 - circle2.center.x ** 2) * (circle1.center.y + circle2.center.y)** 2

    D = b**2 - 4 * a * c

    if D > 0:
            x1 = (-b + D**(1/2)) / (2 * a)
            x2 = (-b - D**(1/2)) / (2 * a)
            
            y1 = circle2.center.y + (circle2.radius**2 - (x1 - circle2.center.x)**2)**(1/2)
            if not circle1.is_on_circle(Point(x1, y1)):
                y1 = circle2.center.y - (circle2.radius**2 - (x1 - circle2.center.x)**2)**(1/2)
            y2 = circle2.center.y + (circle2.radius**2 - (x2 - circle2.center.x)**2)**(1/2)
            if not circle1.is_on_circle(Point(x2, y2)):
                y2 = circle2.center.y - (circle2.radius**2 - (x2 - circle2.center.x)**2)**(1/2)


            return [Point(x1, y1), Point(x2, y2)]
        
    elif D == 0:
        x = (-b) / (2 * a)
        y =  (circle2.center.y + circle2.radius**2 - (x - circle2.center.x)**2)**(1/2)

        if y != -y:
            return [Point(x, y), Point(x, -y)]
        
        return [Point(x,y)]
    
    return None


if __name__ == "__main__":
    line1 = Line(1, -1, 0)
    line2 = Line(-1, -1, 0)
    cross_point1 = crossing_points_two_lines(line1, line2)

    print(f'Cross point x and -x is ({int(cross_point1[1].x)}, {int(cross_point1[1].y)})')

    p1 = Point(1,1)
    p2 = Point(-1,-1)
    p3 = Point(-2,1)
    p4 = Point(2,-1)

    cut1 = Cut_line(p1, p2)
    cut2 = Cut_line(p3, p4)
    cross_point2 = crossing_points_two_cut_lines(cut1, cut2)

    print(f"Cut lines are crossing in {cross_point2}")
    
    circle1 = Circle(Point(0,0), 3)

    cross_point3 = crossing_points_line_circle(line1, circle1)
    print(f'Circle and line are crossing in [({cross_point3[0].x}, {cross_point3[0].y}), \
({cross_point3[1].x}, {cross_point3[1].y})]')
    
    circle2 = Circle(Point(3,1), 3)

    cross_point4 = crossing_points_circles(circle1, circle2)
    print(f'Circles are crossing in [({cross_point4[0].x}, {cross_point4[0].y}), ({cross_point4[1].x}, {cross_point4[1].y})]')

