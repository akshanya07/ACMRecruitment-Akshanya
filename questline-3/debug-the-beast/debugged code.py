# Program: Find the second largest number in a list

def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second = float(-inf)
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    if second != float(-inf):
        return second
    else:
        return None



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

result = second_largest(arr)
if result is None:
    print("second largest DNE")
else:
    print("second largest is", result)