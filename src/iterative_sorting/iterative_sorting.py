# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr


# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#     # for iterable in ~100
#     for i in range(len(arr)):
#         # for iterable2 in 100-iterable-1
#         for j in range(0,len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
        

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr