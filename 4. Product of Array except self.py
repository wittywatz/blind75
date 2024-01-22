def productExceptSelf(nums):
  res = [1] * len(nums)
  for i in range(len(nums)-1): # Prefix from second position
    res[i+1] = res[i] * nums[i]
  postFixProduct = 1
  for i in reversed(range(len(nums)-1)): #Postfix from len-1 position
    postFixProduct *= nums[i+1]
    res[i] *= postFixProduct
  return res

print(productExceptSelf([1,2,3,4]))