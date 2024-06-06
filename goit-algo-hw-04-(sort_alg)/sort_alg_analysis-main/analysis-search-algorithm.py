from merge_sort_alg import merge_sort
from insertion_sort_alg import insertion_sort
import timeit
import random

def compare_sorting_method(list_size, num_trial):
    insertion_faster_count =0
    merge_faster_count =0
    tim_faster_count=0

    for i in range(num_trial):
        random_list = [random.randint(1, 1000) for _ in range(list_size)]

        exc_times = timeit.repeat(lambda: insertion_sort(random_list.copy()), number=100, repeat=5)
        exc_time_ins = min(exc_times)

        exc_times = timeit.repeat(lambda: merge_sort(random_list.copy()), number=100, repeat=5)
        exc_time_mrg = min(exc_times)

        exc_times = timeit.repeat(lambda: sorted(random_list.copy()), number=100, repeat=5)
        exc_time_timsort = min(exc_times)

        if exc_time_ins < exc_time_mrg and exc_time_ins < exc_time_timsort:
            insertion_faster_count += 1
           
        elif exc_time_mrg < exc_time_ins and exc_time_mrg < exc_time_timsort:
            merge_faster_count += 1
           
        else:
            tim_faster_count += 1

    if tim_faster_count>merge_faster_count and tim_faster_count>insertion_faster_count:
        print(f"For list of {list_size}-digit and {num_trial} trials Tim alg was faster {tim_faster_count} times")
    elif merge_faster_count>tim_faster_count and merge_faster_count>insertion_faster_count:
         print(f"For list of {list_size}-digit and {num_trial} trials Merge alg was faster {merge_faster_count} times")
    else:
        print(f"For list of {list_size}-digit and {num_trial} trials Insertion alg was faster {merge_faster_count} times")

compare_sorting_method(10, 100)
compare_sorting_method(10, 1000)
compare_sorting_method(10, 10000)

compare_sorting_method(100, 100)
compare_sorting_method(100, 1000)
compare_sorting_method(100, 10000)

