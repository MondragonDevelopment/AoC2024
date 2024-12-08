from collections import defaultdict

with open("data/Day1.txt") as data:
        lines = data.read().strip().split("\n")
        
i = 0
nums1, nums2 = [], []
count1, count2 = defaultdict(list), defaultdict(list)

for line in lines:
    num1, num2 = map(int, line.split())
    count1[num1].append(num1)
    count2[num2].append(num2)

for k in range(min(count1), max(count1) + 1):
     nums1.extend(count1[k])

for k in range(min(count2), max(count2) + 1):
     nums2.extend(count2[k])

j = 0
res = 0
sim = 0

while j < len(nums1):
    res += abs(nums1[j] - nums2[j])
    num = nums1[j]
    #print(num)
    sim += num * len(count2[num])
    j += 1

print(res, sim)
