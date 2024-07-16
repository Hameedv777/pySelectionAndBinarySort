def selectio_Sort(arr):
    n=len(arr)
    for i in  range(n-1):
        #Assume current index is the minimum.
        min_Index=i
        #Find the index of the minimum elemet in the unsorted array
        for j in range(i+1,n):
            if arr[j]<arr[min_Index]:
                min_Index=j
        arr[i],arr[min_Index]=arr[min_Index],arr[i]
    #Swap the found minimum element with the first element.

    #Example usage:
my_List=[64,25,12,22,11]
selectio_Sort(my_List)
print("Soreted array is:",my_List)
    
    