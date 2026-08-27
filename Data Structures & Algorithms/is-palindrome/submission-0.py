class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = list(s)
        newlist = []
        for i in list1:
            if(i.isalnum()):
                newlist.append(i.lower())
            else:
                continue
        cpy_list = newlist.copy()
        cpy_list.reverse()
        if(newlist == cpy_list):
            return True
        else:
            return False