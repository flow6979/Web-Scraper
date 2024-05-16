import os
import json
import zipfile
import requests
from multiprocessing import Pool

class DataFetcher:
    def __init__(self, combined_list_file_path, url_template, output_folder):
        self.combined_list_file_path = combined_list_file_path
        self.url_template = url_template
        self.output_folder = output_folder

    def fetch_response(self, merchant_id):
        url = self.url_template.format(merchant_id)
        response = requests.get(url)
        output_file_path = os.path.join(self.output_folder, f"{merchant_id}_response.json")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(response.text)
        print(f"Response for ID {merchant_id} saved to {output_file_path}")

    def fetch_responses(self):
        with open(self.combined_list_file_path, "r", encoding="utf-8") as combined_list_file:
            ids = json.load(combined_list_file)
        
        os.makedirs(self.output_folder, exist_ok=True)
        with Pool() as pool:
            pool.map(self.fetch_response, ids)

class DataExtractor:
    def __init__(self, output_folder, output_file_path):
        self.output_folder = output_folder
        self.output_file_path = output_file_path

    def extract_data(self):
        all_data = []
        for filename in os.listdir(self.output_folder):
            if filename.endswith("_response.json"):
                input_file_path = os.path.join(self.output_folder, filename)
                with open(input_file_path, "r", encoding="utf-8") as input_file:
                    data = json.load(input_file)
                    merchant_info = data.get("merchant", {})
                    merchant_id = merchant_info.get("ID")
                    name = merchant_info.get("name")
                    cuisine = merchant_info.get("cuisine")
                    timezone = merchant_info.get("timeZone")
                    photo_href = merchant_info.get("photoHref")
                    eta = merchant_info.get("ETA")
                    latlng = merchant_info.get("latlng")
                    rating = merchant_info.get("Rating")
                    distance_in_km = merchant_info.get("distanceInKm")
                    estimated_delivery_fee = merchant_info.get("estimatedDeliveryFee", {})
                    currency = estimated_delivery_fee.get("currency")
                    price = estimated_delivery_fee.get("price")
                    price_display = estimated_delivery_fee.get("priceDisplay")
                    status = estimated_delivery_fee.get("status")
                    multiplier = estimated_delivery_fee.get("Multiplier")
                    promotions = merchant_info.get("promotions")

                    all_data.append({
                        "ID": merchant_id,
                        "Details": {
                            "Name": name,
                            "Cuisine": cuisine,
                            "TimeZone": timezone,
                            "PhotoHref": photo_href,
                            "ETA": eta,
                            "Latlng": latlng,
                            "Rating": rating,
                            "DistanceInKm": distance_in_km,
                            "EstimatedDeliveryFee": {
                                "Currency": currency,
                                "Price": price,
                                "PriceDisplay": price_display,
                                "Status": status,
                                "Multiplier": multiplier,
                            },
                            "Promotions": promotions,
                        }
                    })

        return all_data

    def export_to_zip(self, all_data):
        with zipfile.ZipFile(self.output_file_path, "w", compression=zipfile.ZIP_DEFLATED) as output_zip:
            with output_zip.open("all_responses.ndjson", "w") as output_file:
                for data in all_data:
                    json_data = json.dumps(data, indent=4)
                    output_file.write(json_data.encode('utf-8'))
                    output_file.write('\n'.encode('utf-8'))
        
        print(f"All responses saved to individual JSON files and extracted data saved to {self.output_file_path}")

combined_list_file_path = "combined_listArray.txt"
url_template = "https://portal.grab.com/foodweb/v2/merchants/{}"
output_folder = "responses"
output_file_path = "all_responses.zip"

data_fetcher = DataFetcher(combined_list_file_path, url_template, output_folder)
data_fetcher.fetch_responses()

data_extractor = DataExtractor(output_folder, output_file_path)
all_data = data_extractor.extract_data()
data_extractor.export_to_zip(all_data)
