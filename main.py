# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution

# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].


#brute force solution:
# use a hashmap?
# use a for loop to iterate through the array
# use a for loop to iterate through the array again
# check if the sum of the two numbers is equal to the target
# if it is, return the indices of the two numbers
# if not, continue

def twoSum(nums, target):
  twoSum = {}
  for i, n in enumerate(nums):
      diff = target - n
      if diff in twoSum:
          return [twoSum[diff], i]
      twoSum[n] = i
  return None  # If no solution is found

nums = [2, 7, 11, 15]
target = 26
print(twoSum(nums, target))  # Output should be [2, 3]

  
  


