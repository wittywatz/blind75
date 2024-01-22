def maxProfit(stocks):
  l,r = 0,1
  maxProfit = 0
  while r < len(stocks):
    if stocks[l] > stocks[r]:
      l = r
    else:
      maxProfit = max(maxProfit, stocks[r]-stocks[l])
    r+=1

  return maxProfit

print(maxProfit([7,1,5,7,6,4]))