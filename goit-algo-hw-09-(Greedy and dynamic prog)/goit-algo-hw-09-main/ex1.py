import timeit

def find_coins_greedy(coins, sum):
    dict1 = {
    '50': 0,
    '25': 0,
    '10': 0,
    '5': 0,
    '2': 0,
    '1': 0
    }
    for coin in coins:
        while sum >= coin:
            dict1[str(coin)] += 1 
            sum -= coin

    del_list = [key for key, val in dict1.items() if val == 0]
    for key in del_list:
        del dict1[key]   
    
    return dict1



def DP_find_coin (coins, amount):
    dp=[amount+1] *(amount+1)
    dp[0]= 0
    coin_used = [-1] * (amount+1)

    for a in range (1, amount+1):
        for c in coins:
            if a  - c >=0:
                if a-c >= 0 and dp[a] > 1 + dp[a-c]:
                    dp[a] = 1+ dp[a-c]
                    coin_used[a] = c 


    if dp[amount] == amount + 1:
        return - 1 

    result = {}
    cur_am = amount
    while cur_am > 0:
        coin = coin_used[cur_am]
        if coin in result:
            result[coin] +=1
        else:
            result[coin] = 1
        cur_am -= coin

    return result

def DP_find_coin_wo_dict(coins, amount):
    dp = [amount + 1] * (amount + 1)  
    dp[0] = 0  

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1




coins = [50,25,10,5,2,1]
amount = 10000

exc_time_DP = timeit.repeat(lambda: DP_find_coin(coins, amount), number=10, repeat=50)
print(sum(exc_time_DP)/len(exc_time_DP))
exc_time_GR = timeit.repeat(lambda: find_coins_greedy(coins, amount), number=10, repeat=50)
print(sum(exc_time_GR)/len(exc_time_GR))
exc_time_DP_wo = timeit.repeat(lambda: DP_find_coin_wo_dict(coins, amount), number=10, repeat=50)
print(sum(exc_time_DP_wo)/len(exc_time_DP_wo))


print(DP_find_coin(coins, amount))
print(find_coins_greedy(coins, amount))

