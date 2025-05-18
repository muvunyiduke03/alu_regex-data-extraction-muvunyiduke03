# Regex Data Extraction Tool

This Is a python project that provides a utility class to extract common data types such as emails and phone numbers using regular expresssions.

## Features

The regular expressions extracts:
    - Email addresses
    - Phone numbers
    - Time (24-hour Format)
    - URLs(HTTP and HTTPS)
    - Credit Card numbers (16-digit format)


## How it works

The "extract_data" class uses the python module "re" to search for patterns in the given string.
Each method target certain type of data using regular expressions.

## How to use

### 1. Clone the repository
### 2. Provide input

Use any string of text that contains data you want to extract. This include a text with:
     - Email addresses
    - Phone numbers
    - Time (24-hour Format)
    - URLs(HTTP and HTTPS)
    - Credit Card numbers (16-digit format)

### 3. Instantiate the class and call the methods

```python
from extract_data import extract_data

text = """
Email: support@MNHD.com
Phone US: (123) 456-7890
Phone Rwanda: +250 788 123 456
Opening hour: 09:00
Website: https://www.MNHD.com
Credit Card: 1234-5678-9101-1121.
"""

extractor = extract_data(text)
results = extractor.extract_all()

for key, value in results.items():
    print(f"{key}: {value}")
```
## Output
```
Extracted Data:
emails: ['support@MNHD.com']
Phone Numbers: ['(123) 456-7890', '+250 788 123 456']
Hours: ['09:00']
URLs: ['https://www.MNHD.com']
Credit Cards: ['1234-5678-9101-1121']
```

## Contributions

Pull requests and any improvements on the code are welcome. Feel free to fork the repository and submit a PR. 

