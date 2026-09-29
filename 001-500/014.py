# Check one character position across ALL strings → if any string differs, stop immediately → otherwise add that character to the prefix.

# The key idea is:

# Position 0 → check everyone
# Position 1 → check everyone
# Position 2 → check everyone
# ...

# So the pattern is:

# Same position across all strings → one mismatch → stop.

# Pattern name

# Primary: String Traversal / Common Prefix Matching
# Technique: Nested loops
# Not: Two pointers ❌
# Not: Sliding window ❌
# Not: Binary search ❌

class Solution:
    def longestCommonPrefix(self, strs):
        prefix=''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i]!=strs[0][i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix
