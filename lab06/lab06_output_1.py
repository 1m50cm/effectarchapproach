def calculate_total_price(product_prices, discount):
    total_price = 0
    for price in product_prices:
        if discount:
            total_price += price * 0.9  # 10% discount
        else:
            total_price += price
    return total_price


def add_tax(price, tax_rate):
    price *= (1 + tax_rate)
    return price

