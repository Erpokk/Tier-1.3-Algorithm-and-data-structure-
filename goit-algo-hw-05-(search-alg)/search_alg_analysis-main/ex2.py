def bin_search(arr, x):
    iter = 0
    low = 0
    high = len(arr)-1
    mid = 0

    while low<=high:
        mid = (high+low)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
            
        else:
            return iter,arr[mid]
        iter +=1
    return (iter, arr[mid])

sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1,]
search_value = 10.0

iter_upper = bin_search(sorted_array, search_value)
print("Кількість ітерацій та верхня межа", iter_upper)
