def backtrack(n: int, weights: list[int], capacity: int, boxes: list[int], min_boxes: int, current: int) -> tuple[int, list[int]]:
    if current == n:
        return min(min_boxes, len(boxes)), boxes
    
    for i in range(len(boxes)):
        if weights[current] + boxes[i] <= capacity:
            boxes[i] += weights[current]
            min_boxes, boxes = backtrack(n, weights, capacity, boxes, min_boxes, current + 1)
            boxes[i] -= weights[current]
    
    boxes.append(weights[current])
    min_boxes, boxes = backtrack(n, weights, capacity, boxes, min_boxes, current + 1)
    boxes.pop()

    return min_boxes, boxes

def boxing(n: int, weights: list[int], capacity: int) -> int:
    min_boxes, boxes = backtrack(n, weights, capacity, [], 2**n, 0)
    return min_boxes

n = 5
weights = [4, 5, 2, 1, 3]
capacity = 6

print(boxing(n, weights, capacity))