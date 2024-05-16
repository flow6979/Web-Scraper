import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

    def scrape_and_save_json(self):
        try:
            with requests.Session() as session:
                response = session.get(self.url, headers=self.headers)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Finding the script tag with id="__NEXT_DATA__"
                    script_tag = soup.find('script', id='__NEXT_DATA__')

                    if script_tag:
                        script_content = script_tag.string.strip()

                        with open(self.filename, 'w', encoding='utf-8') as json_file:
                            json_file.write(script_content)

                        print(f"Data saved to {self.filename}")
                        return True
                    else:
                        print("Error: Script tag with id='__NEXT_DATA__' not found.")
                else:
                    print(f"Error: Unable to fetch content. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return False

url = "https://food.grab.com/sg/en/restaurants"
filename = "resultJson.json"
scraper = Scraper(url, filename)
scraper.scrape_and_save_json()
