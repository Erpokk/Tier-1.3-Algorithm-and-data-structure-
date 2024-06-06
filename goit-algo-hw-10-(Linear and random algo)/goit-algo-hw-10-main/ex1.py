import pulp

model = pulp.LpProblem('Maximize production', pulp.LpMaximize)


Lemonade= pulp.LpVariable('Lemonade', lowBound=0, cat="Integer")
Fruit_juice= pulp.LpVariable('Fruit_juice', lowBound=0, cat="Integer")

max_water = 100
max_sugar = 50
max_lemon_juice = 30
max_fruit_juice = 40 

model += (2 * Lemonade + 1 * Fruit_juice <= max_water)
model += (1 * Lemonade <=   max_sugar)
model += (1 * Lemonade <= max_lemon_juice)
model += (2 * Fruit_juice <= max_fruit_juice)

model += Lemonade + Fruit_juice

model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість лимонаду: {Lemonade.varValue}")
print(f"Кількість фруктового соку: {Fruit_juice.varValue}")