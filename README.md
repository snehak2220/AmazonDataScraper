# AmazonDataScraper

## Description
A Python-based web scraping tool designed to extract product information from Amazon. This scraper collects data such as product names, prices, ratings, and reviews while respecting Amazon's robots.txt and implementing proper delays between requests.

## Features
- Scrapes product details from Amazon search results
- Extracts product names, prices, ratings, and reviews
- Saves data in CSV format
- Implements rate limiting to avoid overwhelming the server
- Uses proxy rotation for better reliability
- Handles pagination automatically

## Installation
1. Clone the repository
```bash
git clone https://github.com/snehak2220/AmazonDataScraper.git
```
2. Navigate to the project directory
```bash
cd AmazonDataScraper
```
3. Install the required dependencies
```bash
pip install -r requirements.txt
```
4. Run the scraper
```bash
python manage.py runserver
```
## Project Structure
AmazonDataScraper/
├── main.py              # Main script
├── config.py           # Configuration settings
├── scraper/
│   ├── __init__.py
│   ├── amazon.py       # Amazon scraping logic
│   └── utils.py        # Utility functions
├── requirements.txt    # Project dependencies
├── README.md
└── output/            # Scraped data storage
    └── scraped_data.csv

## Dependencies
- Python 3.8+
- BeautifulSoup4 4.9.3
- Requests 2.26.0
- Pandas 1.3.3
- Selenium 4.1.0
- ChromeDriver (for Selenium)

## Trae AI
Used 1 Reference

README.md 19-19

I'll create a complete README.md file with proper formatting and structure.

```markdown
# AmazonDataScraper

## Description
A Python-based web scraping tool designed to extract product information from Amazon. This scraper collects data such as product names, prices, ratings, and reviews while respecting Amazon's robots.txt and implementing proper delays between requests.

## Features
- Scrapes product details from Amazon search results
- Extracts product names, prices, ratings, and reviews
- Saves data in CSV format
- Implements rate limiting to avoid overwhelming the server
- Uses proxy rotation for better reliability
- Handles pagination automatically

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Output Format](#output-format)
- [Legal Notice](#legal-notice)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation
1. Clone the repository
```bash
git clone https://github.com/snehak2220/AmazonDataScraper.git
 ```
```

2. Navigate to the project directory
```bash
cd AmazonDataScraper
 ```

3. Create a virtual environment
```bash
python -m venv venv
 ```

4. Activate the virtual environment
```bash
.\venv\Scripts\activate
 ```

5. Install required dependencies
```bash
pip install -r requirements.txt
 ```

## Usage
1. Ensure your virtual environment is activated
2. Configure search parameters in config.py
3. Run the scraper:
```bash
python main.py
 ```

Example output:

```plaintext
Starting Amazon scraper...
Scraping page 1 of search results...
Found 20 products...
Saving data to CSV...
Scraping completed successfully!
 ```

## Project Structure
```plaintext
AmazonDataScraper/
├── main.py              # Main script
├── config.py           # Configuration settings
├── scraper/
│   ├── __init__.py
│   ├── amazon.py       # Amazon scraping logic
│   └── utils.py        # Utility functions
├── requirements.txt    # Project dependencies
├── README.md
└── output/            # Scraped data storage
    └── scraped_data.csv
 ```
```

## Dependencies
- Python 3.8+
- BeautifulSoup4 4.9.3
- Requests 2.26.0
- Pandas 1.3.3
- Selenium 4.1.0
- ChromeDriver (for Selenium)
## Configuration
In config.py , you can modify:

```python
SEARCH_KEYWORDS = ["laptop", "smartphone"]  # Items to search
MAX_PAGES = 5                              # Number of pages to scrape
DELAY_BETWEEN_REQUESTS = 2                 # Delay in seconds
OUTPUT_FORMAT = "csv"                      # Output format (csv/json)
 ```
```

## Output Format
The scraper generates a CSV file with the following columns:
 Column Description Product Name

Full product title Price

Current price in USD Rating

Product rating (0-5 stars) Reviews Count

Number of customer reviews URL

Product page URL ASIN

Amazon Standard Identification Number
## Legal Notice
⚠️ This tool is for educational purposes only. Users must:

- Review Amazon's robots.txt
- Comply with Amazon's Terms of Service
- Implement appropriate delays between requests
- Not use the data for commercial purposes without proper authorization
## Contributing
1. Fork the repository
2. Create a feature branch ( git checkout -b feature/AmazingFeature )
3. Commit changes ( git commit -m 'Add AmazingFeature' )
4. Push to branch ( git push origin feature/AmazingFeature )
5. Open a Pull Request
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Sneha K

## Support
For support, email your queries to [ your-email@example.com ]

## Acknowledgments
- BeautifulSoup4 documentation
- Selenium WebDriver documentation
- Python Requests library