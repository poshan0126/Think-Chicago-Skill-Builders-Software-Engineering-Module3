import re
import os

class EmailExtractor:
    @staticmethod
    def extract_emails(filename):
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        unique_emails = set()
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    emails = re.findall(email_pattern, line)
                    unique_emails.update(emails)
            return list(unique_emails)
        except FileNotFoundError:
            print(f"The file {filename} was not found.")
            return []

# Additional classes for other regex-powered tasks can be defined here
# class OtherTask:
#     @staticmethod
#     def perform_task():
#         pass

# Example usage:
# Note: Replace 'contacts.txt' with the path to your actual text file containing email addresses.
filename = 'contacts.txt'
if os.path.exists(filename):
    emails = EmailExtractor.extract_emails(filename)
    print("Extracted Email Addresses:")
    for email in emails:
        print(email)
else:
    print(f"The file {filename} does not exist. Please provide a valid file path.")
