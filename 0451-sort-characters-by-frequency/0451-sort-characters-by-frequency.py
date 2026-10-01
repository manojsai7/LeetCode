from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        return ''.join(
            sorted(s, key=lambda char: (-freq[char], char))
        )