# Time: O(n2), Space: O(1)
def find_target_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] + arr[j] == target):
                return True


    return False


# Time: O(n), Space: O(n)
def find_target_sum_best(arr, target):
   
    seen = {}


    for i in range(len(arr)):
        req = target-arr[i]


        if(seen.get(req, False)):
            return True
        else:
            seen[arr[i]] = True
   
    return False




# Time: O(n log n), Space: O(1) - Two pointer approch
def find_target_sum(arr, target):
   
    arr = sorted(arr)
    i=0
    j = len(arr)-1


    while(i<j):
        s= arr[i] + arr[j]
        print(s, arr[i], arr[j])
        if(s == target):
            return True
        elif(s > target):
            j -= 1
        elif(s < target):
            i += 1
       
    return False


arr = [0, -1, 2, -3, 1]
target = -2
#arr = [0, 4, 2, 5, 1]
#target = 6
print(find_target_sum(arr, target))


