n,m= [int(x) for x in input('').split()] #떡 개수, 필요한 떡 길이
heights=[int(x) for x in input('').split()] #떡 개별 높이

start=0
end=max(heights)
rslt=0

#이진탐색

while start<=end:
    total=0 #잘린 떡들의 길이 합
    mid = (start + end) // 2 #이진탐색: 중간값 설정

    for h in heights:
        if h > mid:
            total+=h-mid

    if total < m:
        end=mid-1
    else:
       rslt = mid
       start=mid+1

print(rslt) #절단기 높이의 최댓값