# https://leetcode.com/problems/number-of-1-bits/

def hammingWeight(self, n: int) -> int:
    num = bin(n)[2:]
    counter = 0
    for i in num:
        counter += int(i)
    return counter
