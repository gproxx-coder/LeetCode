def partitionDisjoint(nums: list) -> int:
    left, right = [], []
    bigger = nums[0]
    last = nums[-1]
    # left.append(nums[0])
    for num in nums:
        if last > num and num <= bigger:
            left.append(num)
        else:
            right.append(num)
    else:
        if not right:
            right.append(left.pop())
    print(left, right)


# a = [1,1,1,0,6,12]
# a = [5,0,3,8,6]
# a = [1,1]
a = [90,47,69,10,43,92,31,73,61,97]
partitionDisjoint(a)
