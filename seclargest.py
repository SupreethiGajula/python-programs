n = int(input())
arr =list(map(int, input().split()))
for i in range(0,n):
    min = i
    for j in range(i+1,n):
        if (arr[min]>arr[j]):
            arr[min],arr[j]=arr[j],arr[min]
for i in range(0,n):
    print(arr[i])