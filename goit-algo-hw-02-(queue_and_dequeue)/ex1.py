
from queue import Queue
from time import sleep
from random import uniform

# Створити чергу заявок
queue = Queue()
unique_counter = 0


def generate_request():
    global unique_counter
    unique_counter +=1
    id_request = unique_counter
    queue.put(id_request)
    print(f"Request № {id_request} has been added to queue ")
    sleep(uniform(0.5, 3.0))

def process_request():
    if queue.empty() == False:
        id_requst = queue.get()
        print(f"Request №{id_requst} in progress")
        sleep(uniform(0.5, 3.0))
        print(f"Request №{id_requst} has been successfully completed ")
    else:
        print("Queue is empty")

if __name__ == "__main__":
    while True:
        user_input = input("для виходу напишіть 'exit' або щоб продовжити введіть будь-що): ")
        if user_input.lower() == 'exit':
            print("Програма завершила роботу.")
            break
        generate_request()
        process_request()

