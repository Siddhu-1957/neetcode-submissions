class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n="".join(sorted(s))
        nn="".join(sorted(t))
        if(n==nn):
            return True
        else:
            return False
        