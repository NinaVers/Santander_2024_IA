import re

def validate_credit_card_brand(card_number):
    """
    Validates the credit card brand based on the card number format using regex and detailed rules.

    Args:
        card_number (str): The credit card number to validate.

    Returns:
        str: The name of the credit card brand if identified, or "Unknown" if invalid.
    """
    # Remove spaces
    card_number = card_number.replace(" ", "")

    # Regex-based validation
    if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', card_number):
        return "Visa"
    elif re.match(r'^5[1-5][0-9]{14}$', card_number):
        return "MasterCard"
    elif re.match(r'^3[47][0-9]{13}$', card_number):
        return "American Express"
    elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', card_number):
        return "Discover"
    elif re.match(r'^(?:2131|1800|35\d{3})\d{11}$', card_number):
        return "JCB"
    elif re.match(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$', card_number):
        return "Diners Club"
    elif re.match(r'^8699[0-9]{11}$', card_number):
        return "Voyager"
    elif re.match(r'^38[0-9]{11,16}$', card_number):
        return "HiperCard"
    elif re.match(r'^50[0-9]{14}$', card_number):
        return "Aura"

    # Detailed rule-based validation
    card_number = str(card_number)
    if len(card_number) == 15 and card_number[:4] in ["2014", "2149"]:
        return "enRoute"
    elif len(card_number) in [16, 19] and 3528 <= int(card_number[:4]) <= 3589:
        return "JCB"  # Additional JCB logic

    return "Unknown"


def main():
    """
    Main function to provide a user-friendly interface for validating credit card brands.
    """
    print("Welcome to the Credit Card Brand Validator!")
    print("Please enter your credit card number below (spaces are allowed):")
    
    card_number = input("Credit Card Number: ")
    brand = validate_credit_card_brand(card_number)
    
    if brand == "Unknown":
        print("Sorry, we could not determine the brand of your card. Please check the number.")
    else:
        print(f"The credit card brand is: {brand}.")

# Run the program
if __name__ == "__main__":
    main()
