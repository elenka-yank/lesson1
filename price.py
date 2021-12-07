def discounted(price, discount, max_discount = 50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 70:
        raise ValueError('Максимальная скидка не может быть больше 70%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    
    return price_with_discount


print(discounted(100, 40))
print('Hello world')