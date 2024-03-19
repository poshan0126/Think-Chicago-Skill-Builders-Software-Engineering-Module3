import re

class EmailExtractor:
    def __init__(self, text, excluded_domain="exclude.com"):
        self.text = text
        self.excluded_domain = excluded_domain

    def extract_emails(self):
        # Regex pattern to match email addresses
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        # Finding all emails
        all_emails = re.findall(pattern, self.text, re.IGNORECASE)
        # Filtering out emails from the excluded domain
        filtered_emails = [email for email in all_emails if not email.endswith(self.excluded_domain)]
        return filtered_emails

# Example usage
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
email_extractor = EmailExtractor(text)
extracted_emails = email_extractor.extract_emails()
print("Extracted Emails:", extracted_emails)
