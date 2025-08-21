"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
import os
os.system("clear")
nums = [1, 3, 5, 3]
goal = 8

def first_sum(nums, goal):
  print("Start")
  for i in range(len(nums) - 1):
    # while j < len(nums)-1:
    #   if nums[i] + nums[j] == goal:
    #     return [i, j]
    #   j += 1
    for j in range(i + 1, len(nums) - 1):
      if nums[i] + nums[j] == goal:
        return [i, j]
  
  return None

print(first_sum(nums, goal))
