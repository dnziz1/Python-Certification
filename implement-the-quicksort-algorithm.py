def quick_sort(numbers):
    if not numbers:
        return []
    
    if len(numbers) <= 1:
        return numbers

    pivot_value = numbers[-1]
    less_side = []
    greater_side = []
    equal_side = []

    for num in numbers:
        if num < pivot_value:
            less_side.append(num)
        elif num == pivot_value:
            equal_side.append(num)
        else:
            greater_side.append(num)

    return quick_sort(less_side) + equal_side + quick_sort(greater_side)

print(quick_sort([20, 3, 14, 1, 5]))
