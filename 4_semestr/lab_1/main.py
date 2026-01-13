import funcs

n = int(input("Input quantity of dots: "))
dots = []
figure = []

for d in range(n):
    dots.append([int(i) for i in input(f'Dot {d+1}: ').split()])

bottom_dot = dots[0]
for dot in dots:
    if dot[1] < bottom_dot[1]:
        bottom_dot = dot
    elif dot[1] == bottom_dot[1] and dot[0] < bottom_dot[0]:
        bottom_dot = dot

figure.append(dots.pop(dots.index(bottom_dot)))
funcs.quick_sort_for_polar_angles(dots, 0, len(dots) - 1, bottom_dot)

for i in range(len(dots)):
    figure.append(dots[i])

    if len(figure) >= 3:
        while funcs.is_right_rotation(figure[-3], figure[-2], figure[-1]):
            figure.pop(-2)

            if len(figure) < 3:
                break

if len(figure) < 3:
    print("Convex shape not found")
else:
    print(figure)
    funcs.draw(figure, dots)