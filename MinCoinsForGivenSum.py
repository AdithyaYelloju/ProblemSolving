def find_min_coins(coins, n, sum, dp):
    print(sum, dp)

    if(sum == 0):
        return 0

    if dp[sum] != -1:
        return dp[sum]
    
    result = float('inf')

    for i in range(n):
        if(coins[i] <= sum):
            sub_result = find_min_coins(coins, n, sum - coins[i], dp)

            if(sub_result != float('inf') and sub_result + 1 < result):
                result = sub_result + 1

    dp[sum] = result

    return result


def get_min_coins(coins, n, sum):

    dp = [-1] * (sum + 1)

    print(f'dp: {dp}, length: {len(dp)}')

    return find_min_coins(coins, n, sum, dp)


#coins = [9, 6, 5, 1]
#sum = 19
coins = [4,6,2]
n = len(coins)
sum = 5
output =  get_min_coins(coins, n, sum)
print(0 if output == float('inf') else output )
