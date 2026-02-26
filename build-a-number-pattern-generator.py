def number_pattern(n):
    
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n > 0:
        num = ' '.join(str(i) for i in range(1,n+1))
        return num 
    else:
        return 'Argument must be an integer greater than 0.'

print(number_pattern(12))
