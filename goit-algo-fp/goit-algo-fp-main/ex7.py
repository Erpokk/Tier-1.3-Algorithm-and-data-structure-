import random
import matplotlib.pyplot as plt

# Теоретичні ймовірності (в відсотках)
var_pro = {
    '2': 2.78,
    '3': 5.56,
    '4': 8.33,
    '5': 11.11,
    '6': 13.89,
    '7': 16.67,
    '8': 13.89,
    '9': 11.11,
    '10': 8.33,
    '11': 5.56,
    '12': 2.78,  
}


def simple_monte(rep):
    var = {str(i): 0 for i in range(2, 13)}

    for _ in range(rep):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        total = first + second
        var[str(total)] += 1

    for key in var:
        var[key] = (var[key] / rep) * 100 
    return var

def compare_probabilities(theoretical, empirical, qty):
    print("Сума\tТеоретична ймовірність (%)\tЕмпірична ймовірність (%)")
    print("---------------------------------------------------------")
    for key in theoretical:
        print(f"{key}\t{theoretical[key]:.2f}\t\t\t{empirical[key]:.2f}")
    print(f"Для кількості кидків: {qty} кидків")
    
try_qty = 1000
empirical_probs = simple_monte(try_qty)
compare_probabilities(var_pro, empirical_probs, try_qty)


keys = list(var_pro.keys())
theoretical_values = list(var_pro.values())
empirical_values = [empirical_probs[key] for key in keys]
inaccuracy = [abs(theoretical_values[i] - empirical_values[i]) for i in range(len(keys))]
fig, ax = plt.subplots()

bar_width = 0.2
index = range(len(keys))

bar1 = plt.bar(index, theoretical_values, bar_width, label='Теоретичні')
bar2 = plt.bar([i + bar_width for i in index], empirical_values, bar_width, label='Емпіричні')
bar3 = plt.bar([i + 2 * bar_width for i in index], inaccuracy, bar_width, label='Невідповідність')
for i, v in enumerate(inaccuracy):
    ax.text(i + 2 * bar_width, v, str(round(v, 2)), ha='center', va='bottom', rotation=90, color='green')

plt.xlabel('Сума очок')
plt.ylabel('Ймовірність (%)')
plt.title(f'Порівняння теоретичних та емпіричних ймовірностей. \n Для {try_qty} кидків')
plt.xticks([i + bar_width / 2 for i in index], keys)
plt.legend()

plt.tight_layout()
plt.show()