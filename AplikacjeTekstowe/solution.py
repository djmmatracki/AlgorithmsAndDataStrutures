import numpy as np


def aproximateStringMatching(P, T):
    """
    Funkcja wykorzystujaca programowanie dynamiczne do wyznaczania 'podobienstwa' miedzy wzorcem a tekstem
    """
    n = len(P)
    m = len(T)

    D = np.zeros((n, m))
    D[:,0] = np.arange(n)
    D[0,:] = np.arange(m)

    parents = np.zeros((n,m)).astype('str')
    parents[:,:] = "X"
    parents[0,:] = "I"
    parents[:,0] = "D"
    parents[0,0] = "X"

    for i in range(1, n):
        for j in range(1, m):
            more = 1 if P[i] != T[j] else 0

            switch = D[i-1,j-1] + more # S
            insert = D[i, j-1] + 1 # I
            delete = D[i-1, j] + 1 # D

            minimal = min(switch, insert, delete)
            D[i,j] = minimal

            if minimal == switch:
                if more:
                    parents[i,j] = "S"
                    continue
                parents[i,j] = "M"
            
            if minimal == delete:
                parents[i,j] = "D"
                continue

            if minimal == insert:
                parents[i,j] = "I"
                continue
    
    return int(D[n-1,m-1]), parents


def goal_cell(P, T, D):
    i = len(P) - 1
    j = 0
    for k in range(1, len(T)):
        if D[i,k] < D[i,j]:
            j = k
    return j


def matchStrings(P, T):
    """
    Funkcja zwracajaca indeks pierwszego znaku z tekstu, ktory najbardziej pasuje do wzorca
    """
    n = len(P)
    m = len(T)

    D = np.zeros((n, m))
    D[:,0] = np.arange(n)

    parents = np.zeros((n,m)).astype('str')
    parents[:,0] = "D"
    parents[:,1:] = "X"

    for i in range(1, n):
        for j in range(1, m):
            more = 1 if P[i] != T[j] else 0

            switch = D[i-1,j-1] + more # S
            insert = D[i, j-1] + 1 # I
            delete = D[i-1, j] + 1 # D

            minimal = min(switch, insert, delete)
            D[i,j] = minimal

            if minimal == switch:
                if more:
                    parents[i,j] = "S"
                    continue
                parents[i,j] = "M"
            
            if minimal == delete:
                parents[i,j] = "D"
                continue

            if minimal == insert:
                parents[i,j] = "I"
                continue

    
    cell = goal_cell(P, T, D)
    return int(D[n-1,m-1]), parents, cell - len(P) + 1


def longestSequence(P, T):
    """Znajdz najdluzszy podciag, ktory nie stoi obok siebie ale zachowuje kolejnosc"""
    n = len(P)
    m = len(T)

    D = np.zeros((n, m))
    D[:,0] = np.arange(n)
    D[0,:] = np.arange(m)

    parents = np.zeros((n,m)).astype('str')
    parents[:,:] = "X"
    parents[0,:] = "I"
    parents[:,0] = "D"
    parents[0,0] = "X"

    for i in range(1, n):
        for j in range(1, m):
            more = 100 if P[i] != T[j] else 0

            switch = D[i-1,j-1] + more # S
            insert = D[i, j-1] + 1 # I
            delete = D[i-1, j] + 1 # D

            minimal = min(switch, insert, delete)
            D[i,j] = minimal

            if minimal == switch:
                if more:
                    parents[i,j] = "S"
                    continue
                parents[i,j] = "M"
            
            if minimal == delete:
                parents[i,j] = "D"
                continue

            if minimal == insert:
                parents[i,j] = "I"
                continue
    
    changes = getChanges(parents)
    result = ""

    i = 0
    j = 0
    k = 0
    while j < m and i < n and k < len(changes):
        if changes[k] == 'I':
            i += 1
        elif changes[k] == 'D':
            j += 1
        elif changes[k] == 'M':
            i += 1
            j += 1
            result += P[j]
        k += 1
    
    return result


def getChanges(parents):
    """Na podstawie tablicy parents znajdz operacje wykonane na tekscie"""
    n, m = parents.shape
    i = n - 1
    j = m - 1
    result = ""

    while i >= 0 and j >= 0 and parents[i,j] != 'X':
        if parents[i,j] == 'M' or parents[i,j] == 'S':
            result += parents[i,j]
            i -= 1
            j -= 1

        elif parents[i,j] == 'I':
            result += parents[i,j]
            j -= 1

        elif parents[i,j] == 'D':
            result += parents[i,j]
            i -= 1

    return result[::-1]

def string_compare(P, T, i, j):
    """Funkcja rekurencyjna zwracajaca 'podobienstwo' miedzy wzorcem a tekstem"""
    if i == 0: return j
    if j == 0: return i

    more = 1 if P[i] != T[j] else 0
    switch = string_compare(P, T, i-1, j-1) + more
    insert = string_compare(P, T, i, j-1) + 1
    delete = string_compare(P, T, i-1, j) + 1

    return min(switch, insert, delete)


if __name__ == "__main__":
    P = " kot"
    T = " pies"
    print(string_compare(P, T, len(P)-1, len(T)-1))

    P = " bialy autobus"
    T = " czarny autokar"
    res, parents = aproximateStringMatching(P, T)
    print(res)

    P = " thou shalt not"
    T = " you should not"
    res, parents = aproximateStringMatching(P, T)
    print(getChanges(parents))

    P = " bin"
    T = " monkeyssbanana"
    res, parents, cell = matchStrings(P, T)
    print(cell)

    P = " democrat"
    T = " republican"
    sequence = longestSequence(P, T)
    print(sequence)

    T = ' 243517698'
    P = ''.join(sorted(T))
    sequence = longestSequence(P, T)
    print(sequence)
