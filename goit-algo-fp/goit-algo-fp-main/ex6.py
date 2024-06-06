class Item:
    def __init__(self, name,  cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories/cost
        

    def __str__(self) -> str:
        return f"Name {self.name}, cost {self.cost}, cal {self.calories}"




def greedy_algorithm (items, wallet):
    list_of_Items =[]
    for key, char in items.items(): 
        list_of_Items.append(Item(key, char['cost'], char['calories']))
    list_of_Items.sort(key = lambda x: x.ratio, reverse = True)
    total_cal = 0
    total_price = 0
    list_of_prod = []
    for item in list_of_Items:
        if wallet >= item.cost:
            wallet -= item.cost
            total_cal += item.calories
            total_price += item.cost
            list_of_prod.append(item)
    for i in range(len(list_of_prod)):
        print(list_of_prod[i])
    return f"Total cal {total_cal} , Money wasted: {total_price}"

def dynamic_prog(items, wallet):
    list_of_Items =[]
    for key, char in items.items(): 
        list_of_Items.append(Item(key, char['cost'], char['calories']))

    n = len(list_of_Items)

    dp = [[0 for _ in range(wallet + 1)] for _ in range(n + 1)]
    for i in range(1, n+1):
        for w in range(1, wallet+1):
            if list_of_Items[i - 1].cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - list_of_Items[i - 1].cost] + list_of_Items[i - 1].calories)
            else:
                dp[i][w] = dp[i - 1][w]


    total_cal = dp[n][wallet]
    total_price = 0
    w = wallet
    list_of_prod = []

    for i in range(n, 0, -1):
        if total_cal <= 0:
            break
        if total_cal != dp[i - 1][w]:
            list_of_prod.append(list_of_Items[i - 1])
            total_price += list_of_Items[i - 1].cost
            total_cal -= list_of_Items[i - 1].calories
            w -= list_of_Items[i - 1].cost
    
    list_of_prod.reverse()
    for item in list_of_prod:
        print(item)
    
    return f"Total calories: {dp[n][wallet]}, Money spent: {total_price}"

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 100))
print(dynamic_prog(items, 100))

