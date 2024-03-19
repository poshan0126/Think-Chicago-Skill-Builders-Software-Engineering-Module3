import re

class RegexMaster:
    @staticmethod
    def extract_emails(text):
        # Corrected regex pattern to capture email addresses effectively and handle different cases
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(pattern, text, re.IGNORECASE)  # Added re.IGNORECASE to handle different cases
        return emails

    @staticmethod
    def analyze_log(log_data):
        # Reformat the date from 'MM-DD-YYYY' to 'YYYY-MM-DD'
        reformatted_log = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", log_data)
        # Replace all instances of '@username' with '[ANONYMIZED USER]'
        anonymized_log = re.sub(r"@\w+", "[ANONYMIZED USER]", reformatted_log)
        return anonymized_log

# Task 1: Code Correction - Extract Email Addresses
text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
regex_master = RegexMaster()
extracted_emails = regex_master.extract_emails(text)
print("Extracted Emails:", extracted_emails)

# Task 2: Log File Analysis - Reformat Date and Anonymize Usernames
log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."
analyzed_log = regex_master.analyze_log(log_data)
print("Analyzed Log Data:\n", analyzed_log)
