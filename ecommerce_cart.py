def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty"
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total *= 0.9  # 10% discount
    return total

if __name__ == "__main__":
    cart_items = {}
    n = int(input("Enter number of items in cart: "))
    for _ in range(n):
        item = input("Enter item name: ")
        price = float(input(f"Enter price for {item}: "))
        cart_items[item] = price

    print("Total Price:", calculate_total(cart_items))
