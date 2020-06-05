arr=[64,33,22,1,33]

# didnt work because range function doesnt chop a list by the range you put in
def selection_sort_my(arr):
    n=len(arr)

    for i in range(n):
        arr[i] = min(arr.range[i,n])

selection_sort_my(arr)
print(arr)

arr2=[64,33,22,1,33]

# this one however, did work
def selection_sort_tut(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i+1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j

        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]

selection_sort_tut(arr2)
print(arr2)
