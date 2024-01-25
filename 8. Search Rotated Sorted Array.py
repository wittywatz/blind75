def findTarget(nums, target):
  left = 0
  right = len(nums) - 1
  while left <= right:
    
    mid = (left + right) //2
    # print ('M: ',mid,'  L: ',left,'  R: ',right)
    if target == nums[mid]:
      return mid

    if nums[left] <= nums[mid]:
      if target >nums[mid] or target < nums[left]:
        left = mid+1
      else:
        right= mid -1
    else:
      if target < nums[mid] or target > nums[right]:
        right= mid -1
      else:
        left = mid+1
  
      
  return -1

print(findTarget([4,5,6,7,8,1,2,3], 8))