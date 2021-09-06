from bisect import bisect


# custom bisect 
def binary_search_target(nums: list, target: float) -> int:
    start = 0
    end = len(nums) - 1
    

    while start <= end:
        mid = (end + start) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1

    return -1


def binarySearchLeft(nums: list, target: float) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


def binarySearchRight(nums: list, target:float) -> int:
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2

        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return right




print(binary_search_target([1,2,3,3,4,5,6], 3))
assert(binarySearchLeft([1,2,3,3,4,5], 3) == 2)
assert(binarySearchRight([1,2,3,3,4,5], 3) == 3)