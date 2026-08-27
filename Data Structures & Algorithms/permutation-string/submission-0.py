from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        count_s1 = Counter(s1)

        for i in range(len(s2) - len_s1 + 1):
            window = s2[i:i+len_s1]
            if Counter(window) == count_s1:
                return True
        return False