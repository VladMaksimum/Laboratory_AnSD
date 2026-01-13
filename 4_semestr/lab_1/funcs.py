import matplotlib.pyplot as plt

def cos_polar_angle(center: list[int], point: list[int]) -> float:
    x = point[0] - center[0]
    y = point[1] - center[1]

    return x/((x**2 + y**2)**(1/2))

def quick_sort_for_polar_angles(points : list[list[int]], start : int, end : int, center: list[int]):
    if end-start == 1:
        if cos_polar_angle(center, points[end]) > cos_polar_angle(center, points[start]):
            tmp = points[end]
            points[end] = points[start]
            points[start] = tmp

        return
    
    if end - start <= 0:
        return

    i = start
    j = end

    pivot = points[int((i+j)/2)]
    cos_pivot = cos_polar_angle(center, pivot)

    while i <= j:
        cos_i = cos_polar_angle(center, points[i])
        cos_j = cos_polar_angle(center, points[j])

        if cos_i <= cos_pivot and cos_j >= cos_pivot:
            tmp = points[i]
            points[i] = points[j]
            points[j] = tmp

            if cos_j == cos_pivot:
                i+=1
            elif cos_i == cos_pivot:
                j-=1
            else:
                j-=1
                i+=1

            continue

        if cos_i > cos_pivot:
            i+=1
        
        if cos_j < cos_pivot:
            j-=1

    if i-2 <= end:
        quick_sort_for_polar_angles(points, start, i-2, center)
    if j >= start:
        quick_sort_for_polar_angles(points, j, end, center)

def is_right_rotation(point1: list[int], point2: list[int], point3: list[int]) -> bool:
    ba_x = point1[0] - point2[0]
    ba_y = point1[1] - point2[1]

    bc_x = point3[0] - point2[0]
    bc_y = point3[1] - point2[1]

    vector_mult_det = ba_x * bc_y - ba_y * bc_x
    return vector_mult_det >= 0

def draw(shape: list[list[int]], other_points: list[list[int]]):
    fig, ax = plt.subplots()

    #shape
    x = [point[0] for point in shape]
    x.append(x[0])
    y = [point[1] for point in shape]
    y.append(y[0])

    ax.plot(x, y)

    #other
    x_pt = [point[0] for point in other_points]
    x_pt.append(x[0])
    y_pt = [point[1] for point in other_points]
    y_pt.append(y[0])

    ax.plot(x_pt, y_pt, "o")
    fig.savefig("4_semestr/lab_1/shape.png")