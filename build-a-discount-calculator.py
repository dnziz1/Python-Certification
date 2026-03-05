def apply_discount(price, discount):
    result = 0.0
    if (isinstance(price, int) or isinstance(price, float)) == False:
        return 'The price should be a number' 
    elif (isinstance(discount, int) or isinstance(discount, float)) == False:
        return 'The discount should be a number'

    if price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    
    result = price - (price * (discount/100))

    return result

result = apply_discount(200, 50)
print(result)
