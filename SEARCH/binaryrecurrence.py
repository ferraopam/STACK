def binarySearch(lst,l,h,key)
if l<=h:
    mid=(l+h)//2
    if lst[mid]==key:
        return True
    elif lst[mid]<key:
        binarySearch(lst,l+1,h,key)
    else:
        binarySearch(lst,l,h-1,key)
    return False
    