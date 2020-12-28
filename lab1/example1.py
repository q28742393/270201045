def sum_of_a_nested_list(x):
   if not isinstance(x, list):
     return x
   else:
     sum = 0
     for a in x:
        sum += sum_of_a_nested_list(a)
     return sum


print(sum_of_a_nested_list([3, 12, 76, [4, 56, 43], [2, 8], 81, 75]))