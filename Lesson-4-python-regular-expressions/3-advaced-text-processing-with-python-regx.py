import re

class AdvancedTextProcessor:
    @staticmethod
    def extract_value_by_key(text, key):
        # Constructing regex pattern to match 'Key: Value'
        pattern = rf"{key}: ([^;]+)"
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        return None

    @staticmethod
    def validate_urls(urls):
        valid_urls = []
        invalid_urls = []
        # Regex pattern for validating URLs
        pattern = r"^(http://|https://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        for url in urls:
            if re.match(pattern, url):
                valid_urls.append(url)
            else:
                invalid_urls.append(url)
        return valid_urls, invalid_urls

# Task 1: Advanced Data Extraction
text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
extracted_occupation = AdvancedTextProcessor.extract_value_by_key(text, "Occupation")
print("Extracted Occupation:", extracted_occupation)

# Task 2: URL Validator
urls = ["https://example.com", "www.example.com", "http://test.com"]
valid_urls, invalid_urls = AdvancedTextProcessor.validate_urls(urls)
print("Valid URLs:", valid_urls)
print("Invalid URLs:", invalid_urls)
