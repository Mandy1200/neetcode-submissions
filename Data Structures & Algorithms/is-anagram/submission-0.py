class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s :
            dict[i] = dict.get(i,0)+1

        for j in t :
            if j not in dict:
                return False
            dict[j] -= 1

            if dict[j] == 0:
                del dict[j]
        
        return len(dict) == 0         