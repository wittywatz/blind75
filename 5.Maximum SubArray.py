def maximum_subarray(nums):
  curr_sum = max_sum = nums[0]
  for i in range(1,len(nums)): #Kadane's algorithm
    curr_sum = max(nums[i], curr_sum+nums[i])
    max_sum = max(max_sum, curr_sum)

  return max_sum

print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))