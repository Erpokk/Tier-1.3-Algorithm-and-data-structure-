




def merge_two_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

def merge_k_lists(lists):
    if not lists:
        return []
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged.append(merge_two_lists(lists[i], lists[i + 1]))
            else:
                merged.append(lists[i])
        lists = merged
    return lists[0]

print(merge_k_lists([[1,2,5],[5,9,15],[16,18,19]]))