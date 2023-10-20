# https://leetcode.cn/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        tail = len(s) - 1
        while tail >= 0:
            if s[tail].isspace():
                tail -= 1
                continue
            head = tail
            while not s[head].isspace() and head >= 0:
                head -= 1
            words.append(s[head + 1:tail + 1])

            tail = head

        return " ".join(words)
