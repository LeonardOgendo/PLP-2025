# Discount Calculator Program

def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount.
    Apply discount only if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price  # Return original price if discount is less than 20%


# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Display result
if discount >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
