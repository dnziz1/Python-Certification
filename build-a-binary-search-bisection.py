def square_root_bisection(value, tolerance=0.01, max_iteration=100):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if value == 0 or value == 1:
        print(f'The square root of {value} is {value}')
        return value

    if value > 1:
        low = 1
        high = value
    else: 
        low = value
        high = 1

    for iteration in range(max_iteration):
        mid = (low + high) / 2
        
        if (high - low) <= tolerance:
            root = (low + high) / 2
            print(f'The square root of {value} is approximately {root}')
            return root
        
        value_mid = mid * mid
        
        if value_mid < value:
            low = mid
        else:
            high = mid

    print(f'Failed to converge within {max_iteration} iterations')
    return None
