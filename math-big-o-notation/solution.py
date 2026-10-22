def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return (True,i+1)
    return (False,n)


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    n=len(sorted_arr)
    left,right=0,n-1
    count=0
    while left<=right:
        count+=1
        mid=(left+right)>>1
        if (sorted_arr[mid]<target):
            left=mid+1
        elif (sorted_arr[mid]>target):
            right=mid-1
        else:
            return (True,count)
    return (False,count)
