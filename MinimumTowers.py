# Find minimum number of towers - Zeta 1st round

'''
2) There are N houses in a city. Houses are located in a single line at a particular distance  from origin. We have to place the antennas on the houses. 
The range of antennas is a K unit. Find out the minimum number of antennas required so that each house is in range of at-least one antenna.

For eg : 2 , 4, 5, 6,9 ,11, 15  , k = 2
Number of antennas required : 3

'''

def solve(houses, range):
    
    number_of_towers = 0
    i = 0
    n = len(houses)
    location = 0

    while(i<n):
        number_of_towers += 1

        location = houses[i]+ range

        while(i<n and houses[i] <= location):
            i += 1

        i -= 1

        location = houses[i]+ range

        while(i<n and houses[i] <= location):
            i += 1
    
    return number_of_towers


#houses = [1,2,3,4,5]
#k = 1 #-> 2
#houses = [ 2, 4, 5, 6, 7, 9, 11, 12]
#k = 2 #3
houses = [2 , 4, 5, 6,9 ,11, 15]
k = 2 #3

print(solve(houses, k))
