from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """merge two 'sorted' lists (num1 and num2)"""
        merged_list = []
        while nums1 and nums2:
            # compare list front pop smaller item
            merged_list.append(nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0))
        
        merged_list.extend(nums1 if nums1 else nums2)  # add the leftout items in case 

        len_merged_list = len(merged_list)
        mid_point = int((len(merged_list))/2)
        if len_merged_list % 2 == 0:
            return merged_list[mid_point]   # odd case
        else:
            return sum(merged_list[mid_point-1: mid_point +1]) / 2    # even case
