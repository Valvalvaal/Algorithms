n = int(input())
a = [int(i) for i in input().split(" ")]

curr_max = 1
ov_max = 1

for i in range(len(a)-1):
    if a[i+1] >= a[i]:
        curr_max += 1
        if curr_max > ov_max:
            ov_max = curr_max
    else:
        curr_max = 1

print(ov_max)