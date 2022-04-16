from itertools import combinations


def longestCommon(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j+= 1
    return i


def commonChild(s1, s2):
    deletedChars = 1
    n = len(s1)
    maximum = 0

    while deletedChars < n:

        combina = combinations([i for i in range(n)], deletedChars)
        for deleted in combina:
            newS1 = [char for i, char in enumerate(s1) if i not in deleted]
            longest = longestCommon(newS1, s2)
            if longest > maximum:
                maximum = longest


        if maximum >= n - deletedChars - 1:
            return maximum
        
        deletedChars += 1
    return maximum


print(commonChild("SHINCHAN", "NOHARAAA"))