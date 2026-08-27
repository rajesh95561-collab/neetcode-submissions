class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word in anagram:
                anagram[sort_word].append(word)
            else:
                anagram[sort_word]=[word]
        return list(anagram.values())
