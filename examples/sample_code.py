def calculate_discount(price, discount_percentage):
    final_price = price - (price * discount_percentage / 100)
    return final_price

def get_user_input():
    price = input("Enter price: ")
    discount = input("Enter discount: ")
    return calculate_discount(price, discount)

print("Final price is:", get_user_input())
