"""
Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64 Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
"""

list1 = [12, -7, 5, 64, -14]
for num1 in list1:
  if num1 > 0:
    print(num1, end=" ")

print("\n")

list2 = [12, 14, -95, 3]
for num2 in list2:
  if num2 > 0:
    print(num2, end=" ")
