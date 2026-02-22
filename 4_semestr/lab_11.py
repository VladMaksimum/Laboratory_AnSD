def find_colors(n: int, graph: dict[int, list[int]]) -> tuple[int, dict[int, list[int]]]:
    a = [1 << i for i in range(n)]
    flags = [False for _ in range(n)]

    for v1, adj in graph.items():
        for v2 in adj:
            a[v1] |= (1 << v2)
    
    colors: dict[int, list[int]] = {}
    cur_col = 1

    for i in range(n):
        if a[i] == 2**n or flags[i]:
            continue

        colors[cur_col] = [i]
        flags[i] = True

        for j in range(n):
            if a[i] & (1 << j) or flags[j]:
                continue
            
            colors[cur_col].append(j)
            a[i] |= a[j]
            flags[j] = True
        
        cur_col += 1


    return len(colors.keys()), colors 

    


graph = {0: [1, 4, 5],
        1: [0, 2, 3, 7],
        2: [1, 3, 7],
        3: [1, 2, 4, 6],
        4: [0, 3, 5, 6],
        5: [0, 4, 6],
        6: [3, 4, 5, 7],
        7: [1, 2, 6]
    }

print(find_colors(len(graph.keys()), graph))
