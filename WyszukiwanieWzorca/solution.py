import time


def naive_pattern(S, W):
    m = 0
    i = 0
    patters_no = 0
    first_occurence = None
    comparisons = 0

    while m + i < len(S):
        # Znaleziono wzorzec
        if i == len(W):
            if first_occurence is None:
                first_occurence = m
            patters_no += 1
            m = m + i + 1
            i = 0
            continue

        # Przerwano porownanie
        comparisons += 1
        if S[m+i] != W[i]:
            m += 1
            i = 0
            continue
        
        i += 1
    
    if i == len(W):
        patters_no += 1
    
    return patters_no, first_occurence, comparisons


def hash(s, d, q):
    hw = 0
    for i in range(len(s)):
        hw = (hw*d + ord(s[i])) % q
    return hw

# def hashLetter(letter):
#     d = 256
#     q = 101
#     return (hw*d + ord(letter)) % q

def rabinKarp(S, W):
    M = len(S)
    N = len(W)
    d = 256
    q = 101

    hW = hash(W, d, q)
    tab = []
    comparisons = 0
    colisions = 0
    
    # Funkcja hashujaca dla pierwszego segmentu
    hS = hash(S[:N], d, q)

    # Wyliczyc wartosc h
    h = 1
    for _ in range(N - 1):
        h = (h*d) % q

    # Szukanie wzorca
    for m in range(M-N+1):
        comparisons += 1
        
        if hS == hW:
            if S[m:(m+N)] == W:
                tab.append(m)
            else:
                colisions += 1

        if m + N < M:
            hS = (d*(hS - ord(S[m]) * h) + ord(S[m + N])) % q
    
    return len(tab), comparisons, colisions


def kmp_table(word):
    pos = 1
    cnd = 0
    T = [-1]
    while pos < len(word):
        if word[pos] == word[cnd]:
            # T[pos] = T[cnd]
            T.append(T[cnd])
        else:
            # T[pos] = cnd
            T.append(cnd)
            while cnd >= 0 and word[pos] != word[cnd]:
                # print(word[pos],  word[cnd])
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T.append(cnd)

    return T


def knutha_morrisa_pratta(S, W):
    m = 0
    i = 0
    T = kmp_table(W)
    # nP = 0
    P = []
    comparisons = 0

    while m < len(S):
        comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m-i)
                # P[nP] = m - i
                # nP += 1
                i = T[i]
            continue

        i = T[i]
        if i < 0:
            m += 1
            i += 1
    
    return len(P), comparisons


if __name__ == "__main__":
    with open("lotr.txt", 'r', encoding='utf-8') as f:
        text = f.readlines()

    S = ''.join(text).lower()
    time1 = time.time()
    no1, m1, comparisons1 = naive_pattern(S, "time.")
    time2 = time.time()
    no2, comparisons2, colisions = rabinKarp(S, "time.")
    time3 = time.time()
    no3, comparisons3 = knutha_morrisa_pratta(S, "time.")
    time4 = time.time()

    print(f"{no1};{comparisons1}")
    # print("Czas wykonywania dla pierwszej metody:", time2 - time1)
    # print("Liczba porownan dla pierwszej metody:", comparisons1)
    # print("Liczba znalezionych dla pierwszej metody:", no1)
    print()

    print(f"{no2};{comparisons2};{colisions}")
    # print("Czas wykonywania dla drugiej metody:", time3 - time2)
    # print("Liczba porownan dla drugiej metody:", comparisons2)
    # print("Liczba znalezionych dla drugiej metody:", no2)
    print()

    print(f"{no3};{comparisons3};")
    # print("Czas wykonywania dla trzeciej metody:", time4 - time3)
    # print("Liczba porownan dla pierwszej metody:", no3)
    # print("Liczba znalezionych dla drugiej metody:", len(tab))
