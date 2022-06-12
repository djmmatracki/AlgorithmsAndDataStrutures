

def hash(word, b, prime):
    hashIndexes = []

    for number in prime:
        hw = 0
        for i in range(len(word)):
            hw = (hw * number + ord(word[i])) % b
        hashIndexes.append(hw)
    return hashIndexes


def filtrBlooma(S, N, matches):
    b = 18
    M = len(S)
    prime = [119, 13, 101]
    results = []

    bloom = [0 for _ in range(b)]

    for match in matches:
        indexes = hash(match, b, prime) # Trzy funkcje hashujace zwracajace trzy indeksy

        for i in indexes:
            bloom[i] = 1

    hs = hash(S[:N], b, prime)

    # Wyliczyc wartosc h
    h = [1, 1, 1]
    for i, number in enumerate(prime):
        for _ in range(N - 1):
            h[i] = (h[i]*number) % b

    for m in range(M-N+1):
        same = True

        # Sprawdzamy czy funkca hashujaca sie zgadza
        for i in hs:
            if bloom[i] == 0:
                same = False
                break

        if same == True and S[m:m+N] in matches:
            results.append(m)

        if m != M-N:
            for i, number in enumerate(prime):
                hs[i] = (number*(hs[i] - ord(S[m]) * h[i]) + ord(S[m + N])) % b

    return results


if __name__ == "__main__":
    words = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

    with open("lotr.txt", 'r', encoding='utf-8') as f:
        text = f.readlines()
    S = ''.join(text).lower()

    print(len(filtrBlooma(S, 7, words)))

