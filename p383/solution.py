class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for char in magazine:
            m.setdefault(char, 0)
            m[char] += 1
        for char in ransomNote:
            if not m.get(char):
                return False
            m[char] -= 1
        return True
