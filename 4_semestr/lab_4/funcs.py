def count_prefixs(string: str) -> list[int]:
    res: list[int] = [0 for _ in range(len(string))]
    res[0] = -1
    cnt = 0

    for i in range(2, len(string)):
        while cnt != 0 and string[cnt] != string[i]:
            cnt = res[cnt-1]
        
        if string[cnt] == string[i]:
            cnt += 1

        res[i] = cnt
    

    return res