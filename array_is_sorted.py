arr = [3,4,5,1,2]
def arr_is_sorted(arr):
    cnt=0
    for i in range(len(arr)):
        if (arr[i]>=arr[i-1]):
            cnt+=1
    return cnt==0 or cnt==1 and arr[-1]<=arr[0] 

    
print(arr_is_sorted(arr))