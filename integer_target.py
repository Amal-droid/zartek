

# 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# Languages: Python/CPP/Java 
# Example 1:

#  Input: nums = [2,7,11,15], target = 9
#  Output: [0,1]
#  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

#  Input: nums = [3,2,4], target = 6
#  Output: [1,2]
# Example 3:

#  Input: nums = [3,3], target = 6
#  Output: [0,1]
# Constraints:

#  2 <= nums.length <= 104
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#  Only one valid answer exists.
# BONUS: Can you come up with an algorithm that is less than O(n²) time complexity?



print("enter the number of elements of array")
n=int(input())
if(n<=104):
    print("enter an array to perform")
    lst =[]
    for i in range(n):
        ele=int(input())
        lst.append(ele)
    print(lst)
    print("\nenter the target value")
    tgt=int(input())
    for i in range(n):
        for j in range(1,n):
            if lst[i]+lst[j]==tgt:
                break
    print(i,j)
else:
    print("enter values less than 104")    