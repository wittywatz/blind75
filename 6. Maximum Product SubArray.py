def maximum_product_subarray(nums):
  curr_min = curr_max = max_product = 1
  for num in nums:
    tmp_min = min(num, curr_min*num, curr_max*num)
    curr_max = max(num, curr_max*num, curr_min*num)
    curr_min = tmp_min
    max_product = max(max_product, curr_max)

  return max_product

print(maximum_product_subarray([2,3,-2,4]))
print(maximum_product_subarray([-2,0,1]))
print(maximum_product_subarray([2,3,-2,-5,6,-1,4]))