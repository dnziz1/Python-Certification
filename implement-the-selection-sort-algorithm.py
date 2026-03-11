def selection_sort(numbers: list):
    for nums in range(len(numbers)):
        min_index = nums
        for num in range(nums + 1, len(numbers)):
            if numbers[num] < numbers[min_index]:
                min_index = num

        if min_index != nums:
            numbers[nums], numbers[min_index] = numbers[min_index], numbers[nums]

    return numbers
