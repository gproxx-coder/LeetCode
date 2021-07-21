# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarr = []
        while nums1 or nums2:
            if nums1 and nums2 and (nums1[0] <= nums2[0]):
                newarr.append(nums1.pop(0))
            elif not nums1 and nums2:
                newarr.append(nums2.pop(0))
            elif not nums2 and nums1:
                newarr.append(nums1.pop(0))
            else:
                newarr.append(nums2.pop(0))

        arr_len = len(newarr)
        if arr_len < 1:
            median = float(0)
        else:
            median = (newarr[arr_len//2] + newarr[(arr_len//2)-1])/2 if arr_len%2 == 0 else newarr[(arr_len//2)]
        return median
