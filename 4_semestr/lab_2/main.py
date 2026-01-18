from rtree import index
from func import Point

Numeric = int | float
DELTA = 13

class Triangle:
    def __init__(self, points: tuple[Point, Point, Point]):
        self.points = points
    
    def __repr__(self) -> str:
        return str(self.points)
    
    def area(self) -> int | float:
        a = ((self.points[0].x - self.points[1].x)**2 + (self.points[0].y - self.points[1].y)**2) ** (1/2)
        b = ((self.points[1].x - self.points[2].x)**2 + (self.points[1].y - self.points[2].y)**2) ** (1/2)
        c = ((self.points[0].x - self.points[2].x)**2 + (self.points[0].y - self.points[2].y)**2) ** (1/2)

        p = (a + b + c) / 2

        return (p * (p-a) * (p-b) * (p-c)) ** (1/2)
    
    def min_rectangle_coordinates(self) -> tuple[Numeric, Numeric, Numeric, Numeric]:
        return (min(self.points[0].x, self.points[1].x, self.points[2].x), \
                max(self.points[0].x, self.points[1].x, self.points[2].x), \
                min(self.points[0].y, self.points[1].y, self.points[2].y), \
                max(self.points[0].y, self.points[1].y, self.points[2].y))


def make_triangles(points: list[Point]) -> list[Triangle]:
    res: list[Triangle] = []

    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                a = points[j].y - points[i].y
                b = points[i].x - points[j].x
                c = points[i].x * (points[i].y - points[j].y) + points[j].y * (points[j].x - points[i].x)

                if a * points[k].x + b * points[k].y + c == 0:
                    continue

                res.append(Triangle((points[i], points[j], points[k])))
    
    res.sort(key=lambda x: x.area())
    res = res[::-1]

    return res

def make_index_tree(triangles: list[Triangle]) -> index.Index:
    tree = index.Index()
    tree.interleaved = False

    for indx, trngl in enumerate(triangles):
        tree.insert(indx, trngl.min_rectangle_coordinates())
    
    return tree

def is_include(trngl1: Triangle, trngl2: Triangle) -> bool:
    for point in trngl2.points:
        abp = Triangle((trngl1.points[0], trngl1.points[1], point))
        bcp = Triangle((trngl1.points[1], trngl1.points[2], point))
        acp = Triangle((trngl1.points[0], trngl1.points[2], point))

        if round(abp.area() + bcp.area() + acp.area(), DELTA) != round(trngl1.area(), DELTA):
            return False
    
    return True

def find_enclosed_triangles(tree: index.Index, triangles: list[Triangle]) -> list[tuple[Triangle, Triangle]]:
    res: list[tuple[Triangle, Triangle]] = []

    for i, trngl in enumerate(triangles):
        enclosed_indexs = tree.intersection(trngl.min_rectangle_coordinates())
        cnt = 0

        for i_inter in enclosed_indexs:
            cnt += 1
            if i_inter <= i:
                continue
        
            if is_include(triangles[i], triangles[i_inter]):
                res.append((triangles[i], triangles[i_inter]))
        print(cnt, len(triangles))
    
    return res

if __name__ == "__main__":
    n = int(input("Input quantity of dots: "))
    dots = []

    for d in range(n):
        coords = input(f'Dot {d+1}: ').split()
        dots.append(Point(int(coords[0]), int(coords[1])))
    
    trngls = make_triangles(dots)
    tree = make_index_tree(trngls)
    
    nested_trngls = find_enclosed_triangles(tree, trngls)

    for tr1, tr2 in nested_trngls:
        print(tr1, tr2)
    print(len(nested_trngls), len(trngls))