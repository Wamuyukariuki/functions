def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * discount_percent / 100
        selling_price = price - discount

    else:
        selling_price = price

    return selling_price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    selling_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        print(f"The selling price after applying a {discount_percent:.0f}% discount is ksh{selling_price:.2f}.")
    else:
        print(f"The original price of ksh{original_price:.2f} remains unchanged.")
except ValueError:
    print("Invalid input! Please enter numbers only.")
