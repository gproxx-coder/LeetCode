# Problem statement link
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        negative_flag = False
        op = ""
        num = "".join(reversed(str(x)))
        if num[-1] == "-":
            negative_flag = True
            num = num[:-1]


        if num[0] == "0":
            for zero_idx in range(len(num)):
                if num[zero_idx] != '0':
                    op = num[zero_idx:]
                    break
        else:
            op = num

        if not (-2**31 < int(op) < 2**31):
            return 0

        if negative_flag:
            op = "-" + op

        return op
