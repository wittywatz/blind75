def two_sum(nums, target):
  seenObj = {}
  for i in range(len(nums)):
    toFind = target - nums[i]
    if toFind in seenObj:
      return [seenObj[toFind], i]
    seenObj[nums[i]] = i

print(two_sum([2,1,5,3], 4))