def findMin(nums):
  left = 0
  right = len(nums) - 1
  min_value = float('inf')
  while left <= right:
    mid = (left + right) //2
    if nums[mid] >= nums[left]:
      min_value = min(min_value, nums[left])
      left = mid + 1
    else:
      min_value = min(min_value, nums[mid])
      right = mid - 1
      
 
  return min_value

print(findMin([4,5,1,2,3]))