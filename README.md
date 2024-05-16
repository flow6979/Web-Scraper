# GrabFood Web Scraper

## Introduction

The GrabFood Web Scraper is a Python-based tool designed to extract and analyze data from the GrabFood website. This tool facilitates the extraction of information about restaurants, recommended merchants, and various details related to the GrabFood platform.

## Features

- **Web Scraping:** Gathers information from the GrabFood website, prioritizing restaurant details and recommended merchants.
- **Data Processing:** Analyzes the gathered data and structures it into organized formats for further analysis.
- **API Requests:** Utilizes Grab's API to access in-depth insights about individual merchants, enhancing data depth and accuracy.

## How It Works

The GrabFood Web Scraper operates in several stages:

1. **Web Scraping:** The initial script (`scraper.py`) uses BeautifulSoup to scrape HTML content from the GrabFood website.
2. **Data Processing:** The extracted data is then processed and organized, with relevant information stored in a JSON file.
3. **API Requests:** The `listFetch.py` script uses collected IDs to make API requests and fetch detailed information about specific merchants.
4. **Data Combining:** The `listMaking.py` script combines the collected data into a structured format.
5. **Response Grabbing:** Finally, the `dataFetching.py` script fetches responses using the collected IDs, extracting specific details about merchants.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/flow6979/Web-Scraper.git


2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Make the script executable**
   ```bash
   chmod +x run.sh 

4. **Execute the script**
   ```bash
   ./run.sh   


## Approach

I started by taking on the difficult task of gathering and examining data from the GrabFood website. The first thing I did was make sure I knew exactly what information I needed and how to get it off the website. This required looking at GrabFood's page structure to find important components such as merchant suggestions and restaurant listings.

I started looking into web scraping methods and tools that could help me collect data effectively with a specific aim in mind. I looked into a number of choices, and while BeautifulSoup is a well-known Python package, I chose to utilise it because of its simplicity and flexibility.

I then started my web scraping adventure. Equipped with this newfound understanding, I created a script to browse GrabFood's webpages, find pertinent data, and extract it in a way that would be useful. This required managing dynamic material, carefully examining HTML parts, and making sure I got all the information I needed.

After extracting the raw data, it was time to organise and interpret it. I cleaned up any formatting errors and inconsistencies after parsing the retrieved data and organising it into structured representations. Ensuring the accuracy of the data and preparing it for analysis required this step.

I didn't stop there, though. By using Grab's API, I hoped to further enhance the data. I was able to retrieve comprehensive details about individual merchants, including menu items, prices, and delivery choices, by submitting API queries with the merchant IDs I had collected from my scraping activities.

Now that I had my data, I could finally get my hands dirty and start analysing it. I looked over the information gathered to find patterns and insights about eateries, retailers, and customer preferences. Using graphs and charts to visually represent my findings improved my understanding of the data and my ability to present my findings.

I devoted special attention to quality assurance all along the way. I put my solution through a rigorous testing process to make sure the collected data was accurate and reliable, and I handled any edge situations or exceptions with grace.


