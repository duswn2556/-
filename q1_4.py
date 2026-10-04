n,k= [int(x) for x in input('').split()] #배열 크기, 최대 교체 횟수
a = [int(x) for x in input('').split()]
b = [int(x) for x in input('').split()]

a.sort() #오름차순
b.sort(reverse=True) #내림차순

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))