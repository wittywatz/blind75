def containsDuplicate(nums):
  hashSet = set()
  for val in nums:
    if val in hashSet:
      return True
    hashSet.add(val)
  return False

print(containsDuplicate([1,3,2,4,5,1]))
print(containsDuplicate([1,3,2,4,5]))