class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = {}

        # 1. Count each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # 2. Sort characters by frequency
        chars = sorted(freq, key=lambda ch: freq[ch], reverse=True)

        # 3. Repeat each character according to its frequency
        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result
