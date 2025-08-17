# Week 3 Assignment
#This program calculates the final price of an item after applying a discount using the function calculate_discount(price, discount_percent)

# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
if __name__ == "__main__":
    # Prompt the user for input
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Call the function
        final_price = calculate_discount(price, discount_percent)

        # Print result
        if discount_percent >= 20:
            print(f"The final price after {discount_percent}% discount is: {final_price}")
        else:
            print(f"No discount applied. The price remains: {final_price}")
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")
