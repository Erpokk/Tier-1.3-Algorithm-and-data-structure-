import timeit
from KMP_alg import kmp_search
from BM_alg import boyer_moore_search
from RB_alg import rabin_karp_search

def compare_search_method(cmb_lines, num_trials, *patterns):
    for pattern in patterns:
        KMP_faster_count =0
        BM_faster_count =0
        RK_faster_count=0
        for _ in range(num_trials):
            exc_times = timeit.repeat(lambda: boyer_moore_search(cmb_lines, pattern), number=10, repeat=5, )
            exc_BM = min(exc_times)

            exc_times = timeit.repeat(lambda: kmp_search(cmb_lines, pattern), number=10, repeat=5, )
            exc_KMP = min(exc_times)

            exc_times = timeit.repeat(lambda: rabin_karp_search(cmb_lines, pattern), number=10, repeat=5, )
            exc_RK = min(exc_times)

            if exc_RK < exc_BM and exc_RK < exc_KMP:
                RK_faster_count += 1
            
            elif exc_KMP < exc_RK and exc_KMP< exc_BM:
                KMP_faster_count += 1
            
            else:
                BM_faster_count += 1
        print(f'KMP was fater {KMP_faster_count} times , BM was fater {BM_faster_count} times, RK was fater {RK_faster_count} times. For pattern {pattern}')
