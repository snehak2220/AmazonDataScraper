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
├── main.py              
├── config.py            
├── scraper/
│   ├── __init__.py
│   ├── amazon.py       
│   └── utils.py        
├── requirements.txt    
├── README.md
└── output/            
    └── scraped_data.csv

## Dependencies
- Python 3.8+
- BeautifulSoup4 4.9.3
- Requests 2.26.0
- Pandas 1.3.3
- Selenium 4.1.0
- ChromeDriver (for Selenium)

## Legal Notice
⚠️ This tool is for educational purposes only. Users must:

- Review Amazon's robots.txt
- Comply with Amazon's Terms of Service
- Implement appropriate delays between requests
- Not use the data for commercial purposes without proper authorization

## License
This project is licensed under the MIT License - see the LICENSE file for details.

