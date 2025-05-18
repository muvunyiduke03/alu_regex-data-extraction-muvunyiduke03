import re

class extract_data:

    def __init__(self, text):
        self.text = text
    
    def extract_email(self):
        pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        return re.findall(pattern, self.text)
    
    def extract_phoneNumbers(self):
        pattern = r'\b(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b'
        return re.findall(pattern, self.text)
    
    def extract_24hr_time(self):
        pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d\b'
        return re.findall(pattern, self.text)
    
    def extract_urls(self):
        pattern = r'\bhttps?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?\b'
        return re.findall(pattern, self.text)
    
    def extract_creditCard(self):
        pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
        return re.findall(pattern, self.text)
    
    def extract_all(self):
        return {
            "emails": self.extract_email(),
            "Phone Numbers": self.extract_phoneNumbers(),
            "Hours": self.extract_24hr_time(),
            "URLs": self.extract_urls(),
            "Credit Cards": self.extract_creditCard(),
        }
    
if __name__ == "__main__":
    text = """
    Email: support@MNHD.com
    Phone: +250 788-0000
    Opening hour: 09:00 
    Website: https://www.MNHD.com
    Credit Card: 1234-5678-9101-1121.
    """

    extractor = extract_data(text)
    results = extractor.extract_all()
    
    print("Extracted Data:")
    for key, value in results.items():
        print(f"{key}: {value}")
