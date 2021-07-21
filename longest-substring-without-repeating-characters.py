# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

"""
Runtime: 40 ms, faster than 99.71% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 53.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = set()
        current = ''

        for idx in range(len(s)):
            if s[idx] not in current:
                current += s[idx]
            else:
                if current[0] == s[idx]:
                    current = current[1:]
                    current += s[idx]
                else:
                    words.add(current)
                    ix = current.index(s[idx])
                    current = current[ix+1:]
                    current += s[idx]
        else:
            words.add(current)
        return len(reduce(lambda a,b: a if len(a)>len(b) else b, words))

"""
Runtime: 48 ms, faster than 96.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 93.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ''
        max_len = 0
        for idx in range(len(s)):
            if s[idx] not in current:
                current += s[idx]
            else:
                if current[0] == s[idx]:
                    current = current[1:]
                    current += s[idx]
                else:
                    # words.add(current)
                    max_len = len(current) if len(current) > max_len else max_len
                    ix = current.index(s[idx])
                    current = current[ix+1:]
                    current += s[idx]
        else:
            max_len = len(current) if len(current) > max_len else max_len
        return max_len
