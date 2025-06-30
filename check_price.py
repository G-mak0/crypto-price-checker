# Define a function to check the price against a user-defined threshold
def check_price(current_price, threshold):
    if current_price > threshold:
        return "💡 Current price is above your alert threshold. You might consider selling."
    elif current_price < threshold:
        return "📉 Current price is below your threshold. Might be a buying opportunity."
    else:
        return "⚖️ Current price is exactly equal to your threshold."


# Get user input from the terminal
price = float(input("Enter the current crypto price (e.g. 62800): "))
limit = float(input("Enter your price alert threshold: "))

# Use the function to get the analysis
result = check_price(price, limit)

# Print the result
print(result)
