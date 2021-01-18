def selSort(nums):

  n =len(nums)
  for bottom in range(n-1):

    mp=bottom
    for i in range(bottom+1,n):
      if nums[i]<nums [mp]:
        mp=i

    nums[bottom],nums[mp]=nums[mp],nums[bottom]    

sort_list=[55,25,78,2,17,98,13,5]

selSort(sort_list)
