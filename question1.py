nums = input().split()
nums = [int(num) for num in nums]

non_zero_count = 0
for num in nums:
    if num != 0:
        non_zero_count += 1

i = 0
for num in nums:
    if num != 0:
        nums[i] = num
        i += 1

while i < len(nums):
    nums[i] = 0
    i += 1

print(nums)
