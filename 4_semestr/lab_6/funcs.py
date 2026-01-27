def count_hash(pattern: str, power: int, q: int) -> int: #h(p) = p[0]x**m-1 + ... + p[m-1]
    res = (ord(pattern[0]) * power + ord(pattern[1])) % q

    for i in range(2, len(pattern)):
        res = (res * power + ord(pattern[i])) % q
    
    return res

def update_hash(old_hash: int, dlt_str: str, add_str: str, pattern_len: int, power: int, q: int) -> int: 
    #h2 = xh1 - p[0]x**m + p[m]
    res = (power * old_hash - (ord(dlt_str) * power ** pattern_len) % q + ord(add_str)) % q
    return res

if __name__ == "__main__":
    s1 = "aaaa"
    s2 = "aAaa"

    print(count_hash(s1, 128, 2**32), count_hash(s2, 128, 2**32))