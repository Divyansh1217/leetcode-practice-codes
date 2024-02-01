class Solution:
    def minimumPushes(self, word: str) -> int:
        w_len = len(word)
        count = 0
        w_mul = 1
        while w_len > 0:
            count += (w_mul * min(8, w_len))
            w_len = w_len - 8
            w_mul += 1

        return count
