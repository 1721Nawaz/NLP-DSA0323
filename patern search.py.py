import re
text = """
John Smith's email is john.smith@example.com.
You can also reach him at john_smith123@gmail.com.
His phone numbers are 123-456-7890 and (987) 654-3210.
"""
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Emails found:", emails)
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phone_numbers = re.findall(phone_pattern, text)
print("Phone numbers found:", phone_numbers)
search_term = "john_smith123@gmail.com"
if re.search(search_term, text):
    print(f"The email '{search_term}' was found in the text.")
else:
    print(f"The email '{search_term}' was not found in the text.")

