import random

def radix_sort(nums, base=10):
    result_list = []
    power = 0
    while nums:
        bins = [[] for _ in range(base)]
        for x in nums:
            bins[x // base**power % base].append(x)
        nums = []
        for bin in bins:
            for x in bin:
                if x < base**(power+1):
                    result_list.append(x)
                else:
                    nums.append(x)
        power += 1
    return result_list

//check
nums = [random.randint(0, 1000) for _ in range(15)]
print(nums)
print()
nums = radix_sort(nums)
print(nums)
print()