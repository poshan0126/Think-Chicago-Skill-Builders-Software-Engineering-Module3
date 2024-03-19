import re

class EcommerceOperations:
    @staticmethod
    def tag_products(descriptions):
        tags = {
            'Electronics': ['smartphone', 'screen', 'memory'],
            'Apparel': ['t-shirt', 'cotton', 'size'],
            'Home & Kitchen': ['stainless', 'kitchen', 'knife']
        }
        product_tags = []
        for description in descriptions:
            for tag, keywords in tags.items():
                if any(keyword.lower() in description.lower() for keyword in keywords):
                    product_tags.append((description, tag))
                    break
        return product_tags

    @staticmethod
    def standardize_prices(price_data):
        # Regex pattern to find various price formats
        pattern = r"\$?(\d+\.\d{2}) ?USD|\$"
        # Function to replace found patterns with 'USD XX.XX'
        def repl(match):
            return f"USD {match.group(1)}"
        standardized_data = re.sub(pattern, repl, price_data, flags=re.IGNORECASE)
        return standardized_data

# Task 1: Product Description Keyword Tagging
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
tagged_products = EcommerceOperations.tag_products(descriptions)
print("Tagged Products:")
for description, tag in tagged_products:
    print(f"{description}: {tag}")

# Task 2: Pricing Format Standardization
price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
standardized_prices = EcommerceOperations.standardize_prices(price_data)
print("\nStandardized Prices:\n", standardized_prices)
