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

# Solution 2
def partitionDisjoint(nums: list) -> int:
    big, small = 0, 0
    for idx in range(len(nums)):
        if nums[idx] >= nums[big]:
            big = idx
        elif nums[idx] < nums[big]:
            small = idx
    else:
        if small > big:
            small = big - 1
    print(small, big)
    print(nums[:small+1], nums[small+1:])


# a = [1,1,1,0,6,12]
# a = [5,0,3,8,6]
# a = [1,1]
a = [90,47,69,10,43,92,31,73,61,97]
partitionDisjoint(a)



# Final SOlution
def partitionDisjoint(nums: list) -> int:
    big, small, div = nums[0], nums[0], 0
    for idx in range(1, len(nums)):
        if nums[idx] < small:
            div = idx
            small = big
        big = nums[idx] if nums[idx] > big else big
        
    print(small, div, big)
    print(nums[:div+1], nums[div+1:])


# a = [1,1,1,0,6,12]
# a = [5,0,3,8,6]
# a = [1,1]
a = [90,47,69,10,43,92,31,73,61,97]
# a = [26,51,40,58,42,76,30,48,79,91]
partitionDisjoint(a)
