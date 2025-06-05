# Linkedin-Web-Scraping

A web scraper that extracts **Data Analyst** job offers from **LinkedIn** and saves them into a CSV file.

## 📌 Project Overview

This project automates the process of retrieving job listings from LinkedIn using **Python** and **Selenium**. It focuses on Data Analyst positions and outputs the results into a structured CSV file (`linkedin.csv`) for easy analysis and processing.

## Features

* Automated browser interaction with Selenium
* Dynamic page scrolling and "Load more results" handling
* Data extraction: company name, job title, and location
* CSV export for structured data storage
* Basic error and exception handling

## 🛠 Technologies Used

* **Python**
* **Selenium**
* **Pandas**
* **VSCode**
* **Firefox** browser

## 📁 Repository Structure

```
├── README.md                 # Project description and usage
├── Web Scraping Report.pdf  # Detailed report of the project
├── attempt.py               # Python script for scraping
├── linkedin.csv             # Output file containing scraped job data
```

## Approach

1. Open the LinkedIn job search page for Data Analyst positions.
2. Scroll through the job listings to dynamically load more content.
3. Click the "Load more results" button when available.
4. Extract:

   * Company names
   * Job titles
   * Job locations
5. Store the information in lists, convert them to Pandas DataFrames, and combine them.
6. Save the resulting dataset to `linkedin.csv`.

## ⚠️ Challenges

* **Dynamic content loading**
* **Frequent changes in LinkedIn’s page structure**
* **Rate limiting & bot detection**
* **Handling missing or dynamically delayed elements**
* **Lack of robust error handling in earlier stages**

## ✅ Solutions

* Introduced **explicit waits** with Selenium to handle timing issues.
* Ran browser in **headless mode** to minimize bot detection.
* Implemented basic **try-except** blocks to catch scraping errors.

## 📌 How to Run

> **Note:** This script is for educational purposes only. Scraping LinkedIn may violate their [Terms of Service](https://www.linkedin.com/legal/user-agreement). Use responsibly.

1. Install required libraries:

   ```bash
   pip install selenium pandas
   ```

2. Set up Firefox and the appropriate [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

3. Run the script:

   ```bash
   python attempt.py
   ```

4. Check `linkedin.csv` for results.
