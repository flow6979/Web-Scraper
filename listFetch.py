import os
import json

class JSONProcessor:
    def __init__(self, json_file_path, output_file_path):
        self.json_file_path = json_file_path
        self.output_file_path = output_file_path

    def process_and_save(self):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            # Extracting data from "recommendedMerchants" and "restaurantList"
            recommended_merchants = data.get("props", {}).get("initialReduxState", {}).get("pageRestaurantsV2", {}).get("collections", {}).get("recommendedMerchants", {})
            restaurant_list = data.get("props", {}).get("initialReduxState", {}).get("pageRestaurantsV2", {}).get("collections", {}).get("restaurantList", {})

            # Combining both lists
            combined_list = {
                "getRecommendedMerchantsV2/countryCode=SG&latitude=1.287953&longitude=103.851784": recommended_merchants,
                "getRestaurantsV2/countryCode=SG&latlng=1.287953%2C103.851784": restaurant_list
            }

            print("Combined List:", combined_list)

            with open(self.output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(json.dumps(combined_list, indent=2))

            print(f"Combined list stored in '{self.output_file_path}'")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        except FileNotFoundError:
            print(f"Error: File not found at path '{self.json_file_path}'")

json_file_path = r'resultJson.json'
current_directory = os.path.dirname(os.path.abspath(__file__))
output_file_relative_path = "combined_list.txt"
output_file_path = os.path.join(current_directory, output_file_relative_path)

json_processor = JSONProcessor(json_file_path, output_file_path)
json_processor.process_and_save()
