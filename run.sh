#!/bin/bash

# Create a directory for extracted data
mkdir -p extracted_data

# Execute the Python scripts
python3 scraper.py
python3 listFetch.py
python3 listMaking.py
python3 dataFetching.py

# Move necessary files to the extracted_data directory
mv all_responses.zip combined_list.txt combined_listArray.txt resultJson.json extracted_data/
