# 🧪 Periodic Table Elements Scraper

This project scrapes periodic table elements from a national health site using two different methodologies.

## Methodologies

### 1. Playwright Only

- **Description**: Uses Playwright to scrape the periodic table.
- **Tools Used**: Playwright.
- **File**: `playwright_only`

### 2. Scrapy with Playwright

- **Description**: Combines Scrapy and Playwright for enhanced scraping.
- **Tools Used**: Scrapy, Playwright.
- **File**: `scrapy_pw`

## Features

- Extracts detailed information about each element.
- Demonstrates different approaches to handle dynamic content.

## Usage

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. **Run the Scripts**:

   - For Playwright only:

     ```bash
     python main.py
     ```

   - For Scrapy with Playwright:

     ```bash
     scrapy runspider spider.py
