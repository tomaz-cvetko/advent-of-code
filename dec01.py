import numpy as np

nums = np.loadtxt("input.txt", dtype=int)
nums.sort()
# print(nums)

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] > 2020:
            break

        for k in range(j+1, len(nums)): # this part was added for the second part
            sum = nums[i] + nums[j] + nums[k]
            if sum == 2020:
                print(nums[i]*nums[j]*nums[k], nums[i], nums[j], nums[k])
                exit()
            elif sum > 2020:
                break
            