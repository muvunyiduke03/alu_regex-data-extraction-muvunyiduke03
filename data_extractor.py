import re

class extract_data:
    """This class extracts data from a given text"""

    def __init__(self, text):
        self.text = text
    
    
    def extract_email(self):
        """To extract email addresses"""

        pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        return re.findall(pattern, self.text)
    
    def extract_phoneNumbers(self):
        """To extract phone numbers in US(+1) and Rwandan(+250) formats"""
        pattern = r'(?:(?:\+250|0)?7[2389]\d{1}[\s.-]?\d{3}[\s.-]?\d{3})|(?:\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})'
        return re.findall(pattern, self.text)


    def extract_24hr_time(self):
        """To extract 24-hour format time"""
        pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d\b'
        return re.findall(pattern, self.text)
    
    def extract_urls(self):
        """To extract URLs"""
        pattern = r'\bhttps?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?\b'
        return re.findall(pattern, self.text)
    
    def extract_creditCard(self):
        """To extract credit card numbers"""
        pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
        return re.findall(pattern, self.text)
    
    def extract_all(self):
        """To extract all data"""
        return {
            "emails": self.extract_email(),
            "Phone Numbers (+250, +1)": self.extract_phoneNumbers(),
            "Hours": self.extract_24hr_time(),
            "URLs": self.extract_urls(),
            "Credit Cards": self.extract_creditCard(),
        }
    
if __name__ == "__main__":
    text = """
    Email: support@MNHD.com
    Phone Rwanda: +250 788-537-967
    International Phone: +1 234-567-8900
    Opening hour: 09:00 
    Website: https://www.MNHD.com
    Credit Card: 1234-5678-9101-1121.
    bad email: hello@.com
    """

    extractor = extract_data(text)
    results = extractor.extract_all()
    
    print("Extracted Data:")
    for key, value in results.items():
        print(f"{key}: {value}")
