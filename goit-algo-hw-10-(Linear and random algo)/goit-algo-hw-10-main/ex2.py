import scipy.integrate as spi 
import random
def f(x):
    return x**2

def monte(f, a, b, num_samples):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a,b)
        total += f(x)
    avg_val = total / num_samples
    integral =(b-a)*avg_val
    return integral


def compare(a, b , qty, num_samples ):
    list1 = []
    for _ in range(qty):
        integral_value = monte(f, a, b, num_samples)
        result, error = spi.quad(f, a, b)
        dif = integral_value - result
        list1.append(dif)
    return f"На {qty} спроб середне відхиленяня {sum(list1)/qty} "

a = 0
b = 2 
num_samples = 100000  
qty = 100 

print(compare(a, b , qty, num_samples))
