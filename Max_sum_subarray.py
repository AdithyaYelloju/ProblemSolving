# Kadane’s algorithm
def max_sum_subarray(array):
    current_sum = 0
    max_sum = array[0]
    start = 0
    end = 0
    poi = 0
    for i in range(len(array)):
        current_sum += array[i]

        if(current_sum > max_sum):
            max_sum = current_sum
            start = poi
            end = i
       
        if(current_sum < 0):
            current_sum = 0
            poi = i+1
       
    return max_sum,array[start:end+1],start,end


array = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
print(max_sum_subarray(array)) # Sum: 7, [2,3,1,-2,-3,6]
