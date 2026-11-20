class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = sorted(list(s.strip()))
        l2 = sorted(list(t.strip()))

        if l1 == l2:
            return True
        return False