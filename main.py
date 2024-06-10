def solution(n,k,Arr,Brr):
    uniqueD = set(Arr)
    if len(uniqueD) < k:
        return -1
    
    time = 0
    minTimeIndex = []
    count = 0
    lastD = None
    minTime = 0
    for i in range(k):
        index = Brr.index(min(Brr)) + count
        if Arr[index] == lastD:
            Brr.pop(index)
            count += 1
            k += 1
            pass
        else:
            lastD = Arr[index]
            minTimeIndex.append(index)
            minTime += Brr[index]
            Brr.pop(index)
            Arr.pop(index)
            count += 1
    
        
    return minTimeIndex, minTime
        

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,k = input().split(" ")
        Arr = input().split(" ")
        Brr = input().split(" ")
        for i in range(len(Arr)):
            Arr[i] = int(Arr[i])
        for i in range(len(Brr)):
            Brr[i] = int(Brr[i])
        result, minTime = solution(int(n),int(k),Arr,Brr)
        print(minTime)
    
    