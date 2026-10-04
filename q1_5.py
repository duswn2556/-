n,m= [int(x) for x in input('').split()]
heights=[int(x) for x in input('').split()]

start=0
end=max(heights)
rslt=0

while start<=end:
    total=0
    mid = (start + end) // 2

    for h in heights:
        if h > mid:
            total+=h-mid

    if total < m:
        end=mid-1
    else:
       rslt = mid
       start=mid+1

print(rslt)