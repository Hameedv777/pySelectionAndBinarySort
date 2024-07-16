def binary_Search(arr,target):
    low,high=0, len(arr)-1

    while low<=high:
        mid=(low+high)//2
        mid_Element=arr[mid]
        if mid_Element==target:
            return mid
        elif mid_Element<target:
            low=mid+1
        else:high=mid-1
    return -1
sorted_List=[1,2,3,4,5,6,7,8,9]
target_Element=2
result=binary_Search(sorted_List,target_Element)
if result!=-1:
    print(f"Target Elenmen{target_Element} found at index{result}")
else:
    print(f"Target element {target_Element}not found ")

