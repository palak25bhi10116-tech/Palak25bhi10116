# --- Currency Converter Project ---
# Based on the required modular structure:
# 1. Data/Rates Module
# 2. Core Logic/Converter Module
# 3. Main/Interface Module

# --- 1. Data/Rates Module ---
# This dictionary simulates fetching real-time rates.
# The values represent how much 1 INR is worth in the target currency.
def get_exchange_rates_data():
    """
    Provides a dictionary of fixed exchange rates based on INR.
    (This simulates an API call for simplicity.)
    """
    print("Loading fixed exchange rates...")
    
    # Rates are approximate and fixed for the project simplicity.
    # 1 INR = [Value] Target Currency
    return {
        "USD": 0.012,     # United States Dollar
        "EUR": 0.011,     # Euro
        "GBP": 0.0095,    # British Pound
        "JPY": 1.78,      # Japanese Yen
        "AED": 0.044,     # UAE Dirham
        "INR": 1.0        # Indian Rupee (for consistency check)
    }

# --- 2. Core Logic/Converter Module ---
def convert_currency(amount_in_inr, target_currency_code, rates_dictionary):
    """
    Calculates the converted amount based on the provided rates.
    
    Args:
        amount_in_inr (float): The amount of Indian Rupees to convert.
        target_currency_code (str): The code of the currency to convert to.
        rates_dictionary (dict): The current exchange rates.
        
    Returns:
        float or None: The converted amount, or None if the currency code is invalid.
    """
    
    # Check if the desired currency is in our list of rates
    if target_currency_code in rates_dictionary:
        # Get the conversion rate (e.g., rate for USD)
        rate = rates_dictionary[target_currency_code]
        
        # Core Formula: Converted Amount = Input Amount * Rate
        converted_amount = amount_in_inr * rate
        
        return converted_amount
    else:
        # The currency code was not found
        return None

# --- 3. Main/Interface Module ---
def run_converter_interface():
    """
    Handles user interaction (input/output) and coordinates the other modules.
    """
    
    # 1. Get the exchange rates from the Data Module
    rates = get_exchange_rates_data()
    
    BASE_CURRENCY = "INR"
    
    print("\n💰--- INR Currency Converter ---💰")
    print(f"Base Currency: {BASE_CURRENCY}")
    
    # Display supported currencies
    supported_currencies = list(rates.keys())
    print("Supported Currencies:", ", ".join(supported_currencies))

    # --- INPUT PHASE ---
    
    # 1. Get Amount (with validation)
    while True:
        try:
            amount_input = input(f"Enter amount in {BASE_CURRENCY}: ")
            amount_in_inr = float(amount_input)
            
            if amount_in_inr <= 0:
                print("Error: Amount must be a positive number.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number (e.g., 500 or 10.50).")
            
    # 2. Get Target Currency (with validation)
    while True:
        target_currency = input("Enter Target Currency Code (e.g., USD): ").upper()
        
        if target_currency in rates:
            break
        print(f"Error: Invalid currency code. Please choose from: {', '.join(supported_currencies)}")

    # --- CONVERSION PHASE ---
    
    # Call the Core Logic Module
    result = convert_currency(amount_in_inr, target_currency, rates)

    # --- OUTPUT PHASE ---
    
    if result is not None:
        print("\n--- Conversion Result ---")
        # Display the result, formatted to two decimal places
        print(f"{amount_in_inr:,.2f} {BASE_CURRENCY} is equal to:")
        print(f"👉 {result:,.2f} {target_currency}")
        
        # Also display the rate used
        print(f"Rate Used: 1 {BASE_CURRENCY} = {rates[target_currency]:.4f} {target_currency}")
    else:
        # Should not happen if input validation is correct, but good to have.
        print(f"\nConversion failed. Check the currency code: {target_currency}")


# This line runs the main function when you execute the script.
if __name__ == "__main__":
    run_converter_interface()