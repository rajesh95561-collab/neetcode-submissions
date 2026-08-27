class Solution:
    def isValid(self, s: str) -> bool:
        make_list = {')': '(', '}': '{', ']': '['}
        result_list = []
        
        for char in s:
            if char in make_list.values():   # opening bracket
                result_list.append(char)
            elif char in make_list:          # closing bracket
                if result_list and result_list[-1] == make_list[char]:
                    result_list.pop()
                else:
                    return False
        return not result_list